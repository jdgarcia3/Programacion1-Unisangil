#Lamar funciones del archivo Figuras.py
from Figuras import area_cuadrado, area_triangulo, area_circulo
#from Figuras import *
#Lamar funciones del archivo Interfaz.py
from Interfaz import solicitar_datos_cuadrado, mostrar_area_cuadrado
#Funcion principal
lado = solicitar_datos_cuadrado()
area = area_cuadrado(lado)
mostrar_area_cuadrado(area)