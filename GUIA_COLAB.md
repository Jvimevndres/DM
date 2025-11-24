# 🌐 Guía Rápida: Google Colab

## ¿Qué es Google Colab?

Google Colab es un entorno de Jupyter Notebook gratuito que se ejecuta en la nube. No necesitas instalar nada en tu computadora.

**Ventajas:**
- ✅ Gratis y sin instalación
- ✅ Ejecución en servidores de Google
- ✅ GPU/TPU disponible
- ✅ Fácil de compartir
- ✅ Guardado automático en Google Drive

---

## 🚀 Inicio Rápido (5 pasos)

### Paso 1: Abrir Google Colab

1. Ve a: **https://colab.research.google.com/**
2. Inicia sesión con tu cuenta de Google

### Paso 2: Subir el Notebook

**Opción A: Desde tu computadora**
1. File → Upload notebook
2. Selecciona: `notebooks/earthquakes_analysis_colab.ipynb`

**Opción B: Desde GitHub (si lo subes)**
1. File → Open notebook
2. Tab "GitHub"
3. Pega la URL de tu repositorio

### Paso 3: Subir el Dataset

**Método 1: Carga Manual (Recomendado)**

Ejecuta la celda que tiene:
```python
from google.colab import files
uploaded = files.upload()
```

Luego:
1. Haz clic en "Choose Files"
2. Selecciona `Earthquakes_USGS.csv`
3. Espera a que termine de subir (1-5 minutos)

**Método 2: Desde Google Drive**

Si tu dataset está en Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')

# Luego carga desde Drive
df = pd.read_csv('/content/drive/MyDrive/Earthquakes_USGS.csv')
```

### Paso 4: Ejecutar Todo

**Opción A: Ejecutar todo el notebook**
- Runtime → Run all (o Ctrl+F9)
- Espera 15-30 minutos

**Opción B: Ejecutar celda por celda**
- Haz clic en cada celda y presiona Shift+Enter
- Revisa resultados antes de continuar

### Paso 5: Descargar Resultados

```python
from google.colab import files

# Descargar dataset limpio
files.download('earthquakes_clean.csv')

# O comprimir y descargar todo
!zip -r results.zip outputs/
files.download('results.zip')
```

---

## 💡 Tips para Usar Colab

### Acelerar la Ejecución

1. **Activar GPU** (opcional, para modelos grandes):
   - Runtime → Change runtime type
   - Hardware accelerator → GPU
   - Save

2. **Usar muestra más pequeña:**
   ```python
   # En la celda de carga de datos, cambia:
   sample_size = 100000  # En lugar de procesar todo
   ```

### Guardar tu Trabajo

- **Auto-guardado:** Colab guarda automáticamente en Google Drive
- **Manual:** File → Save (Ctrl+S)
- **Descargar:** File → Download → Download .ipynb

### Compartir tu Notebook

1. **Con profesor/compañeros:**
   - Click en "Share" (arriba derecha)
   - Elige "Anyone with the link"
   - Copy link y comparte

2. **Ver sin ejecutar:**
   - File → Download → Download .ipynb
   - Súbelo a GitHub
   - Se verá automáticamente

---

## 🔧 Solución de Problemas en Colab

### Problema 1: "Session timed out"

**Causa:** Colab desconecta después de 90 min de inactividad

**Solución:**
```javascript
// Ejecuta esto en una celda:
function ClickConnect(){
  console.log("Clicking");
  document.querySelector("colab-connect-button").click()
}
setInterval(ClickConnect, 60000)
```

### Problema 2: "Out of Memory"

**Causa:** Dataset muy grande para RAM disponible

**Solución 1:** Usar muestra
```python
df = pd.read_csv('Earthquakes_USGS.csv', nrows=100000)
```

**Solución 2:** Activar High-RAM runtime
- Runtime → Change runtime type → High-RAM

### Problema 3: Archivo perdido después de desconexión

**Causa:** Colab borra archivos cuando se desconecta

**Solución:** Guardar en Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')

# Guardar dataset limpio en Drive
df.to_csv('/content/drive/MyDrive/earthquakes_clean.csv', index=False)
```

