#Solicitud de datos
#Solicitud datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita al usuario la longitud del lado del cuadrado.
    Retorna la longitud del lado como un número flotante.
    """
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado
#Mostrar datos
#Mostrar area cuadrado
def mostrar_area_cuadrado(area):
    """
    Muestra el área del cuadrado al usuario.
    Parámetros:
        area (float): El área del cuadrado a mostrar.
    """
    print(f"El área del cuadrado es: {area}")