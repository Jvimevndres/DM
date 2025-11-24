# ==============================================================================
# SCRIPT: Mapas de Terremotos - R con ggplot2 y sf
# ==============================================================================
# Autor: Jaime
# Proyecto: Minería de Datos - Análisis de Terremotos Globales
# Fecha: Noviembre 2025
#
# DESCRIPCIÓN:
# Este script genera mapas mundiales de alta calidad mostrando la 
# distribución geográfica de terremotos, utilizando las librerías
# ggplot2, sf y rnaturalearth.
#
# MAPAS GENERADOS:
#   1. Mapa mundial con todos los sismos (muestra de 50,000)
#   2. Mapa de sismos de alta magnitud (mag >= 7.0)
#   3. Mapa de densidad de actividad sísmica
#   4. Mapa por profundidad de sismos
#
# OUTPUTS:
#   - Figuras: outputs/figures/map_*.png
#
# ==============================================================================

# Limpiar environment
rm(list = ls())

# ==============================================================================
# INSTALACIÓN Y CARGA DE LIBRERÍAS
# ==============================================================================

cat("\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n")
cat("GENERACIÓN DE MAPAS - TERREMOTOS USGS\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")

cat("[0/4] Cargando librerías...\n")

# Función para instalar librerías si no están disponibles
install_if_missing <- function(package) {
  if (!require(package, character.only = TRUE, quietly = TRUE)) {
    cat(sprintf("   Instalando %s...\n", package))
    install.packages(package, repos = "https://cloud.r-project.org/", quiet = TRUE)
    library(package, character.only = TRUE)
  }
}

# Instalar y cargar librerías necesarias
packages <- c("ggplot2", "sf", "rnaturalearth", "rnaturalearthdata", "dplyr", 
              "readr", "viridis", "scales")

suppressPackageStartupMessages({
  for (pkg in packages) {
    install_if_missing(pkg)
  }
})

cat("   ✓ Todas las librerías cargadas correctamente\n\n")

# ==============================================================================
# CONFIGURACIÓN DE RUTAS Y PARÁMETROS
# ==============================================================================

base_dir <- getwd()
clean_data_path <- file.path(base_dir, "data", "processed", "earthquakes_clean.csv")
figures_path <- file.path(base_dir, "outputs", "figures")

# Crear directorio de figuras si no existe
if (!dir.exists(figures_path)) {
  dir.create(figures_path, recursive = TRUE)
}

cat(sprintf("Dataset: %s\n", clean_data_path))
cat(sprintf("Salida: %s\n", figures_path))
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")

# Configurar tema de ggplot2
theme_set(theme_minimal())

# ==============================================================================
# CARGAR DATOS
# ==============================================================================

cat("[1/4] Cargando datos...\n")

if (!file.exists(clean_data_path)) {
  stop(sprintf("❌ ERROR: No se encontró el archivo %s\n
                Ejecuta primero: python scripts/python/01_data_cleaning.py", 
                clean_data_path))
}

earthquakes <- read_csv(clean_data_path, show_col_types = FALSE)

cat(sprintf("   ✓ Datos cargados: %s registros\n\n", 
            format(nrow(earthquakes), big.mark = ",")))

# ==============================================================================
# PREPARAR MAPA BASE DEL MUNDO
# ==============================================================================

cat("   Preparando mapa base del mundo...\n")

# Obtener mapa mundial de rnaturalearth
world <- ne_countries(scale = "medium", returnclass = "sf")

cat("   ✓ Mapa base cargado\n\n")

# ==============================================================================
# MAPA 1: MAPA MUNDIAL CON TODOS LOS SISMOS (MUESTRA)
# ==============================================================================

cat("[2/4] Generando mapa mundial con muestra de sismos...\n")

# Tomar una muestra si hay demasiados datos (para mejor rendimiento)
SAMPLE_SIZE <- 50000

if (nrow(earthquakes) > SAMPLE_SIZE) {
  cat(sprintf("   (usando muestra aleatoria de %s registros)\n", 
              format(SAMPLE_SIZE, big.mark = ",")))
  earthquakes_sample <- earthquakes %>% 
    sample_n(SAMPLE_SIZE)
} else {
  earthquakes_sample <- earthquakes
}

