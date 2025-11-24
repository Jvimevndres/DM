"""
==============================================================================
SCRIPT: Modelos Analíticos - Terremotos USGS
==============================================================================
Autor: Jaime
Proyecto: Minería de Datos - Análisis de Terremotos Globales
Fecha: Noviembre 2025

DESCRIPCIÓN:
Este script implementa modelos analíticos avanzados sobre el dataset de 
terremotos, incluyendo regresión lineal, clustering (KMeans), y análisis
predictivo. Los modelos son modulares y reutilizables.

MODELOS IMPLEMENTADOS:
  1. Regresión Lineal Simple: magnitud ~ profundidad
  2. Regresión Lineal Múltiple: magnitud ~ profundidad + coordenadas
  3. Clustering KMeans: Agrupación de sismos por características
  4. Análisis de componentes principales (PCA)

INPUT:
  - Archivo: data/processed/earthquakes_clean.csv

OUTPUT:
  - Modelos entrenados: outputs/results/models/
  - Visualizaciones: outputs/figures/model_*.png
  - Reportes: outputs/results/model_report.txt
==============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.metrics import silhouette_score, davies_bouldin_score
import joblib
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# ==============================================================================
# CONFIGURACIÓN DE RUTAS
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLEAN_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'earthquakes_clean.csv')
FIGURES_PATH = os.path.join(BASE_DIR, 'outputs', 'figures')
RESULTS_PATH = os.path.join(BASE_DIR, 'outputs', 'results')
MODELS_PATH = os.path.join(RESULTS_PATH, 'models')

os.makedirs(MODELS_PATH, exist_ok=True)

print("="*80)
print("MODELOS ANALÍTICOS - TERREMOTOS USGS")
print("="*80)
print(f"Dataset: {CLEAN_DATA_PATH}")
print("="*80 + "\n")


# ==============================================================================
# FUNCIÓN: CARGAR DATOS
# ==============================================================================
def load_data(file_path, sample_size=None):
    """
    Carga el dataset limpio.
    
    Parámetros:
    -----------
    sample_size : int, opcional
        Si se especifica, usa una muestra aleatoria (útil para pruebas rápidas)
    """
    print("[0/5] Cargando datos...")
    
    try:
        df = pd.read_csv(file_path, parse_dates=['time'])
        
        if sample_size and len(df) > sample_size:
            print(f"   (usando muestra de {sample_size:,} registros)")
            df = df.sample(n=sample_size, random_state=42)
        
        print(f"   ✓ Datos cargados: {len(df):,} registros\n")
        return df
    
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo {file_path}")
        print("   Ejecuta primero: python scripts/python/01_data_cleaning.py")
        return None


# ==============================================================================
# MODELO 1: REGRESIÓN LINEAL SIMPLE (mag ~ depth)
# ==============================================================================
def linear_regression_simple(df):
    """
    Regresión lineal simple: magnitud predicha por profundidad.
    
    NOTA PARA INFORME:
    "Se implementó un modelo de regresión lineal simple para evaluar la 
    capacidad predictiva de la profundidad sobre la magnitud del terremoto."
    
    PARA PRESENTACIÓN:
    "El modelo de regresión lineal simple mostró un R² de X.XX, indicando 
    que la profundidad explica solo un X% de la varianza en la magnitud."
    """
    print("[1/5] Modelo de Regresión Lineal Simple: mag ~ depth...")
    
    # Preparar datos
    df_model = df[['depth', 'mag']].dropna()
    X = df_model[['depth']].values
    y = df_model['mag'].values
    
    # Entrenar modelo
    model = LinearRegression()
    model.fit(X, y)
    
    # Predicciones
    y_pred = model.predict(X)
    
    # Métricas
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)
    
    # Mostrar resultados
    print(f"\n   📊 RESULTADOS:")
    print(f"      Coeficiente (pendiente):  {model.coef_[0]:.6f}")
    print(f"      Intercepto:               {model.intercept_:.4f}")
    print(f"      R² (coef. determinación): {r2:.4f}")
    print(f"      RMSE:                     {rmse:.4f}")
    print(f"      MAE:                      {mae:.4f}")
    
    print(f"\n   📝 ECUACIÓN DEL MODELO:")
    print(f"      mag = {model.coef_[0]:.6f} * depth + {model.intercept_:.4f}")
    
    print(f"\n   💡 INTERPRETACIÓN:")
    if abs(model.coef_[0]) < 0.001:
        print(f"      La profundidad tiene un efecto MÍNIMO sobre la magnitud.")
    elif model.coef_[0] > 0:
        print(f"      Por cada km de profundidad, la magnitud aumenta {model.coef_[0]:.6f} unidades.")
    else:
        print(f"      Por cada km de profundidad, la magnitud disminuye {abs(model.coef_[0]):.6f} unidades.")
    
    if r2 < 0.1:
        print(f"      El modelo tiene BAJO poder predictivo (R²={r2:.4f}).")
        print(f"      La profundidad NO es un buen predictor de la magnitud.")
    elif r2 < 0.5:
        print(f"      El modelo tiene poder predictivo MODERADO (R²={r2:.4f}).")
    else:
        print(f"      El modelo tiene BUEN poder predictivo (R²={r2:.4f}).")
    
    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Subplot 1: Scatter plot con línea de regresión
    sample_indices = np.random.choice(len(X), min(10000, len(X)), replace=False)
    ax1.scatter(X[sample_indices], y[sample_indices], alpha=0.3, s=10, label='Datos observados')
    ax1.plot(X, y_pred, color='red', linewidth=2, label='Línea de regresión')
    ax1.set_xlabel('Profundidad (km)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Magnitud', fontsize=12, fontweight='bold')
    ax1.set_title('Regresión Lineal: Magnitud vs Profundidad', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Residuos
    residuals = y - y_pred
    ax2.scatter(y_pred[sample_indices], residuals[sample_indices], alpha=0.3, s=10)
    ax2.axhline(0, color='red', linestyle='--', linewidth=2)
    ax2.set_xlabel('Valores Predichos', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Residuos', fontsize=12, fontweight='bold')
    ax2.set_title('Análisis de Residuos', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, 'model_01_linear_regression_simple.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n   ✓ Visualización guardada: {output_path}")
    
    # Guardar modelo
    model_path = os.path.join(MODELS_PATH, 'linear_regression_simple.pkl')
    joblib.dump(model, model_path)
    print(f"   ✓ Modelo guardado: {model_path}\n")
    
    return {
        'model': model,
        'r2': r2,
        'rmse': rmse,
        'mae': mae,
        'coef': model.coef_[0],
        'intercept': model.intercept_
    }


# ==============================================================================
# MODELO 2: REGRESIÓN LINEAL MÚLTIPLE (mag ~ depth + lat + lon)
# ==============================================================================
def linear_regression_multiple(df):
    """
    Regresión lineal múltiple: magnitud predicha por profundidad y coordenadas.
    
    NOTA PARA INFORME:
    "Se amplió el modelo a una regresión múltiple incluyendo coordenadas 
    geográficas para evaluar si la ubicación mejora la predicción de magnitud."
    """
    print("[2/5] Modelo de Regresión Lineal Múltiple: mag ~ depth + lat + lon...")
    
    # Preparar datos
    df_model = df[['depth', 'latitude', 'longitude', 'mag']].dropna()
    X = df_model[['depth', 'latitude', 'longitude']].values
    y = df_model['mag'].values
    
    # Entrenar modelo
    model = LinearRegression()
    model.fit(X, y)
    
    # Predicciones
    y_pred = model.predict(X)
    
    # Métricas
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)
    
    # Mostrar resultados
    print(f"\n   📊 RESULTADOS:")
    print(f"      Coeficientes:")
    print(f"         - depth:      {model.coef_[0]:.6f}")
    print(f"         - latitude:   {model.coef_[1]:.6f}")
    print(f"         - longitude:  {model.coef_[2]:.6f}")
    print(f"      Intercepto:               {model.intercept_:.4f}")
    print(f"      R²:                       {r2:.4f}")
    print(f"      RMSE:                     {rmse:.4f}")
    print(f"      MAE:                      {mae:.4f}")
    
    print(f"\n   💡 INTERPRETACIÓN:")
    print(f"      El modelo múltiple tiene R²={r2:.4f}, comparado con el modelo simple.")
    
    # Guardar modelo
    model_path = os.path.join(MODELS_PATH, 'linear_regression_multiple.pkl')
    joblib.dump(model, model_path)
    print(f"\n   ✓ Modelo guardado: {model_path}\n")
    
    return {
        'model': model,
        'r2': r2,
        'rmse': rmse,
        'mae': mae
    }


# ==============================================================================
# MODELO 3: CLUSTERING (KMEANS)
# ==============================================================================
def kmeans_clustering(df, n_clusters=5):
    """
    Clustering KMeans para agrupar sismos por características.
    
    Parámetros:
    -----------
    n_clusters : int
        Número de clusters a crear
    
    NOTA PARA INFORME:
    "Se implementó un algoritmo de clustering KMeans para identificar 
    patrones naturales de agrupación en los datos sísmicos, considerando 
    magnitud, profundidad y ubicación geográfica."
    
    PARA PRESENTACIÓN:
    "El análisis de clustering reveló X grupos distintos de actividad 
    sísmica, caracterizados por diferentes combinaciones de magnitud, 
    profundidad y ubicación geográfica."
    """
    print(f"[3/5] Clustering KMeans (k={n_clusters})...")
    
    # Preparar datos
    features = ['mag', 'depth', 'latitude', 'longitude']
    df_model = df[features].dropna()
    
    # Tomar muestra si es muy grande (para rendimiento)
    if len(df_model) > 100000:
        print(f"   (usando muestra de 100,000 registros para clustering)")
        df_model = df_model.sample(n=100000, random_state=42)
    
    X = df_model.values
    
    # Escalar datos (importante para KMeans)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Entrenar modelo KMeans
    print(f"   Entrenando KMeans con {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10, max_iter=300)
    clusters = kmeans.fit_predict(X_scaled)
    
    # Métricas de evaluación
    silhouette = silhouette_score(X_scaled, clusters)
    davies_bouldin = davies_bouldin_score(X_scaled, clusters)
    inertia = kmeans.inertia_
    
    print(f"\n   📊 MÉTRICAS DE CLUSTERING:")
    print(f"      Silhouette Score:         {silhouette:.4f}  (0 a 1, mayor es mejor)")
    print(f"      Davies-Bouldin Index:     {davies_bouldin:.4f}  (menor es mejor)")
    print(f"      Inertia (suma de dist²):  {inertia:.2f}")
    
    # Añadir clusters al DataFrame
    df_model['cluster'] = clusters
    
    # Estadísticas por cluster
    print(f"\n   📊 CARACTERÍSTICAS DE CADA CLUSTER:")
    print("   " + "-" * 70)
    
    for i in range(n_clusters):
        cluster_data = df_model[df_model['cluster'] == i]
        print(f"\n   CLUSTER {i} (n={len(cluster_data):,}):")
        print(f"      Magnitud promedio:    {cluster_data['mag'].mean():.2f}")
        print(f"      Profundidad promedio: {cluster_data['depth'].mean():.2f} km")
        print(f"      Latitud promedio:     {cluster_data['latitude'].mean():.2f}°")
        print(f"      Longitud promedio:    {cluster_data['longitude'].mean():.2f}°")
    
    # Visualización 1: Scatter plot mag vs depth coloreado por cluster
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    colors = plt.cm.viridis(np.linspace(0, 1, n_clusters))
    
    for i in range(n_clusters):
        cluster_data = df_model[df_model['cluster'] == i]
        ax1.scatter(cluster_data['depth'], cluster_data['mag'], 
                   c=[colors[i]], label=f'Cluster {i}', alpha=0.5, s=20)
    
    ax1.set_xlabel('Profundidad (km)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Magnitud', fontsize=12, fontweight='bold')
    ax1.set_title('Clusters: Magnitud vs Profundidad', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Visualización 2: Mapa con clusters
    for i in range(n_clusters):
        cluster_data = df_model[df_model['cluster'] == i]
        ax2.scatter(cluster_data['longitude'], cluster_data['latitude'], 
                   c=[colors[i]], label=f'Cluster {i}', alpha=0.5, s=20)
    
    ax2.set_xlabel('Longitud', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Latitud', fontsize=12, fontweight='bold')
    ax2.set_title('Clusters: Distribución Geográfica', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, 'model_02_kmeans_clustering.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n   ✓ Visualización guardada: {output_path}")
    
    # Guardar modelo y scaler
    model_path = os.path.join(MODELS_PATH, 'kmeans_model.pkl')
    scaler_path = os.path.join(MODELS_PATH, 'kmeans_scaler.pkl')
    joblib.dump(kmeans, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"   ✓ Modelo guardado: {model_path}")
    print(f"   ✓ Scaler guardado: {scaler_path}\n")
    
    return {
        'model': kmeans,
        'scaler': scaler,
        'silhouette': silhouette,
        'davies_bouldin': davies_bouldin,
        'clusters_df': df_model
    }


# ==============================================================================
# MODELO 4: ANÁLISIS DE COMPONENTES PRINCIPALES (PCA)
# ==============================================================================
def pca_analysis(df, n_components=3):
    """
    PCA para reducción de dimensionalidad y visualización.
    
    NOTA PARA INFORME:
    "Se aplicó Análisis de Componentes Principales (PCA) para reducir la 
    dimensionalidad de los datos y visualizar patrones en un espacio de 
    menor dimensión."
    """
    print(f"[4/5] Análisis de Componentes Principales (PCA, n={n_components})...")
    
    # Preparar datos
    features = ['mag', 'depth', 'latitude', 'longitude']
    df_model = df[features].dropna()
    
    # Muestra para visualización
    if len(df_model) > 50000:
        print(f"   (usando muestra de 50,000 registros)")
        df_model = df_model.sample(n=50000, random_state=42)
    
    X = df_model.values
    
    # Escalar datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Aplicar PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    # Varianza explicada
    print(f"\n   📊 VARIANZA EXPLICADA POR CADA COMPONENTE:")
    for i, var in enumerate(pca.explained_variance_ratio_):
        print(f"      PC{i+1}: {var*100:.2f}%")
    print(f"      Total acumulado: {sum(pca.explained_variance_ratio_)*100:.2f}%")
    
    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Subplot 1: Scatter de PC1 vs PC2 coloreado por magnitud
    scatter = ax1.scatter(X_pca[:, 0], X_pca[:, 1], c=df_model['mag'], 
                         cmap='YlOrRd', alpha=0.5, s=20)
    ax1.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', 
                   fontsize=12, fontweight='bold')
    ax1.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', 
                   fontsize=12, fontweight='bold')
    ax1.set_title('PCA: Primeras 2 Componentes Principales', 
                  fontsize=14, fontweight='bold')
    plt.colorbar(scatter, ax=ax1, label='Magnitud')
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Varianza explicada acumulada
    cumulative_var = np.cumsum(pca.explained_variance_ratio_)
    ax2.plot(range(1, n_components+1), cumulative_var, 'bo-', linewidth=2, markersize=8)
    ax2.set_xlabel('Número de Componentes', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Varianza Explicada Acumulada', fontsize=12, fontweight='bold')
    ax2.set_title('Varianza Explicada por Componentes', fontsize=14, fontweight='bold')
    ax2.set_ylim([0, 1])
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, 'model_03_pca_analysis.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n   ✓ Visualización guardada: {output_path}")
    
    # Guardar modelo
    model_path = os.path.join(MODELS_PATH, 'pca_model.pkl')
    joblib.dump(pca, model_path)
    print(f"   ✓ Modelo guardado: {model_path}\n")
    
    return {
        'model': pca,
        'explained_variance': pca.explained_variance_ratio_,
        'X_transformed': X_pca
    }


# ==============================================================================
# FUNCIÓN 5: MÉTODO DEL CODO PARA ENCONTRAR K ÓPTIMO
# ==============================================================================
def elbow_method(df, max_k=10):
    """
    Método del codo para determinar el número óptimo de clusters.
    
    NOTA PARA INFORME:
    "Se aplicó el método del codo para determinar el número óptimo de 
    clusters en el análisis KMeans."
    """
    print(f"[5/5] Método del Codo para K óptimo (k=2 a {max_k})...")
    
    # Preparar datos
    features = ['mag', 'depth', 'latitude', 'longitude']
    df_model = df[features].dropna()
    
    if len(df_model) > 50000:
        print(f"   (usando muestra de 50,000 registros)")
        df_model = df_model.sample(n=50000, random_state=42)
    
    X = df_model.values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Calcular inercia para diferentes valores de k
    inertias = []
    silhouette_scores = []
    k_range = range(2, max_k + 1)
    
    print(f"   Probando diferentes valores de k...")
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
        print(f"      k={k}: Inertia={kmeans.inertia_:.2f}, Silhouette={silhouette_scores[-1]:.4f}")
    
    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Subplot 1: Método del codo
    ax1.plot(k_range, inertias, 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel('Número de Clusters (k)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Inertia', fontsize=12, fontweight='bold')
    ax1.set_title('Método del Codo', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Silhouette Score
    ax2.plot(k_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
    ax2.set_xlabel('Número de Clusters (k)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Silhouette Score', fontsize=12, fontweight='bold')
    ax2.set_title('Silhouette Score por k', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(FIGURES_PATH, 'model_04_elbow_method.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n   ✓ Visualización guardada: {output_path}")
    
    # Sugerir k óptimo
    best_k = k_range[silhouette_scores.index(max(silhouette_scores))]
    print(f"\n   💡 SUGERENCIA: k óptimo = {best_k} (mayor Silhouette Score)")
    print()
    
    return {
        'k_range': list(k_range),
        'inertias': inertias,
        'silhouette_scores': silhouette_scores,
        'best_k': best_k
    }


# ==============================================================================
# FUNCIÓN: GENERAR REPORTE COMPLETO
# ==============================================================================
def generate_model_report(linear_simple, linear_multiple, clustering, pca, elbow):
    """Genera un reporte de texto con todos los resultados de los modelos."""
    print("Generando reporte de modelos...")
    
    report_path = os.path.join(RESULTS_PATH, 'model_report.txt')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("REPORTE DE MODELOS ANALÍTICOS - TERREMOTOS USGS\n")
        f.write("=" * 80 + "\n")
        f.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Regresión lineal simple
        f.write("1. REGRESIÓN LINEAL SIMPLE: mag ~ depth\n")
        f.write("-" * 80 + "\n")
        f.write(f"   Ecuación: mag = {linear_simple['coef']:.6f} * depth + {linear_simple['intercept']:.4f}\n")
        f.write(f"   R²:       {linear_simple['r2']:.4f}\n")
        f.write(f"   RMSE:     {linear_simple['rmse']:.4f}\n")
        f.write(f"   MAE:      {linear_simple['mae']:.4f}\n\n")
        
        # Regresión lineal múltiple
        f.write("2. REGRESIÓN LINEAL MÚLTIPLE: mag ~ depth + lat + lon\n")
        f.write("-" * 80 + "\n")
        f.write(f"   R²:       {linear_multiple['r2']:.4f}\n")
        f.write(f"   RMSE:     {linear_multiple['rmse']:.4f}\n")
        f.write(f"   MAE:      {linear_multiple['mae']:.4f}\n\n")
        
        # Clustering
        f.write("3. CLUSTERING KMEANS\n")
        f.write("-" * 80 + "\n")
        f.write(f"   Silhouette Score:     {clustering['silhouette']:.4f}\n")
        f.write(f"   Davies-Bouldin Index: {clustering['davies_bouldin']:.4f}\n")
        f.write(f"   K óptimo sugerido:    {elbow['best_k']}\n\n")
        
        # PCA
        f.write("4. ANÁLISIS DE COMPONENTES PRINCIPALES (PCA)\n")
        f.write("-" * 80 + "\n")
        for i, var in enumerate(pca['explained_variance']):
            f.write(f"   PC{i+1}: {var*100:.2f}% de varianza explicada\n")
        f.write(f"   Total acumulado: {sum(pca['explained_variance'])*100:.2f}%\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("FIN DEL REPORTE\n")
        f.write("=" * 80 + "\n")
    
    print(f"   ✓ Reporte guardado: {report_path}\n")


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================
def main():
    """
    Función principal que ejecuta todos los modelos analíticos.
    """
    
    # Cargar datos
    # NOTA: Puedes ajustar sample_size para pruebas rápidas (ej. 100000)
    df = load_data(CLEAN_DATA_PATH, sample_size=None)
    
    if df is None:
        print("❌ No se pudo continuar sin datos. Abortando.")
        return
    
    # Ejecutar modelos
    linear_simple = linear_regression_simple(df)
    linear_multiple = linear_regression_multiple(df)
    clustering = kmeans_clustering(df, n_clusters=5)
    pca = pca_analysis(df, n_components=3)
    elbow = elbow_method(df, max_k=10)
    
    # Generar reporte
    generate_model_report(linear_simple, linear_multiple, clustering, pca, elbow)
    
    print("=" * 80)
    print("✓✓✓ MODELOS ANALÍTICOS COMPLETADOS EXITOSAMENTE ✓✓✓")
    print("=" * 80)
    print(f"\nModelos guardados en: {MODELS_PATH}")
    print(f"Visualizaciones en: {FIGURES_PATH}")
    print(f"Reporte en: {RESULTS_PATH}")
    print("\nPróximos pasos:")
    print("  1. Revisar visualizaciones y reportes generados")
    print("  2. Integrar resultados en el informe final")
    print("  3. Preparar presentación con insights clave")
    print("=" * 80 + "\n")


# ==============================================================================
# EJECUCIÓN DEL SCRIPT
# ==============================================================================
if __name__ == "__main__":
    main()
