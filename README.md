# Proyecto Final: Análisis de Terremotos Globales (USGS)
## Minería de Datos - 2025

### 📊 Descripción del Proyecto
Análisis exhaustivo de más de 1,000,000 de registros de terremotos globales desde 1900 hasta 2025, utilizando datos del USGS (United States Geological Survey).

### 🎯 Objetivos
- Limpiar y preparar el dataset masivo de terremotos
- Realizar análisis descriptivo y exploratorio
- Crear visualizaciones avanzadas incluyendo mapas interactivos
- Implementar modelos analíticos (regresión, clustering)
- Generar insights para informe técnico y presentación

### 📁 Estructura del Proyecto
```
DM/
├── data/
│   ├── raw/                    # Dataset original
│   │   └── Earthquakes_USGS.csv
│   └── processed/              # Datos limpios
│       └── earthquakes_clean.csv
├── scripts/
│   ├── python/
│   │   ├── 01_data_cleaning.py
│   │   ├── 02_descriptive_analysis.py
│   │   ├── 03_visualizations.py
│   │   └── 04_analytical_models.py
│   └── R/
│       ├── 01_load_and_clean.R
│       └── 02_maps_visualization.R
├── notebooks/
│   └── earthquakes_analysis_colab.ipynb
├── outputs/
│   ├── figures/                # Gráficos generados
│   └── results/                # Resultados numéricos
└── README.md
```

### 🛠️ Tecnologías Utilizadas
- **Python**: pandas, numpy, matplotlib, seaborn, scikit-learn
- **R**: dplyr, ggplot2, sf, rnaturalearth
- **Entornos**: Google Colab, RStudio

### 📝 Columnas del Dataset
- `time`: Fecha y hora del terremoto
- `latitude`, `longitude`: Coordenadas del epicentro
- `depth`: Profundidad en kilómetros
- `mag`: Magnitud del terremoto
- `magType`: Tipo de magnitud medida
- `place`: Ubicación descriptiva
- `net`, `type`, `id`: Metadatos
- Otras: columnas de error y actualización

### 🚀 Cómo Usar Este Proyecto

#### Paso 1: Preparar el dataset
Coloca el archivo `Earthquakes_USGS.csv` en la carpeta `data/raw/`

#### Paso 2: Ejecutar limpieza de datos
```bash
python scripts/python/01_data_cleaning.py
```

#### Paso 3: Análisis descriptivo
```bash
python scripts/python/02_descriptive_analysis.py
```

#### Paso 4: Generar visualizaciones
```bash
python scripts/python/03_visualizations.py
Rscript scripts/R/02_maps_visualization.R
```

#### Paso 5: Modelos analíticos
```bash
python scripts/python/04_analytical_models.py
```

### 📊 Resultados Esperados
- Dataset limpio con más de 900,000+ registros válidos
- Estadísticos descriptivos completos
- Visualizaciones de distribuciones y tendencias temporales
- Mapas mundiales de epicentros
- Modelos de regresión y clustering

### 👨‍🎓 Autor
Jaime - Proyecto Final de Minería de Datos

### 📅 Fecha
Noviembre 2025
