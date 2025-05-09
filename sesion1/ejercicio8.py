cantidad = int(input("Ingrese la cantidad de números: "))

if cantidad > 0:
    numero = float(input("Ingrese el número 1: "))
    mayor = numero
    menor = numero

    for i in range(1, cantidad):
        numero = float(input(f"Ingrese el número {i+1}: "))
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    print("Mayor:", mayor)
    print("Menor:", menor)
else:
    print("Debe ingresar al menos un número.")
