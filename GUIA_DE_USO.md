# 📘 Guía de Uso - Proyecto de Análisis de Terremotos

## 🎯 Bienvenido

Esta guía te ayudará a ejecutar todos los componentes del proyecto de análisis de terremotos. Lee cuidadosamente cada sección antes de comenzar.

---

## 📋 Prerrequisitos

### Software Necesario

1. **Python 3.8 o superior**
   - Descarga desde: https://www.python.org/downloads/
   - Asegúrate de marcar "Add Python to PATH" durante la instalación

2. **R y RStudio** (para mapas)
   - R desde: https://cran.r-project.org/
   - RStudio desde: https://posit.co/download/rstudio-desktop/

3. **Editor de código** (opcional pero recomendado)
   - VS Code: https://code.visualstudio.com/

### Dataset Requerido

**Archivo:** `Earthquakes_USGS.csv`
- Colócalo en: `data/raw/Earthquakes_USGS.csv`
- Si no tienes el archivo, descárgalo del USGS Earthquake Catalog

---

## 🚀 Instalación

### 1. Instalar Dependencias de Python

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
# Instalar todas las librerías necesarias
pip install pandas numpy matplotlib seaborn scikit-learn scipy joblib
```

**Librerías instaladas:**
- `pandas`: Manipulación de datos
- `numpy`: Operaciones numéricas
- `matplotlib` y `seaborn`: Visualizaciones
- `scikit-learn`: Modelos de machine learning
- `scipy`: Estadísticas avanzadas
- `joblib`: Guardado de modelos

### 2. Instalar Paquetes de R

Abre RStudio y ejecuta:

```r
# Instalar paquetes necesarios
install.packages(c("ggplot2", "sf", "rnaturalearth", 
                   "rnaturalearthdata", "dplyr", "readr", 
                   "viridis", "scales"))
