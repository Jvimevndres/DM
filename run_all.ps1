# Ejecucion Rapida - Script de Automatizacion

# Este script ejecuta todo el pipeline del proyecto de forma secuencial.
# Usalo para ejecutar todos los analisis de una sola vez.

# ==============================================================================
# INSTRUCCIONES DE USO
# ==============================================================================
# 
# 1. Asegurate de tener el dataset en: data/raw/Earthquakes_USGS.csv
# 2. Instala dependencias: pip install -r requirements.txt
# 3. Abre PowerShell en esta carpeta
# 4. Ejecuta: .\run_all.ps1
# 
# Tiempo estimado: 20-40 minutos
# ==============================================================================

Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  PROYECTO DE ANALISIS DE TERREMOTOS - EJECUCION AUTOMATICA" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que Python esta instalado
Write-Host "[VERIFICACION] Comprobando Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK Python detectado: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "ERROR: Python no encontrado. Instala Python 3.8+ primero." -ForegroundColor Red
    exit 1
}

# Verificar que R esta instalado (opcional)
Write-Host "[VERIFICACION] Comprobando R..." -ForegroundColor Yellow

# Buscar Rscript en ubicaciones comunes
$rscriptPaths = @(
    "C:\Program Files\R\R-4.5.2\bin\Rscript.exe",
    "C:\Program Files\R\R-4.5.1\bin\Rscript.exe",
    "C:\Program Files\R\R-4.4.2\bin\Rscript.exe"
)

$rscriptPath = $null
foreach ($path in $rscriptPaths) {
    if (Test-Path $path) {
        $rscriptPath = $path
        break
    }
}

if ($rscriptPath) {
    $rVersion = & $rscriptPath --version 2>&1
    Write-Host "OK R detectado: $rscriptPath" -ForegroundColor Green
    $hasR = $true
} else {
    # Intentar con Rscript en PATH
    try {
        $rVersion = Rscript --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $rscriptPath = "Rscript"
            Write-Host "OK R detectado en PATH" -ForegroundColor Green
            $hasR = $true
        } else {
            throw "Rscript no funciona"
        }
    } catch {
        Write-Host "WARNING R no detectado. Los mapas no se generaran." -ForegroundColor Yellow
        $hasR = $false
    }
}

# Verificar dataset
Write-Host "[VERIFICACION] Comprobando dataset..." -ForegroundColor Yellow
$datasetPath = "data\raw\Earthquakes_USGS.csv"
if (Test-Path $datasetPath) {
    $fileSize = (Get-Item $datasetPath).Length / 1MB
    Write-Host "OK Dataset encontrado: $([math]::Round($fileSize, 2)) MB" -ForegroundColor Green
} else {
    Write-Host "ERROR: Dataset no encontrado en $datasetPath" -ForegroundColor Red
    Write-Host "   Por favor, coloca el archivo Earthquakes_USGS.csv en data/raw/" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  INICIANDO PIPELINE DE ANALISIS" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""

# Crear directorios si no existen
Write-Host "[SETUP] Creando directorios de salida..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "data\processed" | Out-Null
New-Item -ItemType Directory -Force -Path "outputs\figures" | Out-Null
New-Item -ItemType Directory -Force -Path "outputs\results" | Out-Null
New-Item -ItemType Directory -Force -Path "outputs\results\models" | Out-Null
Write-Host "OK Directorios preparados" -ForegroundColor Green
Write-Host ""

# ==============================================================================
# PASO 1: LIMPIEZA DE DATOS
# ==============================================================================
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " PASO 1/5: LIMPIEZA DE DATOS" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ejecutando: scripts\python\01_data_cleaning.py" -ForegroundColor White
Write-Host ""

$step1Start = Get-Date
python scripts\python\01_data_cleaning.py
$step1End = Get-Date
$step1Duration = ($step1End - $step1Start).TotalMinutes

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "OK PASO 1 COMPLETADO en $([math]::Round($step1Duration, 2)) minutos" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERROR en Paso 1. Abortando pipeline." -ForegroundColor Red
    exit 1
}

# ==============================================================================
# PASO 2: ANALISIS DESCRIPTIVO
# ==============================================================================
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " PASO 2/5: ANALISIS DESCRIPTIVO" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ejecutando: scripts\python\02_descriptive_analysis.py" -ForegroundColor White
Write-Host ""

$step2Start = Get-Date
python scripts\python\02_descriptive_analysis.py
$step2End = Get-Date
$step2Duration = ($step2End - $step2Start).TotalMinutes

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "OK PASO 2 COMPLETADO en $([math]::Round($step2Duration, 2)) minutos" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERROR en Paso 2. Continuando con precaucion..." -ForegroundColor Yellow
    Write-Host ""
}

# ==============================================================================
# PASO 3: VISUALIZACIONES PYTHON
# ==============================================================================
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " PASO 3/5: VISUALIZACIONES EN PYTHON" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ejecutando: scripts\python\03_visualizations.py" -ForegroundColor White
Write-Host ""

$step3Start = Get-Date
python scripts\python\03_visualizations.py
$step3End = Get-Date
$step3Duration = ($step3End - $step3Start).TotalMinutes

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "OK PASO 3 COMPLETADO en $([math]::Round($step3Duration, 2)) minutos" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERROR en Paso 3. Continuando con precaucion..." -ForegroundColor Yellow
    Write-Host ""
}

