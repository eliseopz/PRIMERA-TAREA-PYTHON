#Aplicar el IVA al precio de un producto.

cantidad = int(input("Digite la cantidad de producto comprado: "))
precio = int(input("Digite el precio del producto: "))

IVA = (cantidad*precio) * 0.15
total = IVA + (cantidad*precio)

print("El IVA de la compra es: ", IVA)
print("El total con el IVA agregado: ", total)