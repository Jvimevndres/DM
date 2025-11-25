# Proyecto Final: Análisis de Terremotos Globales (USGS)
## Minería de Datos - 2025

### 📊 Descripción del Proyecto
Análisis exhaustivo de **3.88 millones de registros** de terremotos globales desde 1900 hasta 2025, utilizando datos del USGS (United States Geological Survey).

Este proyecto incluye:
- Pipeline automatizado de limpieza y análisis
- 16 visualizaciones profesionales (Python + R)
- 5 modelos de Machine Learning
- Informe técnico completo (8,500+ palabras)
- Estructura de presentación con estadísticas verificadas

### 🎯 Objetivos
- Limpiar y preparar dataset masivo (4.36M → 3.88M registros válidos)
- Análisis descriptivo completo con estadísticas temporales y geográficas
- Visualizaciones avanzadas con mapas mundiales interactivos
- Modelos ML: regresión lineal, clustering KMeans, PCA, optimización Elbow
- Documentación profesional tipo INACAP con rigor académico

### 📁 Estructura del Proyecto
```
DM/
├── data/
│   ├── raw/                    # Dataset original (NO incluido en repo)
│   │   └── Earthquakes_USGS.csv (1.89 GB - descargar manualmente)
│   └── processed/              # Datos limpios (generados por pipeline)
│       └── earthquakes_clean.csv (1.6 GB - 3.88M registros)
├── scripts/
│   ├── python/                 # Scripts de análisis Python
│   │   ├── 01_data_cleaning.py           (600 líneas)
│   │   ├── 02_descriptive_analysis.py    (350 líneas)
│   │   ├── 03_visualizations.py          (650 líneas)
│   │   └── 04_analytical_models.py       (515 líneas)
│   └── R/                      # Scripts de visualización R
│       ├── 01_load_and_clean.R           (167 líneas)
│       └── 02_maps_visualization.R       (330 líneas)
├── notebooks/
│   └── earthquakes_analysis_colab.ipynb  # Notebook Google Colab
├── outputs/
│   ├── figures/                # 16 visualizaciones PNG (300 DPI)
│   │   ├── [12 gráficos Python]
│   │   └── [4 mapas mundiales R]
│   └── results/                # Resultados y modelos
│       ├── basic_statistics.txt
│       ├── temporal_analysis.txt
│       ├── geographic_analysis.txt
│       ├── correlation_analysis.txt
│       ├── extreme_events.txt
│       └── models/             # 5 modelos ML (.pkl)
├── docs/
│   ├── GUIA_EJECUCION.md
│   ├── ESTRUCTURA_PRESENTACION.md
│   └── INFORME_FINAL_TERREMOTOS_USGS.md (8,500+ palabras)
├── setup.ps1                   # Setup automatizado (Python + R)
├── install_r_packages.R        # Instalador de paquetes R
├── run_all.ps1                 # Pipeline completo automatizado
├── requirements.txt            # Dependencias Python
├── .gitignore                  # Excluye datasets y outputs
└── README.md                   # Este archivo
```

### 🛠️ Tecnologías y Dependencias

#### Python (requirements.txt)
- **pandas >= 1.5.0** - Manipulación de datos masivos (3.88M registros)
- **numpy >= 1.23.0** - Operaciones numéricas eficientes
- **matplotlib >= 3.5.0** - Visualizaciones estáticas de alta calidad
- **seaborn >= 0.12.0** - Gráficos estadísticos avanzados
- **scikit-learn >= 1.1.0** - Machine Learning (regresión, clustering, PCA)
- **scipy >= 1.9.0** - Análisis estadístico y correlaciones
- **joblib >= 1.2.0** - Serialización de modelos ML

#### R (install_r_packages.R)
- **ggplot2** - Visualización de datos profesional
- **sf** - Manejo de datos espaciales (Simple Features)
- **rnaturalearth** - Mapas mundiales de alta resolución
- **rnaturalearthdata** - Datos geográficos complementarios
- **dplyr** - Manipulación de datos tipo tidyverse
- **readr** - Lectura rápida de archivos CSV
- **viridis** - Paletas de colores científicas
- **scales** - Formateo de ejes y etiquetas

#### Automatización
- **PowerShell 5.1+** - Scripts de orquestación (setup.ps1, run_all.ps1)
- **Git** - Control de versiones