# Crear el mapa
map1 <- ggplot() +
  # Mapa base
  geom_sf(data = world, fill = "lightgray", color = "white", size = 0.2) +
  # Sismos como puntos
  geom_point(data = earthquakes_sample, 
             aes(x = longitude, y = latitude, color = mag, size = mag),
             alpha = 0.4) +
  # Escala de colores
  scale_color_viridis(option = "plasma", name = "Magnitud", 
                      breaks = seq(0, 10, 2)) +
  scale_size_continuous(range = c(0.1, 3), guide = "none") +
  # Títulos y etiquetas
  labs(
    title = "Distribución Global de Terremotos",
    subtitle = sprintf("Muestra de %s eventos sísmicos registrados por USGS", 
                      format(nrow(earthquakes_sample), big.mark = ",")),
    x = "Longitud",
    y = "Latitud"
  ) +
  # Tema
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 11, hjust = 0.5, color = "gray30"),
    legend.position = "bottom",
    legend.key.width = unit(2, "cm"),
    panel.grid.major = element_line(color = "gray90", size = 0.2),
    panel.background = element_rect(fill = "aliceblue")
  ) +
  coord_sf(xlim = c(-180, 180), ylim = c(-90, 90))

# Guardar mapa
output_path1 <- file.path(figures_path, "map_01_world_earthquakes.png")
ggsave(output_path1, map1, width = 14, height = 8, dpi = 300)

cat(sprintf("   ✓ Guardado: %s\n\n", output_path1))

# ==============================================================================
# MAPA 2: SISMOS DE ALTA MAGNITUD (mag >= 7.0)
# ==============================================================================

cat("[3/4] Generando mapa de sismos de alta magnitud (mag ≥ 7.0)...\n")

# Filtrar sismos de alta magnitud
high_magnitude <- earthquakes %>% 
  filter(mag >= 7.0)

cat(sprintf("   Total de sismos con mag ≥ 7.0: %s\n", 
            format(nrow(high_magnitude), big.mark = ",")))

# Crear el mapa
map2 <- ggplot() +
  # Mapa base
  geom_sf(data = world, fill = "lightgray", color = "white", size = 0.2) +
  # Sismos de alta magnitud
  geom_point(data = high_magnitude, 
             aes(x = longitude, y = latitude, color = mag, size = mag),
             alpha = 0.7) +
  # Escala de colores
  scale_color_gradient(low = "orange", high = "darkred", 
                       name = "Magnitud",
                       breaks = seq(7, 10, 0.5)) +
  scale_size_continuous(range = c(1, 6), guide = "none") +
  # Títulos y etiquetas
  labs(
    title = "Terremotos de Alta Magnitud (≥ 7.0)",
    subtitle = sprintf("%s eventos catastróficos registrados", 
                      format(nrow(high_magnitude), big.mark = ",")),
    x = "Longitud",
    y = "Latitud",
    caption = "Fuente: USGS Earthquake Catalog"
  ) +
  # Tema
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5, color = "darkred"),
    plot.subtitle = element_text(size = 11, hjust = 0.5, color = "gray30"),
    legend.position = "bottom",
    legend.key.width = unit(2, "cm"),
    panel.grid.major = element_line(color = "gray90", size = 0.2),
    panel.background = element_rect(fill = "aliceblue")
  ) +
  coord_sf(xlim = c(-180, 180), ylim = c(-90, 90))

# Guardar mapa
output_path2 <- file.path(figures_path, "map_02_high_magnitude.png")
ggsave(output_path2, map2, width = 14, height = 8, dpi = 300)

cat(sprintf("   ✓ Guardado: %s\n\n", output_path2))

# ==============================================================================
# MAPA 3: MAPA DE DENSIDAD (HEXBIN)
# ==============================================================================

cat("[4/4] Generando mapa de densidad de actividad sísmica...\n")

# Mapa de densidad hexagonal
map3 <- ggplot() +
  # Mapa base
  geom_sf(data = world, fill = "gray20", color = "white", linewidth = 0.2) +
  # Densidad hexagonal - agregamos z aesthetic
  stat_summary_hex(data = earthquakes_sample, 
                   aes(x = longitude, y = latitude, z = mag),
                   fun = "length",  # Contar número de eventos
                   bins = 60, alpha = 0.8) +
  # Escala de colores
  scale_fill_viridis(option = "inferno", name = "Densidad\nde Sismos",
                     trans = "log10",
                     labels = scales::comma) +
  # Títulos y etiquetas
  labs(
    title = "Densidad de Actividad Sísmica Global",
    subtitle = "Concentración de eventos sísmicos por región geográfica",
    x = "Longitud",
    y = "Latitud"
  ) +
  # Tema
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 11, hjust = 0.5, color = "gray30"),
    legend.position = "right",
    panel.grid.major = element_line(color = "gray30", linewidth = 0.2),
    panel.background = element_rect(fill = "gray10"),
    plot.background = element_rect(fill = "white")
  ) +
  coord_sf(xlim = c(-180, 180), ylim = c(-90, 90))

