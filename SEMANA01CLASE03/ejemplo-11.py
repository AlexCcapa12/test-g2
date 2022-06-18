
"copiar los elementos de una lista"

lista1 = ["mysql", "postgres", "sqlserver", "rDS"]

lista2 = lista1.copy()
lista2.append("sqlite3")
lista2.append("c++")

print("el valor de mi lista1 es : ", lista1)
print("el valor de mi lista2 es : ", lista2)