# ==============================================================================
# PASO 4: MODELOS ANALITICOS
# ==============================================================================
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " PASO 4/5: MODELOS ANALITICOS" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ejecutando: scripts\python\04_analytical_models.py" -ForegroundColor White
Write-Host ""

$step4Start = Get-Date
python scripts\python\04_analytical_models.py
$step4End = Get-Date
$step4Duration = ($step4End - $step4Start).TotalMinutes

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "OK PASO 4 COMPLETADO en $([math]::Round($step4Duration, 2)) minutos" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERROR en Paso 4. Continuando con precaucion..." -ForegroundColor Yellow
    Write-Host ""
}

# ==============================================================================
# PASO 5: MAPAS EN R (OPCIONAL)
# ==============================================================================
if ($hasR) {
    Write-Host "================================================================================" -ForegroundColor Cyan
    Write-Host " PASO 5/5: MAPAS EN R" -ForegroundColor Cyan
    Write-Host "================================================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Ejecutando: scripts\R\02_maps_visualization.R" -ForegroundColor White
    Write-Host ""
    
    $step5Start = Get-Date
    & $rscriptPath scripts\R\02_maps_visualization.R
    $step5End = Get-Date
    $step5Duration = ($step5End - $step5Start).TotalMinutes
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "OK PASO 5 COMPLETADO en $([math]::Round($step5Duration, 2)) minutos" -ForegroundColor Green
        Write-Host ""
    } else {
        Write-Host ""
        Write-Host "ERROR en Paso 5. Los mapas no se generaron." -ForegroundColor Yellow
        Write-Host ""
    }
} else {
    Write-Host "================================================================================" -ForegroundColor Cyan
    Write-Host " PASO 5/5: MAPAS EN R - OMITIDO (R no instalado)" -ForegroundColor Cyan
    Write-Host "================================================================================" -ForegroundColor Cyan
    Write-Host ""
}

# ==============================================================================
# RESUMEN FINAL
# ==============================================================================
$totalEnd = Get-Date
$totalDuration = ($totalEnd - $step1Start).TotalMinutes

Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " PIPELINE COMPLETADO" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Tiempo total de ejecucion: $([math]::Round($totalDuration, 2)) minutos" -ForegroundColor Green
Write-Host ""
Write-Host "Resumen de tiempos por paso:" -ForegroundColor White
Write-Host "  1. Limpieza de datos:       $([math]::Round($step1Duration, 2)) min" -ForegroundColor White
Write-Host "  2. Analisis descriptivo:    $([math]::Round($step2Duration, 2)) min" -ForegroundColor White
Write-Host "  3. Visualizaciones Python:  $([math]::Round($step3Duration, 2)) min" -ForegroundColor White
Write-Host "  4. Modelos analiticos:      $([math]::Round($step4Duration, 2)) min" -ForegroundColor White
if ($hasR) {
    Write-Host "  5. Mapas en R:              $([math]::Round($step5Duration, 2)) min" -ForegroundColor White
}
Write-Host ""

# Verificar archivos generados
Write-Host "Verificando archivos generados..." -ForegroundColor Yellow
Write-Host ""

$checks = @(
    @{Path="data\processed\earthquakes_clean.csv"; Name="Dataset limpio"},
    @{Path="outputs\results\cleaning_report.txt"; Name="Reporte de limpieza"},
    @{Path="outputs\results\descriptive_statistics.txt"; Name="Estadisticas descriptivas"},
    @{Path="outputs\results\model_report.txt"; Name="Reporte de modelos"},
    @{Path="outputs\figures\01_magnitude_distribution.png"; Name="Grafico: Distribucion magnitudes"},
    @{Path="outputs\figures\model_01_linear_regression_simple.png"; Name="Grafico: Regresion lineal"}
)

$allGood = $true
foreach ($check in $checks) {
    if (Test-Path $check.Path) {
        Write-Host "  OK $($check.Name)" -ForegroundColor Green
    } else {
        Write-Host "  ERROR $($check.Name) - NO ENCONTRADO" -ForegroundColor Red
        $allGood = $false
    }
}

Write-Host ""

if ($allGood) {
    Write-Host "================================================================================" -ForegroundColor Green
    Write-Host " TODOS LOS ANALISIS COMPLETADOS EXITOSAMENTE" -ForegroundColor Green
    Write-Host "================================================================================" -ForegroundColor Green
} else {
    Write-Host "================================================================================" -ForegroundColor Yellow
    Write-Host " ANALISIS COMPLETADO CON ALGUNAS ADVERTENCIAS" -ForegroundColor Yellow
    Write-Host "================================================================================" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Archivos generados disponibles en:" -ForegroundColor White
Write-Host "  - Dataset limpio:      data\processed\" -ForegroundColor Cyan
Write-Host "  - Visualizaciones:     outputs\figures\" -ForegroundColor Cyan
Write-Host "  - Reportes:            outputs\results\" -ForegroundColor Cyan
Write-Host "  - Modelos entrenados:  outputs\results\models\" -ForegroundColor Cyan
Write-Host ""
Write-Host "Proximos pasos:" -ForegroundColor White
Write-Host "  1. Revisar los reportes en outputs\results\" -ForegroundColor White
Write-Host "  2. Ver las visualizaciones en outputs\figures\" -ForegroundColor White
Write-Host "  3. Usar las frases de FRASES_INFORME.md para tu informe" -ForegroundColor White
Write-Host ""
Write-Host "Proyecto listo!" -ForegroundColor Green
Write-Host ""
