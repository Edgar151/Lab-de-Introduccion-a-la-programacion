MAX_INTENTOS = 3
USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "Admin2026"


def validar_login(usuario_ok: str, contrasena_ok: str) -> bool:
    """Pide credenciales, valida formato y revisa usuario/contraseña."""
    try:
        usuario_ing = input("Ingresa el usuario:\n").strip()
        contrasena_ing = input("Ingresa tu contraseña:\n").strip()

        sin_espacios = (" " not in usuario_ing) and (" " not in contrasena_ing)
        usuario_alnum = usuario_ing.isalnum()
        contrasena_alnum = contrasena_ing.isalnum()
        largo_ok = len(contrasena_ing) >= 8
        numero_ok = any(c.isdigit() for c in contrasena_ing)
        letra_ok = any(c.isalpha() for c in contrasena_ing)

        match sin_espacios:
            case False:
                print("No se permiten espacios")
            case True:
                pass

        match usuario_alnum:
            case False:
                print("Usuario: solo se permite alfanumérico")
            case True:
                pass

        match contrasena_alnum:
            case False:
                print("Contraseña: solo se permite alfanumérico")
            case True:
                pass

        match largo_ok:
            case False:
                print("La contraseña debe tener mínimo 8 caracteres")
            case True:
                pass

        match numero_ok:
            case False:
                print("La contraseña debe tener al menos un número")
            case True:
                pass

        match letra_ok:
            case False:
                print("La contraseña debe contener al menos una letra")
            case True:
                pass

        valido = all(
            (
                sin_espacios,
                usuario_alnum,
                contrasena_alnum,
                largo_ok,
                numero_ok,
                letra_ok,
            )
        )

        match valido:
            case False:
                return False
            case True:
                pass

        match (usuario_ing == usuario_ok, contrasena_ing == contrasena_ok):
            case (True, True):
                print("Acceso concedido ✅")
                return True
            case (False, _):
                print("El usuario es incorrecto")
                return False
            case (True, False):
                print("La contraseña es incorrecta")
                return False

    except Exception:
        print("Ingresa algo válido")
        return False


def clasificar_numeros() -> None:
    """Clasifica números hasta que el usuario escriba 's'."""
    while True:
        entrada = input(
            "Ingresa el número que quieres clasificar "
            "(si quieres salir ingresa 's'):\n"
        ).strip().lower()

        match entrada:
            case "s":
                break
            case _:
                pass

        try:
            n = int(entrada)
        except ValueError:
            print("Entrada inválida\n")
            continue

        match (n > 0, n < 0):
            case (True, False):
                print("El número es positivo")
            case (False, True):
                print("El número es negativo")
            case (False, False):
                print("El número es 0")

        match n:
            case 0:
                print("")
            case _:
                match n % 2:
                    case 0:
                        print("El número es par\n")
                    case _:
                        print("El número es impar\n")


def categoria_edad_y_permisos() -> None:
    """Opción 2: edad + INE + licencia."""
    while True:
        print("Elegiste: Categoría de edad y permisos")

        try:
            edad = int(input("Ingresa una edad válida entre 0 a 120:\n"))
        except ValueError:
            print("Ingresa una edad válida\n")
            continue

        match 0 <= edad <= 120:
            case False:
                print("Ingresa una edad válida\n")
                continue
            case True:
                pass

        ine = input("¿Cuentas con Identificación oficial? (s/n):\n").strip().lower()
        match ine in ("s", "n"):
            case False:
                print("Ingresa una opción válida en INE\n")
                continue
            case True:
                pass

        licencia = input("¿Cuentas con licencia de conducir? (s/n):\n").strip().lower()
        match licencia in ("s", "n"):
            case False:
                print("Ingresa una opción válida en Licencia\n")
                continue
            case True:
                pass

        print("Datos correctos ✅\n")

        match (edad <= 12, edad <= 17, edad <= 64):
            case (True, _, _):
                print("Estás en una etapa de niñez, no puedes ingresar\n")
            case (False, True, _):
                print(
                    "Estás en adolescencia: puedes registrarte, "
                    "pero no comprar sin tutor\n"
                )
            case (False, False, True):
                print("Estás en adultez: puedes comprar sin tutor\n")
            case (False, False, False):
                print("Estás en adulto mayor: tienes derecho a tu compra legal\n")

        match (ine == "s") and (edad >= 21):
            case True:
                print("Acceso al servicio premium\n")
            case False:
                print("No puedes realizar la compra\n")

        match (licencia == "s") and (edad >= 18):
            case True:
                print("Sí puedes conducir\n")
            case False:
                print("No puedes conducir (sin licencia)\n")

        break


