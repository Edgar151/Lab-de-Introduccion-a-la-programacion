#  🐍 Creación y Uso de Entorno Virtual en Python + Instalación de Numpy (Windows)

Este instructivo documenta paso a paso cómo crear, activar y verificar un entorno virtual (venv) en Python, instalar numpy y configurarlo correctamente en VS Code, incluyendo capturas reales del proceso.

##  📌 ¿Qué es un entorno virtual?

Un entorno virtual es un espacio aislado donde Python instala librerías solo para un proyecto, evitando conflictos con:

Otras versiones de Python

Librerías globales

Otros proyectos

Es una práctica fundamental en el desarrollo profesional.

✅ Requisitos

Windows

Python 3.11 o superior

CMD o PowerShell

VS Code

### Verificar instalación de Python:
 ```bash
python --version
```
### 📁 1. Crear y entrar a la carpeta del proyecto
```bash
cd C:\mkdir python\entorno1
```

### 🧱 2. Crear el entorno virtual
```bash
python -m venv env
```

Esto crea la carpeta:

env/


Que contiene la instalación aislada de Python.

▶️ 3. Activar el entorno virtual

En Windows:
```bash
env\Scripts\activate
```

Si se activa correctamente aparecerá:

(env) C:\python\entorno1>


📸 Captura – Entorno virtual activo y verificación con where python:

🔎 4. Verificar que se está usando el Python del entorno
where python


Debe mostrar:

C:\python\entorno1\env\Scripts\python.exe


Esto confirma que NO estás usando el Python global.

🔄 5. Actualizar pip
python -m pip install --upgrade pip


En tu caso se actualizó de:

pip 24.0 → pip 26.0.1

📦 6. Instalar numpy dentro del entorno
python -m pip install numpy


📸 Captura – Instalación correcta de numpy:

Verificación adicional:

pip list

🧠 7. Probar numpy desde Python

Entrar al intérprete:

python


Luego escribir:

import numpy as np
print(np.random.randint(1, 101))


Ejemplo de salida:

71


Salir del intérprete:

exit()

💻 8. Configurar el intérprete en VS Code

Abrir el proyecto en VS Code:

code .


Presionar:

Ctrl + Shift + P


Escribir:

Python: Select Interpreter


Seleccionar:

Python 3.11.9 (env) \Scripts\python.exe


📸 Captura – Selección del intérprete correcto:

🧪 9. Probar desde un archivo .py

Crear archivo:

New-Item mat.py


Contenido del archivo:

import numpy as np

numero = np.random.randint(1, 101)
print(numero)


Ejecutar:

python mat.py

🚫 10. Desactivar el entorno virtual

Cuando termines:

deactivate


El (env) desaparecerá de la terminal.

📂 11. Ignorar el entorno en Git

Crear .gitignore y agregar:

env/

✅ Conclusión

✔ Se creó correctamente el entorno virtual
✔ Se activó correctamente
✔ Se verificó con where python
✔ Se actualizó pip
✔ Se instaló numpy correctamente
✔ Se configuró el intérprete en VS Code
✔ Se probó el funcionamiento con código real

🎯 Importancia Profesional

El uso de entornos virtuales es obligatorio en:

Desarrollo de software

Ciencia de datos

Ingeniería en software

Proyectos académicos universitarios

Permite mantener proyectos organizados, reproducibles y sin conflictos.
