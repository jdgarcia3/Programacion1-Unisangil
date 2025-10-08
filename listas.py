#Crear una lista
lista = [10,"a",False,3.14,"Unisangil"]
print(lista) 
print(type(lista)) 
#Acceder a un elemento de la lista
#index+
print(lista[1])
print(lista[3])
print(lista[4])
print(lista[0])
print(lista[2])
#index-
print(lista[-3])
print(lista[-5])
print(lista[-1])
print(lista[-2])
print(lista[-4])
#Tamaño de una lista
print(f"Tamaño lista = {len(lista)}")
#Recorrer una lista
#Index+
print(lista[:])
print(lista[2:])
print(lista[:2])
print(lista[1:4])
print(lista[1:])
#index-
print(lista[-3:])
print(lista[-3:-1])
print(lista[-5:-1])
print(lista[:-1])
#Extraer datos de una lista
for datos in lista:
    print(datos)
#Crear una lista vacia
personas = []
print(personas) 
#Agregar elementos a una lista
#append agrega un elemento al final de la lista
personas.append("Juan")
print(personas)
personas.append("Gonzalez")
print(personas)
personas.append(1015434287)
print(personas)
personas.append("Maria")
print(personas)
personas.append("Lopez")
print(personas)
personas.append(1053709211)
print(personas)
#insrtar en posicio especifica
personas.insert(3,"Perez")
print(personas)
personas.insert(5,100)
print(personas)
personas.insert(3,True)
print(personas)
personas.insert(7,True)
print(personas)
#Reemplazar información de la lista
personas[0] = "jgarcia3@unisangil"
print(personas)
personas[3] = False
print(personas)
#Eliminar datos de una lista
personas.remove('jgarcia3@unisangil')
print(personas)
personas.remove('Lopez')
print(personas)
personas.remove(False)
print(personas)
personas.pop()
print(personas)
personas.pop(0)
print(personas)
personas.pop(2)
print(personas)
personas[2:]= []
print(personas)
personas.reverse()
print(personas)
personas[:]= []
print(personas)
#Ordenar datos de una lista
numeros = [5,3,8,1,4,9,2,7,6]
print(numeros)
#Ascendente
numeros.sort()
print(numeros)
#Descendente
numeros.sort(reverse=True)
print(numeros)
