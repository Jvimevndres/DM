
# ==============================================================================
# SCRIPT: Limpieza y Preparación de Datos en R - Terremotos USGS
# ==============================================================================
# Autor: Jaime
# Proyecto: Minería de Datos - Análisis de Terremotos Globales
# Fecha: Noviembre 2025
#
# DESCRIPCIÓN:
# Este script carga y prepara el dataset de terremotos en R, creando
# las columnas necesarias para el análisis y visualización de mapas.
#
# ==============================================================================

# Limpiar environment
rm(list = ls())

# Cargar librerías necesarias
suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
  library(lubridate)
})

cat("\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n")
cat("LIMPIEZA DE DATOS EN R - TERREMOTOS USGS\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")

# ==============================================================================
# CONFIGURACIÓN DE RUTAS
# ==============================================================================
base_dir <- getwd()
raw_data_path <- file.path(base_dir, "data", "raw", "Earthquakes_USGS.csv")
processed_data_path <- file.path(base_dir, "data", "processed", "earthquakes_clean.csv")

cat(sprintf("Directorio base: %s\n", base_dir))
cat(sprintf("Archivo de entrada: %s\n", raw_data_path))
cat(sprintf("Archivo de salida: %s\n", processed_data_path))
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")

# ==============================================================================
# CARGAR Y LIMPIAR DATOS
# ==============================================================================

cat("[1/4] Cargando datos...\n")

# Verificar si existe el archivo procesado de Python
if (file.exists(processed_data_path)) {
  cat("   ✓ Encontrado dataset limpio de Python\n")
  earthquakes <- read_csv(processed_data_path, show_col_types = FALSE)
} else if (file.exists(raw_data_path)) {
  cat("   ⚠ Dataset limpio no encontrado, cargando dataset original...\n")
  earthquakes <- read_csv(raw_data_path, show_col_types = FALSE)
  
  # Limpiar datos básico
  earthquakes <- earthquakes %>%
    mutate(
      time = ymd_hms(time),
      year = year(time),
      decade = floor(year / 10) * 10,
      month = month(time)
    ) %>%
    filter(
      !is.na(mag),
      !is.na(depth),
      !is.na(latitude),
      !is.na(longitude),
      !is.na(time),
      mag >= 0, mag <= 10,
      depth >= 0, depth <= 700,
      latitude >= -90, latitude <= 90,
      longitude >= -180, longitude <= 180
    )
} else {
  stop("❌ ERROR: No se encontró ningún archivo de datos. Por favor, coloca 
       'Earthquakes_USGS.csv' en data/raw/")
}

cat(sprintf("   ✓ Datos cargados: %s registros\n\n", format(nrow(earthquakes), big.mark = ",")))

# ==============================================================================
# PREPARAR DATOS PARA VISUALIZACIÓN
# ==============================================================================

cat("[2/4] Preparando datos para visualización...\n")

# Asegurar que las columnas necesarias existen
required_cols <- c("latitude", "longitude", "mag", "depth")
missing_cols <- setdiff(required_cols, names(earthquakes))

if (length(missing_cols) > 0) {
  stop(sprintf("❌ ERROR: Faltan columnas requeridas: %s", 
               paste(missing_cols, collapse = ", ")))
}

# Convertir tipos de datos
earthquakes <- earthquakes %>%
  mutate(
    latitude = as.numeric(latitude),
    longitude = as.numeric(longitude),
    mag = as.numeric(mag),
    depth = as.numeric(depth)
  )

cat("   ✓ Datos preparados correctamente\n\n")

cat("[3/4] Resumen del dataset:\n")
cat(sprintf("   Registros totales:        %s\n", format(nrow(earthquakes), big.mark = ",")))
cat(sprintf("   Rango temporal:           %s - %s\n", 
            min(earthquakes$year, na.rm = TRUE), 
            max(earthquakes$year, na.rm = TRUE)))
cat(sprintf("   Magnitud mínima:          %.2f\n", min(earthquakes$mag, na.rm = TRUE)))
cat(sprintf("   Magnitud máxima:          %.2f\n", max(earthquakes$mag, na.rm = TRUE)))
cat(sprintf("   Profundidad promedio:     %.2f km\n\n", mean(earthquakes$depth, na.rm = TRUE)))

cat("[4/4] Exportando dataset para mapas...\n")

# Guardar dataset procesado si no existía
if (!file.exists(processed_data_path)) {
  write_csv(earthquakes, processed_data_path)
  cat(sprintf("   ✓ Dataset guardado: %s\n", processed_data_path))
}

cat("\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n")
cat("✓ DATOS PREPARADOS PARA VISUALIZACIÓN DE MAPAS\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")


