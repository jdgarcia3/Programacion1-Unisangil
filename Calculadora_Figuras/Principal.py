#Lamar funciones del archivo Figuras.py
from Figuras import area_cuadrado, area_triangulo, area_circulo
#from Figuras import *
#Lamar funciones del archivo Interfaz.py
#from Interfaz import solicitar_datos_cuadrado, mostrar_area_cuadrado
from Interfaz import *
#Funcion principal
#Variables menu
opcion = 0
CUADRADO = 1
TRIANGULO = 2
CIRCULO = 3
SALIR = 4
while opcion != SALIR:
    opcion = mostrar_menu()
    if opcion == CUADRADO:
        lado = solicitar_datos_cuadrado()
        area = area_cuadrado(lado)
        mostrar_area_cuadrado(area)
    elif opcion == TRIANGULO:
        base, altura = solicitar_datos_triangulo()
        area = area_triangulo(base, altura)
        mostrar_area_triangulo(area)
    elif opcion == CIRCULO:
        radio = solicitar_datos_circulo()
        area = area_circulo(radio)
        mostrar_area_circulo(area)
    elif opcion == SALIR:
        print("Saliendo de la calculadora. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")