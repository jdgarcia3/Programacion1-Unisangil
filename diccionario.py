#Crear un diccionario
persona = {}
# Diccionario frutas
Programacion_1 = {
    "docente": "David Garcia",
    "estudiantes":[
        {
            "nombre": "Juan Gonzalez",
            "cedula": 1015434287,
            "correo": "juango@unisangil.edu.co",
            "edad": 20
        },
        {
            "nombre": "Camila Suarez",
            "cedula": 1015685432,
            "correo": "camilasu@unisangil.edu.co",
            "edad": 23
        }
    ],
    "temas": [
        "Introducción a la programación",
        "Variables",
        "Estructuras de control",
        "Programación orientada a objetos"
    ],
    "creditos": 3,
    "cortes":[
        {
            "nombre": "Corte 1",
            "porcentaje": 50
        },
        {
            "nombre": "Corte 2",
            "porcentaje": 50
        }
    ]
}
#Imprimir diccionario
#print(Programacion_1)
#Acceder a la informacion del diccionario
print(Programacion_1["docente"])
print(Programacion_1["creditos"])
print(Programacion_1["estudiantes"])
#Individualizar estudiante
print(Programacion_1["estudiantes"][1])
print(Programacion_1["temas"][2])
#Sacar los datos de temas
for tema in Programacion_1["temas"]:
    print(tema)
print(Programacion_1["cortes"][1]["nombre"])
print(Programacion_1["estudiantes"][0]["correo"])
#Modificar datos del diccionario
Programacion_1["creditos"] = 4
print(Programacion_1)
Programacion_1["estudiantes"][1]["nombre"] = "Jesus Caro"
Programacion_1["estudiantes"][1]["cedula"] = 1234567890
Programacion_1["estudiantes"][1]["correo"] = "jgarcia@unisangil.edu.co"
Programacion_1["estudiantes"][1]["edad"] = 31
print(Programacion_1)
#Agregar nuevos datos al diccionario
Programacion_1["estado"] = True
print(Programacion_1)
#Eliminar datos del diccionario
del Programacion_1["creditos"]
print(Programacion_1)
#Items
for clave, valor in Programacion_1.items():
    print(f"{clave}: {valor}")
#Keys
for clave in Programacion_1.keys():
    print(clave)
#Values
for valor in Programacion_1.values():
    print(valor)
#Get
print(Programacion_1.get("docente"))
#Limpiar informacion del diccionario
Programacion_1["docente"] = ""
print(Programacion_1)
Programacion_1.clear()
print(Programacion_1)