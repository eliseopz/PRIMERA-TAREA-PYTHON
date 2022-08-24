"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95."""

nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
promedio = int(input("Ingrese su promedio: "))

resp= input("Estudia o aplico para una beca en ISI? SI-NO")
if (resp == "SI"):
    if (promedio>=95):
        print("Es apto para la beca")
    else:
        print("No es apto para la beca")

elif(promedio >= 85):
    print("Es apto para la beca")
else:
    print("No es apto para la beca")

  


