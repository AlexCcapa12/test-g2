
"from funciones import suma, resta, multiplicacion, division"
from funciones import *

x = int(input("ingrese un valor: "))
y = int(input("ingrese un segundo valor: "))

sum = suma(x, y)
print("el resultado de la suma de los 2 valores es: ", sum)

div = division(x, y)
print("el resultado de la division de los 2 valores es: ", div)

res = resta(x, y)
print("el resultado de la resta de los 2 valores es: ", res)

