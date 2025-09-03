#Solicitar datos del terreno
base = float(input("Ingrese la base del terreno en metros: "))
altura = float(input("Ingrese la altura del terreno en metros: "))
#Calcular el area del terreno
Area_Triangulo = (base * altura) / 2
Area_Cuadrado = base * base
Area_Total = Area_Triangulo + Area_Cuadrado
#Precio del terreno
Precio_metro_cuadrado = 4400000
Precio_Total_Terreno = Area_Total * Precio_metro_cuadrado
#Mostrar la informacion
print(f"El area total del terrono es:{Area_Total} mts2")
print(f"El precio total del terreno es: ${Precio_Total_Terreno} COP")