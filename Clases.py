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

#Clase vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, ano, color, tipo, kilometraje, combustible):
        # Atributos de la clase Vehiculo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color
        self.tipo = tipo  # Ej. 'coche', 'moto', 'camioneta'
        self.kilometraje = kilometraje
        self.combustible = combustible # Ej. 'gasolina', 'diesel', 'eléctrico'
        print(f"Vehículo {self.marca} {self.modelo} creado.")

    def arrancar(self):
        """Método para arrancar el vehículo."""
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

    def acelerar(self, velocidad):
        """Método para acelerar el vehículo a una velocidad dada."""
        print(f"El vehículo {self.marca} {self.modelo} está acelerando a {velocidad} km/h.")

    def frenar(self):
        """Método para frenar el vehículo."""
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")

    def obtener_informacion(self):
        """Método para mostrar la información del vehículo."""
        print("--- Información del Vehículo ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Combustible: {self.combustible}")
        print("--------------------------------")

    def actualizar_kilometraje(self, nuevos_km):
        """Método para actualizar el kilometraje del vehículo."""
        if nuevos_km > self.kilometraje:
            self.kilometraje = nuevos_km
            print(f"Kilometraje actualizado a {self.kilometraje} km.")
        else:
            print("El nuevo kilometraje debe ser mayor que el actual.")

#Objetos y metodos
# Crear una instancia de la clase Vehiculo
mi_coche = Vehiculo("Toyota", "Corolla", 2020, "Rojo", "Sedán", 50000, "Gasolina")

# Usar los métodos
mi_coche.obtener_informacion()
mi_coche.arrancar()
mi_coche.acelerar(100)
mi_coche.frenar()
mi_coche.actualizar_kilometraje(52000)
mi_coche.obtener_informacion()