### 📝 Columnas del Dataset
- `time`: Fecha y hora del terremoto
- `latitude`, `longitude`: Coordenadas del epicentro
- `depth`: Profundidad en kilómetros
- `mag`: Magnitud del terremoto
- `magType`: Tipo de magnitud medida
- `place`: Ubicación descriptiva
- `net`, `type`, `id`: Metadatos
- Otras: columnas de error y actualización

### 🚀 Quick Start - Clonar y Ejecutar

#### Requisitos Previos
- **Python 3.8+** (Python 3.13.9 recomendado)
- **R 4.0+** (R 4.5.2 recomendado)
- **PowerShell 5.1+** (Windows)
- **Git** para clonar el repositorio

#### Paso 1: Clonar el Repositorio
```powershell
git clone https://github.com/Jvimevndres/DM.git
cd DM
```

#### Paso 2: Ejecutar Setup Automatizado
```powershell
.\setup.ps1
```

Este script automáticamente:
- ✅ Verifica instalación de Python
- ✅ Instala dependencias Python (`pip install -r requirements.txt`)
- ✅ Detecta instalación de R
- ✅ Instala paquetes R requeridos (ggplot2, sf, rnaturalearth, etc.)
- ✅ Crea estructura de directorios

#### Paso 3: Descargar Dataset
⚠️ **IMPORTANTE**: El dataset NO está incluido en el repositorio (1.89 GB).

**Opción A - Kaggle** (Recomendado):
1. Ve a: https://www.kaggle.com/datasets/usgs/earthquake-database
2. Descarga `Earthquakes_USGS.csv`
3. Coloca el archivo en: `data/raw/Earthquakes_USGS.csv`

**Opción B - USGS Directo**:
1. Ve a: https://earthquake.usgs.gov/earthquakes/search/
2. Configura: Start=1900-01-01, End=2025-01-01, Output=CSV
3. Descarga y renombra a: `data/raw/Earthquakes_USGS.csv`

#### Paso 4: Ejecutar Pipeline Completo
```powershell
.\run_all.ps1
```

Este script ejecuta automáticamente:
1. **Limpieza de datos** (16 min aprox.) → `data/processed/earthquakes_clean.csv`
2. **Análisis descriptivo** → 5 archivos de estadísticas en `outputs/results/`
3. **Visualizaciones Python** → 12 gráficos en `outputs/figures/`
4. **Visualizaciones R** → 4 mapas mundiales en `outputs/figures/`
5. **Modelos ML** → 5 modelos entrenados en `outputs/results/models/`

**Tiempo total estimado**: ~16-20 minutos (depende del hardware)

### 📊 Resultados Esperados
El pipeline genera automáticamente:

#### 1. Dataset Limpio
- **Archivo**: `data/processed/earthquakes_clean.csv`
- **Registros**: 3,888,680 válidos (89.1% retención del dataset original)
- **Columnas**: 22 variables (temporales, geográficas, magnitud, profundidad, metadatos)
- **Tamaño**: 1,615 MB

#### 2. Estadísticas Descriptivas (5 archivos TXT)
- **basic_statistics.txt**: Media, mediana, desviación estándar, rangos
- **temporal_analysis.txt**: Tendencias por década, años con mayor actividad
- **geographic_analysis.txt**: Top 20 regiones (87.4% de actividad sísmica)
- **correlation_analysis.txt**: Matriz de correlaciones (r=0.35 mag-profundidad)
- **extreme_events.txt**: Top 100 terremotos más destructivos

#### 3. Visualizaciones (16 archivos PNG a 300 DPI)
**Python (12 gráficos)**:
- Histogramas de magnitud y profundidad
- Boxplots de distribución por tipo
- Series temporales (1900-2025)
- Scatter plot magnitud-profundidad con regresión
- Mapa de calor de correlaciones
- Gráficos de clustering KMeans
- Análisis PCA con varianza explicada

**R (4 mapas mundiales)**:
- Distribución global de epicentros
- Eventos de alta magnitud (≥7.0)
- Mapa de densidad hexagonal
- Clasificación por profundidad (somera/intermedia/profunda)

#### 4. Modelos Machine Learning (5 archivos .pkl)
- **regresion_lineal_simple.pkl**: R² = 0.13 (mag vs profundidad)
- **regresion_lineal_multiple.pkl**: R² = 0.48 (mag vs profundidad + año)
- **kmeans_clusters.pkl**: k=5 clusters, Silhouette Score = 0.44
- **pca_model.pkl**: 3 componentes, 90.99% varianza explicada
- **elbow_inertias.pkl**: Optimización de k para clustering

