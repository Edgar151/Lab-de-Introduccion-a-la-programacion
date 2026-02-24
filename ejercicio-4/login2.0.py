usuario = "admin"
contraseña = "Admin2026"
usuario_1 = ""
contraseña_1 = ""
intentos = 0
menu=0


def contar_pass(contraseña_1):
     numero_letras = len(contraseña_1)
     if numero_letras < 8:
          print("La contraseña debe tener minimo 8 caracteres")

def numero(contraseña_1):
    if not any(c.isdigit() for c in contraseña_1):
        print("La contraseña debe tener al menos un numero")

def letra(contraseña_1):
    if not any(c.isalpha() for c in contraseña_1):
        print("La contraseña debe contener al menos una letra")

while intentos < 3:

    usuario_1 = input("ingresa el Usuario:\n")
    if not usuario_1.isalnum():
            print("solo se permite alfanumerico")
            
    contraseña_1 = input("ingresa tu contraseña\n")

    contar_pass(contraseña_1)
    numero(contraseña_1)
    letra(contraseña_1)

    if not contraseña_1.isalnum():
            print("solo se permite alfanumerico")
    if " " in usuario_1 or " " in contraseña_1:
            print("No se permiten espacios")
    
    if usuario != usuario_1:
         print("el usuario es incorrecto")
    elif contraseña != contraseña_1: 
        print("la contraseña es incorrecta")
    
    if usuario_1 == usuario and contraseña_1 == contraseña:
        print("Acceso concedido")
        acceso = 1
        while acceso==1:
            menu = int(input("Ingresa una opcion\n 1 Clasificar numero \n 2 Categoria de edad y permisos \n 3 Calcular tarifa final \n 4 Cerrar sesion \n 5 Salir \n"))
            match menu:
                 case 1:
                    print("elegiste, Claisificar numeros")
                 case 2:
                    print("elegiste, Categoria de edad y permisos")
                 case 3:
                    print("elegiste, Calcular tarifa final")
                 case 4:
                      acceso = 0
                 case 5:
                    print("todo termino gracias por usar mi programa")
                    acceso = -1
                    break 
                 case _:
                    print("opcion no valida")
                    
        if acceso == -1:
         break 
    else:
          print("Usuario o Contrseña incorrectos")
          intentos +=1

if intentos >=3:
    print("Intentos caducados vuelve a intenterlo mas tarde")
