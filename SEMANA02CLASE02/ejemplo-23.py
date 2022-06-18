"uso del flujo condicional if"

edad = int(input("cual es su edad: "))
if 0 < edad < 18:
    print("es usted menor de edad")
elif 18 < edad and edad < 65:
    print("es usted una persona adulta")
elif edad > 65:
    print("es usted una persona de la tercera edad")
else:
    print("usted ingreso una edad erronea")



