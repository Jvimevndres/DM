"""
==============================================================================
SCRIPT: Análisis Descriptivo - Terremotos USGS
==============================================================================
Autor: Jaime
Proyecto: Minería de Datos - Análisis de Terremotos Globales
Fecha: Noviembre 2025

DESCRIPCIÓN:
Este script realiza el análisis estadístico descriptivo del dataset de 
terremotos ya limpio. Calcula métricas clave y genera insights para el
informe técnico.

ANÁLISIS REALIZADOS:
  1. Estadísticas descriptivas de magnitud y profundidad
  2. Distribución temporal (sismos por año, década)
  3. Análisis geográfico (regiones más afectadas)
  4. Correlaciones entre variables
  5. Identificación de eventos extremos

INPUT:
  - Archivo: data/processed/earthquakes_clean.csv

OUTPUT:
  - Reporte estadístico: outputs/results/descriptive_statistics.txt
  - Tablas de frecuencia: outputs/results/frequency_tables.csv
==============================================================================
"""

import pandas as pd
import numpy as np
from scipy import stats
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ==============================================================================
# CONFIGURACIÓN DE RUTAS
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLEAN_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'earthquakes_clean.csv')
RESULTS_PATH = os.path.join(BASE_DIR, 'outputs', 'results')

print("="*80)
print("ANÁLISIS DESCRIPTIVO - TERREMOTOS USGS")
print("="*80)
print(f"Dataset: {CLEAN_DATA_PATH}")
print("="*80 + "\n")


# ==============================================================================
# FUNCIÓN 1: CARGAR DATOS LIMPIOS
# ==============================================================================
def load_clean_data(file_path):
    """
    Carga el dataset limpio.
    
    Parámetros:
    -----------
    file_path : str
        Ruta al archivo CSV limpio
    
    Retorna:
    --------
    pandas.DataFrame
        Dataset limpio cargado
    """
    print("[1/7] Cargando datos limpios...")
    
    try:
        df = pd.read_csv(file_path, parse_dates=['time'])
        print(f"   ✓ Datos cargados: {len(df):,} registros")
        print(f"   ✓ Columnas disponibles: {len(df.columns)}")
        print(f"   ✓ Memoria utilizada: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n")
        return df
    
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo {file_path}")
        print("   Por favor, ejecuta primero el script 01_data_cleaning.py")
        return None
    except Exception as e:
        print(f"❌ ERROR al cargar datos: {str(e)}")
        return None


