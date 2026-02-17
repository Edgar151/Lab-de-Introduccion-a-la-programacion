# 🧮 Conversión de Decimal a Binario, Octal y Hexadecimal
## 📌 Explicación del código

### Autor: Edgar Estrella

## 📍 1. Objetivo del Programa

Este programa permite:

Ingresar un número decimal.

Convertirlo manualmente a:

Binario (base 2)

Octal (base 8)

Hexadecimal (base 16)

Mostrar cada resultado en pantalla.

El procedimiento se hace usando divisiones sucesivas y residuos.

## 📍 2. Paso 1 — Entrada del número

Primero pedimos al usuario que ingrese un número decimal.

```bash
numero = int(input("Ingresa un número: "))
original = numero
```
🔎 Explicación

input() permite que el usuario escriba un número.

int() convierte el texto a número entero.

Guardamos el valor en original porque después vamos a modificar numero.

Así conservamos el valor inicial para reutilizarlo.

## 📍 3. Conversión a Binario (Base 2)
🔢 ¿Cómo funciona?

Para convertir a binario:

Dividimos el número entre 2.

Guardamos el residuo (0 o 1).

Repetimos hasta que el número sea 0.

Los residuos se leen de abajo hacia arriba.

### 💻 Código
```bash
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
```
🧠 Explicación Paso a Paso

binario = ""
Creamos una variable vacía donde guardaremos el resultado.

if numero == 0:
Si el número es 0, el binario también es 0.

while numero > 0:
Se repite el proceso mientras el número sea mayor que 0.

residuo = numero % 2
Obtenemos el residuo de dividir entre 2.

binario = str(residuo) + binario
Agregamos el residuo al inicio de la cadena.

numero = numero // 2
División entera para eliminar decimales.

## 📍 4. Conversión a Octal (Base 8)
🔢 ¿Cómo funciona?

Se divide el número entre 8.

Se guarda el residuo.

Se usa una cadena "01234567" para representar los valores válidos en base 8.

### 💻 Código
```bash 
#----- Octal-----------
numero = original
residuo = 0
octal = ""
digitos = "01234567"

if numero == 0:
    octal = "0"
else:
    while numero > 0:
        residuo = numero % 8
        octal = digitos[residuo] + octal
        numero = numero // 8

print("Octal:", octal)
```
🧠 Explicación Paso a Paso

numero = original
Recuperamos el número inicial.

digitos = "01234567"
Cadena con los valores permitidos en sistema octal.

residuo = numero % 8
Obtenemos el residuo al dividir entre 8.

octal = digitos[residuo] + octal
Usamos el residuo como índice en la cadena.

numero = numero // 8
División entera para continuar el proceso.

## 📍 5. Conversión a Hexadecimal (Base 16)
🔢 ¿Cómo funciona?

Se divide el número entre 16.

Se usa la cadena "0123456789ABCDEF" para representar valores.

Los números mayores a 9 se representan con letras:

10 = A

11 = B

12 = C

13 = D

14 = E

15 = F

### 💻 Código
```bash
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
```
🧠 Explicación Paso a Paso

digitos = "0123456789ABCDEF"
Contiene todos los símbolos válidos en base 16.

residuo = numero % 16
Obtenemos el residuo al dividir entre 16.

hexagecimal = digitos[residuo] + hexagecimal
Convertimos el residuo en su representación hexadecimal.

numero = numero // 16
División entera para continuar el ciclo.

## 📍 6. Resultado Final

El programa mostrará algo así:

Ingresa un número: 25
Binario: 11001
Octal: 31
Hexadecimal: 19

## 📍 7. Conclusión

Este programa demuestra cómo funcionan internamente los sistemas de numeración:

Base 2 → Computadoras

Base 8 → Sistemas antiguos

Base 16 → Programación y memoria

Se utiliza:

División entera //

Residuo %

Ciclos while

Condicionales if
