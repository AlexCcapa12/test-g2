""""Pedir a un usuario ingresar su dirección email. Imprimir un mensaje
indicando si la dirección es válida o no, valiéndose de una función para
decidirlo. Una dirección se considerará válida si contiene el símbolo @"""

def validar(email):
    caracterpedido = "@"
    emailvalido = False
    for caracter in email:
        if caracter == caracterpedido:
            return True
    return False
emailusuario = input("ingrese su email: ")
if validar(emailusuario):
    print("email valido")
else:
    print("email invalido")