# ==============================================================================
# FUNCIÓN 2: ESTADÍSTICAS DESCRIPTIVAS DE MAGNITUD Y PROFUNDIDAD
# ==============================================================================
def calculate_basic_statistics(df):
    """
    Calcula estadísticas descriptivas para magnitud y profundidad.
    
    NOTA PARA INFORME:
    "Se calcularon medidas de tendencia central y dispersión para las 
    variables magnitud y profundidad, permitiendo caracterizar la 
    distribución de los eventos sísmicos."
    
    PARA PRESENTACIÓN:
    "La magnitud promedio de los terremotos registrados es de X.X, con 
    una desviación estándar de Y.Y. La profundidad media es de Z.Z km."
    """
    print("[2/7] Calculando estadísticas descriptivas básicas...")
    
    stats_dict = {}
    
    # Estadísticas para MAGNITUD
    if 'mag' in df.columns:
        print("\n   📊 MAGNITUD (mag):")
        mag_stats = {
            'count': df['mag'].count(),
            'mean': df['mag'].mean(),
            'median': df['mag'].median(),
            'std': df['mag'].std(),
            'min': df['mag'].min(),
            'q1': df['mag'].quantile(0.25),
            'q3': df['mag'].quantile(0.75),
            'max': df['mag'].max(),
            'iqr': df['mag'].quantile(0.75) - df['mag'].quantile(0.25),
            'cv': (df['mag'].std() / df['mag'].mean()) * 100  # Coeficiente de variación
        }
        
        stats_dict['magnitud'] = mag_stats
        
        print(f"      Media (promedio):         {mag_stats['mean']:.3f}")
        print(f"      Mediana (Q2):             {mag_stats['median']:.3f}")
        print(f"      Desviación estándar:      {mag_stats['std']:.3f}")
        print(f"      Mínimo:                   {mag_stats['min']:.3f}")
        print(f"      Cuartil 1 (Q1):           {mag_stats['q1']:.3f}")
        print(f"      Cuartil 3 (Q3):           {mag_stats['q3']:.3f}")
        print(f"      Máximo:                   {mag_stats['max']:.3f}")
        print(f"      Rango intercuartílico:    {mag_stats['iqr']:.3f}")
        print(f"      Coef. de variación:       {mag_stats['cv']:.2f}%")
    
    # Estadísticas para PROFUNDIDAD
    if 'depth' in df.columns:
        print("\n   📊 PROFUNDIDAD (depth en km):")
        depth_stats = {
            'count': df['depth'].count(),
            'mean': df['depth'].mean(),
            'median': df['depth'].median(),
            'std': df['depth'].std(),
            'min': df['depth'].min(),
            'q1': df['depth'].quantile(0.25),
            'q3': df['depth'].quantile(0.75),
            'max': df['depth'].max(),
            'iqr': df['depth'].quantile(0.75) - df['depth'].quantile(0.25),
            'cv': (df['depth'].std() / df['depth'].mean()) * 100
        }
        
        stats_dict['profundidad'] = depth_stats
        
        print(f"      Media (promedio):         {depth_stats['mean']:.2f} km")
        print(f"      Mediana (Q2):             {depth_stats['median']:.2f} km")
        print(f"      Desviación estándar:      {depth_stats['std']:.2f} km")
        print(f"      Mínimo:                   {depth_stats['min']:.2f} km")
        print(f"      Cuartil 1 (Q1):           {depth_stats['q1']:.2f} km")
        print(f"      Cuartil 3 (Q3):           {depth_stats['q3']:.2f} km")
        print(f"      Máximo:                   {depth_stats['max']:.2f} km")
        print(f"      Rango intercuartílico:    {depth_stats['iqr']:.2f} km")
        print(f"      Coef. de variación:       {depth_stats['cv']:.2f}%")
    
    print("\n   ✓ Estadísticas básicas calculadas\n")
    return stats_dict


# ==============================================================================
# FUNCIÓN 3: DISTRIBUCIÓN TEMPORAL (SISMOS POR AÑO Y DÉCADA)
# ==============================================================================
def analyze_temporal_distribution(df):
    """
    Analiza la distribución temporal de los terremotos.
    
    NOTA PARA INFORME:
    "Se analizó la distribución temporal de eventos sísmicos, revelando 
    patrones de frecuencia a lo largo de décadas y años específicos."
    
    PARA PRESENTACIÓN:
    "Se observa un incremento significativo en el registro de sismos a 
    partir de la década de 1960, posiblemente debido a la expansión de 
    la red sismográfica global."
    """
    print("[3/7] Analizando distribución temporal...")
    
    temporal_stats = {}
    
    # Sismos por año
    if 'year' in df.columns:
        yearly_counts = df['year'].value_counts().sort_index()
        temporal_stats['por_anio'] = yearly_counts
        
        print("\n   📅 DISTRIBUCIÓN POR AÑO:")
        print(f"      Años analizados:          {int(df['year'].min())} - {int(df['year'].max())}")
        print(f"      Total de años:            {int(df['year'].max() - df['year'].min() + 1)}")
        print(f"      Promedio sismos/año:      {yearly_counts.mean():.0f}")
        print(f"      Mediana sismos/año:       {yearly_counts.median():.0f}")
        print(f"      Año con más sismos:       {yearly_counts.idxmax()} ({yearly_counts.max():,} sismos)")
        print(f"      Año con menos sismos:     {yearly_counts.idxmin()} ({yearly_counts.min():,} sismos)")
    
    # Sismos por década
    if 'decade' in df.columns:
        decade_counts = df['decade'].value_counts().sort_index()
        temporal_stats['por_decada'] = decade_counts
        
        print("\n   📅 DISTRIBUCIÓN POR DÉCADA:")
        for decade in sorted(decade_counts.index):
            count = decade_counts[decade]
            pct = (count / len(df)) * 100
            print(f"      {int(decade)}s:  {count:>12,} sismos ({pct:>5.2f}%)")
        
        # Identificar tendencias
        decades_list = sorted(decade_counts.index)
        if len(decades_list) >= 2:
            recent_decades = decades_list[-3:]  # Últimas 3 décadas
            old_decades = decades_list[:3]       # Primeras 3 décadas
            
            recent_avg = decade_counts[recent_decades].mean()
            old_avg = decade_counts[old_decades].mean()
            
            if recent_avg > old_avg:
                increase_factor = recent_avg / old_avg
                print(f"\n      📈 Tendencia: Incremento de {increase_factor:.1f}x en registros")
                print(f"         (comparando primeras vs últimas 3 décadas)")
    
    # Sismos por mes (estacionalidad)
    if 'month' in df.columns:
        monthly_counts = df['month'].value_counts().sort_index()
        temporal_stats['por_mes'] = monthly_counts
        
        months_names = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                       'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        
        print("\n   📅 DISTRIBUCIÓN POR MES (promedio):")
        for month in range(1, 13):
            if month in monthly_counts.index:
                count = monthly_counts[month]
                print(f"      {months_names[month-1]}:  {count:>12,} sismos")
    
    print("\n   ✓ Análisis temporal completado\n")
    return temporal_stats