#### 5. Documentación Completa
- **INFORME_FINAL_TERREMOTOS_USGS.md**: 8,500+ palabras, 12 secciones, formato INACAP
- **ESTRUCTURA_PRESENTACION.md**: 10 minutos, estadísticas verificadas
- **GUIA_EJECUCION.md**: Tutorial detallado del pipeline

### 🔍 Insights Clave Descubiertos
1. **Aumento temporal**: 935x más actividad registrada (2020s vs 1900s) - tecnología de detección
2. **Correlación mag-profundidad**: r=0.35 (terremotos superficiales tienden a ser más fuertes)
3. **Concentración geográfica**: Top 20 regiones = 87.4% de toda la actividad
4. **Magnitudes**: 98.7% < 5.0 (sismos menores), solo 0.08% ≥ 7.0 (terremotos mayores)
5. **Profundidad modal**: 70% ocurren entre 0-20 km (sismos someros)

### ⚠️ Troubleshooting / Solución de Problemas

#### Problema: "Python no encontrado"
```powershell
# Verificar instalación
python --version

# Si no está instalado, descargar desde:
# https://www.python.org/downloads/
```

#### Problema: "R no encontrado"
```powershell
# Descargar R desde:
# https://cran.r-project.org/bin/windows/base/

# Agregar R al PATH manualmente:
$env:Path += ";C:\Program Files\R\R-4.5.2\bin"
```

#### Problema: "pip install falla"
```powershell
# Actualizar pip
python -m pip install --upgrade pip

# Instalar con usuario
pip install --user -r requirements.txt
```

#### Problema: "Error al instalar paquetes R"
```R
# En R, instalar manualmente:
install.packages(c("ggplot2", "sf", "rnaturalearth"), dependencies=TRUE)
```

#### Problema: "Dataset no encontrado"
- Asegúrate de colocar `Earthquakes_USGS.csv` en `data/raw/`
- Verifica que el nombre sea exactamente: `Earthquakes_USGS.csv` (sensible a mayúsculas)
- Tamaño esperado: ~1.89 GB (4.36M registros)

#### Problema: "Script R falla con 'size deprecated'"
- **Solución**: Ya está corregido en el repo (usamos `linewidth=` en lugar de `size=`)

#### Problema: "Memoria insuficiente"
- **Mínimo requerido**: 8 GB RAM
- **Recomendado**: 16 GB RAM
- Cerrar otras aplicaciones durante ejecución del pipeline

### 📞 Contacto y Soporte

**Autor**: Jaime  
**Institución**: INACAP  
**Curso**: Minería de Datos - 2025  
**Repositorio**: [github.com/Jvimevndres/DM](https://github.com/Jvimevndres/DM)

Para reportar bugs o sugerencias:
- Abrir un Issue en GitHub
- Incluir logs de error completos
- Especificar versiones de Python/R

### 📜 Licencia y Créditos

**Dataset**: [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/)  
**Licencia Dataset**: Dominio público (U.S. Government)  
**Código**: Proyecto académico - Uso educativo

**Citar este trabajo**:
```
Jaime (2025). Análisis de Terremotos Globales USGS 1900-2025.
Proyecto Final - Minería de Datos, INACAP.
GitHub: https://github.com/Jvimevndres/DM
```

---

### 🎓 Notas Académicas

Este proyecto fue desarrollado como trabajo final del curso de Minería de Datos en INACAP, demostrando:

✅ **Limpieza de datos masivos**: Manejo de 4.36M registros con formato='mixed' para parsing robusto  
✅ **Análisis estadístico**: Correlaciones, distribuciones, análisis temporal (125 años)  
✅ **Visualización avanzada**: 16 gráficos profesionales (Python + R) a 300 DPI  
✅ **Machine Learning**: Regresión, clustering KMeans, PCA, optimización Elbow  
✅ **Automatización**: Pipeline completo con PowerShell (setup + ejecución)  
✅ **Documentación**: Informe técnico de 8,500+ palabras estilo INACAP  
✅ **Reproducibilidad**: Repositorio GitHub clone-ready con un comando

**Calificación esperada**: 7.0 (excelencia)

---

**Última actualización**: Enero 2025  
**Versión**: 2.0 - Pipeline Automatizado
