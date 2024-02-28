'''### **Ejercicio 7.9**
Crear un programa en Python que lea el archivo JSON  (estudiantes.json) 
e imprima la siguiente información para cada estudiante:


1. Nombre del estudiante.
2. Edad del estudiante.
3. Lista de asignaturas que está cursando.'''

import json
import os


def obtener_path():
    return os.path.abspath(os.path.dirname(__file__))


try:
    with open(f"{obtener_path()}//studiantes.json", "r") as fichero:
        diccionario = json.load(fichero)
        fichero.close()
except:
    print("No se encontro el archivo")

for estudiante in diccionario["estudiantes"]:
    print(
        f"Nombre: {estudiante.get('nombre', None)} - Edad: {estudiante['edad']} - Asignaturas: {estudiante['asignaturas']}")