# ==============================================================================
# FUNCIÓN 4: ANÁLISIS GEOGRÁFICO (REGIONES MÁS AFECTADAS)
# ==============================================================================
def analyze_geographic_distribution(df, top_n=20):
    """
    Analiza las regiones más afectadas por terremotos.
    
    Parámetros:
    -----------
    top_n : int
        Número de regiones principales a mostrar
    
    NOTA PARA INFORME:
    "Se identificaron las regiones geográficas con mayor actividad sísmica 
    mediante el análisis de la columna 'place', extrayendo información de 
    ubicación a nivel de país/región."
    
    PARA PRESENTACIÓN:
    "Las regiones con mayor actividad sísmica incluyen: [lista de top 5], 
    concentrando el X% de los eventos registrados."
    """
    print(f"[4/7] Analizando distribución geográfica (Top {top_n})...")
    
    geographic_stats = {}
    
    if 'place' not in df.columns:
        print("   ⚠ Columna 'place' no encontrada, saltando análisis geográfico\n")
        return geographic_stats
    
    # Extraer país/región de la columna 'place'
    # Formato típico: "13km ESE of Volcano, Hawaii" -> extraer "Hawaii"
    # O: "Japan" -> extraer "Japan"
    
    def extract_region(place_str):
        """Extrae la región/país de la descripción del lugar."""
        if pd.isna(place_str):
            return 'Unknown'
        
        # Muchos lugares tienen formato "X km DIR of Location, Country"
        if ',' in place_str:
            parts = place_str.split(',')
            return parts[-1].strip()  # Última parte suele ser el país/región
        else:
            # Si no hay coma, extraer palabras capitalizadas al final
            words = place_str.split()
            if len(words) > 0:
                return words[-1]
            return 'Unknown'
    
    print("   Extrayendo información de regiones...")
    df['region'] = df['place'].apply(extract_region)
    
    # Contar sismos por región
    region_counts = df['region'].value_counts().head(top_n)
    geographic_stats['por_region'] = region_counts
    
    print(f"\n   🌍 TOP {top_n} REGIONES CON MÁS SISMOS:")
    print("   " + "-" * 70)
    print(f"   {'#':<4} {'Región':<35} {'Sismos':>12} {'Porcentaje':>10}")
    print("   " + "-" * 70)
    
    for idx, (region, count) in enumerate(region_counts.items(), 1):
        pct = (count / len(df)) * 100
        print(f"   {idx:<4} {region:<35} {count:>12,} {pct:>9.2f}%")
    
    # Estadísticas adicionales
    total_top_regions = region_counts.sum()
    pct_top_regions = (total_top_regions / len(df)) * 100
    
    print("   " + "-" * 70)
    print(f"   Total en Top {top_n}:                        {total_top_regions:>12,} {pct_top_regions:>9.2f}%")
    print("   " + "-" * 70)
    
    print("\n   ✓ Análisis geográfico completado\n")
    return geographic_stats