def calcular_tarifa_final() -> None:
    """Opción 3: calcular servicio final con recargos y descuentos."""
    while True:
        print("Elegiste: Calcular tarifa final")

        servicio = 200.0

        try:
            edad = int(input("Ingresa una edad de 0 a 120:\n"))
        except ValueError:
            print("Ingresa una edad válida\n")
            continue

        match 0 <= edad <= 120:
            case False:
                print("Ingresa una edad válida\n")
                continue
            case True:
                pass

        dia = input(
            "Ingresa qué día de la semana es:\n"
            "1 Lunes\n2 Martes\n3 Miércoles\n4 Jueves\n"
            "5 Viernes\n6 Sábado\n7 Domingo\n"
        ).strip()

        match dia in ("1", "2", "3", "4", "5", "6", "7"):
            case False:
                print("Ingresa una opción válida en día\n")
                continue
            case True:
                pass

        estudiante = input("¿Eres estudiante? (s/n):\n").strip().lower()
        match estudiante in ("s", "n"):
            case False:
                print("Ingresa una opción válida en Estudiante\n")
                continue
            case True:
                pass

        miembro = input("¿Eres miembro? (s/n):\n").strip().lower()
        match miembro in ("s", "n"):
            case False:
                print("Ingresa una opción válida en Miembro\n")
                continue
            case True:
                pass

        metodo = input("Método de pago (e=efectivo, t=tarjeta):\n").strip().lower()
        match metodo in ("e", "t"):
            case False:
                print("Ingresa un método de pago válido\n")
                continue
            case True:
                pass

        match dia in ("6", "7"):
            case True:
                print("Se te aplicará un recargo del 10%")
                servicio *= 1.10
            case False:
                pass

        servicio_base = servicio
        porcentaje = 0

        match (edad <= 12, edad <= 17, edad <= 64):
            case (True, _, _):
                porcentaje += 50
            case (False, True, _):
                porcentaje += 20
            case (False, False, True):
                porcentaje += 0
            case (False, False, False):
                porcentaje += 30

        match (estudiante == "s") and (edad >= 13):
            case True:
                porcentaje += 15
            case False:
                pass

        match miembro == "s":
            case True:
                porcentaje += 10
            case False:
                pass

        match metodo == "e":
            case True:
                porcentaje += 5
            case False:
                pass

        match porcentaje > 60:
            case True:
                print(f"Tu descuento era de {porcentaje}% pero el máximo es 60%")
                porcentaje = 60
            case False:
                pass

        descuento = servicio_base * (porcentaje / 100)
        total = servicio_base - descuento

        print(f"Servicio base (con recargo si aplica): {servicio_base:.2f}")
        print(f"Descuento aplicado: {porcentaje}%")
        print(f"Monto de descuento: {descuento:.2f}")
        print(f"TOTAL A PAGAR: {total:.2f}\n")

        break


def menu_principal() -> str:
    """Devuelve 'logout' o 'exit' según la opción elegida."""
    while True:
        try:
            opcion = int(
                input(
                    "Ingresa una opción:\n"
                    "1 Clasificar número\n"
                    "2 Categoría de edad y permisos\n"
                    "3 Calcular tarifa final\n"
                    "4 Cerrar sesión\n"
                    "5 Salir\n"
                )
            )
        except ValueError:
            print("Opción inválida, ingresa un número.\n")
            continue

        match opcion:
            case 1:
                clasificar_numeros()
            case 2:
                categoria_edad_y_permisos()
            case 3:
                calcular_tarifa_final()
            case 4:
                print("Sesión cerrada.\n")
                return "logout"
            case 5:
                print("Todo terminó, gracias por usar mi programa.")
                return "exit"
            case _:
                print("Opción no válida\n")


def main() -> None:
    """Login (máx 3 intentos) -> menú."""
    while True:
        intentos = 0

        while intentos < MAX_INTENTOS:
            match validar_login(USUARIO_ADMIN, CONTRASENA_ADMIN):
                case True:
                    accion = menu_principal()
                    match accion:
                        case "exit":
                            return
                        case "logout":
                            break
                case False:
                    intentos += 1
                    print(f"Intento {intentos}/{MAX_INTENTOS}\n")

        match intentos >= MAX_INTENTOS:
            case True:
                print("Intentos caducados, vuelve a intentarlo más tarde.")
                return
            case False:
                pass


match __name__:
    case "__main__":
        main()
    case _:
        pass
