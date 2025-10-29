#importar libreria
import math
#Area cuadrado
def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado.
       Retorna el área calculada del cuadrado.
         Parámetros:
              lado (float): La longitud del lado del cuadrado.
              area = lado * lado
              return area
    """
    area = lado * lado
    return area
#Area Triangulo
def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado la base y la altura.
       Retorna el área calculada del triángulo.
         Parámetros:
              base (float): La longitud de la base del triángulo.
              altura (float): La altura del triángulo.
              area = (base * altura) / 2
              return area
              """
    area = (base * altura) / 2
    return area
#Area circulo
def area_circulo(radio):
    """Calcula el área de un círculo dado el radio.
       Retorna el área calculada del círculo.
         Parámetros:
              radio (float): La longitud del radio del círculo.
              area = pi * radio * radio
              return area
    """
    area = math.pi * (radio ** 2)
    return area