"""
Suma de números pares e impares
o Enunciado: Pide al usuario una lista de números (pueden ser ingresados uno a la
vez hasta que el usuario ingrese un valor de fin, como 0 o -1). Calcula la suma de
los números pares y la suma de los números impares.
o Especificación: Usa un bucle while, acumuladores para la suma de pares e impares,
y un contador (opcional, dependiendo de la implementación).

"""

numero_lista = int(input("Ingrese un numero : "))
pares=0
impares=0
while numero_lista != 0 and numero_lista!= -1:
    if numero_lista % 2 == 0:
        pares += numero_lista
    else:
        impar += numero_lista
        numero_lista= int(input("Ingresa un numero: "))

print(f"La suma de los pares es: ,{pares}")
print(f"La suma de los impares es: ,{impares}")