### Problema 4: Carga muy lenta del dataset

**Solución:** Comprimir antes de subir
```powershell
# En tu computadora:
zip Earthquakes_USGS.zip Earthquakes_USGS.csv
```

Luego en Colab:
```python
!unzip Earthquakes_USGS.zip
```

---

## 📊 Visualizar Resultados en Colab

### Gráficos Inline

Los gráficos aparecen automáticamente en Colab. Para mejor visualización:

```python
import matplotlib.pyplot as plt

# Configurar tamaño
plt.figure(figsize=(14, 8))

# Tu código de gráfico aquí
plt.plot(...)

# Mostrar con alta resolución
plt.savefig('grafico.png', dpi=150, bbox_inches='tight')
plt.show()
```

### Tablas Interactivas

```python
# Mostrar tabla con scroll
display(df.head(100))

# O con formato
from IPython.display import display, HTML
display(HTML(df.head(20).to_html()))
```

---

## 🎓 Modo Presentación en Colab

Para presentar tu trabajo:

1. **Ocultar código:**
   - View → Collapse all code

2. **Mostrar solo resultados:**
   - Tools → Settings → Site → Theme → Dark (opcional)
   - Ejecuta todo primero
   - Colapsa celdas de código
   - Scroll por los resultados

3. **Presentar en pantalla completa:**
   - F11 para fullscreen
   - Zoom del navegador: Ctrl + Mouse Wheel

---

## 📥 Exportar desde Colab

### Opción 1: Como Notebook
```
File → Download → Download .ipynb
```
Puedes abrirlo en Jupyter local después.

### Opción 2: Como Python Script
```
File → Download → Download .py
```
Convierte todo el notebook a script Python.

### Opción 3: Como HTML
```python
# Instalar nbconvert
!pip install nbconvert

# Convertir
!jupyter nbconvert --to html /content/earthquakes_analysis_colab.ipynb

# Descargar
from google.colab import files
files.download('earthquakes_analysis_colab.html')
```

### Opción 4: Como PDF
```
File → Print → Save as PDF
```
O usando:
```python
!pip install nbconvert[webpdf]
!jupyter nbconvert --to pdf earthquakes_analysis_colab.ipynb
```

---

## 🔄 Sincronizar con GitHub

### Guardar en GitHub

1. **Desde Colab:**
   - File → Save a copy in GitHub
   - Autoriza GitHub
   - Elige repositorio y branch
   - Add commit message
   - OK

2. **Desde Git local:**
   - Descarga el .ipynb
   - `git add notebooks/earthquakes_analysis_colab.ipynb`
   - `git commit -m "Add Colab notebook"`
   - `git push`

### Abrir desde GitHub

1. En Colab: File → Open notebook
2. Tab "GitHub"
3. Pega URL de tu repo
4. Selecciona el notebook

---

## 🌟 Características Avanzadas

### 1. Instalar Paquetes Adicionales

```python
# Instalar cualquier paquete de Python
!pip install nombre_paquete

# Instalar versión específica
!pip install pandas==1.5.0

# Instalar desde GitHub
!pip install git+https://github.com/usuario/repo
```

### 2. Comandos de Sistema

```python
# Listar archivos
!ls -lh

# Ver uso de disco
!df -h

# Ver uso de RAM
!free -h

# Ver información de CPU/GPU
!nvidia-smi  # Si GPU está activada
```

### 3. Cargar desde URLs

```python
# Descargar dataset desde URL
!wget https://url-del-dataset.com/data.csv

# O con pandas directo
df = pd.read_csv('https://url-del-dataset.com/data.csv')
```

### 4. Formularios Interactivos

```python
#@title Configuración del Análisis { run: "auto" }

sample_size = 50000  #@param {type:"slider", min:10000, max:1000000, step:10000}
n_clusters = 5  #@param {type:"integer"}
generate_maps = True  #@param {type:"boolean"}

print(f"Analizando {sample_size} registros con {n_clusters} clusters")
```

---

## ⚡ Atajos de Teclado en Colab

