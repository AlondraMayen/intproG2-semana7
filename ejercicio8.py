"""
Encontrar el mayor y el menor de N números
o Enunciado: Pide al usuario la cantidad N de números y luego solicita cada número.
Encuentra el número mayor y el número menor.
o Especificación: Usa un bucle for, y acumuladores.

"""

cantidad = int(input("Ingrese la cantidad de numeros: "))

mayor = 0
menor = 999999

for i in range (cantidad):
    numero = float(input(f"Ingrese el numero {i+1}:"))
    if numero > mayor:
        mayor = numero
    if numero <menor:
        menor = numero
    
print("Mayor:", mayor)
print("Menor:", menor)