```

---

## 📂 Estructura del Proyecto

```
DM/
├── data/
│   ├── raw/                    # Dataset original aquí
│   │   └── Earthquakes_USGS.csv
│   └── processed/              # Datos limpios (generados)
│       └── earthquakes_clean.csv
├── scripts/
│   ├── python/
│   │   ├── 01_data_cleaning.py          # Limpieza de datos
│   │   ├── 02_descriptive_analysis.py   # Análisis estadístico
│   │   ├── 03_visualizations.py         # Gráficos Python
│   │   └── 04_analytical_models.py      # Modelos ML
│   └── R/
│       ├── 01_load_and_clean.R          # Carga en R
│       └── 02_maps_visualization.R      # Mapas mundiales
├── notebooks/
│   └── earthquakes_analysis_colab.ipynb # Notebook completo
├── outputs/
│   ├── figures/                # Gráficos generados
│   └── results/                # Reportes y modelos
└── README.md
```

---

## 🎬 Ejecución Paso a Paso

### OPCIÓN A: Ejecución Local (Python + R)

#### Paso 1: Limpieza de Datos (Python)

```powershell
cd "C:\Users\jaime\Documents\DM"
python scripts/python/01_data_cleaning.py
```

**Qué hace:**
- Carga el dataset original
- Elimina duplicados y valores inválidos
- Crea columnas de año, década, mes
- Exporta: `data/processed/earthquakes_clean.csv`
- Genera: `outputs/results/cleaning_report.txt`

**Tiempo estimado:** 2-10 minutos (depende del tamaño del dataset)

**Salida esperada:**
```
✓✓✓ LIMPIEZA COMPLETADA EXITOSAMENTE ✓✓✓
Registros finales: XXX,XXX
```

---

#### Paso 2: Análisis Descriptivo (Python)

```powershell
python scripts/python/02_descriptive_analysis.py
```

**Qué hace:**
- Calcula estadísticas descriptivas (media, mediana, desviación)
- Analiza distribución temporal (por año, década)
- Identifica regiones más afectadas
- Calcula correlaciones
- Genera: `outputs/results/descriptive_statistics.txt`

**Tiempo estimado:** 1-3 minutos

**Salida esperada:**
```
✓✓✓ ANÁLISIS DESCRIPTIVO COMPLETADO EXITOSAMENTE ✓✓✓
```

---

#### Paso 3: Visualizaciones en Python

```powershell
python scripts/python/03_visualizations.py
```

**Qué hace:**
- Genera 8 visualizaciones profesionales:
  1. Histograma de magnitudes
  2. Histograma de profundidades
  3. Boxplots por década
  4. Tendencia temporal
  5. Magnitud promedio por año
  6. Scatter profundidad vs magnitud
  7. Heatmap de correlaciones
  8. Top regiones afectadas

**Archivos generados:** `outputs/figures/01_*.png` a `08_*.png`

**Tiempo estimado:** 2-5 minutos

---

#### Paso 4: Mapas en R

**Opción 4A: Desde RStudio**

1. Abre RStudio
2. File → Open File → `scripts/R/02_maps_visualization.R`
3. Selecciona todo el código (Ctrl+A)
4. Run (Ctrl+Enter)

**Opción 4B: Desde línea de comandos**

```powershell
Rscript scripts/R/02_maps_visualization.R
```

**Qué hace:**
- Genera 4 mapas mundiales de alta calidad:
  1. Distribución global de sismos
  2. Sismos de alta magnitud (≥7.0)
  3. Mapa de densidad
  4. Clasificación por profundidad

**Archivos generados:** `outputs/figures/map_01_*.png` a `map_04_*.png`

**Tiempo estimado:** 3-8 minutos

---

#### Paso 5: Modelos Analíticos (Python)

```powershell
python scripts/python/04_analytical_models.py
```

**Qué hace:**
- Regresión lineal simple y múltiple
- Clustering KMeans
- PCA (Análisis de Componentes Principales)
- Método del codo para K óptimo
- Guarda modelos entrenados en `outputs/results/models/`

**Tiempo estimado:** 3-10 minutos

---

### OPCIÓN B: Google Colab (Todo en uno)

Si prefieres ejecutar todo en Google Colab:

1. **Subir el notebook:**
   - Ve a: https://colab.research.google.com/
   - File → Upload notebook
   - Selecciona: `notebooks/earthquakes_analysis_colab.ipynb`

2. **Subir dataset:**
   - Usa el botón 📁 en el panel izquierdo
   - Sube `Earthquakes_USGS.csv`
   - O ejecuta la celda de carga que incluye `files.upload()`

3. **Ejecutar todo:**
   - Runtime → Run all
   - O ejecuta celda por celda (Shift+Enter)

**Ventajas de Colab:**
- No requiere instalación local
- Gratis con GPU/TPU
- Fácil de compartir
- Todo en un solo archivo

**Tiempo estimado total:** 15-30 minutos

---

## 📊 Verificación de Resultados

### Archivos que deben generarse:

#### En `data/processed/`:
- ✅ `earthquakes_clean.csv` - Dataset limpio

#### En `outputs/figures/`:
- ✅ `01_magnitude_distribution.png`
- ✅ `02_depth_distribution.png`
- ✅ `03_magnitude_by_decade.png`
- ✅ `04_earthquakes_per_year.png`
- ✅ `05_average_magnitude_per_year.png`
- ✅ `06_depth_vs_magnitude.png`
- ✅ `07_correlation_heatmap.png`
- ✅ `08_top_regions.png`
- ✅ `map_01_world_earthquakes.png`
- ✅ `map_02_high_magnitude.png`
- ✅ `map_03_density.png`
- ✅ `map_04_depth_classification.png`
- ✅ `model_01_linear_regression_simple.png`
- ✅ `model_02_kmeans_clustering.png`
- ✅ `model_03_pca_analysis.png`
- ✅ `model_04_elbow_method.png`

#### En `outputs/results/`:
- ✅ `cleaning_report.txt`
- ✅ `descriptive_statistics.txt`
- ✅ `model_report.txt`
- ✅ `frequency_tables_decades.csv`
- ✅ `frequency_tables_regions.csv`

#### En `outputs/results/models/`:
- ✅ `linear_regression_simple.pkl`
- ✅ `linear_regression_multiple.pkl`
- ✅ `kmeans_model.pkl`
- ✅ `kmeans_scaler.pkl`
- ✅ `pca_model.pkl`

---

## 🐛 Solución de Problemas

### Problema 1: "No se encontró el archivo"

**Error:**
```
❌ ERROR: No se encontró el archivo data/raw/Earthquakes_USGS.csv
```

**Solución:**
1. Verifica que el archivo esté en la ubicación correcta
2. Verifica que el nombre sea exactamente `Earthquakes_USGS.csv`
3. Asegúrate de estar en el directorio correcto del proyecto

---

### Problema 2: "ModuleNotFoundError"

**Error:**
```
ModuleNotFoundError: No module named 'pandas'
```

**Solución:**
```powershell
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

