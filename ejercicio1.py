"""
Suma de los primeros N números
o Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los
números desde 1 hasta N.
o Especificación: Usa un bucle for y un acumulador

"""
n = int(input("Ingrese un numero entero: "))

if n > 0:
    suma = 0
    for i in range (1, n + 1):
        suma += i
    print (f"La suma de los numero desde 1 hasta {n} es: {suma}")
else:_
print ("Porfavor ingrese un numero positivo")