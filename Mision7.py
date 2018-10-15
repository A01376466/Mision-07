# Author: Ivan Honc Ayón
# Descripción: Este programa hace divisiones con restas y compara números para saber cuál es el mayor.


# Esta función recibe de parámetros el dividendo y el divisor, realiza división de los números a través de restas
# e imprime el resultado.
def division(dividendo, divisor):
    print("Calculando divisiones")
    dividendoRestante = dividendo
    residuo = dividendoRestante
    cociente = 0
    while residuo >= 0:
        residuo = dividendoRestante
        dividendoRestante = dividendoRestante-divisor
        if dividendoRestante<0:
            dividendoRestante = dividendoRestante+divisor
            break
        else:
            cociente = cociente+1
    if residuo < 0:
        residuo = residuo*(-1)
    print("%d / %d = %d, sobra %d" % (dividendo, divisor, cociente, residuo))


# Esta función permite al usuario ingresar la cantidad de números que quiera y al terminar imprie el mayor de ellos.
def calcularMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    contador = 0
    numeroMayor = 0
    while contador !=1:
        numeroUsuario = int(input("Teclea un número [-1 para salir]: "))
        if numeroUsuario > numeroMayor:
            numeroMayor = numeroUsuario
        if numeroUsuario == -1:
            print("El mayor es: %d" % (numeroMayor))
            contador = 1
        if numeroUsuario < -1:
            print("Error: Ingresar solo números enteros positivos")


# Esta función establece un ciclo while que mantiene el menú de opciones abierto hasta que el usuario le instruya salir,
# asimismo manda a llamar a las otras funciones cuando se requiere.
def menu():
    numeroActividad = int
    while numeroActividad != 0:
        print("""
Misión 07. Ciclos while
Autor: Ivan Honc Ayón
Matricula: A01376466
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
        numeroActividad = int(input("Teclea tu opción: "))
        if numeroActividad == 1:
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            division(dividendo, divisor)
        if numeroActividad == 2:
            calcularMayor()
        if numeroActividad == 3:
            print("Terminando programa")
            numeroActividad = 0
        if 3<numeroActividad<1:
            print("Error: Teclea 1, 2, o 3")


# Esta es la función principal que manda llamar al menú para posteriormente usar cualquiera de las otras funciones.
def main():
    menu()


main()