Si persiste, verifica tu instalación de Python:
```powershell
python --version
pip --version
```

---

### Problema 3: Errores en R

**Error:**
```
Error: package 'ggplot2' not found
```

**Solución:**
```r
install.packages("ggplot2")
```

---

### Problema 4: Memoria insuficiente

Si el dataset es muy grande (>500MB):

**Solución en Python:**
Edita los scripts y activa el muestreo:
```python
# En la función load_data, cambia:
SAMPLE_SIZE = 100000  # Usar solo 100,000 registros
```

**Solución en R:**
```r
# En 02_maps_visualization.R, ajusta:
SAMPLE_SIZE <- 30000
```

---

## 💡 Tips y Mejores Prácticas

### Para el Informe:

1. **Usa las "Frases Sugeridas"** que aparecen en los reportes de texto
2. **Incluye las visualizaciones** generadas en `outputs/figures/`
3. **Cita las métricas** de los modelos (R², Silhouette Score, etc.)
4. **Interpreta los resultados** con las notas incluidas en los scripts

### Para la Presentación:

1. **Selecciona 4-6 gráficos clave:**
   - Distribución de magnitudes
   - Tendencia temporal
   - Mapa de alta magnitud
   - Resultados de clustering

2. **Estructura sugerida:**
   - Slide 1: Introducción y objetivos
   - Slide 2: Dataset y metodología
   - Slide 3-4: Análisis descriptivo con gráficos
   - Slide 5-6: Modelos y resultados
   - Slide 7: Conclusiones y recomendaciones

### Para Experimentar Más:

1. **Cambia parámetros de clustering:**
   ```python
   # En 04_analytical_models.py
   clustering = kmeans_clustering(df, n_clusters=7)  # Probar con 7 clusters
   ```

2. **Filtra por regiones específicas:**
   ```python
   df_california = df[df['place'].str.contains('California', na=False)]
   ```

3. **Analiza períodos específicos:**
   ```python
   df_recent = df[df['year'] >= 2000]
   ```

---

## 📚 Recursos Adicionales

### Documentación Oficial:
- **Pandas:** https://pandas.pydata.org/docs/
- **Scikit-learn:** https://scikit-learn.org/stable/
- **ggplot2:** https://ggplot2.tidyverse.org/
- **USGS:** https://earthquake.usgs.gov/

### Tutoriales Recomendados:
- Python para Data Science: https://www.kaggle.com/learn/python
- R para visualizaciones: https://r4ds.had.co.nz/
- Machine Learning básico: https://www.coursera.org/learn/machine-learning

---

## 📞 Soporte

Si encuentras problemas:

1. **Revisa los mensajes de error** - suelen indicar qué falta
2. **Verifica las rutas de archivos** - deben ser absolutas o relativas correctas
3. **Comprueba las versiones** de Python y paquetes
4. **Consulta los comentarios** en el código - hay explicaciones detalladas

---

## ✅ Checklist Final

Antes de entregar tu proyecto, verifica:

- [ ] Todos los scripts ejecutan sin errores
- [ ] Se generaron todas las figuras (16 archivos .png)
- [ ] Los reportes de texto están completos
- [ ] El dataset limpio fue creado
- [ ] Los modelos fueron guardados
- [ ] Las visualizaciones son legibles y profesionales
- [ ] El informe incluye citas de los resultados
- [ ] La presentación tiene 7-10 slides máximo
- [ ] Has interpretado los resultados (no solo copiar números)

---

**¡Éxito con tu proyecto!** 🎉

*Desarrollado con ❤️ para Minería de Datos 2025*
