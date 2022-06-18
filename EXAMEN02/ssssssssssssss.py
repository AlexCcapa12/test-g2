"""Pregunta 1"""

class Persona:

   def __init__(self, nombre, nacionalidad, edad):
       self.nombre = nombre
       self.nacionalidad = nacionalidad
       self.edad = edad

"""Instanciamos nuestra clase"""
persona1 = Persona("Henry", "Peruano", 24)
print("El nombre de la persona es: ", persona1.nombre)
print("Su nacionalidad es : ", persona1.nacionalidad)
print("Su edad es : ", persona1.edad, "años")


from datetime import date, datetime

import time

tiempo = datetime.now()

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("La fecha y hora de registro es: ", tiempo)