# ==============================================================================
# FUNCIÓN 5: CORRELACIÓN ENTRE MAGNITUD Y PROFUNDIDAD
# ==============================================================================
def analyze_correlations(df):
    """
    Calcula la correlación entre magnitud y profundidad.
    
    NOTA PARA INFORME:
    "Se calculó el coeficiente de correlación de Pearson entre magnitud y 
    profundidad para evaluar si existe una relación lineal entre estas 
    variables."
    
    PARA PRESENTACIÓN:
    "Se observó una correlación [débil/moderada/fuerte] de r=X.XX entre 
    magnitud y profundidad, sugiriendo que [interpretación]."
    """
    print("[5/7] Analizando correlaciones...")
    
    correlation_stats = {}
    
    if 'mag' in df.columns and 'depth' in df.columns:
        # Eliminar NaN para el cálculo
        df_corr = df[['mag', 'depth']].dropna()
        
        # Correlación de Pearson
        pearson_corr, pearson_pval = stats.pearsonr(df_corr['mag'], df_corr['depth'])
        
        # Correlación de Spearman (no paramétrica)
        spearman_corr, spearman_pval = stats.spearmanr(df_corr['mag'], df_corr['depth'])
        
        correlation_stats['pearson'] = {
            'correlation': pearson_corr,
            'p_value': pearson_pval
        }
        
        correlation_stats['spearman'] = {
            'correlation': spearman_corr,
            'p_value': spearman_pval
        }
        
        print("\n   📊 CORRELACIÓN: MAGNITUD vs PROFUNDIDAD")
        print("   " + "-" * 60)
        print(f"      Coeficiente de Pearson:   {pearson_corr:>7.4f}")
        print(f"      P-valor:                  {pearson_pval:.2e}")
        print(f"      Coeficiente de Spearman:  {spearman_corr:>7.4f}")
        print(f"      P-valor:                  {spearman_pval:.2e}")
        
        # Interpretación
        print("\n   💡 INTERPRETACIÓN:")
        abs_corr = abs(pearson_corr)
        if abs_corr < 0.3:
            strength = "débil"
        elif abs_corr < 0.7:
            strength = "moderada"
        else:
            strength = "fuerte"
        
        direction = "positiva" if pearson_corr > 0 else "negativa"
        
        print(f"      Existe una correlación {strength} {direction} (r={pearson_corr:.4f})")
        
        if pearson_pval < 0.05:
            print(f"      La correlación es estadísticamente significativa (p<0.05)")
        else:
            print(f"      La correlación NO es estadísticamente significativa (p≥0.05)")
        
        # Frase sugerida para el informe
        print("\n   📝 FRASE SUGERIDA PARA INFORME:")
        print(f"      \"Se observa una correlación {strength} {direction} entre magnitud")
        print(f"       y profundidad (r={pearson_corr:.3f}, p{'<' if pearson_pval < 0.001 else '='}0.001),")
        if abs_corr < 0.3:
            print(f"       indicando que la profundidad tiene poca relación lineal con la")
            print(f"       magnitud del terremoto.\"")
        else:
            print(f"       sugiriendo que ambas variables están relacionadas.\"")
    
    print("\n   ✓ Análisis de correlaciones completado\n")
    return correlation_stats


# ==============================================================================
# FUNCIÓN 6: IDENTIFICACIÓN DE EVENTOS EXTREMOS
# ==============================================================================
def identify_extreme_events(df, top_n=10):
    """
    Identifica los terremotos más significativos (mayor magnitud).
    
    NOTA PARA INFORME:
    "Se identificaron los eventos sísmicos de mayor magnitud registrados 
    en el dataset, incluyendo información de ubicación, profundidad y fecha."
    
    PARA PRESENTACIÓN:
    "El terremoto de mayor magnitud registrado fue de X.X en [ubicación], 
    ocurrido el [fecha]."
    """
    print(f"[6/7] Identificando eventos extremos (Top {top_n})...")
    
    if 'mag' not in df.columns:
        print("   ⚠ No se puede identificar eventos extremos sin columna 'mag'\n")
        return None
    
    # Ordenar por magnitud descendente
    top_events = df.nlargest(top_n, 'mag')
    
    print(f"\n   ⚠️  TOP {top_n} TERREMOTOS DE MAYOR MAGNITUD:")
    print("   " + "=" * 78)
    
    for idx, row in enumerate(top_events.itertuples(), 1):
        print(f"\n   #{idx}")
        print(f"      Magnitud:       {row.mag:.2f}")
        
        if hasattr(row, 'place'):
            print(f"      Ubicación:      {row.place}")
        
        if hasattr(row, 'time'):
            print(f"      Fecha:          {row.time}")
        
        if hasattr(row, 'depth'):
            print(f"      Profundidad:    {row.depth:.2f} km")
        
        if hasattr(row, 'latitude') and hasattr(row, 'longitude'):
            print(f"      Coordenadas:    {row.latitude:.4f}°N, {row.longitude:.4f}°E")
    
    print("\n   " + "=" * 78)
    
    # Estadísticas de eventos de alta magnitud
    high_magnitude_threshold = 7.0
    high_mag_count = (df['mag'] >= high_magnitude_threshold).sum()
    high_mag_pct = (high_mag_count / len(df)) * 100
    
    print(f"\n   📊 EVENTOS DE ALTA MAGNITUD (≥{high_magnitude_threshold}):")
    print(f"      Total:                    {high_mag_count:,} eventos")
    print(f"      Porcentaje del total:     {high_mag_pct:.3f}%")
    
    print("\n   ✓ Eventos extremos identificados\n")
    
    return top_events