# Guardar mapa
output_path3 <- file.path(figures_path, "map_03_density.png")
ggsave(output_path3, map3, width = 14, height = 8, dpi = 300)

cat(sprintf("   ✓ Guardado: %s\n\n", output_path3))

# ==============================================================================
# MAPA 4: SISMOS POR PROFUNDIDAD
# ==============================================================================

cat("[5/5] Generando mapa de sismos por profundidad...\n")

# Clasificar por profundidad
earthquakes_sample <- earthquakes_sample %>%
  mutate(
    depth_category = case_when(
      depth < 70 ~ "Superficial (0-70 km)",
      depth < 300 ~ "Intermedio (70-300 km)",
      TRUE ~ "Profundo (300-700 km)"
    ),
    depth_category = factor(depth_category, 
                           levels = c("Superficial (0-70 km)", 
                                     "Intermedio (70-300 km)", 
                                     "Profundo (300-700 km)"))
  )

# Crear el mapa
map4 <- ggplot() +
  # Mapa base
  geom_sf(data = world, fill = "lightgray", color = "white", linewidth = 0.2) +
  # Sismos por profundidad
  geom_point(data = earthquakes_sample, 
             aes(x = longitude, y = latitude, color = depth_category, size = mag),
             alpha = 0.4) +
  # Escala de colores
  scale_color_manual(values = c("Superficial (0-70 km)" = "red",
                                "Intermedio (70-300 km)" = "orange",
                                "Profundo (300-700 km)" = "blue"),
                     name = "Tipo de Sismo") +
  scale_size_continuous(range = c(0.1, 3), name = "Magnitud") +
  # Títulos y etiquetas
  labs(
    title = "Distribución de Terremotos por Profundidad",
    subtitle = "Clasificación: Superficiales, Intermedios y Profundos",
    x = "Longitud",
    y = "Latitud"
  ) +
  # Tema
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 11, hjust = 0.5, color = "gray30"),
    legend.position = "bottom",
    legend.box = "vertical",
    panel.grid.major = element_line(color = "gray90", linewidth = 0.2),
    panel.background = element_rect(fill = "aliceblue")
  ) +
  coord_sf(xlim = c(-180, 180), ylim = c(-90, 90))

# Guardar mapa
output_path4 <- file.path(figures_path, "map_04_depth_classification.png")
ggsave(output_path4, map4, width = 14, height = 8, dpi = 300)

cat(sprintf("   ✓ Guardado: %s\n\n", output_path4))

# ==============================================================================
# RESUMEN FINAL
# ==============================================================================

cat("\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n")
cat("✓✓✓ MAPAS GENERADOS EXITOSAMENTE ✓✓✓\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")

cat("Mapas generados:\n")
cat(sprintf("  1. %s\n", basename(output_path1)))
cat(sprintf("  2. %s\n", basename(output_path2)))
cat(sprintf("  3. %s\n", basename(output_path3)))
cat(sprintf("  4. %s\n", basename(output_path4)))

cat("\n")
cat(sprintf("Ubicación: %s\n", figures_path))
cat("\n")
cat("Próximos pasos:\n")
cat("  1. Revisar los mapas generados\n")
cat("  2. Ejecutar modelos: python scripts/python/04_analytical_models.py\n")
cat("  3. Integrar resultados en el informe final\n")
cat("\n")
cat(paste(rep("=", 80), collapse = ""))
cat("\n\n")

# ==============================================================================
# NOTAS PARA EL INFORME
# ==============================================================================

cat("📝 FRASES SUGERIDAS PARA EL INFORME:\n")
cat(paste(rep("-", 80), collapse = ""))
cat("\n")
cat("1. \"Se generaron mapas mundiales que evidencian la concentración de\n")
cat("   actividad sísmica en el Cinturón de Fuego del Pacífico y zonas de\n")
cat("   subducción activa.\"\n\n")
cat("2. \"Los terremotos de alta magnitud (≥7.0) se distribuyen principalmente\n")
cat("   a lo largo de los límites de placas tectónicas convergentes.\"\n\n")
cat("3. \"El análisis espacial por profundidad revela que los sismos superficiales\n")
cat("   (<70 km) son los más frecuentes, mientras que los profundos (>300 km)\n")
cat("   se concentran en zonas de subducción específicas.\"\n")
cat(paste(rep("-", 80), collapse = ""))
cat("\n\n")
