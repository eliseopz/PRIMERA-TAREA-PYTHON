#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.

precios = []
cantPrecios = 1
resp = "si"
while (resp.upper() != "NO"):
    try:
        precio = float(input("Ingrese el precio: "))
        precios.append(precio)
        resp = input("Desea ingresar mas precios?: SI-NO")
        cantPrecios += 1
    except Exception as ex:
        print("Error: ", str(ex), "Intente de nuevo")

print("El numero mayor es: ", max(precios))