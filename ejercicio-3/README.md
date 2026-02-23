# 🔐 Sistema de Login en Python
# Autor: Edgar Estrella
# ----------------------------------------
# Sistema básico de autenticación con:
# - Validación de usuario
# - Validación de contraseña
# - Máximo 3 intentos
# - Restricción a caracteres alfanuméricos
# ----------------------------------------

---

## 📌 1. VARIABLES GLOBALES

```bash
# Credenciales registradas (simulación de base de datos)
usuario = "admin"
contraseña = "Admin2026"

# Variables de entrada
usuario_1 = ""
contraseña_1 = ""

# Contador de intentos
intentos = 0
```

---

## 🧠 2. FUNCIONES DE VALIDACIÓN

```bash
# Validar longitud mínima
def contar_pass(contraseña_1):
    if len(contraseña_1) < 8:
        print("❌ Mínimo 8 caracteres")

# Validar que contenga al menos un número
def numero(contraseña_1):
    if not any(c.isdigit() for c in contraseña_1):
        print("❌ Debe contener un número")

# Validar que contenga al menos una letra
def letra(contraseña_1):
    if not any(c.isalpha() for c in contraseña_1):
        print("❌ Debe contener una letra")
```

---

## 🔁 3. CICLO PRINCIPAL (MÁXIMO 3 INTENTOS)

```bash
while intentos < 3:

    # ---------------------------
    # 👤 VALIDACIÓN DE USUARIO
    # ---------------------------
    usuario_1 = input("Ingresa el Usuario:\n")

    if not usuario_1.isalnum():
        print("⚠ Solo se permite alfanumérico")

    # ---------------------------
    # 🔐 VALIDACIÓN DE CONTRASEÑA
    # ---------------------------
    contraseña_1 = input("Ingresa tu contraseña:\n")

    contar_pass(contraseña_1)
    numero(contraseña_1)
    letra(contraseña_1)

    if not contraseña_1.isalnum():
        print("⚠ Solo se permite alfanumérico")

    if " " in usuario_1 or " " in contraseña_1:
        print("⚠ No se permiten espacios")

    # ---------------------------
    # 🆚 COMPARACIÓN DE DATOS
    # ---------------------------
    if usuario != usuario_1:
        print("❌ Usuario incorrecto")

    elif contraseña != contraseña_1:
        print("❌ Contraseña incorrecta")

    # ---------------------------
    # ✅ ACCESO CORRECTO
    # ---------------------------
    if usuario_1 == usuario and contraseña_1 == contraseña:
        print("✅ Acceso concedido")
        break

    # ---------------------------
    # 🚫 ACCESO DENEGADO
    # ---------------------------
    else:
        print("🚫 Usuario o contraseña incorrectos")
        intentos += 1
```

---

## ⛔ 4. BLOQUEO DEL SISTEMA

```bash
if intentos >= 3:
    print("⛔ Intentos caducados. Vuelve a intentarlo más tarde.")
```

---

## 📊 FLUJO GENERAL

Inicio  
↓  
Ingresar usuario  
↓  
Validar formato  
↓  
Ingresar contraseña  
↓  
Validar reglas  
↓  
Comparar credenciales  
↓  
¿Correcto?  
├── Sí → Acceso concedido  
└── No → Aumentar intento  
         ↓  
     ¿3 intentos?  
         ├── Sí → Bloqueo  
         └── No → Repetir  

---

## 🧩 NOTA TÉCNICA

Python es estricto con la indentación.  
Un error en espacios o estructura puede romper la ejecución.  
Las funciones actuales solo imprimen errores (no usan return).  
El sistema puede mejorarse usando validaciones booleanas.

---
