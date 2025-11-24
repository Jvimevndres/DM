"""
==============================================================================
SCRIPT: Visualizaciones en Python - Terremotos USGS
==============================================================================
Autor: Jaime
Proyecto: Minería de Datos - Análisis de Terremotos Globales
Fecha: Noviembre 2025

DESCRIPCIÓN:
Este script genera visualizaciones avanzadas del dataset de terremotos,
incluyendo histogramas, boxplots, gráficos de línea y scatter plots.
Todas las figuras se guardan en alta resolución.

VISUALIZACIONES GENERADAS:
  1. Histograma de distribución de magnitudes
  2. Histograma de distribución de profundidades
  3. Boxplots de magnitud por década
  4. Gráfico de línea: tendencia de sismos por año
  5. Gráfico de línea: tendencia de magnitud promedio por año
  6. Scatter plot: profundidad vs magnitud
  7. Heatmap de correlaciones
  8. Gráfico de barras: Top 15 regiones más afectadas

INPUT:
  - Archivo: data/processed/earthquakes_clean.csv

OUTPUT:
  - Figuras: outputs/figures/*.png
==============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo de visualizaciones
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

# ==============================================================================
# CONFIGURACIÓN DE RUTAS
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLEAN_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'earthquakes_clean.csv')
FIGURES_PATH = os.path.join(BASE_DIR, 'outputs', 'figures')

os.makedirs(FIGURES_PATH, exist_ok=True)

print("="*80)
print("GENERACIÓN DE VISUALIZACIONES - TERREMOTOS USGS")
print("="*80)
print(f"Dataset: {CLEAN_DATA_PATH}")
print(f"Salida: {FIGURES_PATH}")
print("="*80 + "\n")


# ==============================================================================
# FUNCIÓN: CARGAR DATOS
# ==============================================================================
def load_data(file_path):
    """Carga el dataset limpio."""
    print("[0/8] Cargando datos...")
    
    try:
        df = pd.read_csv(file_path, parse_dates=['time'])
        print(f"   ✓ Datos cargados: {len(df):,} registros\n")
        return df
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo {file_path}")
        print("   Ejecuta primero: python scripts/python/01_data_cleaning.py")
        return None


# ==============================================================================
# VISUALIZACIÓN 1: HISTOGRAMA DE MAGNITUDES
# ==============================================================================
def plot_magnitude_distribution(df):
    """
    Histograma de la distribución de magnitudes.
    
    NOTA PARA INFORME:
    "La distribución de magnitudes muestra un patrón característico con 
    mayor frecuencia de eventos de baja magnitud y disminución exponencial 
    hacia magnitudes altas, consistente con la ley de Gutenberg-Richter."
    """
    print("[1/8] Generando histograma de magnitudes...")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Histograma con KDE
    ax.hist(df['mag'], bins=50, color='steelblue', alpha=0.7, edgecolor='black')
    
    # Línea de densidad
    ax2 = ax.twinx()
    df['mag'].plot(kind='kde', ax=ax2, color='red', linewidth=2, label='Densidad')
    
    # Añadir línea vertical para la media
    mean_mag = df['mag'].mean()
    ax.axvline(mean_mag, color='darkgreen', linestyle='--', linewidth=2, 
               label=f'Media = {mean_mag:.2f}')
    
    # Añadir línea vertical para la mediana
    median_mag = df['mag'].median()
    ax.axvline(median_mag, color='orange', linestyle='--', linewidth=2,
               label=f'Mediana = {median_mag:.2f}')
    
    ax.set_xlabel('Magnitud', fontsize=13, fontweight='bold')
    ax.set_ylabel('Frecuencia', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Densidad', fontsize=13, fontweight='bold')
    ax.set_title('Distribución de Magnitudes de Terremotos', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '01_magnitude_distribution.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 2: HISTOGRAMA DE PROFUNDIDADES
# ==============================================================================
def plot_depth_distribution(df):
    """
    Histograma de la distribución de profundidades.
    
    NOTA PARA INFORME:
    "La distribución de profundidades revela los diferentes tipos de 
    sismos: superficiales (0-70 km), intermedios (70-300 km) y profundos 
    (300-700 km)."
    """
    print("[2/8] Generando histograma de profundidades...")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Histograma
    n, bins, patches = ax.hist(df['depth'], bins=60, color='coral', 
                                alpha=0.7, edgecolor='black')
    
    # Colorear según tipo de sismo
    for i in range(len(patches)):
        if bins[i] < 70:
            patches[i].set_facecolor('lightcoral')  # Superficial
        elif bins[i] < 300:
            patches[i].set_facecolor('orange')       # Intermedio
        else:
            patches[i].set_facecolor('darkred')      # Profundo
    
    # Líneas divisorias
    ax.axvline(70, color='black', linestyle='--', linewidth=1.5, alpha=0.7,
               label='Límite superficial/intermedio (70 km)')
    ax.axvline(300, color='black', linestyle='--', linewidth=1.5, alpha=0.7,
               label='Límite intermedio/profundo (300 km)')
    
    # Estadísticas
    mean_depth = df['depth'].mean()
    median_depth = df['depth'].median()
    
    ax.axvline(mean_depth, color='blue', linestyle='-', linewidth=2,
               label=f'Media = {mean_depth:.1f} km')
    ax.axvline(median_depth, color='green', linestyle='-', linewidth=2,
               label=f'Mediana = {median_depth:.1f} km')
    
    ax.set_xlabel('Profundidad (km)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Frecuencia', fontsize=13, fontweight='bold')
    ax.set_title('Distribución de Profundidades de Terremotos', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '02_depth_distribution.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 3: BOXPLOTS DE MAGNITUD POR DÉCADA
# ==============================================================================
def plot_magnitude_by_decade(df):
    """
    Boxplots comparativos de magnitud por década.
    
    NOTA PARA INFORME:
    "El análisis por décadas muestra la variabilidad de magnitudes a lo 
    largo del tiempo, permitiendo identificar períodos con mayor actividad 
    sísmica significativa."
    """
    print("[3/8] Generando boxplots de magnitud por década...")
    
    # Filtrar décadas con suficientes datos
    decade_counts = df['decade'].value_counts()
    valid_decades = decade_counts[decade_counts >= 100].index
    df_filtered = df[df['decade'].isin(valid_decades)]
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Boxplot
    decades_sorted = sorted(df_filtered['decade'].unique())
    df_filtered['decade_str'] = df_filtered['decade'].astype(int).astype(str) + 's'
    
    sns.boxplot(data=df_filtered, x='decade_str', y='mag', 
                palette='viridis', ax=ax)
    
    ax.set_xlabel('Década', fontsize=13, fontweight='bold')
    ax.set_ylabel('Magnitud', fontsize=13, fontweight='bold')
    ax.set_title('Distribución de Magnitudes por Década', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Rotar etiquetas
    plt.xticks(rotation=45)
    
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '03_magnitude_by_decade.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 4: TENDENCIA DE SISMOS POR AÑO
# ==============================================================================
def plot_earthquakes_per_year(df):
    """
    Gráfico de línea mostrando la tendencia temporal.
    
    NOTA PARA INFORME:
    "Se observa un incremento significativo en el número de sismos 
    registrados a partir de mediados del siglo XX, reflejando la expansión 
    de la red global de monitoreo sísmico más que un aumento real en la 
    actividad sísmica."
    """
    print("[4/8] Generando tendencia de sismos por año...")
    
    # Agrupar por año
    yearly_counts = df.groupby('year').size().reset_index(name='count')
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Gráfico de línea
    ax.plot(yearly_counts['year'], yearly_counts['count'], 
            color='darkblue', linewidth=2, marker='o', markersize=3, alpha=0.7)
    
    # Añadir línea de tendencia (regresión lineal simple)
    z = np.polyfit(yearly_counts['year'], yearly_counts['count'], 1)
    p = np.poly1d(z)
    ax.plot(yearly_counts['year'], p(yearly_counts['year']), 
            "r--", linewidth=2, alpha=0.8, label=f'Tendencia lineal')
    
    ax.set_xlabel('Año', fontsize=13, fontweight='bold')
    ax.set_ylabel('Número de Terremotos', fontsize=13, fontweight='bold')
    ax.set_title('Tendencia Temporal: Número de Terremotos por Año', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Formato del eje x
    ax.set_xlim(yearly_counts['year'].min(), yearly_counts['year'].max())
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '04_earthquakes_per_year.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 5: MAGNITUD PROMEDIO POR AÑO
# ==============================================================================
def plot_average_magnitude_per_year(df):
    """
    Gráfico de línea de magnitud promedio por año.
    
    NOTA PARA INFORME:
    "La magnitud promedio anual se mantiene relativamente estable a lo 
    largo del tiempo, con variaciones que reflejan la aleatoriedad 
    natural de los procesos sísmicos."
    """
    print("[5/8] Generando magnitud promedio por año...")
    
    # Agrupar por año y calcular media
    yearly_avg_mag = df.groupby('year')['mag'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Gráfico de línea con área sombreada
    ax.plot(yearly_avg_mag['year'], yearly_avg_mag['mag'], 
            color='darkgreen', linewidth=2, marker='o', markersize=3, alpha=0.7)
    
    # Añadir banda de confianza (desviación estándar)
    yearly_std = df.groupby('year')['mag'].std().reset_index()
    ax.fill_between(yearly_avg_mag['year'], 
                     yearly_avg_mag['mag'] - yearly_std['mag'],
                     yearly_avg_mag['mag'] + yearly_std['mag'],
                     alpha=0.2, color='green')
    
    # Línea horizontal para la media global
    global_mean = df['mag'].mean()
    ax.axhline(global_mean, color='red', linestyle='--', linewidth=2,
               label=f'Media global = {global_mean:.2f}')
    
    ax.set_xlabel('Año', fontsize=13, fontweight='bold')
    ax.set_ylabel('Magnitud Promedio', fontsize=13, fontweight='bold')
    ax.set_title('Evolución de la Magnitud Promedio por Año', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '05_average_magnitude_per_year.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 6: SCATTER PLOT - PROFUNDIDAD VS MAGNITUD
# ==============================================================================
def plot_depth_vs_magnitude(df, sample_size=10000):
    """
    Scatter plot de profundidad vs magnitud.
    
    Parámetros:
    -----------
    sample_size : int
        Número de puntos a graficar (muestra aleatoria si el dataset es grande)
    
    NOTA PARA INFORME:
    "El diagrama de dispersión entre profundidad y magnitud permite 
    visualizar la relación entre ambas variables, complementando el 
    análisis de correlación."
    """
    print(f"[6/8] Generando scatter plot profundidad vs magnitud (n={sample_size})...")
    
    # Si el dataset es muy grande, tomar una muestra
    if len(df) > sample_size:
        df_sample = df.sample(n=sample_size, random_state=42)
        print(f"   (usando muestra aleatoria de {sample_size:,} registros)")
    else:
        df_sample = df
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Scatter plot con colormap por magnitud
    scatter = ax.scatter(df_sample['depth'], df_sample['mag'], 
                        c=df_sample['mag'], cmap='YlOrRd', 
                        alpha=0.5, s=20, edgecolors='black', linewidth=0.3)
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Magnitud', fontsize=12, fontweight='bold')
    
    # Línea de regresión
    z = np.polyfit(df_sample['depth'], df_sample['mag'], 1)
    p = np.poly1d(z)
    ax.plot(df_sample['depth'], p(df_sample['depth']), 
            "b--", linewidth=2, alpha=0.8, label=f'Regresión lineal: y={z[0]:.4f}x+{z[1]:.2f}')
    
    ax.set_xlabel('Profundidad (km)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Magnitud', fontsize=13, fontweight='bold')
    ax.set_title('Relación entre Profundidad y Magnitud', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '06_depth_vs_magnitude.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 7: HEATMAP DE CORRELACIONES
# ==============================================================================
def plot_correlation_heatmap(df):
    """
    Heatmap de correlaciones entre variables numéricas.
    
    NOTA PARA INFORME:
    "La matriz de correlación permite identificar relaciones lineales 
    entre las variables cuantitativas del dataset."
    """
    print("[7/8] Generando heatmap de correlaciones...")
    
    # Seleccionar columnas numéricas relevantes
    numeric_cols = ['mag', 'depth', 'latitude', 'longitude']
    df_corr = df[numeric_cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Heatmap
    sns.heatmap(df_corr, annot=True, fmt='.3f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                ax=ax, vmin=-1, vmax=1)
    
    ax.set_title('Matriz de Correlación - Variables Sísmicas', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '07_correlation_heatmap.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# VISUALIZACIÓN 8: TOP REGIONES MÁS AFECTADAS
# ==============================================================================
def plot_top_regions(df, top_n=15):
    """
    Gráfico de barras de las regiones más afectadas.
    
    NOTA PARA INFORME:
    "Las regiones con mayor actividad sísmica registrada corresponden 
    principalmente al Cinturón de Fuego del Pacífico y zonas de alta 
    actividad tectónica."
    """
    print(f"[8/8] Generando gráfico de top {top_n} regiones...")
    
    # Extraer región (como en el análisis descriptivo)
    def extract_region(place_str):
        if pd.isna(place_str):
            return 'Unknown'
        if ',' in place_str:
            return place_str.split(',')[-1].strip()
        else:
            words = place_str.split()
            return words[-1] if len(words) > 0 else 'Unknown'
    
    df['region'] = df['place'].apply(extract_region)
    
    # Top N regiones
    top_regions = df['region'].value_counts().head(top_n)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Gráfico de barras horizontal
    colors = plt.cm.viridis(np.linspace(0, 1, len(top_regions)))
    ax.barh(range(len(top_regions)), top_regions.values, color=colors, 
            edgecolor='black', linewidth=0.5)
    
    ax.set_yticks(range(len(top_regions)))
    ax.set_yticklabels(top_regions.index)
    ax.invert_yaxis()
    
    ax.set_xlabel('Número de Terremotos', fontsize=13, fontweight='bold')
    ax.set_ylabel('Región', fontsize=13, fontweight='bold')
    ax.set_title(f'Top {top_n} Regiones con Mayor Actividad Sísmica', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Añadir valores en las barras
    for i, v in enumerate(top_regions.values):
        ax.text(v + top_regions.max() * 0.01, i, f'{v:,}', 
                va='center', fontweight='bold')
    
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, '08_top_regions.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"   ✓ Guardado: {output_path}\n")


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================
def main():
    """
    Función principal que genera todas las visualizaciones.
    """
    
    # Cargar datos
    df = load_data(CLEAN_DATA_PATH)
    
    if df is None:
        print("❌ No se pudo continuar sin datos. Abortando.")
        return
    
    # Generar todas las visualizaciones
    plot_magnitude_distribution(df)
    plot_depth_distribution(df)
    plot_magnitude_by_decade(df)
    plot_earthquakes_per_year(df)
    plot_average_magnitude_per_year(df)
    plot_depth_vs_magnitude(df, sample_size=10000)
    plot_correlation_heatmap(df)
    plot_top_regions(df, top_n=15)
    
    print("=" * 80)
    print("✓✓✓ VISUALIZACIONES GENERADAS EXITOSAMENTE ✓✓✓")
    print("=" * 80)
    print(f"\nTodas las figuras guardadas en: {FIGURES_PATH}")
    print("\nPróximos pasos:")
    print("  1. Revisar figuras generadas")
    print("  2. Crear mapas en R: Rscript scripts/R/02_maps_visualization.R")
    print("  3. Ejecutar modelos: python scripts/python/04_analytical_models.py")
    print("=" * 80 + "\n")


# ==============================================================================
# EJECUCIÓN DEL SCRIPT
# ==============================================================================
if __name__ == "__main__":
    main()
