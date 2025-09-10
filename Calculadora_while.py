#Libreria
import math
#While True
while True:
    print("\nCalculadora de operadores básicos")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")
    op = int(input("Ingrese la operación que desea realizar (1-6): "))
    if op == 1:
        #Variables de entrada
        numero1 = int(input("Ingrese el número 1: "))
        numero2 = int(input("Ingrese el número 2: "))
        rta = numero1 + numero2
        print(f"La suma es: {rta}")
    elif op == 2:
        numero1 = int(input("Ingrese el número 1: "))
        numero2 = int(input("Ingrese el número 2: "))
        rta = numero1 - numero2
        print(f"La resta es: {rta}")
    elif op == 3:
        numero1 = int(input("Ingrese el número 1: "))
        numero2 = int(input("Ingrese el número 2: "))
        rta = numero1 * numero2
        print(f"La multiplicación es: {rta}")
    elif op == 4:
        numero1 = int(input("Ingrese el número 1: "))
        numero2 = int(input("Ingrese el número 2: "))
        if numero2 != 0:
            rta = numero1 / numero2
            print(f"La división es: {rta}")
        else:
            print("Error!!! No se puede dividir por cero")
    elif op == 5:
        numero1 = int(input("Ingrese el número 1: "))
        rta = numero1 ** 2
        print(f"La potencia al cuadrado es: {rta}")
    elif op == 6:
        break
    else:
        print(f"Error!!!, Seleccione una opción dentro del menu (1-6)")
print("Gracias por usar la calculadora")