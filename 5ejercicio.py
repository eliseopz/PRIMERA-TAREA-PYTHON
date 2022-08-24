#Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números enteros.
valorIni = int(input("Ingrese el primer valor: "))
valorFInal = int(input("Ingrese el segundo valor: "))

for i in range(valorIni, valorFInal):
    if i%2 == 0:
        print(i)

        
