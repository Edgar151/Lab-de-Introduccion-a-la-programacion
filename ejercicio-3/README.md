# 🔐 Sistema de Login en Python
## Autor: Edgar Estrella
---
# 📘 DESCRIPCIÓN GENERAL
### Este programa simula un sistema básico de autenticación.
### Permite al usuario ingresar credenciales y valida:
###   - Formato del usuario
###   - Reglas de seguridad de la contraseña
###   - Coincidencia con credenciales registradas
###   - Límite máximo de 3 intentos
---

---

## 📌 1️⃣ VARIABLES GLOBALES

### Estas variables representan las credenciales registradas.
### En un sistema real vendrían de una base de datos.

```bash
usuario = "admin"
contraseña = "Admin2026"
```

### Variables auxiliares que almacenan lo que el usuario escribe.
### Se inicializan vacías porque aún no hay entrada.

```bash
usuario_1 = ""
contraseña_1 = ""
```

### Contador de intentos fallidos.
### Se usa para limitar el acceso a máximo 3 intentos.

```bash
intentos = 0
```

---

## 🧠 2️⃣ FUNCIONES DE VALIDACIÓN

### Estas funciones separan la lógica de validación.
### Esto mejora la organización y permite reutilizar código.

---

### 🔎 contar_pass()

### Verifica que la contraseña tenga mínimo 8 caracteres.
### Utiliza len() para medir la longitud del string.

```bash
def contar_pass(contraseña_1):
    if len(contraseña_1) < 8:
        print("❌ Mínimo 8 caracteres")
```

---

### 🔢 numero()

### Verifica que exista al menos un número.
### any() recorre cada carácter y evalúa si alguno cumple la condición.

```bash
def numero(contraseña_1):
    if not any(c.isdigit() for c in contraseña_1):
        print("❌ Debe contener un número")
```

---

### 🔤 letra()

### Verifica que exista al menos una letra.
### isalpha() detecta caracteres alfabéticos.

```bash
def letra(contraseña_1):
    if not any(c.isalpha() for c in contraseña_1):
        print("❌ Debe contener una letra")
```

---

## 🔁 3️⃣ CICLO PRINCIPAL

### while intentos < 3:
### El programa se ejecuta mientras los intentos sean menores a 3.
### Cada fallo aumenta el contador.

```bash
while intentos < 3:
```

---

## 👤 4️⃣ VALIDACIÓN DE USUARIO

### input() captura lo que el usuario escribe.
### isalnum() permite únicamente letras y números.
### Evita caracteres especiales y símbolos.

```bash
usuario_1 = input("Ingresa el Usuario:\n")

if not usuario_1.isalnum():
    print("⚠ Solo se permite alfanumérico")
```

---

## 🔐 5️⃣ VALIDACIÓN DE CONTRASEÑA

### Se solicita la contraseña.
### Luego se ejecutan las funciones creadas previamente.
### También se valida que no contenga espacios.

```bash
contraseña_1 = input("Ingresa tu contraseña:\n")

contar_pass(contraseña_1)
numero(contraseña_1)
letra(contraseña_1)

if not contraseña_1.isalnum():
    print("⚠ Solo se permite alfanumérico")

if " " in usuario_1 or " " in contraseña_1:
    print("⚠ No se permiten espacios")
```

---

## 🆚 6️⃣ COMPARACIÓN DE CREDENCIALES

### Se comparan los datos ingresados con los registrados.
### Si el usuario no coincide, se muestra error.
### Si la contraseña no coincide, también.

```bash
if usuario != usuario_1:
    print("❌ Usuario incorrecto")

elif contraseña != contraseña_1:
    print("❌ Contraseña incorrecta")
```

---

## ✅ 7️⃣ ACCESO CORRECTO

### Si ambos coinciden exactamente,
### se concede acceso y se rompe el ciclo con break.

```bash
if usuario_1 == usuario and contraseña_1 == contraseña:
    print("✅ Acceso concedido")
    break
```

---

## 🚫 8️⃣ INTENTO FALLIDO

### Si no coinciden, entra en el else.
### Se incrementa el contador intentos en +1.

```bash
else:
    print("🚫 Usuario o contraseña incorrectos")
    intentos += 1
```

---

## ⛔ 9️⃣ BLOQUEO DEL SISTEMA

### Cuando intentos alcanza 3,
### el sistema se bloquea y muestra mensaje final.

```bash
if intentos >= 3:
    print("⛔ Intentos caducados. Vuelve más tarde.")
```

---

## 📊 FLUJO LÓGICO DEL PROGRAMA

Inicio  
↓  
Inicializar variables  
↓  
Ejecutar ciclo while (máx 3 intentos)  
↓  
Validar usuario  
↓  
Validar contraseña  
↓  
Comparar credenciales  
↓  
¿Coinciden?  
├── Sí → Acceso concedido → break  
└── No → intentos += 1  
         ↓  
     ¿intentos == 3?  
         ├── Sí → Bloqueo  
         └── No → Repetir ciclo  

---

## 🧩 ANÁLISIS TÉCNICO

✔ Código modular gracias a funciones  
✔ Uso correcto de estructuras condicionales  
✔ Control de flujo con while y break  
✔ Validación básica de seguridad  

⚠ Mejoras posibles:
- Usar return en funciones
- Detener flujo si validación falla
- Usar hash para contraseña
- Implementar sistema orientado a objetos

---

# 🚀 CONCLUSIÓN

Este sistema representa una implementación básica de autenticación
en consola utilizando estructuras fundamentales de Python:
variables, funciones, ciclos y condicionales.

Es un buen ejercicio para comprender:
- Control de flujo
- Validación de datos
- Seguridad básica en entradas

---