### Ejecución
- `Ctrl + Enter` - Ejecutar celda actual
- `Shift + Enter` - Ejecutar celda y mover a la siguiente
- `Alt + Enter` - Ejecutar celda e insertar nueva abajo

### Edición
- `Ctrl + M + A` - Insertar celda arriba
- `Ctrl + M + B` - Insertar celda abajo
- `Ctrl + M + D` - Eliminar celda
- `Ctrl + M + M` - Convertir a Markdown
- `Ctrl + M + Y` - Convertir a Code

### Navegación
- `Ctrl + M + K` - Mover celda arriba
- `Ctrl + M + J` - Mover celda abajo
- `Ctrl + F` - Buscar en el notebook
- `Ctrl + H` - Buscar y reemplazar

### Útiles
- `Ctrl + /` - Comentar/descomentar líneas
- `Tab` - Autocompletar
- `Shift + Tab` - Mostrar documentación

---

## 📱 Usar Colab desde Móvil

Sí, ¡puedes usar Colab desde tu celular!

1. **Abrir en navegador móvil:**
   - Ve a colab.research.google.com
   - Funciona en Chrome/Safari móvil

2. **Limitaciones:**
   - Teclado pequeño
   - Difícil editar código extenso
   - Mejor para visualizar resultados

3. **Recomendación:**
   - Ejecuta todo en PC primero
   - Usa móvil solo para revisar/presentar

---

## 🎯 Checklist para Entregar con Colab

Antes de compartir tu notebook:

- [ ] Ejecuta "Restart and run all" para verificar
- [ ] Revisa que todas las celdas ejecutaron sin errores
- [ ] Limpia outputs innecesarios (Cell → Clear outputs)
- [ ] Añade comentarios en celdas complejas
- [ ] Verifica que los gráficos se vean bien
- [ ] Prueba el link compartido en ventana incógnita
- [ ] Guarda una copia de respaldo en Drive

---

## 📧 Compartir con Profesor

### Opción 1: Link de Colab

1. Click en "Share" (arriba derecha)
2. "Get link" → "Anyone with the link can view"
3. Copy link y envía al profesor
4. **Ventaja:** Puede ver y ejecutar directamente

### Opción 2: Descargar y enviar

1. File → Download → Download .ipynb
2. Adjunta en email o plataforma del curso
3. **Ventaja:** No depende de conexión a internet

### Opción 3: GitHub

1. Sube a tu repositorio de GitHub
2. Comparte URL del repositorio
3. **Ventaja:** Muestra tu código profesionalmente

---

## 🏆 Tips para Impresionar

### 1. Usa Markdown Rico

```markdown
# Título Principal

## Subtítulo

### Sección

**Negrita** y *cursiva*

- Lista 1
- Lista 2

1. Numerada 1
2. Numerada 2

> Cita importante

`código inline`

[Link](https://url.com)
```

### 2. Añade Imágenes

```markdown
![Texto alternativo](https://url-de-imagen.com/imagen.png)
```

### 3. Usa Ecuaciones LaTeX

```markdown
$$ y = mx + b $$

$$ R^2 = 1 - \frac{SS_{res}}{SS_{tot}} $$
```

### 4. Crea Tabla de Contenidos

```markdown
## 📑 Contenido

1. [Introducción](#introduccion)
2. [Metodología](#metodologia)
3. [Resultados](#resultados)
```

---

## 🎉 ¡Listo para Usar Colab!

Con esta guía puedes:
- ✅ Subir y ejecutar tu notebook
- ✅ Cargar datasets grandes
- ✅ Generar visualizaciones
- ✅ Compartir tu trabajo
- ✅ Resolver problemas comunes

**Google Colab es perfecto para tu proyecto de terremotos.**

---

## 🔗 Links Útiles

- **Colab:** https://colab.research.google.com/
- **Colab FAQ:** https://research.google.com/colaboratory/faq.html
- **Colab Tutorials:** https://colab.research.google.com/notebooks/
- **Markdown Guide:** https://www.markdownguide.org/cheat-sheet/

---

**¡Disfruta trabajando en la nube! ☁️**
