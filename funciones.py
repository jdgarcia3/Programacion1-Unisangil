#Funcion simple
def mensaje():
    """
    Esta función imprime un mensaje de bienvenida.
    """
    print("Hola, bienvenido a la función mensaje.")
#Llamar la funcion
mensaje()
#Funcion simple con retorno
def suma():
    """
    Esta función suma dos numeros.
    """
    rta = 5 + 3
    return rta
#Llamar la funcion
print("suma:", suma())
#Funcion con parametros
def resta(a, b):
    """
    Esta función recibe dos números y devuelve su resta.
    """
    rta = a - b
    print("Resta:", rta)
#Llamar la funcion
resta(10, 4)
#Funcion simple con valores de retorno
def solicitud_datos():
    """
    Esta función solicita datos al usuario y los retorna.
    """
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2
#Llamar la funcion
num1, num2 = solicitud_datos()
#Funcion con parametros y retorno
def multiplicacion(num1, num2):
    """
    Esta función recibe dos números y devuelve su multiplicación.
    """
    rta = num1 * num2
    return rta
#Llamar la funcion
print("Multiplicación:", multiplicacion(num1, num2))