# ==============================================================================
# FUNCIÓN 7: GENERAR REPORTE COMPLETO
# ==============================================================================
def generate_comprehensive_report(df, stats_dict, temporal_stats, 
                                  geographic_stats, correlation_stats):
    """
    Genera un reporte de texto completo con todos los resultados.
    """
    print("[7/7] Generando reporte completo...")
    
    report_path = os.path.join(RESULTS_PATH, 'descriptive_statistics.txt')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("REPORTE DE ANÁLISIS DESCRIPTIVO - TERREMOTOS USGS\n")
        f.write("=" * 80 + "\n")
        f.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total de registros analizados: {len(df):,}\n")
        f.write("=" * 80 + "\n\n")
        
        # 1. ESTADÍSTICAS DE MAGNITUD
        f.write("1. ESTADÍSTICAS DESCRIPTIVAS - MAGNITUD\n")
        f.write("-" * 80 + "\n")
        if 'magnitud' in stats_dict:
            mag_stats = stats_dict['magnitud']
            f.write(f"   Media:                    {mag_stats['mean']:>10.3f}\n")
            f.write(f"   Mediana:                  {mag_stats['median']:>10.3f}\n")
            f.write(f"   Desviación estándar:      {mag_stats['std']:>10.3f}\n")
            f.write(f"   Mínimo:                   {mag_stats['min']:>10.3f}\n")
            f.write(f"   Cuartil 1:                {mag_stats['q1']:>10.3f}\n")
            f.write(f"   Cuartil 3:                {mag_stats['q3']:>10.3f}\n")
            f.write(f"   Máximo:                   {mag_stats['max']:>10.3f}\n")
            f.write(f"   Rango intercuartílico:    {mag_stats['iqr']:>10.3f}\n")
            f.write(f"   Coef. de variación:       {mag_stats['cv']:>10.2f}%\n")
        f.write("\n")
        
        # 2. ESTADÍSTICAS DE PROFUNDIDAD
        f.write("2. ESTADÍSTICAS DESCRIPTIVAS - PROFUNDIDAD (km)\n")
        f.write("-" * 80 + "\n")
        if 'profundidad' in stats_dict:
            depth_stats = stats_dict['profundidad']
            f.write(f"   Media:                    {depth_stats['mean']:>10.2f} km\n")
            f.write(f"   Mediana:                  {depth_stats['median']:>10.2f} km\n")
            f.write(f"   Desviación estándar:      {depth_stats['std']:>10.2f} km\n")
            f.write(f"   Mínimo:                   {depth_stats['min']:>10.2f} km\n")
            f.write(f"   Cuartil 1:                {depth_stats['q1']:>10.2f} km\n")
            f.write(f"   Cuartil 3:                {depth_stats['q3']:>10.2f} km\n")
            f.write(f"   Máximo:                   {depth_stats['max']:>10.2f} km\n")
            f.write(f"   Rango intercuartílico:    {depth_stats['iqr']:>10.2f} km\n")
            f.write(f"   Coef. de variación:       {depth_stats['cv']:>10.2f}%\n")
        f.write("\n")
        
        # 3. DISTRIBUCIÓN TEMPORAL POR DÉCADA
        f.write("3. DISTRIBUCIÓN TEMPORAL - POR DÉCADA\n")
        f.write("-" * 80 + "\n")
        if 'por_decada' in temporal_stats:
            for decade in sorted(temporal_stats['por_decada'].index):
                count = temporal_stats['por_decada'][decade]
                pct = (count / len(df)) * 100
                f.write(f"   {int(decade)}s:  {count:>15,} sismos ({pct:>6.2f}%)\n")
        f.write("\n")
        
        # 4. REGIONES MÁS AFECTADAS
        f.write("4. REGIONES GEOGRÁFICAS MÁS AFECTADAS (Top 20)\n")
        f.write("-" * 80 + "\n")
        if 'por_region' in geographic_stats:
            for idx, (region, count) in enumerate(geographic_stats['por_region'].items(), 1):
                pct = (count / len(df)) * 100
                f.write(f"   {idx:>2}. {region:<40} {count:>10,} ({pct:>5.2f}%)\n")
        f.write("\n")
        
        # 5. CORRELACIÓN
        f.write("5. CORRELACIÓN: MAGNITUD vs PROFUNDIDAD\n")
        f.write("-" * 80 + "\n")
        if 'pearson' in correlation_stats:
            f.write(f"   Coeficiente de Pearson:   {correlation_stats['pearson']['correlation']:>10.4f}\n")
            f.write(f"   P-valor:                  {correlation_stats['pearson']['p_value']:>10.2e}\n")
            f.write(f"   Coeficiente de Spearman:  {correlation_stats['spearman']['correlation']:>10.4f}\n")
            f.write(f"   P-valor:                  {correlation_stats['spearman']['p_value']:>10.2e}\n")
        f.write("\n")
        
        f.write("=" * 80 + "\n")
        f.write("FIN DEL REPORTE\n")
        f.write("=" * 80 + "\n")
    
    print(f"   ✓ Reporte guardado en: {report_path}")
    
    # También guardar tablas en CSV
    csv_path = os.path.join(RESULTS_PATH, 'frequency_tables.csv')
    
    if 'por_decada' in temporal_stats and 'por_region' in geographic_stats:
        # Crear DataFrame combinado
        decades_df = temporal_stats['por_decada'].reset_index()
        decades_df.columns = ['Década', 'Frecuencia']
        decades_df.to_csv(csv_path.replace('.csv', '_decades.csv'), index=False)
        
        regions_df = geographic_stats['por_region'].reset_index()
        regions_df.columns = ['Región', 'Frecuencia']
        regions_df.to_csv(csv_path.replace('.csv', '_regions.csv'), index=False)
        
        print(f"   ✓ Tablas de frecuencia guardadas en: {RESULTS_PATH}")
    
    print()


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================
def main():
    """
    Función principal que ejecuta todo el pipeline de análisis descriptivo.
    """
    
    # Paso 1: Cargar datos limpios
    df = load_clean_data(CLEAN_DATA_PATH)
    
    if df is None:
        print("❌ No se pudo continuar sin datos. Abortando.")
        return
    
    # Paso 2: Estadísticas básicas
    stats_dict = calculate_basic_statistics(df)
    
    # Paso 3: Distribución temporal
    temporal_stats = analyze_temporal_distribution(df)
    
    # Paso 4: Distribución geográfica
    geographic_stats = analyze_geographic_distribution(df, top_n=20)
    
    # Paso 5: Correlaciones
    correlation_stats = analyze_correlations(df)
    
    # Paso 6: Eventos extremos
    top_events = identify_extreme_events(df, top_n=10)
    
    # Paso 7: Generar reporte completo
    generate_comprehensive_report(df, stats_dict, temporal_stats, 
                                  geographic_stats, correlation_stats)
    
    print("=" * 80)
    print("✓✓✓ ANÁLISIS DESCRIPTIVO COMPLETADO EXITOSAMENTE ✓✓✓")
    print("=" * 80)
    print("\nPróximos pasos:")
    print("  1. Revisar reportes en: outputs/results/")
    print("  2. Ejecutar visualizaciones: python scripts/python/03_visualizations.py")
    print("  3. Crear mapas en R: Rscript scripts/R/02_maps_visualization.R")
    print("=" * 80 + "\n")


# ==============================================================================
# EJECUCIÓN DEL SCRIPT
# ==============================================================================
if __name__ == "__main__":
    main()
