"""
==============================================================================
SCRIPT: Limpieza y Preparación de Datos - Terremotos USGS
==============================================================================
Autor: Jaime
Proyecto: Minería de Datos - Análisis de Terremotos Globales
Fecha: Noviembre 2025

DESCRIPCIÓN:
Este script se encarga de cargar, limpiar y preparar el dataset masivo de 
terremotos del USGS (>1M registros). Realiza las siguientes operaciones:
  1. Carga eficiente del archivo CSV
  2. Conversión de fechas a formato datetime
  3. Creación de columnas derivadas (year, decade, month)
  4. Eliminación de duplicados y valores faltantes críticos
  5. Exportación del dataset limpio

DATASET DE ENTRADA:
  - Archivo: data/raw/Earthquakes_USGS.csv
  - Tamaño esperado: >1,000,000 registros

DATASET DE SALIDA:
  - Archivo: data/processed/earthquakes_clean.csv
  - Registros esperados: ~900,000+ (después de limpieza)
==============================================================================
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# ==============================================================================
# CONFIGURACIÓN DE RUTAS
# ==============================================================================
# Obtener directorio base del proyecto (2 niveles arriba desde este script)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'Earthquakes_USGS.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'earthquakes_clean.csv')
RESULTS_PATH = os.path.join(BASE_DIR, 'outputs', 'results')

# Crear directorio de resultados si no existe
os.makedirs(RESULTS_PATH, exist_ok=True)

print("="*80)
print("INICIANDO PROCESO DE LIMPIEZA DE DATOS - TERREMOTOS USGS")
print("="*80)
print(f"Directorio base: {BASE_DIR}")
print(f"Archivo de entrada: {RAW_DATA_PATH}")
print(f"Archivo de salida: {PROCESSED_DATA_PATH}")
print("="*80)


# ==============================================================================
# FUNCIÓN 1: CARGA EFICIENTE DE DATOS
# ==============================================================================
def load_earthquake_data(file_path, sample_size=None):
    """
    Carga el dataset de terremotos de forma eficiente.
    
    Parámetros:
    -----------
    file_path : str
        Ruta al archivo CSV
    sample_size : int, opcional
        Si se especifica, carga solo una muestra aleatoria de N filas
        (útil para pruebas rápidas con datasets masivos)
    
    Retorna:
    --------
    pandas.DataFrame
        Dataset cargado
    
    NOTA PARA INFORME:
    "Se implementó una carga eficiente del dataset utilizando pandas, 
    optimizando el uso de memoria mediante la especificación de tipos de datos."
    """
    print("\n[1/6] Cargando datos...")
    
    try:
        # Verificar si el archivo existe
        if not os.path.exists(file_path):
            print(f"❌ ERROR: No se encontró el archivo {file_path}")
            print(f"Por favor, coloca el archivo 'Earthquakes_USGS.csv' en la carpeta 'data/raw/'")
            sys.exit(1)
        
        # Obtener tamaño del archivo
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        print(f"   Tamaño del archivo: {file_size_mb:.2f} MB")
        
        # Especificar tipos de datos para optimizar memoria
        dtype_dict = {
            'latitude': 'float32',
            'longitude': 'float32',
            'depth': 'float32',
            'mag': 'float32',
            'magType': 'category',
            'net': 'category',
            'type': 'category'
        }
        
        # Cargar datos (con o sin muestreo)
        if sample_size:
            print(f"   Cargando muestra de {sample_size:,} registros...")
            # Para muestreo, primero obtenemos el número total de líneas
            n_lines = sum(1 for _ in open(file_path)) - 1  # -1 por el header
            skip_idx = np.random.choice(range(1, n_lines+1), n_lines - sample_size, replace=False)
            df = pd.read_csv(file_path, dtype=dtype_dict, skiprows=skip_idx)
        else:
            print("   Cargando dataset completo...")
            df = pd.read_csv(file_path, dtype=dtype_dict, low_memory=False)
        
        print(f"   ✓ Datos cargados exitosamente: {len(df):,} registros")
        print(f"   ✓ Columnas disponibles: {list(df.columns)}")
        print(f"   ✓ Uso de memoria: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR al cargar datos: {str(e)}")
        sys.exit(1)


# ==============================================================================
# FUNCIÓN 2: CONVERSIÓN DE FECHAS Y CREACIÓN DE COLUMNAS TEMPORALES
# ==============================================================================
def process_datetime_columns(df):
    """
    Convierte la columna 'time' a formato datetime y crea columnas derivadas.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        Dataset con columna 'time'
    
    Retorna:
    --------
    pandas.DataFrame
        Dataset con nuevas columnas: year, decade, month
    
    NOTA PARA INFORME:
    "Se realizó la conversión de la columna temporal a formato datetime y se 
    crearon variables derivadas (año, década, mes) para facilitar el análisis 
    de tendencias temporales."
    """
    print("\n[2/6] Procesando fechas y creando columnas temporales...")
    
    try:
        # Convertir columna 'time' a datetime
        # Usar format='mixed' para manejar diferentes formatos de fecha
        df['time'] = pd.to_datetime(df['time'], format='mixed', errors='coerce')
        
        print(f"   ✓ Columna 'time' convertida a datetime")
        
        # Verificar cuántos valores fueron convertidos exitosamente
        valid_dates = df['time'].notna().sum()
        print(f"   ✓ Fechas válidas: {valid_dates:,} de {len(df):,} ({valid_dates/len(df)*100:.2f}%)")
        
        # Crear columnas derivadas
        df['year'] = df['time'].dt.year
        df['decade'] = (df['time'].dt.year // 10) * 10  # Década: 1990, 2000, 2010, etc.
        df['month'] = df['time'].dt.month
        
        print(f"   ✓ Columnas creadas: year, decade, month")
        
        # Mostrar rango temporal solo si hay fechas válidas
        if valid_dates > 0:
            print(f"   ✓ Rango temporal: {int(df['year'].min())} - {int(df['year'].max())}")
            decades = sorted([int(d) for d in df['decade'].dropna().unique()])
            print(f"   ✓ Décadas cubiertas: {decades[0]}s - {decades[-1]}s ({len(decades)} décadas)")
        
        return df
    
    except Exception as e:
        print(f"❌ ERROR al procesar fechas: {str(e)}")
        import traceback
        traceback.print_exc()
        return df


# ==============================================================================
# FUNCIÓN 3: ELIMINACIÓN DE DUPLICADOS
# ==============================================================================
def remove_duplicates(df):
    """
    Elimina registros duplicados basándose en la columna 'id'.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        Dataset potencialmente con duplicados
    
    Retorna:
    --------
    pandas.DataFrame
        Dataset sin duplicados
    
    NOTA PARA INFORME:
    "Se identificaron y eliminaron registros duplicados utilizando el 
    identificador único de cada evento sísmico."
    """
    print("\n[3/6] Eliminando duplicados...")
    
    initial_count = len(df)
    
    # Verificar si existe la columna 'id'
    if 'id' in df.columns:
        # Eliminar duplicados basándose en 'id'
        df = df.drop_duplicates(subset=['id'], keep='first')
        duplicates_removed = initial_count - len(df)
        print(f"   ✓ Duplicados eliminados (por 'id'): {duplicates_removed:,}")
    else:
        # Si no existe 'id', eliminar duplicados por todas las columnas principales
        print("   ⚠ Columna 'id' no encontrada, eliminando duplicados por columnas principales...")
        df = df.drop_duplicates(subset=['time', 'latitude', 'longitude', 'mag', 'depth'], keep='first')
        duplicates_removed = initial_count - len(df)
        print(f"   ✓ Duplicados eliminados: {duplicates_removed:,}")
    
    print(f"   ✓ Registros restantes: {len(df):,}")
    
    return df


# ==============================================================================
# FUNCIÓN 4: ELIMINACIÓN DE VALORES FALTANTES CRÍTICOS
# ==============================================================================
def remove_critical_missing_values(df):
    """
    Elimina filas con valores faltantes en columnas críticas para el análisis.
    
    Columnas críticas: mag, depth, latitude, longitude, time
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        Dataset con posibles valores faltantes
    
    Retorna:
    --------
    pandas.DataFrame
        Dataset sin valores faltantes en columnas críticas
    
    NOTA PARA INFORME:
    "Se eliminaron registros con valores faltantes en variables esenciales 
    (magnitud, profundidad, coordenadas geográficas y tiempo), garantizando 
    la integridad del dataset para análisis posteriores."
    """
    print("\n[4/6] Eliminando valores faltantes críticos...")
    
    initial_count = len(df)
    
    # Columnas críticas que no deben tener valores faltantes
    critical_columns = ['mag', 'depth', 'latitude', 'longitude', 'time']
    
    # Mostrar cantidad de valores faltantes antes de eliminar
    print("   Valores faltantes por columna (antes):")
    for col in critical_columns:
        if col in df.columns:
            missing = df[col].isna().sum()
            pct = (missing / len(df)) * 100
            print(f"      - {col}: {missing:,} ({pct:.2f}%)")
    
    # Eliminar filas con valores faltantes en columnas críticas
    df = df.dropna(subset=[col for col in critical_columns if col in df.columns])
    
    rows_removed = initial_count - len(df)
    pct_removed = (rows_removed / initial_count) * 100
    
    print(f"\n   ✓ Filas eliminadas: {rows_removed:,} ({pct_removed:.2f}%)")
    print(f"   ✓ Registros restantes: {len(df):,}")
    
    return df


# ==============================================================================
# FUNCIÓN 5: LIMPIEZA ADICIONAL Y VALIDACIÓN
# ==============================================================================
def additional_cleaning(df):
    """
    Realiza validaciones y limpiezas adicionales sobre el dataset.
    
    - Valida rangos de magnitud (0 - 10)
    - Valida rangos de profundidad (0 - 700 km)
    - Valida coordenadas (-90 a 90 lat, -180 a 180 lon)
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        Dataset a validar
    
    Retorna:
    --------
    pandas.DataFrame
        Dataset validado y limpio
    
    NOTA PARA INFORME:
    "Se aplicaron filtros de validación para garantizar que los valores de 
    magnitud, profundidad y coordenadas geográficas estuvieran dentro de 
    rangos físicamente plausibles."
    """
    print("\n[5/6] Aplicando validaciones y limpieza adicional...")
    
    initial_count = len(df)
    
    # Validar magnitud (0 - 10)
    if 'mag' in df.columns:
        invalid_mag = ((df['mag'] < 0) | (df['mag'] > 10)).sum()
        df = df[(df['mag'] >= 0) & (df['mag'] <= 10)]
        if invalid_mag > 0:
            print(f"   ✓ Registros con magnitud inválida eliminados: {invalid_mag:,}")
    
    # Validar profundidad (0 - 700 km, típico rango sísmico)
    if 'depth' in df.columns:
        invalid_depth = ((df['depth'] < 0) | (df['depth'] > 700)).sum()
        df = df[(df['depth'] >= 0) & (df['depth'] <= 700)]
        if invalid_depth > 0:
            print(f"   ✓ Registros con profundidad inválida eliminados: {invalid_depth:,}")
    
    # Validar coordenadas geográficas
    if 'latitude' in df.columns and 'longitude' in df.columns:
        invalid_coords = (
            (df['latitude'] < -90) | (df['latitude'] > 90) |
            (df['longitude'] < -180) | (df['longitude'] > 180)
        ).sum()
        df = df[
            (df['latitude'] >= -90) & (df['latitude'] <= 90) &
            (df['longitude'] >= -180) & (df['longitude'] <= 180)
        ]
        if invalid_coords > 0:
            print(f"   ✓ Registros con coordenadas inválidas eliminados: {invalid_coords:,}")
    
    total_removed = initial_count - len(df)
    if total_removed > 0:
        print(f"   ✓ Total de registros eliminados en validación: {total_removed:,}")
    else:
        print(f"   ✓ Todos los registros pasaron las validaciones")
    
    print(f"   ✓ Registros finales: {len(df):,}")
    
    return df


# ==============================================================================
# FUNCIÓN 6: EXPORTAR DATASET LIMPIO
# ==============================================================================
def export_clean_data(df, output_path):
    """
    Exporta el dataset limpio a un archivo CSV.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        Dataset limpio
    output_path : str
        Ruta donde guardar el archivo CSV
    
    NOTA PARA INFORME:
    "El dataset limpio fue exportado en formato CSV para su uso en análisis 
    posteriores, visualizaciones y modelado analítico."
    """
    print("\n[6/6] Exportando dataset limpio...")
    
    try:
        # Exportar a CSV
        df.to_csv(output_path, index=False)
        
        file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
        
        print(f"   ✓ Dataset exportado exitosamente")
        print(f"   ✓ Ubicación: {output_path}")
        print(f"   ✓ Tamaño: {file_size_mb:.2f} MB")
        print(f"   ✓ Registros: {len(df):,}")
        print(f"   ✓ Columnas: {len(df.columns)}")
        
    except Exception as e:
        print(f"❌ ERROR al exportar datos: {str(e)}")


# ==============================================================================
# FUNCIÓN 7: GENERAR REPORTE DE LIMPIEZA
# ==============================================================================
def generate_cleaning_report(df_original, df_clean):
    """
    Genera un reporte de texto con estadísticas del proceso de limpieza.
    
    Parámetros:
    -----------
    df_original : pandas.DataFrame
        Dataset original
    df_clean : pandas.DataFrame
        Dataset limpio
    """
    print("\n" + "="*80)
    print("REPORTE DE LIMPIEZA DE DATOS")
    print("="*80)
    
    report_path = os.path.join(RESULTS_PATH, 'cleaning_report.txt')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("REPORTE DE LIMPIEZA DE DATOS - TERREMOTOS USGS\n")
        f.write("="*80 + "\n")
        f.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("ESTADÍSTICAS GENERALES:\n")
        f.write("-" * 80 + "\n")
        f.write(f"Registros originales:        {len(df_original):>15,}\n")
        f.write(f"Registros finales:           {len(df_clean):>15,}\n")
        f.write(f"Registros eliminados:        {len(df_original) - len(df_clean):>15,}\n")
        f.write(f"Porcentaje retenido:         {(len(df_clean)/len(df_original)*100):>14.2f}%\n\n")
        
        f.write("RANGO TEMPORAL:\n")
        f.write("-" * 80 + "\n")
        f.write(f"Año inicial:                 {df_clean['year'].min():>15.0f}\n")
        f.write(f"Año final:                   {df_clean['year'].max():>15.0f}\n")
        f.write(f"Años cubiertos:              {df_clean['year'].max() - df_clean['year'].min():>15.0f}\n\n")
        
        f.write("DISTRIBUCIÓN POR DÉCADA:\n")
        f.write("-" * 80 + "\n")
        decade_counts = df_clean['decade'].value_counts().sort_index()
        for decade, count in decade_counts.items():
            f.write(f"  {int(decade)}s:                     {count:>15,}\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("DATASET LISTO PARA ANÁLISIS\n")
        f.write("="*80 + "\n")
    
    print(f"\n✓ Reporte guardado en: {report_path}")


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================
def main():
    """
    Función principal que ejecuta todo el pipeline de limpieza.
    """
    
    # NOTA: Para pruebas rápidas, puedes usar sample_size (ej. 100000)
    # Para producción, déjalo en None para procesar todo el dataset
    SAMPLE_SIZE = None  # Cambiar a un número (ej. 100000) para pruebas rápidas
    
    # Paso 1: Cargar datos
    df = load_earthquake_data(RAW_DATA_PATH, sample_size=SAMPLE_SIZE)
    df_original = df.copy()  # Guardar copia para el reporte
    
    # Paso 2: Procesar fechas
    df = process_datetime_columns(df)
    
    # Paso 3: Eliminar duplicados
    df = remove_duplicates(df)
    
    # Paso 4: Eliminar valores faltantes críticos
    df = remove_critical_missing_values(df)
    
    # Paso 5: Limpieza y validación adicional
    df = additional_cleaning(df)
    
    # Paso 6: Exportar dataset limpio
    export_clean_data(df, PROCESSED_DATA_PATH)
    
    # Paso 7: Generar reporte
    generate_cleaning_report(df_original, df)
    
    print("\n" + "="*80)
    print("✓✓✓ LIMPIEZA COMPLETADA EXITOSAMENTE ✓✓✓")
    print("="*80)
    print("\nPróximos pasos:")
    print("  1. Ejecutar análisis descriptivo: python scripts/python/02_descriptive_analysis.py")
    print("  2. Generar visualizaciones: python scripts/python/03_visualizations.py")
    print("  3. Crear modelos analíticos: python scripts/python/04_analytical_models.py")
    print("="*80 + "\n")


# ==============================================================================
# EJECUCIÓN DEL SCRIPT
# ==============================================================================
if __name__ == "__main__":
    main()
