numero_lista = int(input("Ingrese un número (0 o -1 para salir): "))

pares = 0
impares = 0

while numero_lista != 0 and numero_lista != -1:
    if numero_lista % 2 == 0:
        pares += numero_lista
    else:
        impares += numero_lista
    numero_lista = int(input("Ingrese otro número (0 o -1 para salir): "))

print(f"La suma de los números pares es: {pares}")
print(f"La suma de los números impares es: {impares}")