# 🚀 Quick Start Guide - 5 Minutos

## Ejecución Rápida en 3 Comandos

### 1️⃣ Clonar e Instalar (5 minutos)
```powershell
git clone https://github.com/Jvimevndres/DM.git
cd DM
.\setup.ps1
```

### 2️⃣ Descargar Dataset (3 minutos)
Ve a: **https://www.kaggle.com/datasets/usgs/earthquake-database**

Descarga `Earthquakes_USGS.csv` → Coloca en `data\raw\`

### 3️⃣ Ejecutar Pipeline (16 minutos)
```powershell
.\run_all.ps1
```

## ✅ Verificación de Resultados

Después de ejecutar, deberías tener:

### Datos Procesados
- `data\processed\earthquakes_clean.csv` (1.6 GB, 3.88M registros)

### Visualizaciones (16 archivos PNG)
```
outputs\figures\
├── magnitude_distribution.png
├── depth_distribution.png
├── magnitude_by_type.png
├── depth_by_type.png
├── earthquakes_timeline.png
├── magnitude_depth_scatter.png
├── correlation_heatmap.png
├── kmeans_scatter.png
├── kmeans_silhouette.png
├── elbow_curve.png
├── pca_2d_scatter.png
├── pca_variance_explained.png
├── world_earthquakes_map.png
├── high_magnitude_map.png
├── density_hexbin_map.png
└── depth_classification_map.png
```

### Estadísticas (5 archivos TXT)
```
outputs\results\
├── basic_statistics.txt
├── temporal_analysis.txt
├── geographic_analysis.txt
├── correlation_analysis.txt
└── extreme_events.txt
```

### Modelos ML (5 archivos .pkl)
```
outputs\results\models\
├── regresion_lineal_simple.pkl
├── regresion_lineal_multiple.pkl
├── kmeans_clusters.pkl
├── pca_model.pkl
└── elbow_inertias.pkl
```

## 🔍 Insights Rápidos

Abre estos archivos para ver resultados clave:

1. **basic_statistics.txt**: Media magnitud = 1.51, Profundidad = 21.45 km
2. **temporal_analysis.txt**: 935x aumento 2020s vs 1900s
3. **geographic_analysis.txt**: Top región = California (11.2% actividad global)
4. **correlation_analysis.txt**: r=0.35 magnitud-profundidad
5. **extreme_events.txt**: Top terremoto = 9.1 (Chile 2011)

## 📊 Ver Visualizaciones

Abre cualquier PNG en `outputs\figures\` con doble clic.

**Recomendados**:
- `world_earthquakes_map.png` - Mapa mundial impresionante
- `earthquakes_timeline.png` - 125 años de historia sísmica
- `magnitude_depth_scatter.png` - Relación magnitud-profundidad

## 📖 Documentación Completa

Lee el **informe técnico completo** (8,500 palabras):
```
docs\INFORME_FINAL_TERREMOTOS_USGS.md
```

## ⚠️ Problemas Comunes

### Error: "Python no encontrado"
Instala Python 3.8+: https://www.python.org/downloads/

### Error: "R no encontrado"
Instala R 4.0+: https://cran.r-project.org/bin/windows/base/

### Error: "Dataset no encontrado"
Asegúrate de colocar `Earthquakes_USGS.csv` en `data\raw\`

## 🎯 Próximos Pasos

1. ✅ Ejecutar pipeline (ya lo hiciste)
2. 📊 Revisar visualizaciones en `outputs\figures\`
3. 📈 Leer estadísticas en `outputs\results\`
4. 📖 Leer informe técnico en `docs\INFORME_FINAL_TERREMOTOS_USGS.md`
5. 🎤 Preparar presentación con `docs\ESTRUCTURA_PRESENTACION.md`

## 💡 Comandos Útiles

### Re-ejecutar solo limpieza
```powershell
python scripts\python\01_data_cleaning.py
```

### Re-ejecutar solo visualizaciones
```powershell
python scripts\python\03_visualizations.py
Rscript scripts\R\02_maps_visualization.R
```

### Re-ejecutar solo modelos ML
```powershell
python scripts\python\04_analytical_models.py
```

---


