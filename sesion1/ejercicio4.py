cantidad = int(input("Ingresa la cantidad de calificaciones: "))
suma = 0

for i in range(cantidad):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    suma += calificacion

promedio = suma / cantidad
print(f"El promedio de las calificaciones es: {promedio:.2f}")