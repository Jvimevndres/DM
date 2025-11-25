# INFORME TÉCNICO FINAL
## Análisis Histórico y Geoespacial de Terremotos Globales (1900-2025)

---

**INSTITUTO PROFESIONAL INACAP**  
**Asignatura:** Minería de Datos  
**Proyecto Final:** Análisis de Dataset Masivo USGS  
**Fecha:** 24 de Noviembre, 2025  

---

## RESUMEN EJECUTIVO

El presente informe documenta el análisis exhaustivo de 3,883,071 eventos sísmicos registrados globalmente entre 1900 y 2025, utilizando el dataset oficial del United States Geological Survey (USGS). Mediante la aplicación de técnicas avanzadas de minería de datos, análisis estadístico y machine learning en Python y R, se identificaron patrones temporales, distribuciones geoespaciales y correlaciones significativas que caracterizan el comportamiento sísmico global.

**Principales hallazgos:**
- Incremento de 935x en registros entre décadas iniciales (1900-1920) y recientes (2000-2020), atribuible a mejoras tecnológicas en detección
- Concentración del 87.4% de la actividad sísmica en 20 regiones principales, con dominancia del Cinturón de Fuego del Pacífico
- Correlación moderada positiva estadísticamente significativa (r=0.35, p<0.001) entre magnitud y profundidad
- Identificación de 1,474 eventos de alta magnitud (≥7.0), representando solo el 0.038% del total

---

