# 📥 Dataset Original - Instrucciones de Descarga

## ⚠️ IMPORTANTE: Dataset NO Incluido en Repositorio

El archivo `Earthquakes_USGS.csv` **NO está incluido** en este repositorio porque:
- Tamaño: **1.89 GB** (demasiado grande para GitHub)
- Registros: **4.36 millones** de terremotos
- Periodo: **1900-2025** (125 años de datos)

## 📥 Cómo Obtener el Dataset

### Opción 1: Kaggle (Recomendado)

1. Ve a: **https://www.kaggle.com/datasets/usgs/earthquake-database**
2. Haz clic en **"Download"** (necesitas cuenta Kaggle gratuita)
3. Descomprime el archivo descargado
4. Renombra el archivo a: `Earthquakes_USGS.csv` (si tiene otro nombre)
5. Coloca el archivo en esta carpeta: `data/raw/`

### Opción 2: USGS Directo

1. Ve a: **https://earthquake.usgs.gov/earthquakes/search/**
2. Configura:
   - **Start Time**: 1900-01-01 00:00:00
   - **End Time**: 2025-01-01 00:00:00
   - **Output Format**: CSV
3. Haz clic en **"Search"** y luego **"Download"**
4. Renombra el archivo descargado a: `Earthquakes_USGS.csv`
5. Coloca el archivo en esta carpeta: `data/raw/`

## ✅ Verificación

Después de descargar, verifica que el archivo esté correcto:

```powershell
# Debe mostrar algo como: "1894.11 MB"
Get-Item "data\raw\Earthquakes_USGS.csv" | Select-Object Name, @{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}

# Debe mostrar ~4.36 millones
(Get-Content "data\raw\Earthquakes_USGS.csv" | Measure-Object -Line).Lines
```

## 📋 Columnas del Dataset

El archivo CSV debe contener estas columnas:

- `time` - Fecha y hora del terremoto (formato ISO 8601)
- `latitude` - Latitud del epicentro (grados)
- `longitude` - Longitud del epicentro (grados)
- `depth` - Profundidad en kilómetros
- `mag` - Magnitud del terremoto
- `magType` - Tipo de magnitud (mb, ml, ms, mw, etc.)
- `nst` - Número de estaciones sísmicas
- `gap` - Brecha azimutal
- `dmin` - Distancia horizontal mínima
- `rms` - Error RMS del ajuste temporal
- `net` - Red que reportó el evento
- `id` - Identificador único del evento
- `updated` - Última actualización
- `place` - Descripción de la ubicación
- `type` - Tipo de evento (earthquake, explosion, etc.)
- Y otras columnas adicionales...

## 🚀 Próximo Paso

Una vez que tengas el archivo en esta carpeta:

```powershell
# Ejecutar el pipeline completo
.\run_all.ps1
```

El script verificará automáticamente que el dataset esté en la ubicación correcta.

## 🔍 Estadísticas del Dataset Original

Después de descargarlo:
- **Tamaño**: ~1.89 GB
- **Registros**: 4,362,900 terremotos
- **Periodo**: 1900-01-01 a 2025-01-01
- **Columnas**: 22 variables

Después de limpieza (ejecutar pipeline):
- **Registros válidos**: 3,888,680 (89.1% retención)
- **Archivo limpio**: `data/processed/earthquakes_clean.csv` (1.6 GB)

---

**Nota**: Este README se incluye en el repositorio para facilitar la descarga del dataset.
