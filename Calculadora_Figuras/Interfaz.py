#Solicitud de datos
#Solicitud datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita al usuario la longitud del lado del cuadrado.
    Retorna la longitud del lado como un número flotante.
    """
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado
#Solicitud datos triangulo
def solicitar_datos_triangulo():
    """
    Solicita al usuario la base y la altura del triángulo.
    Retorna la base y la altura como números flotantes.
    """
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura
#Solicitud datos circulo
def solicitar_datos_circulo():
    """
    Solicita al usuario el radio del círculo.
    Retorna el radio como un número flotante.
    """
    radio = float(input("Ingrese el radio del círculo: "))
    return radio
#Mostrar datos
#Mostrar area cuadrado
def mostrar_area_cuadrado(area):
    """
    Muestra el área del cuadrado al usuario.
    Parámetros:
        area (float): El área del cuadrado a mostrar.
    """
    print(f"El área del cuadrado es: {area}")
#Mostrar area triangulo
def mostrar_area_triangulo(area):    
    """
    Muestra el área del triángulo al usuario.
    Parámetros:
        area (float): El área del triángulo a mostrar.
    """
    print(f"El área del triángulo es: {area}")
#Mostrar area circulo
def mostrar_area_circulo(area):
    """
    Muestra el área del círculo al usuario.
    Parámetros:
        area (float): El área del círculo a mostrar.
    """
    print(f"El área del círculo es: {area}")
#Menu calculadora
def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    Retorna la opción seleccionada por el usuario como un entero.
    """
    print("Calculadora de Áreas de Figuras Geométricas")
    print("1. Calcular área del cuadrado")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del círculo")
    print("4. Salir")
    opcion = int(input("Seleccione una opción (1-4): "))
    return opcion