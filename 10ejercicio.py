""""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro."""

saldo = int(input("Ingrese su saldo: "))
monto = int(input("Ingrese el monto a retirar: "))

if (monto>saldo):
    print("Fondos insuficientes")
else:
    print("El retiro se ha realizado con exito")
    print("El saldo restante es: ", saldo-monto)