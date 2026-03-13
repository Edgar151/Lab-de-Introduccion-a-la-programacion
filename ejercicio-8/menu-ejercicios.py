import random
def palabra10():
    i = 1
    palabra = input("Ingresa la palabra que quieres que se repita 10 veces:\n")
    for i in range(10):
        print(palabra)

def edad_cumplida():
    edad = int(input("Ingresa tu edad: "))
    
    for a in range(1, edad + 1):
        print("haz cumplido", a, "Años")

def numeros_impares():
    
    numero = int(input("Ingresa un numero"))
    for a in range(1, numero + 1):
        if a % 2:
           print("el numero:", a, "Es impar" )

def cuenta_atras():
    numeroe = int(input("Ingresa un numero entero"))
    for i in range(numeroe, 0, -1):
        print(i, end=(", "))

def interes():
    invetir=float(input("Ingresa la cantidad que quieres invertir: "))
    interes=float(input("Ingresa el interes anual (%): ")) / 100
    años=int(input("Ingresa cuantos años vas a dejar el dinero: "))
    for i in range(1, años + 1):
        obtenido = invetir * (1 + interes) ** i
        print("Año", i, ":", obtenido)

def triagulo_rectangulo():
    triangulo= input("Ingresa un numero para crear tu triangulo: ")
    for i in range(1, 6):
        print(triangulo * i)

def tablas_de_multiplicar():
    print("te voy a mostrar las tablas del1 al 10")
    for i in range(1, 11):
        print("tablas del", i,)
        print("1 * ",i,"=", i*1)
        print("2 * ",i,"=", i*2)
        print("3 * ",i,"=", i*3)
        print("4 * ",i,"=", i*4)
        print("5 * ",i,"=", i*5)
        print("6 * ",i,"=", i*6)
        print("7 * ",i,"=", i*7)
        print("8 * ",i,"=", i*8)
        print("9 * ",i,"=", i*9)
        print("10 * ",i,"=", i*10)

def triagulo():
    triangulo= input("Ingresa un numero para crear tu triangulo: ")
    for i in range(1, 6):
        print(triangulo * int(random))

print("Ingresa 1 para repetir una palabra 10 veces\nIngresa 2 pasa saber cuantos años haz cumplido")
print("Ingresa 3 para saber numeros impares\nIngresa 4 pasa saber numeros anteriores ")
print("Ingresa 5 para saber la cantidad de capital de una invercion\nIngresa 6 para triangulo rectangulo")
print("Ingresa 7 para trablas de multiplicar\nIngresa 8 para triangulo rectangulo de numeros")
print("Ingresa 9 para validar contraseña\nIngresa 10 para saber numero primo")
opcion = int(input("Ingresa 11 pasa sbaer si tu numero es numero primo\nIngresa 12 pasa saber la letra de la frase\nIngresa 13 para mirar eco y poder salir:\n"))
    
match opcion:
    case 1:
        palabra10()
    case 2:
        edad_cumplida()
    case 3:
        numeros_impares()
    case 4:
        cuenta_atras()
    case 5:
        interes()
    case 6:
        triagulo_rectangulo()
    case 7: 
        tablas_de_multiplicar()
    case 8:

    case _:
        print("Opcion no valida")

