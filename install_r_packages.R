# Script de instalación de paquetes R
# Ejecutar con: Rscript install_r_packages.R

cat("================================================================================\n")
cat("INSTALACIÓN DE PAQUETES R PARA PROYECTO DE TERREMOTOS\n")
cat("================================================================================\n\n")

# Lista de paquetes requeridos
packages <- c(
  "ggplot2",       # Visualizaciones
  "sf",            # Datos geoespaciales
  "rnaturalearth", # Mapas mundiales
  "rnaturalearthdata", # Data de mapas
  "dplyr",         # Manipulación de datos
  "readr",         # Lectura de CSV
  "viridis",       # Paletas de colores
  "scales"         # Escalas para gráficos
)

cat(sprintf("Paquetes a instalar: %d\n", length(packages)))
cat(paste(packages, collapse = ", "), "\n\n")

# Verificar e instalar paquetes faltantes
installed <- installed.packages()[, "Package"]
to_install <- packages[!packages %in% installed]

if (length(to_install) > 0) {
  cat(sprintf("Instalando %d paquetes faltantes...\n\n", length(to_install)))
  
  for (pkg in to_install) {
    cat(sprintf("[%d/%d] Instalando '%s'...\n", 
                which(to_install == pkg), 
                length(to_install), 
                pkg))
    
    tryCatch({
      install.packages(pkg, 
                      repos = "https://cloud.r-project.org",
                      dependencies = TRUE,
                      quiet = FALSE)
      cat(sprintf("  ✓ '%s' instalado exitosamente\n\n", pkg))
    }, error = function(e) {
      cat(sprintf("  ✗ Error instalando '%s': %s\n\n", pkg, e$message))
    })
  }
} else {
  cat("✓ Todos los paquetes ya están instalados\n\n")
}

# Verificación final
cat("================================================================================\n")
cat("VERIFICACIÓN DE INSTALACIÓN\n")
cat("================================================================================\n\n")

all_installed <- TRUE
for (pkg in packages) {
  if (pkg %in% installed.packages()[, "Package"]) {
    cat(sprintf("✓ %s\n", pkg))
  } else {
    cat(sprintf("✗ %s - NO INSTALADO\n", pkg))
    all_installed <- FALSE
  }
}

cat("\n")
if (all_installed) {
  cat("================================================================================\n")
  cat("✓✓✓ INSTALACIÓN COMPLETADA EXITOSAMENTE ✓✓✓\n")
  cat("================================================================================\n")
  cat("\nAhora puedes ejecutar: .\\run_all.ps1\n")
} else {
  cat("================================================================================\n")
  cat("⚠ ALGUNOS PAQUETES NO SE INSTALARON CORRECTAMENTE\n")
  cat("================================================================================\n")
  cat("\nIntenta instalar manualmente los paquetes faltantes desde RStudio\n")
}
