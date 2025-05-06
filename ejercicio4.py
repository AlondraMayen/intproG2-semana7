"""
Promedio de N calificaciones
o Enunciado: Pide al usuario la cantidad N de calificaciones y luego solicita cada
calificación. Calcula el promedio de las calificaciones ingresadas.
o Especificación: Usa un bucle for para leer las calificaciones, un acumulador para la
suma, y un contador para la cantidad.

"""

cantidad = int(input("Ingresa la cantidad de calificaciones: "))
suma = 0
contador = 0

for i in range (cantidad):
    calificacion = float(input("Ingrese la calificacion {i+1}: "))
    suma += calificacion
promedio = suma / cantidad
print(f"El promedio de las calificaciones es: {promedio:.2f}")