#Operadores logicos
#AND
num1 = 5
num2 = 10
print(num1 < 10 and num2 > 5) # 1 1 = 1
print(num1 < 10 and num2 < 5) # 1 0 = 0
print(num1 > 10 and num2 > 5) # 0 1 = 0
print(num1 > 10 and num2 < 5) # 0 0 = 0

#Inicio de Sesion
usuario = "jgarcia3"
contrasena = 1234
#Solicitar nombre usuario y contrasena
#input_usuario = input("Ingrese su nombre de usuario: ")
#input_contrasena = int(input("Ingrese su contrasena: "))
#print(input_usuario == usuario and input_contrasena == contrasena)

#OR
print(num1 < 10 or num2 > 5) # 1 1 = 1
print(num1 < 10 or num2 < 5) # 1 0 = 1
print(num1 > 10 or num2 > 5) # 0 1 = 1
print(num1 > 10 or num2 < 5) # 0 0 = 0

#NOT
print(not(num1 < 10)) # not(1) = 0
print(not(num1 > 10)) # not(0) = 1