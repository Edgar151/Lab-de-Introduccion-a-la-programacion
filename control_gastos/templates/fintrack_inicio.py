# ==============================================================================
#                 GESTOR DE FINANZAS PERSONALES — Terminal
# ==============================================================================

# Base de datos simulada con listas indexadas (se conectan por su posición)
usuarios      = ["morgan", "chagouaz"]
passwords     = ["morgan123", "chagouaz123"]
saldos        = [15000.0, 8500.0]
transacciones = [[], []]   # Listas vacías para el historial de cada usuario

# ------------------------------------------------------------------------------
#  MÓDULO DE AUTENTICACIÓN
# ------------------------------------------------------------------------------
def autenticar():
    """ Solicita el usuario y contraseña para validar el acceso. """
    print("\n--- INICIO DE SESIÓN ---")
    usuario  = input("Usuario: ")
    password = input("Contraseña: ")

    # Comprobamos si el usuario existe en la lista
    if usuario in usuarios:
        i = usuarios.index(usuario) # Obtenemos la posición (índice) del usuario
        
        # Validamos si la contraseña coincide en esa misma posición
        if passwords[i] == password:
            print(f"\n✅ ¡Bienvenido, {usuario}!")
            return i  # Retorna el índice del usuario logueado
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")
    
    return None # Si algo falla, no retorna ningún índice

# ------------------------------------------------------------------------------
#  MÓDULO DE OPERACIONES FINANCIERAS
# ------------------------------------------------------------------------------
def ver_saldo(i):
    """ Muestra el saldo actual del usuario en sesión. """
    print(f"\n💰 Saldo actual: ${saldos[i]}")

def ingresar(i):
    """ Registra un ingreso de dinero en la cuenta del usuario. """
    monto = float(input("Monto a ingresar: $"))
    descripcion = input("Descripción: ")
    
    # Validación básica de negocio
    if monto <= 0:
        print("❌ El monto debe ser mayor a 0.")
        return # Termina la función de inmediato
        
    saldos[i] = saldos[i] + monto # Actualizamos el saldo
    
    # Guardamos los datos de la transacción en una lista de texto directo
    transacciones[i].append(f"▲ INGRESO: +${monto} — {descripcion}")
    print("✅ Ingreso registrado con éxito.")

def gastar(i):
    """ Registra un gasto si el usuario tiene fondos suficientes. """
    monto = float(input("Monto a gastar: $"))
    descripcion = input("Descripción: ")
    
    if monto <= 0:
        print("❌ El monto debe ser mayor a 0.")
        return
        
    # Validación para no quedar en saldo negativo
    if monto > saldos[i]:
        print(f"❌ Fondos insuficientes. Tu saldo es de ${saldos[i]}")
        return
        
    saldos[i] = saldos[i] - monto # Restamos el gasto del saldo
    transacciones[i].append(f"▼ GASTO: -${monto} — {descripcion}")
    print("✅ Gasto registrado con éxito.")

def ver_historial(i):
    """ Muestra todos los movimientos registrados por el usuario. """
    print("\n--- HISTORIAL DE MOVIMIENTOS ---")
    
    # Si la lista de transacciones del usuario está vacía
    if not transacciones[i]:
        print("No hay movimientos registrados.")
    else:
        # Recorremos e imprimimos cada movimiento guardado
        for movimiento in transacciones[i]:
            print(movimiento)

def resumen(i):
    """ Muestra los datos generales de la cuenta de forma rápida. """
    print(f"\n📊 RESUMEN DE CUENTA — {usuarios[i]}")
    print(f"Saldo disponible: ${saldos[i]}")
    print(f"Total de movimientos: {len(transacciones[i])}")

def cambiar_password(i):
    """ Cambia la contraseña del usuario tras validar la actual. """
    actual = input("Contraseña actual: ")
    
    if actual != passwords[i]:
        print("❌ Contraseña incorrecta.")
        return
        
    nueva = input("Nueva contraseña: ")
    confirmar = input("Confirma tu nueva contraseña: ")
    
    if nueva == confirmar:
        passwords[i] = nueva # Reemplazamos la contraseña vieja por la nueva
        print("🔒 Contraseña actualizada con éxito.")
    else:
        print("❌ Las contraseñas no coinciden.")

# ------------------------------------------------------------------------------
#  MENÚ PRINCIPAL
# ------------------------------------------------------------------------------
def menu(i):
    """ Muestra las opciones disponibles y redirige a la función seleccionada. """
    activo = True
    while activo:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver saldo")
        print("2. Registrar ingreso")
        print("3. Registrar gasto")
        print("4. Ver historial")
        print("5. Ver resumen")
        print("6. Cambiar contraseña")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if   opcion == "1": ver_saldo(i)
        elif opcion == "2": ingresar(i)
        elif opcion == "3": gastar(i)
        elif opcion == "4": ver_historial(i)
        elif opcion == "5": resumen(i)
        elif opcion == "6": cambiar_password(i)
        elif opcion == "7":
            print("\n👋 ¡Hasta luego!")
            activo = False # Apaga el bucle para cerrar el programa
        else:
            print("❌ Opción inválida.")

# ------------------------------------------------------------------------------
#  INICIO DEL PROGRAMA
# ------------------------------------------------------------------------------
# Primero corremos la autenticación y guardamos la posición devuelta
indice_usuario = autenticar()

# Si el índice es válido (es decir, no es None), abrimos el menú para ese usuario
if indice_usuario is not None:
    menu(indice_usuario)