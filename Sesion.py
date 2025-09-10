#Inicio de Sesion
usuario = "jgarcia3"
contrasena = 1234
#Solicitar nombre usuario y contrasena
input_usuario = input("Ingrese su nombre de usuario: ")
input_contrasena = int(input("Ingrese su contrasena: "))
if input_usuario == usuario and input_contrasena == contrasena:
    print("Inicio de sesion exitoso")
else:
    print("Usuario o contrasena incorrecta")