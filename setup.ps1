# Setup completo del proyecto - Ejecutar UNA SOLA VEZ
# Este script instala todas las dependencias necesarias

Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  SETUP INICIAL - PROYECTO ANÁLISIS DE TERREMOTOS" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""

# ==============================================================================
# PASO 1: Verificar Python
# ==============================================================================
Write-Host "[1/4] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK Python detectado: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python no encontrado"
    }
} catch {
    Write-Host "  ERROR: Python no está instalado" -ForegroundColor Red
    Write-Host "  Descarga Python desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# ==============================================================================
# PASO 2: Instalar paquetes Python
# ==============================================================================
Write-Host ""
Write-Host "[2/4] Instalando paquetes Python..." -ForegroundColor Yellow
Write-Host "  Esto puede tardar varios minutos..." -ForegroundColor Gray

try {
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK Paquetes Python instalados" -ForegroundColor Green
    } else {
        throw "Error instalando paquetes"
    }
} catch {
    Write-Host "  ERROR: Falló la instalación de paquetes Python" -ForegroundColor Red
    Write-Host "  Intenta manualmente: pip install -r requirements.txt" -ForegroundColor Yellow
    exit 1
}

# ==============================================================================
# PASO 3: Verificar/Instalar R
# ==============================================================================
Write-Host ""
Write-Host "[3/4] Verificando R..." -ForegroundColor Yellow

# Buscar Rscript
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

if (-not $rscriptPath) {
    # Intentar en PATH
    try {
        $rVersion = Rscript --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $rscriptPath = "Rscript"
        }
    } catch {}
}

if ($rscriptPath) {
    Write-Host "  OK R detectado: $rscriptPath" -ForegroundColor Green
    
    # Instalar paquetes R
    Write-Host "  Instalando paquetes R..." -ForegroundColor Gray
    & $rscriptPath install_r_packages.R
    
} else {
    Write-Host "  WARNING R no está instalado (opcional)" -ForegroundColor Yellow
    Write-Host "  Los mapas NO se generarán sin R" -ForegroundColor Yellow
    Write-Host "  Descarga R desde: https://inacapmailcl-my.sharepoint.com/:f:/g/personal/paulo_taipe_inacapmail_cl/EmSLtERmpmxHqvlbQfAOMucBpdKvON2jUXe-QrqvHC4Xgw?e=G3VAGW" -ForegroundColor Gray
}

# ==============================================================================
# PASO 4: Verificar estructura de directorios
# ==============================================================================
Write-Host ""
Write-Host "[4/4] Verificando estructura de directorios..." -ForegroundColor Yellow

$directories = @(
    "data\raw",
    "data\processed",
    "outputs\figures",
    "outputs\results",
    "outputs\results\models"
)

$allExist = $true
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        Write-Host "  WARNING: Falta directorio $dir" -ForegroundColor Yellow
        $allExist = $false
    }
}

if ($allExist) {
    Write-Host "  OK Estructura de directorios correcta" -ForegroundColor Green
} else {
    Write-Host "  NOTA: Algunos directorios faltan (se crearán automáticamente al ejecutar)" -ForegroundColor Gray
}

# ==============================================================================
# RESUMEN FINAL
# ==============================================================================
Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "  SETUP COMPLETADO" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor White
Write-Host ""
Write-Host "  1. Descarga el dataset:" -ForegroundColor Yellow
Write-Host "     - Archivo: Earthquakes_USGS.csv" -ForegroundColor White
Write-Host "     - Ubicación: data\raw\Earthquakes_USGS.csv" -ForegroundColor White
Write-Host "     - Link: https://inacapmailcl-my.sharepoint.com/:f:/g/personal/paulo_taipe_inacapmail_cl/EmSLtERmpmxHqvlbQfAOMucBpdKvON2jUXe-QrqvHC4Xgw?e=G3VAGW" -ForegroundColor Cyan
Write-Host ""
Write-Host "  2. Ejecuta el análisis completo:" -ForegroundColor Yellow
Write-Host "     .\run_all.ps1" -ForegroundColor White
Write-Host ""
Write-Host "  3. Revisa los resultados en:" -ForegroundColor Yellow
Write-Host "     - outputs\figures\ (visualizaciones)" -ForegroundColor White
Write-Host "     - outputs\results\ (reportes)" -ForegroundColor White
Write-Host ""
Write-Host "Tiempo estimado de ejecución: 15-20 minutos" -ForegroundColor Gray
Write-Host ""
