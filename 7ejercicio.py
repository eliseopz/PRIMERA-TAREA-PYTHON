#Leer x cantidad de edades y mostrar el promedio de dichas edades.
from statistics import mean
import statistics
edades = []
cantEdad = 1
resp = "si"
while (resp.upper() != "NO"):
    try:
        edad = float(input("Ingrese la edad del sujeto: "))
        edades.append(edad)
        resp = input("Desea ingresar mas edades?: SI-NO")
        cantEdad += 1
    except Exception as ex:
        print("Error: ", str(ex), "Intente de nuevo")

media = statistics.mean(edades)
print("La media es: ", media)

