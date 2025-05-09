n = int(input("Ingrese un número entero positivo: "))

if n > 0:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los números desde 1 hasta {n} es: {suma}")
else:
    print("Por favor, ingrese un número positivo.")