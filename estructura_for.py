#Estructura ciclo for
#for val_control in range(1):
#    print("Valor actual del control: ", val_control)
#Inicio y fin
#for i in range(5,11):
#    print("Valor actual del control: ", i)
#Inicio, fin y paso
for j in range(1,5,3):
    print("Valor actual del control: ", j)

#Cadena de texto
for letra in "Python":
    print("Letra actual: ", letra)
    if letra == "h":
        break
print("Fuera del ciclo")
#Tabla de multiplicar 2
for mul in range(1,11):
    print(f"2 x {mul} = {2*mul}")