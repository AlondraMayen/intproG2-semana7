M = int(input("Ingrese un número entero positivo (M): "))

while M <= 0:
    M = int(input("Debe ser un número positivo. Intente de nuevo: "))

contador = 0     
numero = 2       
producto = 1     

while contador < M:
    producto *= numero
    numero += 2
    contador += 1

print(f"El producto de los primeros {M} números pares es: {producto}")