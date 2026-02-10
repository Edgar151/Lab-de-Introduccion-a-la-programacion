📌 1. ¿Qué es un entorno virtual?

Un entorno virtual (venv) es una carpeta especial que contiene una instalación aislada de Python.

Sirve para:

Instalar librerías sin afectar otras instalaciones del sistema.

Tener dependencias diferentes para cada proyecto.

Trabajar de manera profesional y organizada.

Evitar conflictos entre versiones de librerías.

📌 Regla profesional:
Cada proyecto debe tener su propio entorno virtual.

🧩 PROCESO PASO A PASO
🔹 2. Verificar que Python esté instalado
Abrir la terminal (CMD)

Presiona Win + R

Escribe:

cmd


Presiona Enter

Verificar versión de Python
python --version


Si aparece algo como:

Python 3.11.9


Entonces está correctamente instalado.

⚠️ Si no funciona, descarga Python desde:
https://www.python.org

Y marca la opción:

✔ Add Python to PATH

🔹 3. Crear la carpeta del proyecto
cd C:\
mkdir python_proyecto
cd python_proyecto

Explicación:

cd C:\ → Te lleva al disco C

mkdir python_proyecto → Crea la carpeta

cd python_proyecto → Entra a la carpeta

🔹 4. Crear el entorno virtual
python -m venv env

Explicación:

-m venv → Ejecuta el módulo que crea entornos virtuales

env → Nombre del entorno (puede cambiarse, pero normalmente se usa "env")

Se creará una carpeta llamada:

env/

🔹 5. Activar el entorno virtual (Windows)
env\Scripts\activate


Si se activa correctamente verás algo como:

(env) C:\python_proyecto>


Eso significa que el entorno está activo.

🔹 6. Verificar que estás usando el Python del entorno
where python


Debe aparecer algo como:

C:\python_proyecto\env\Scripts\python.exe


Esto confirma que estás usando el entorno virtual y no el Python global.

📷 Evidencia 1 – Verificación del entorno en la terminal

🔹 7. Actualizar pip
python -m pip install --upgrade pip

🔹 8. Instalar librerías (ejemplo: numpy)
pip install numpy


Verificar instalación:

pip list


Debe aparecer:

numpy

📷 Evidencia 2 – Instalación de numpy

🔹 9. Abrir proyecto en Visual Studio Code

Desde la carpeta del proyecto:

code .


⚠️ Si no funciona, reinstala VS Code y marca:

✔ Add to PATH

🔹 10. Seleccionar el intérprete correcto en VS Code

Presiona:

Ctrl + Shift + P


Escribe:

Python: Select Interpreter


Selecciona el que tenga la ruta:

python_proyecto\env\Scripts\python.exe

📷 Evidencia 3 – Selección del intérprete

🔹 11. Probar que todo funciona

Crea un archivo llamado:

test.py


Y escribe:

import numpy as np

print("Entorno funcionando correctamente")
print(np.random.randint(1, 101))


Ejecuta el archivo:

python test.py


Si no hay errores, todo está funcionando correctamente.

🔹 12. Desactivar el entorno virtual

Cuando termines:

deactivate


El (env) desaparecerá de la terminal.

✅ CONCLUSIÓN

Ahora sabes:

✔ Verificar Python

✔ Crear una carpeta de proyecto

✔ Crear un entorno virtual

✔ Activarlo

✔ Verificar que funciona

✔ Instalar librerías

✔ Usarlo en VS Code

✔ Desactivarlo

🎯 Importancia Profesional

El uso de entornos virtuales es una práctica fundamental en:

Desarrollo profesional

Ciencia de datos

Ingeniería en software

Desarrollo web

Proyectos académicos

Permite mantener proyectos organizados, limpios y sin conflictos.
