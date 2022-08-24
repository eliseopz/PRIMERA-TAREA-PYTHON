#Mostrar el total a pagar por la compra de n cantidad de productos a un precio desconocido.

venta = []
cantProd = 1
resp = "si"
while (resp.upper() != "NO"):
    try:
        precio = float(input("Ingrese el precio del producto: "))
        venta.append(precio)
        resp = input("Desea ingresar la compra de otro producto: SI-NO")
        cantProd += 1
    except Exception as ex:
        print("Error: ", str(ex), "Intente de nuevo")

total = sum(venta)

print("El total es: ", total)




