n = int(input("Ingrese un número entero positivo: "))

while n < 0:
    n = int(input("Número no válido. Ingrese un número entero positivo: "))

factorial = 1
contador = 1

while contador <= n:
    factorial *= contador
    contador += 1

# Mostrar resultado
print(f"El factorial de {n} es: {factorial}")
