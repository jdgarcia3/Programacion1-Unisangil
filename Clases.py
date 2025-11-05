#Crear clase persona
class Persona:
    #Constructor
    def __init__(self, nombre, edad, correo, cedula):
        #Atributos
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cedula = cedula
    #Metodo para mostrar datos
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo} y Cedula: {self.cedula}")
    
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre}, tengo {self.edad} años, mi contacto de correo es {self.correo}")
    
    def incremento_años(self,incremento):
        self.edad += 10
        print(f"Edad con incremento: {self.edad}") 

#Llamar clase
David = Persona("David", 33, "jgarcia3@unisangil.edu.co", 10154376544)
Maria = Persona("Maria", 25, "maria123@unisangil.edu.co", 10153452211)
#Llamar metodos
David.mostrar_datos()
David.saludo()
Maria.mostrar_datos()
Maria.saludo()
David.incremento_años(10)
Maria.incremento_años(5)