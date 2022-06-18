"uso del for"

ingenierias = ["software", "sistemas", "indutrial", "mecanica"]
i = 0
nombre = input("ingrese su primer nombre: ")
print("el tamano de nuestra lista es: {}, programa creado por: {} " .format(len(ingenierias), nombre))

for carrera in ingenierias:
    print("ingenieria {} " .format(carrera))
    i += 1
    print("esta es la vuelta numero: ", i)

print("llego al final del for")

