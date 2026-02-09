# Lab-de-Introduccion-a-la-programacion
ejercios y documentos de programacion
1. ¿Qué es un entorno virtual?
Un entorno virtual (venv) es una carpeta especial que contiene una instalación aislada de Python.
Sirve para:
Instalar librerías sin afectar otras instalaciones del sistema.
Tener dependencias diferentes para cada proyecto.
Trabajar de manera profesional y organizada.
Cada proyecto debe tener su propio entorno virtual.

2. Paso 1: Verificar que Python esté instalado
Abrir la terminal (CMD)
Presiona Win + R
Escribe:
cmd


Presiona Enter
Verificar versión de Python
En la terminal escribe:
python --version

Si aparece algo como:
Python 3.12.0

Entonces Python está instalado correctamente.
Si no aparece, necesitas instalar Python desde:
https://www.python.org
⚠️ IMPORTANTE: Cuando lo instales, marca la opción
"Add Python to PATH"

3. Paso 2: Crear la carpeta del proyecto
Primero vamos a crear una carpeta donde estará nuestro proyecto.
En la terminal escribe:
cd C:\
mkdir python_proyecto
cd python_proyecto

Explicación:
cd C:\ → Te lleva al disco C
mkdir python_proyecto → Crea la carpeta
cd python_proyecto → Entra a la carpeta
Ahora ya estás dentro del proyecto.

4. Paso 3: Crear el entorno virtual
Escribe:
python -m venv env

Explicación:
-m venv → Ejecuta el módulo que crea entornos virtuales
env → Es el nombre del entorno (se puede llamar diferente, pero normalmente se usa "env")
Después de ejecutar el comando, se creará una carpeta llamada:
env

Dentro estarán todos los archivos del entorno virtual.

5. Paso 4: Activar el entorno virtual
En Windows escribe:
env\Scripts\activate

Si se activa correctamente, verás algo así:
(env) C:\python_proyecto>

Eso significa que el entorno está activo.

6. Paso 5: Verificar que el entorno está funcionando
Escribe:
where python

Debe aparecer algo como:
C:\python_proyecto\env\Scripts\python.exe

Eso confirma que estás usando el Python del entorno virtual y no el global.

7. Paso 6: Instalar librerías (ejemplo con numpy)
Con el entorno activado escribe:
pip install numpy

Para verificar que se instaló correctamente:
pip list

Ahí debe aparecer numpy en la lista.

8. Paso 7: Abrir el proyecto en Visual Studio Code
Desde la misma carpeta escribe:
code .

(Si no funciona, instala VS Code y asegúrate de marcar la opción
"Add to PATH")

9. Seleccionar el intérprete correcto en VS Code
Dentro de VS Code:
Presiona:
Ctrl + Shift + P


Escribe:
Python: Select Interpreter


Selecciona el que tenga la ruta:
python_proyecto\env\Scripts\python.exe


Eso asegura que VS Code use el entorno virtual.

10. Probar que todo funciona
Crea un archivo llamado:
test.py

Y escribe:
import numpy as np

print("Entorno funcionando correctamente")

Ejecuta el archivo.
Si no hay errores, todo está instalado correctamente.

11. Desactivar el entorno virtual
Cuando termines, escribe:
deactivate

Y desaparecerá el (env) de la terminal.

CONCLUSIÓN
Ahora sabes:
✅ Verificar Python
✅ Crear una carpeta de proyecto
✅ Crear un entorno virtual
✅ Activarlo
✅ Verificar que funciona
✅ Instalar librerías
✅ Usarlo en VS Code
✅ Desactivarlo
Este procedimiento es fundamental para trabajar trabajar profesionalmente con Python.


