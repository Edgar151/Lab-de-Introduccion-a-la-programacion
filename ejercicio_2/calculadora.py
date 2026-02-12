numero = int(input("Ingresa un número: "))
original = numero

# ------ Binario --------
binario = ""

if numero == 0:
    binario = "0"
else:
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

print("Binario:", binario)

#----- octal-----------
numero = original
residuo = 0
octal= ""
digitos = "01234567"

if numero == 0:
    octal = "0"
else:
    while numero > 0:
        residuo = numero % 8
        octal = digitos[residuo] + octal
        numero = numero // 8
print("octal:", octal)

# --------- Hexadecimal ---------
numero = original
hexagecimal = ""
digitos = "0123456789ABCDEF"
residuo = 0
if numero == 0:
    hexagecimal = "0"
else:
    while numero > 0:
        residuo = numero % 16
        hexagecimal = digitos[residuo] + hexagecimal
        numero = numero // 16

print("Hexadecimal:", hexagecimal)
