"""Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni” """

cantidad = int(input("Ingrese la cantidad de estudiantes a registrar: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")

    mail = (nombre.lower()+apellido.lower()+"@est.uca.edu.ni")
    print(mail)