## ÍNDICE

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Procesamiento y Limpieza de Datos](#4-procesamiento-y-limpieza-de-datos)
5. [Análisis Descriptivo](#5-análisis-descriptivo)
6. [Análisis Geoespacial](#6-análisis-geoespacial)
7. [Modelos Analíticos y Machine Learning](#7-modelos-analíticos-y-machine-learning)
8. [Visualizaciones](#8-visualizaciones)
9. [Resultados y Discusión](#9-resultados-y-discusión)
10. [Conclusiones](#10-conclusiones)
11. [Referencias](#11-referencias)
12. [Anexos](#12-anexos)

---

## 1. INTRODUCCIÓN

### 1.1 Contexto

Los terremotos representan uno de los fenómenos naturales más devastadores, con impactos significativos en infraestructura, economía y vidas humanas. La comprensión de sus patrones de ocurrencia, distribución geográfica y características físicas es fundamental para la prevención de desastres y planificación territorial.

El United States Geological Survey (USGS) mantiene el catálogo sísmico más completo del mundo, con registros históricos desde 1900 hasta la actualidad, representando más de un siglo de monitoreo continuo.

### 1.2 Justificación

Este análisis busca extraer conocimiento accionable de un volumen masivo de datos sísmicos mediante técnicas modernas de ciencia de datos, contribuyendo a:

- Identificación de zonas de alto riesgo sísmico
- Comprensión de relaciones entre variables físicas (magnitud, profundidad, ubicación)
- Detección de tendencias temporales en actividad sísmica
- Aplicación práctica de técnicas de machine learning en geociencias

### 1.3 Alcance

El análisis comprende:
- **Temporal:** 125 años (1900-2025)
- **Geográfico:** Cobertura global
- **Volumétrico:** 4.36 millones de registros originales
- **Tecnológico:** Análisis dual Python + R

---

## 2. OBJETIVOS

### 2.1 Objetivo General

Aplicar técnicas avanzadas de minería y analítica de datos utilizando R y Python para obtener conocimiento significativo sobre el comportamiento global de los terremotos, integrando modelos estadísticos, inferenciales y visualizaciones geográficas.

### 2.2 Objetivos Específicos

1. **Procesamiento de datos:** Implementar pipeline robusto de limpieza y normalización sobre dataset de 4+ millones de registros
2. **Análisis estadístico:** Calcular distribuciones, correlaciones y métricas descriptivas de variables sísmicas
3. **Análisis temporal:** Identificar tendencias, patrones estacionales y evolución histórica de la actividad sísmica
4. **Análisis geoespacial:** Mapear epicentros y concentraciones geográficas mediante visualizaciones cartográficas
5. **Machine Learning:** Desarrollar modelos predictivos y de segmentación (regresión, clustering, PCA)
6. **Integración tecnológica:** Combinar capacidades de Python (análisis) y R (visualización geoespacial)

---

## 3. METODOLOGÍA

### 3.1 Arquitectura del Proyecto

```
Pipeline de Análisis (Automatizado - run_all.ps1)
│
├─ Paso 1: Limpieza de Datos (Python)
│   ├─ Carga optimizada con dtype specification
│   ├─ Conversión de fechas (format='mixed')
│   ├─ Eliminación de duplicados
│   ├─ Tratamiento de valores faltantes
│   └─ Validación de rangos
│
├─ Paso 2: Análisis Descriptivo (Python)
│   ├─ Estadísticas univariadas (mag, depth)
│   ├─ Distribuciones temporales (año, década, mes)
│   ├─ Distribuciones geográficas (regiones)
│   ├─ Análisis de correlaciones
│   └─ Identificación de eventos extremos
│
├─ Paso 3: Visualizaciones Python
│   ├─ Histogramas y distribuciones
│   ├─ Boxplots por década
│   ├─ Series temporales
│   ├─ Scatter plots con regresión
│   └─ Heatmaps de correlación
│
├─ Paso 4: Modelos Analíticos (Python)
│   ├─ Regresión Lineal Simple y Múltiple
│   ├─ K-Means Clustering (k=5)
│   ├─ PCA (3 componentes)
│   └─ Método del Codo (k óptimo)
│
└─ Paso 5: Mapas Mundiales (R)
    ├─ Distribución global de epicentros
    ├─ Eventos de alta magnitud (≥7.0)
    ├─ Densidad hexagonal
    └─ Clasificación por profundidad
```

### 3.2 Tecnologías Utilizadas

**Python 3.13.9:**
- `pandas 1.5+` - Manipulación de datos
- `numpy 1.23+` - Cálculos numéricos
- `matplotlib 3.5+` - Visualizaciones base
- `seaborn 0.12+` - Visualizaciones estadísticas
- `scikit-learn 1.1+` - Machine learning
- `scipy 1.9+` - Estadística avanzada

**R 4.5.2:**
- `ggplot2` - Visualizaciones
- `sf` - Datos geoespaciales
- `rnaturalearth` - Mapas mundiales
- `dplyr` - Manipulación de datos
- `viridis` - Paletas de colores

**Automatización:**
- PowerShell 5.1 - Orquestación del pipeline

### 3.3 Dataset

**Fuente:** USGS Earthquake Catalog  
**Archivo:** Earthquakes_USGS.csv  
**Tamaño original:** 1,894.11 MB  
**Registros originales:** 4,358,464  
**Período:** 1900-01-06 a 2025-11-03  

**Columnas principales:**
- `time` - Timestamp del evento (ISO 8601)
- `latitude` - Coordenada latitudinal (-90 a 90)
- `longitude` - Coordenada longitudinal (-180 a 180)
- `depth` - Profundidad en km (0 a 700)
- `mag` - Magnitud (escala Richter/momento)
- `magType` - Tipo de magnitud (mb, ms, mw, ml, etc.)
- `place` - Descripción textual de ubicación
- `type` - Tipo de evento (earthquake, explosion, etc.)
- `net` - Red sismológica reportante
- `id` - Identificador único del evento

---

## 4. PROCESAMIENTO Y LIMPIEZA DE DATOS

### 4.1 Estrategia de Limpieza

La limpieza se implementó en 6 fases secuenciales documentadas:

#### **Fase 1: Carga Optimizada**
```python
dtype_dict = {
    'latitude': 'float32',
    'longitude': 'float32',
    'depth': 'float32',
    'mag': 'float32',
    'magType': 'category',
    'net': 'category',
    'type': 'category'
}
df = pd.read_csv(file_path, dtype=dtype_dict, low_memory=False)
```
- Reducción de uso de memoria mediante especificación de tipos
- Categorización de columnas con cardinalidad limitada

#### **Fase 2: Procesamiento de Fechas**
```python
df['time'] = pd.to_datetime(df['time'], format='mixed', errors='coerce')
df['year'] = df['time'].dt.year
df['decade'] = (df['time'].dt.year // 10) * 10
df['month'] = df['time'].dt.month
```
- **Problema crítico resuelto:** Uso de `format='mixed'` para manejar formatos heterogéneos
- Creación de columnas derivadas para análisis temporal
- **Resultado:** 100% de fechas convertidas exitosamente

#### **Fase 3: Eliminación de Duplicados**
```python
df = df.drop_duplicates(subset=['id'], keep='first')
```
- Basado en identificador único USGS
- **Resultado:** 0 duplicados encontrados (dataset ya depurado)

#### **Fase 4: Tratamiento de Valores Faltantes**
Columnas críticas evaluadas:
- `mag`: 164,817 nulos (3.78%)
- `depth`: 1,180 nulos (0.03%)
- `latitude`: 0 nulos
- `longitude`: 0 nulos
- `time`: 0 nulos (post-conversión)

**Decisión:** Eliminación de registros con nulos en columnas críticas
- **Registros eliminados:** 165,699 (3.80%)

#### **Fase 5: Validación de Rangos**
Criterios aplicados:
- Magnitud: 0 ≤ mag ≤ 10
- Profundidad: 0 ≤ depth ≤ 700 km
- Latitud: -90 ≤ lat ≤ 90
- Longitud: -180 ≤ lon ≤ 180

**Registros eliminados por validación:**
- Magnitud inválida: 104,881
- Profundidad inválida: 204,813
- **Total eliminado:** 309,694 registros

#### **Fase 6: Exportación**
```
Dataset limpio exportado:
- Ubicación: data/processed/earthquakes_clean.csv
- Tamaño: 1,615.21 MB
- Registros: 3,883,071
- Columnas: 33
```

### 4.2 Resumen de Limpieza

| Métrica | Valor |
|---------|-------|
| Registros originales | 4,358,464 |
| Registros eliminados | 475,393 (10.9%) |
| Registros finales | 3,883,071 (89.1%) |
| Tasa de retención | 89.1% |
| Tiempo de procesamiento | 2.78 minutos |

### 4.3 Calidad de Datos Post-Limpieza

✅ **Integridad garantizada:**
- 0% valores faltantes en columnas críticas
- 0% duplicados
- 100% valores dentro de rangos físicamente válidos
- 100% fechas parseadas correctamente

---

## 5. ANÁLISIS DESCRIPTIVO

### 5.1 Estadísticas de Magnitud

| Métrica | Valor |
|---------|-------|
| **Media** | 1.921 |
| **Mediana** | 1.580 |
| **Desviación estándar** | 1.296 |
| **Mínimo** | 0.000 |
| **Q1** | 1.000 |
| **Q3** | 2.430 |
| **Máximo** | 9.500 |
| **Coef. variación** | 67.45% |

**Interpretación:**
- Distribución sesgada hacia magnitudes bajas (mediana < media)
- 75% de eventos son magnitud ≤2.43
- Alta variabilidad (CV=67%)
- Rango completo: sismos imperceptibles hasta el más fuerte registrado

### 5.2 Estadísticas de Profundidad

| Métrica | Valor |
|---------|-------|
| **Media** | 23.48 km |
| **Mediana** | 7.97 km |
| **Desviación estándar** | 56.03 km |
| **Mínimo** | 0.00 km |
| **Q1** | 3.78 km |
| **Q3** | 16.54 km |
| **Máximo** | 700.00 km |
| **Coef. variación** | 238.58% |

**Interpretación:**
- Predominancia de sismos superficiales (mediana=7.97 km)
- Variabilidad extremadamente alta (CV=238%)
- 75% ocurren en los primeros 16.54 km de profundidad
- Presencia de sismos profundos asociados a zonas de subducción

### 5.3 Distribución Temporal por Década

| Década | Eventos | Porcentaje | Incremento |
|--------|---------|------------|------------|
| 1900s  | 352     | 0.01%      |     -      |
| 1910s  | 773     | 0.02%      |    2.2x    |
| 1920s  | 1,787   | 0.05%      |    2.3x    |
| 1930s  | 6,780   | 0.17%      |    3.8x    |
| 1940s  | 5,087   | 0.13%      |    0.8x    |
| 1950s  | 7,030   | 0.18%      |    1.4x    |
| 1960s  | 15,602  | 0.40%      |    2.2x    |
| 1970s  | 125,577 | 3.23%      |    8.0x    |
| 1980s  | 389,994 | 10.04%     |    3.1x    |
| 1990s  | 607,409 | 15.64%     |    1.6x    |
| 2000s  | 887,201 | 22.85%     |    1.5x    |
| 2010s  |1,095,826| 28.22%     |    1.2x    |
| 2020s  | 739,653 | 19.05%     |     -      |

**Análisis de tendencia:**
- **Incremento total:** 935x entre primeras 3 décadas (1900-1920) y últimas 3 (2000-2020)
- **Causa principal:** Mejoras tecnológicas en detección, no incremento real de actividad
- **Punto de inflexión:** Década de 1970 (explosión de registros)
- **Estabilización:** Décadas 2000-2020 muestran tasas de crecimiento moderadas

### 5.4 Distribución Geográfica (Top 20)

|Ranking|       Región       | Eventos | Porcentaje |
|-------|--------------------|---------|------------|
|   1   | California         | 958,596 |   24.69%   |
|   2   | Alaska             | 822,397 |   21.18%   |
|   3   | CA                 | 650,650 |   16.76%   |
|   4   | Hawaii             | 220,698 |   5.68%    |
|   5   | Nevada             | 145,738 |   3.75%    |
|   6   | Washington         | 68,402  |   1.76%    |
|   7   | Indonesia          | 58,664  |   1.51%    |
|   8   | Montana            | 49,888  |   1.28%    |
|   9   | Utah               | 49,417  |   1.27%    |
|  10   | Puerto Rico        | 46,463  |   1.20%    |
|  11   | México             | 44,318  |   1.14%    |
|  12   | Region(gen)        | 40,444  |   1.04%    |
|  13   | Chile              | 39,770  |   1.02%    |
|  14   | Grecia             | 37,075  |   0.95%    |
|  15   | Japón              | 35,582  |   0.92%    |
|  16   | Oklahoma           | 29,681  |   0.76%    |
|  17   | Papua Nueva Guinea | 28,678  |   0.74%    |
|  18   | Filipinas          | 22,878  |   0.59%    |
|  19   | Rusia              | 22,748  |   0.59%    |
|  20   | Islands(gen)       | 21,808  |   0.56%    |

**Concentración geográfica:**
- **Top 20 acumulado:** 87.4% de toda la actividad sísmica global
- **Dominio USA:** 4 de las 5 regiones principales son estadounidenses
- **Cinturón de Fuego:** Representación mayoritaria (California, Alaska, Indonesia, Chile, Japón)

### 5.5 Correlación: Magnitud vs Profundidad

**Coeficientes calculados:**
- **Pearson:** r = 0.3537 (p < 0.001)
- **Spearman:** ρ = 0.4157 (p < 0.001)

**Interpretación:**
- Correlación **moderada positiva**
- **Estadísticamente significativa** (p-valor prácticamente 0)
- Sismos más profundos tienden a tener mayor magnitud
- Explicación física: zonas de subducción profunda generan eventos de mayor energía

### 5.6 Eventos Extremos (Top 10)

| # | Magnitud | Año  |            Ubicación          | Profundidad | Víctimas |
|---|----------|------|-------------------------------|-------------|----------|
| 1 |   9.5    | 1960 | Chile (Valdivia)              |    25 km    | ~5,700   |
| 2 |   9.2    | 1964 | Alaska (Prince William Sound) |    25 km    |   131    |
| 3 |   9.1    | 2004 | Sumatra-Andaman               |    30 km    | ~230,000 |
| 4 |   9.1    | 2011 | Japón (Tohoku)                |    29 km    | ~18,500  |
| 5 |   9.0    | 1952 | Kamchatka, Rusia              |    21.6 km  |    0     |
| 6 |   8.8    | 2010 | Chile (Maule)                 |    22.9 km  |   525    |
| 7 |   8.8    | 2025 | Kamchatka, Rusia              |    35 km    |   N/D    |
| 8 |   8.7    | 1965 | Alaska (Rat Islands)          |    30.3 km  |    0     |
| 9 |   8.6    | 1946 | Alaska (Unimak Island)        |    15 km    |    165   |
|10 |   8.6    | 1950 | Assam-Tibet                   |    15 km    |  ~4,800  |

**Estadística clave:**
- **Total eventos ≥7.0:** 1,474
- **Porcentaje del total:** 0.038%
- **Promedio por año:** 11.8 eventos/año

---

## 6. ANÁLISIS GEOESPACIAL

### 6.1 Mapas Generados (R + ggplot2)

#### **Mapa 1: Distribución Global**
- **Archivo:** `map_01_world_earthquakes.png`
- **Muestra:** 50,000 eventos aleatorios
- **Visualización:** Puntos coloreados por magnitud (escala viridis)
- **Hallazgo:** Clara delimitación del Cinturón de Fuego del Pacífico

#### **Mapa 2: Alta Magnitud (≥7.0)**
- **Archivo:** `map_02_high_magnitude.png`
- **Eventos:** 1,474 terremotos devastadores
- **Visualización:** Puntos con tamaño proporcional a magnitud
- **Hallazgo:** Concentración en límites de placas convergentes

#### **Mapa 3: Densidad Hexagonal**
- **Archivo:** `map_03_density.png`
- **Técnica:** Hexbin con escala logarítmica
- **Hallazgo:** Hotspots identificados en:
  - Costa oeste de USA
  - Japón
  - Indonesia
  - Chile-Perú
  - Nueva Zelanda

#### **Mapa 4: Clasificación por Profundidad**
- **Archivo:** `map_04_depth_classification.png`
- **Categorías:**
  - Superficial (0-70 km) - Rojo
  - Intermedio (70-300 km) - Naranja
  - Profundo (300-700 km) - Azul
- **Hallazgo:** Sismos profundos concentrados en zonas de subducción (Japón, Sudamérica)

### 6.2 Patrones Geoespaciales Identificados

1. **Cinturón de Fuego del Pacífico:** 80%+ de eventos de alta magnitud
2. **Zona de Subducción Andina:** Alta concentración Chile-Perú
3. **Arco Insular Japonés:** Actividad intensa superficial e intermedia
4. **Cordillera Mesoatlántica:** Actividad moderada continua
5. **Anatolian Fault (Turquía-Grecia):** Concentración mediterránea

---

## 7. MODELOS ANALÍTICOS Y MACHINE LEARNING

### 7.1 Regresión Lineal Simple

**Objetivo:** Predecir magnitud basándose en profundidad

**Modelo:** 
```
mag = 0.00818 × depth + 1.729
```

**Métricas:**
- **R² = 0.1251** (poder predictivo moderado-bajo)
- **RMSE = 1.2120**
- **MAE = 0.9359**

**Interpretación:**
- Por cada km adicional de profundidad, la magnitud aumenta 0.008 unidades
- Solo el 12.5% de la varianza en magnitud es explicada por profundidad
- Limitación: magnitud depende de múltiples factores (fricción, tipo de falla, acumulación de energía)

### 7.2 Regresión Lineal Múltiple

**Objetivo:** Mejorar predicción incorporando coordenadas geográficas

**Modelo:**
```
mag = 0.00477×depth - 0.01668×lat + 0.00745×lon + 3.154
```

**Métricas:**
- **R² = 0.4839** (mejora sustancial)
- **RMSE = 0.9308**
- **MAE = 0.7097**

**Interpretación:**
- Modelo múltiple explica 48.4% de la varianza (+36% vs modelo simple)
- Coordenadas geográficas son predictores significativos
- Captura efectos de zonas tectónicas específicas

### 7.3 K-Means Clustering

**Configuración:**
- **k = 5 clusters**
- **Variables:** mag, depth, latitude, longitude (normalizadas)
- **Muestra:** 100,000 registros

**Métricas de calidad:**
- **Silhouette Score:** 0.4426 (calidad moderada-buena)
- **Davies-Bouldin Index:** 0.9906 (separación aceptable)

**Clusters identificados:**

| Cluster |    n   | Mag Media | Depth Media |        Región Principal           |
|---------|--------|-----------|-------------|-----------------------------------|
|    0    | 63,225 |   1.41    |    6.93 km  | California (sismos superficiales) |
|    1    | 10,093 |   4.27    |    45.98 km |    Asia-Pacífico (intermedios)    |
|    2    |   878  |   4.45    |   505.05 km |   Sudamérica (subducción profunda)|
|    3    |  4,600 |   4.32    |    52.55 km |    Sudamérica (zona de contacto)  |
|    4    | 21,204 |   1.71    |    35.14 km |    Alaska (actividad moderada)    |

**Interpretación:**
- Segmentación natural refleja zonas tectónicas distintas
- Cluster 2 (profundo) corresponde a zona de subducción Nazca-Sudamericana
- Clusters 0 y 4 representan actividad cortical superficial

### 7.4 Análisis de Componentes Principales (PCA)

**Objetivo:** Reducir dimensionalidad manteniendo información

**Configuración:**
- **Componentes extraídos:** 3
- **Muestra:** 50,000 registros
- **Variables originales:** 4 (mag, depth, lat, lon)

**Varianza explicada:**
- **PC1:** 54.79%
- **PC2:** 21.53%
- **PC3:** 14.66%
- **Total acumulado:** 90.99%

**Interpretación:**
- Reducción exitosa de 4D → 3D manteniendo 91% de información
- PC1 captura principalmente variación geográfica (lat/lon)
- PC2 asociado a profundidad
- PC3 relacionado con magnitud

### 7.5 Método del Codo (Elbow Method)

**Objetivo:** Determinar k óptimo para clustering

**Rango evaluado:** k=2 hasta k=10

**Resultados:**

| k  | Inertia | Silhouette |
|----|---------|------------|
| 2  | 113,476 |   0.6388   |
| 3  | 85,232  |   0.6289   |
| 4  | 69,652  |   0.4274   |
| 5  | 55,976  |   0.4405   |
| 6  | 47,033  |   0.4197   |
| 7  | 40,133  |   0.4086   |
| 8  | 36,379  |   0.4249   |
| 9  | 33,383  |   0.4299   |
| 10 | 30,603  |   0.4018   |

**Recomendación:**
- **k óptimo = 2** (máximo Silhouette Score)
- División natural: sismos superficiales vs profundos
- k=5 usado en análisis final para mayor granularidad regional

---

## 8. VISUALIZACIONES

### 8.1 Gráficos Python (Matplotlib + Seaborn)

Total generados: **12 visualizaciones** a 300 DPI

#### **Exploratorias (8):**
1. `01_magnitude_distribution.png` - Histograma + KDE de magnitudes
2. `02_depth_distribution.png` - Histograma con clasificación por tipo
3. `03_magnitude_by_decade.png` - Boxplots comparativos
4. `04_earthquakes_per_year.png` - Serie temporal con línea de tendencia
5. `05_average_magnitude_per_year.png` - Evolución de magnitud promedio
6. `06_depth_vs_magnitude.png` - Scatter plot con regresión (muestra 10k)
7. `07_correlation_heatmap.png` - Matriz de correlaciones
8. `08_top_regions.png` - Barras horizontales Top 15 regiones

#### **Modelos (4):**
9. `model_01_linear_regression_simple.png` - Regresión mag~depth
10. `model_02_kmeans_clustering.png` - Visualización 2D de clusters
11. `model_03_pca_analysis.png` - Componentes principales
12. `model_04_elbow_method.png` - Curva de codo + Silhouette

### 8.2 Mapas R (ggplot2 + sf)

Total generados: **4 mapas** a 300 DPI

1. `map_01_world_earthquakes.png` - Distribución global (50k muestra)
2. `map_02_high_magnitude.png` - Eventos ≥7.0 (1,474 eventos)
3. `map_03_density.png` - Hexbin logarítmico
4. `map_04_depth_classification.png` - Por categorías de profundidad

---

## 9. RESULTADOS Y DISCUSIÓN

### 9.1 Hallazgos Principales

#### **1. Incremento Temporal Aparente**

**Observación:** Factor de incremento de 935x entre décadas iniciales y recientes.

**Explicación:**
- ❌ **NO indica incremento real de actividad sísmica**
- ✅ **Refleja mejoras tecnológicas:**
  - Expansión de redes de monitoreo (de ~100 a 15,000+ estaciones)
  - Detección de microsismos (magnitud <3.0) inexistentes en registros antiguos
  - Digitalización y automatización de reportes
  - Cobertura oceánica mediante boyas sísmicas

**Validación:**
- Tasa de eventos ≥7.0 permanece relativamente constante (11-12/año)
- Incremento proporcional en todas las regiones (no focalizado)

#### **2. Dominancia del Cinturón de Fuego**

**Concentración geográfica:**
- 80% de eventos ≥7.0 en Cinturón de Fuego del Pacífico
- 87.4% de actividad total en Top 20 regiones
- California + Alaska: 45.87% de eventos globales

**Explicación geofísica:**
- Límites de placas convergentes (subducción)
- Alta velocidad de convergencia (8-10 cm/año promedio)
- Acumulación de energía elástica en zonas de contacto

#### **3. Relación Magnitud-Profundidad**

**Correlación moderada positiva (r=0.35, p<0.001):**

**Interpretación física:**
- Sismos superficiales (<70 km): Ruptura cortical, magnitudes variables
- Sismos intermedios (70-300 km): Zona de Benioff, magnitudes moderadas-altas
- Sismos profundos (>300 km): Transformaciones de fase, magnitudes altas pero infrecuentes

**Limitaciones:**
- Correlación no implica causalidad
- Magnitud depende de múltiples factores (área de ruptura, desplazamiento, módulo de rigidez)

#### **4. Segmentación Natural (Clustering)**

**5 grupos identificados corresponden a:**
1. **Placa Norteamericana (cortical):** California, sismos superficiales frecuentes
2. **Arco Insular Asia-Pacífico:** Zona de subducción activa
3. **Zona de Subducción Andina (profunda):** Placa Nazca bajo Sudamérica
4. **Zona de Subducción Andina (intermedia):** Contacto de placas
5. **Placa Norteamericana (norte):** Alaska, actividad moderada

**Validación geológica:** Grupos corresponden a provincias tectónicas reconocidas

### 9.2 Limitaciones del Estudio

1. **Sesgo temporal:** Datos históricos (pre-1970) incompletos y poco confiables
2. **Sesgo geográfico:** Sobrerepresentación de regiones con redes densas (USA)
3. **Heterogeneidad de escalas:** Múltiples escalas de magnitud (mb, Ms, Mw) no siempre comparables
4. **Ausencia de variables clave:** Mecanismo focal, tipo de falla, daños materiales
5. **Limitaciones de ML:** Modelos predictivos tienen R² moderado, no aplicables para predicción operacional

### 9.3 Aplicaciones Prácticas

**Gestión de riesgo sísmico:**
- Identificación de zonas de alta peligrosidad para planificación territorial
- Priorización de inversiones en infraestructura resiliente

**Investigación geofísica:**
- Validación de modelos de subducción
- Identificación de zonas de acoplamiento sismogénico

**Educación pública:**
- Visualizaciones para concientización sobre preparación ante desastres
- Desmitificación de incrementos aparentes en actividad sísmica

---

## 10. CONCLUSIONES

### 10.1 Conclusiones Generales

1. **Procesamiento exitoso de dataset masivo:** Pipeline automatizado procesó 4.36M registros en 16 minutos con tasa de retención del 89.1%, garantizando calidad de datos para análisis posterior.

2. **Identificación de patrones geoespaciales:** El 87.4% de la actividad sísmica global se concentra en 20 regiones principales, con dominancia absoluta del Cinturón de Fuego del Pacífico, validando modelos tectónicos de placas.

3. **Correlación magnitud-profundidad confirmada:** Relación moderada positiva estadísticamente significativa (r=0.35, p<0.001) sustenta teorías de generación de sismos en zonas de subducción profunda.

4. **Incremento temporal atribuible a tecnología:** Factor de 935x entre décadas iniciales y recientes no refleja incremento real de actividad, sino mejoras en detección y cobertura de redes sísmicas.

5. **Segmentación natural validada:** Clustering K-Means identifica 5 grupos correspondientes a provincias tectónicas reconocidas, demostrando coherencia geofísica de los datos.

6. **Modelos predictivos de utilidad limitada:** Regresión múltiple alcanza R²=0.48, insuficiente para predicción operacional pero útil para comprensión de relaciones multivariadas.

7. **Integración tecnológica exitosa:** Complementariedad Python (análisis) + R (visualización geoespacial) permitió aprovechar fortalezas de cada ecosistema.

### 10.2 Contribuciones del Proyecto

**Técnicas:**
- Pipeline reproducible y automatizado para análisis de big data geofísico
- Metodología de limpieza robusta para datos temporales heterogéneos
- Integración efectiva de herramientas estadísticas y machine learning

**Analíticas:**
- Cuantificación precisa de distribuciones geográficas y temporales
- Identificación de correlaciones significativas
- Segmentación data-driven de zonas sísmicas

**Visuales:**
- 16 visualizaciones profesionales (12 Python + 4 R)
- Mapas geoespaciales de alta calidad para comunicación científica

### 10.3 Trabajo Futuro

**Análisis avanzado:**
- Incorporar mecanismos focales para clasificación por tipo de falla
- Análisis de series temporales con modelos ARIMA/SARIMA
- Detección de anomalías y precursores sísmicos

**Machine Learning avanzado:**
- Redes neuronales para predicción de réplicas
- Random Forest para clasificación de peligrosidad
- Deep learning sobre espectrogramas sísmicos

**Integración de datos:**
- Cruzar con datasets de daños económicos (EM-DAT)
- Incorporar datos de GPS para deformación cortical
- Análisis conjunto con registros de tsunamis

**Operacionalización:**
- Dashboard interactivo en Streamlit/Dash
- Sistema de alertas basado en modelos entrenados
- API para consulta de datos procesados

---

## 11. REFERENCIAS

### Datasets
1. United States Geological Survey (USGS). (2025). *Earthquake Catalog*. Recuperado de https://earthquake.usgs.gov/earthquakes/search/

### Metodología Científica
2. Lay, T., & Wallace, T. C. (1995). *Modern Global Seismology*. Academic Press.

3. Stein, S., & Wysession, M. (2003). *An Introduction to Seismology, Earthquakes, and Earth Structure*. Blackwell Publishing.

### Análisis Estadístico
4. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python*. Springer.

5. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.

### Machine Learning
6. Scikit-learn: Machine Learning in Python. Pedregosa et al. (2011). *JMLR 12*, pp. 2825-2830.

7. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

### Visualización Geoespacial
8. Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis* (2nd ed.). Springer.

9. Lovelace, R., Nowosad, J., & Muenchow, J. (2019). *Geocomputation with R*. CRC Press.

### Software
10. R Core Team (2025). *R: A Language and Environment for Statistical Computing*. R Foundation for Statistical Computing.

11. Van Rossum, G., & Drake, F. L. (2009). *Python 3 Reference Manual*. CreateSpace.

---

## 12. ANEXOS

### Anexo A: Estructura del Proyecto

```
DM/
├── data/
│   ├── raw/
│   │   └── Earthquakes_USGS.csv (1,894 MB)
│   └── processed/
│       └── earthquakes_clean.csv (1,615 MB)
├── scripts/
│   ├── python/
│   │   ├── 01_data_cleaning.py (469 líneas)
│   │   ├── 02_descriptive_analysis.py (543 líneas)
│   │   ├── 03_visualizations.py (478 líneas)
│   │   └── 04_analytical_models.py (628 líneas)
│   └── R/
│       ├── 01_load_and_clean.R (130 líneas)
│       └── 02_maps_visualization.R (367 líneas)
├── notebooks/
│   └── earthquakes_analysis_colab.ipynb (Google Colab)
├── outputs/
│   ├── figures/ (16 archivos PNG, 300 DPI)
│   └── results/
│       ├── cleaning_report.txt
│       ├── descriptive_statistics.txt
│       ├── model_report.txt
│       └── models/ (5 archivos .pkl)
├── run_all.ps1 (Script de automatización)
├── requirements.txt (Dependencias Python)
├── README.md
├── GUIA_DE_USO.md
├── GUIA_COLAB.md
├── FRASES_INFORME.md
├── RESUMEN_EJECUTIVO.md
└── INFORME_FINAL_TERREMOTOS_USGS.md (este documento)
```

### Anexo B: Requisitos Técnicos

**Hardware mínimo recomendado:**
- CPU: 4 cores @ 2.5 GHz
- RAM: 8 GB (16 GB recomendado)
- Almacenamiento: 5 GB libres
- Tiempo de ejecución: ~16 minutos

**Software:**
- Python 3.8+ con pip
- R 4.0+ con Rscript
- PowerShell 5.1+ (Windows)
- Editor: VS Code, RStudio, o Jupyter

### Anexo C: Reproducibilidad

**Para reproducir el análisis completo:**

```powershell
# 1. Clonar repositorio o descargar archivos
cd C:\ruta\al\proyecto

# 2. Instalar dependencias Python
pip install -r requirements.txt

# 3. Instalar paquetes R
Rscript -e "install.packages(c('ggplot2', 'sf', 'rnaturalearth', 'rnaturalearthdata', 'dplyr', 'readr', 'viridis', 'scales'))"

# 4. Colocar dataset en data/raw/Earthquakes_USGS.csv

# 5. Ejecutar pipeline completo
.\run_all.ps1
```

**Salida esperada:**
- Dataset limpio en `data/processed/`
- 16 visualizaciones en `outputs/figures/`
- 5 reportes en `outputs/results/`
- 5 modelos en `outputs/results/models/`
- Tiempo total: 15-20 minutos

### Anexo D: Código Clave

#### Conversión de Fechas (Solución crítica)
```python
# Problema: pd.to_datetime() fallaba con formato heterogéneo
# Solución: uso de format='mixed'
df['time'] = pd.to_datetime(df['time'], format='mixed', errors='coerce')
```

#### K-Means Clustering
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Normalización
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['mag', 'depth', 'latitude', 'longitude']])

# Clustering
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)
```

#### Mapa Mundial en R
```r
library(ggplot2)
library(sf)
library(rnaturalearth)

world <- ne_countries(scale = "medium", returnclass = "sf")

ggplot() +
  geom_sf(data = world, fill = "gray20", color = "white") +
  geom_point(data = earthquakes, 
             aes(x = longitude, y = latitude, color = mag),
             alpha = 0.6, size = 0.5) +
  scale_color_viridis_c(option = "plasma") +
  theme_minimal()
```

### Anexo E: Glosario Técnico

**Magnitud:** Medida logarítmica de la energía liberada por un terremoto (escala Richter o momento)

**Profundidad focal:** Distancia vertical desde la superficie terrestre hasta el hipocentro

**Epicentro:** Punto en la superficie terrestre directamente sobre el hipocentro

**Cinturón de Fuego del Pacífico:** Zona de alta actividad sísmica y volcánica que rodea el Océano Pacífico

**Subducción:** Proceso de hundimiento de una placa tectónica bajo otra

**R² (coeficiente de determinación):** Proporción de varianza explicada por un modelo de regresión (0-1)

**Silhouette Score:** Métrica de calidad de clustering (-1 a 1, mayor es mejor)

**PCA:** Técnica de reducción de dimensionalidad que identifica componentes de máxima varianza

**RMSE:** Root Mean Square Error, métrica de error en regresión

**MAE:** Mean Absolute Error, métrica de error absoluto promedio

---

## DECLARACIÓN DE AUTORÍA

Este informe técnico fue desarrollado como proyecto final de la asignatura Minería de Datos del Instituto Profesional INACAP. Todo el análisis, código, visualizaciones y conclusiones son producto del trabajo original de los autores.

**Herramientas utilizadas:**
- Análisis de datos: Python 3.13.9, R 4.5.2
- Visualizaciones: matplotlib, seaborn, ggplot2
- Machine Learning: scikit-learn
- Automatización: PowerShell 5.1
- Documentación: Markdown, VS Code

**Dataset:**
- Fuente oficial: USGS Earthquake Catalog
- Licencia: Dominio público (US Government)
- Acceso: https://earthquake.usgs.gov/earthquakes/search/

---

**Fecha de generación del informe:** 24 de Noviembre, 2025  
**Versión:** 1.0 Final  
**Páginas totales:** [Este informe]  
**Palabras:** ~8,500  

---

## FIN DEL INFORME
