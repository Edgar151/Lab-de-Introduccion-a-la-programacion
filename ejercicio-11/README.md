# 📷 Escáner PRO — QR & Código de Barras con Flask + ZXing

Una aplicación web ligera, rápida y funcional para escanear **códigos QR y códigos de barras** directamente desde el navegador usando la cámara del dispositivo 📱💻.

Diseñada para ser simple pero potente: detecta códigos en tiempo real, evita lecturas duplicadas y abre automáticamente enlaces detectados.

---

# 🚀 Características principales

* 📷 Acceso a cámara en tiempo real (compatible con celular y PC)
* 🔍 Escaneo de:

  * Códigos QR
  * Códigos de barras (EAN, CODE128, etc.)
* ⚡ Detección rápida y continua
* 🔁 Evita lecturas repetidas
* 🔗 Apertura automática de URLs
* 🔊 Feedback sonoro al escanear
* 🎯 Uso de cámara trasera en móviles (modo óptimo)

---

# 🧠 Tecnologías utilizadas

## Backend

* **Flask** → servidor web ligero en Python

## Frontend

* **HTML5 + CSS3 + JavaScript**
* **ZXing (Zebra Crossing)** → librería para escaneo de códigos

---

# 📦 Instalación

## 1. Clonar o copiar el proyecto

```bash
git clone <tu-repo>
cd <tu-proyecto>
```

## 2. Instalar dependencias

```bash
pip install flask
```

---

# ▶️ Ejecución

```bash
python app.py
```

Luego abre en tu navegador:

```
http://localhost:5000
```

---

# ⚠️ IMPORTANTE — Uso en celular

Los navegadores **bloquean la cámara si no estás en HTTPS**.

## 🔥 Solución recomendada: usar ngrok

### Instalar:

```bash
pip install flask-ngrok
```

### Modificar el código:

```python
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)
```

### Ejecutar:

```bash
python app.py
```

Obtendrás un enlace como:

```
https://xxxx.ngrok.io
```

👉 Ese enlace **sí permite usar la cámara en celular**

---

# 🧩 Estructura del código

## Backend (Flask)

```python
app = Flask(__name__)
```

Inicializa la aplicación web.

```python
@app.route("/")
def home():
    return render_template_string(HTML)
```

* Define la ruta principal `/`
* Renderiza directamente el HTML embebido

```python
app.run(debug=True, host="0.0.0.0", port=5000)
```

* Ejecuta el servidor
* `0.0.0.0` permite acceso desde otros dispositivos en la red

---

## Frontend (HTML + JS)

### 📷 Video de la cámara

```html
<video id="video" autoplay playsinline></video>
```

* `autoplay`: inicia automáticamente
* `playsinline`: evita pantalla completa en iOS

---

### 🧠 Inicialización del lector

```javascript
const codeReader = new ZXing.BrowserMultiFormatReader();
```

Permite detectar múltiples tipos de códigos (QR + barras).

---

### 🎯 Acceso a cámara trasera

```javascript
facingMode: { ideal: "environment" }
```

* Fuerza el uso de la cámara trasera en móviles
* Mejora la precisión del escaneo

---

### 🔍 Escaneo en tiempo real

```javascript
codeReader.decodeFromConstraints(...)
```

* Lee continuamente los frames del video
* Detecta códigos automáticamente

---

### 🚫 Evitar lecturas duplicadas

```javascript
if (result.text !== lastResult)
```

Evita repetir el mismo resultado múltiples veces.

---

### 🔊 Feedback sonoro

```javascript
new Audio("...").play();
```

Reproduce sonido al detectar un código.

---

### 🔗 Apertura automática de enlaces

```javascript
if (result.text.startsWith("http"))
```

* Detecta si el contenido es una URL
* Abre automáticamente en otra pestaña

---

# 🎨 Diseño UI

* Fondo oscuro (`#0f0f0f`)
* Bordes neon verde (`#00ff88`)
* Diseño centrado y responsive
* Adaptado para móvil y escritorio

---

# 🧪 Tipos de códigos soportados

* QR Code
* EAN-13 / EAN-8
* Code 128
* Code 39
* UPC
* Otros compatibles con ZXing

---

# 🐞 Problemas comunes y soluciones

## ❌ No detecta la cámara

**Causa:**

* No estás en HTTPS

**Solución:**

* Usa ngrok

---

## ❌ Permiso denegado

**Solución:**

* Ir al candado 🔒 del navegador
* Permitir acceso a cámara

---

## ❌ No escanea bien códigos de barras

**Posibles causas:**

* Mala iluminación
* Código muy pequeño
* Cámara frontal

**Solución:**

* Usa cámara trasera
* Mejora iluminación
* Acerca el código

---

# 🚀 Posibles mejoras

* 📊 Integrar API de productos (ej: código → nombre del producto)
* 💾 Historial de escaneos
* 📱 Convertir a PWA (app instalable)
* 🎯 Auto zoom y enfoque
* 🌐 Soporte offline

---

# 🧾 Licencia

Libre para uso personal y educativo.
Puedes modificarlo y adaptarlo a tus necesidades.

---

# 👨‍💻 Autor

Desarrollado como proyecto práctico usando Flask + ZXing.

---

# 💥 Resumen

Este proyecto es una base sólida para:

* Apps de inventario
* Lectores de productos
* Sistemas de verificación
* Herramientas móviles rápidas

Simple, directo y potente.

---

🔥 Si quieres llevarlo a nivel “industrial” (tipo Walmart / Amazon), se puede escalar con APIs, bases de datos y optimización avanzada.
