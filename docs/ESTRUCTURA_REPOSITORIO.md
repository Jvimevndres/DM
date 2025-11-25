# 📂 Organización del Repositorio GitHub

## Estructura de Carpetas Completa

Este repositorio ya incluye todas las carpetas necesarias con archivos `.gitkeep` para mantener la estructura:

```
DM/
├── data/
│   ├── raw/                    ← Contiene .gitkeep + README
│   │   └── .gitkeep
│   └── processed/              ← Contiene .gitkeep
│       └── .gitkeep
│
├── outputs/
│   ├── figures/                ← Contiene .gitkeep
│   │   └── .gitkeep
│   └── results/                ← Contiene .gitkeep
│       ├── .gitkeep
│       └── models/             ← Contiene .gitkeep
│           └── .gitkeep
│
├── scripts/
│   ├── python/                 ← 4 scripts Python (2,115 líneas)
│   │   ├── 01_data_cleaning.py
│   │   ├── 02_descriptive_analysis.py
│   │   ├── 03_visualizations.py
│   │   └── 04_analytical_models.py
│   └── R/                      ← 2 scripts R (497 líneas)
│       ├── 01_load_and_clean.R
│       └── 02_maps_visualization.R
│
├── notebooks/
│   └── earthquakes_analysis_colab.ipynb
│
├── docs/                       ← (Carpeta opcional - puede crearse)
│   ├── GUIA_EJECUCION.md
│   ├── ESTRUCTURA_PRESENTACION.md
│   └── INFORME_FINAL_TERREMOTOS_USGS.md
│
├── setup.ps1                   ← Setup automatizado
├── install_r_packages.R        ← Instalador de paquetes R
├── run_all.ps1                 ← Pipeline completo
├── requirements.txt            ← Dependencias Python
├── .gitignore                  ← Configurado con excepciones para .gitkeep
├── README.md                   ← Documentación completa
└── QUICKSTART.md               ← Guía rápida
```

## ¿Por Qué Usar .gitkeep?

Git no versiona carpetas vacías. Los archivos `.gitkeep` son una convención para:

1. ✅ Mantener la estructura de carpetas en el repositorio
2. ✅ Evitar errores cuando alguien clona el repo
3. ✅ Documentar qué carpeta contendrá qué tipo de archivos
4. ✅ Eliminar la necesidad de crear carpetas manualmente

## Configuración del .gitignore

El `.gitignore` está configurado para:

```gitignore
# Excluir archivos pesados pero mantener carpetas
data/raw/*.csv
data/processed/*.csv
outputs/figures/*.png
outputs/results/*.txt
outputs/results/models/*.pkl

# Mantener la estructura con .gitkeep
!data/raw/.gitkeep
!data/processed/.gitkeep
!outputs/figures/.gitkeep
!outputs/results/.gitkeep
!outputs/results/models/.gitkeep
```

## Archivos que SÍ se versionan

✅ **Scripts y código**:
- Todos los archivos `.py` en `scripts/python/`
- Todos los archivos `.R` en `scripts/R/`
- Notebook `.ipynb` en `notebooks/`

✅ **Configuración y automatización**:
- `setup.ps1`
- `run_all.ps1`
- `install_r_packages.R`
- `requirements.txt`
- `.gitignore`

✅ **Documentación**:
- `README.md`
- `QUICKSTART.md`
- Todos los archivos `.md` en `docs/`

✅ **Estructura de carpetas**:
- Archivos `.gitkeep` en todas las carpetas importantes

## Archivos que NO se versionan

❌ **Datos pesados** (se generan localmente):
- `data/raw/Earthquakes_USGS.csv` (1.89 GB - descargar de Kaggle)
- `data/processed/earthquakes_clean.csv` (1.6 GB - generado por pipeline)

❌ **Outputs generados** (se recrean con `run_all.ps1`):
- 16 visualizaciones PNG en `outputs/figures/`
- 5 archivos TXT de estadísticas en `outputs/results/`
- 5 modelos ML (.pkl) en `outputs/results/models/`

❌ **Artefactos de desarrollo**:
- `__pycache__/` (Python)
- `.Rhistory` (R)
- `.vscode/` (IDE)
- `.DS_Store` (macOS)

## Ventajas de Esta Estructura

1. **Clone-Ready**: Al clonar, todas las carpetas ya existen
2. **Sin errores**: Los scripts no fallan por carpetas faltantes
3. **Documentado**: Cada `.gitkeep` explica qué contendrá la carpeta
4. **Ligero**: El repo pesa <5 MB (sin datos ni outputs)
5. **Profesional**: Sigue las mejores prácticas de Git

## Comandos Útiles

### Ver estructura local (con archivos generados)
```powershell
tree /F
```

### Ver estructura del repo (solo versionados)
```powershell
git ls-tree -r --name-only HEAD
```

### Verificar qué archivos Git ignora
```powershell
git status --ignored
```

### Agregar nuevos archivos respetando .gitignore
```powershell
git add .
```

## Para Nuevos Contribuidores

Cuando clones este repositorio:

1. ✅ Las carpetas ya estarán creadas (gracias a `.gitkeep`)
2. ✅ Solo ejecuta `.\setup.ps1` para instalar dependencias
3. ✅ Descarga el dataset manualmente en `data/raw/`
4. ✅ Ejecuta `.\run_all.ps1` para generar todos los outputs

**No necesitas crear ninguna carpeta manualmente.**

---

Esta estructura garantiza que el repositorio sea completamente funcional desde el primer `git clone`.
