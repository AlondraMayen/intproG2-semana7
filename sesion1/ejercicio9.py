numero = int(input("Ingrese un número entero: "))
frecuencia = [0] * 10

while numero != 0:
    digito = numero % 10
    frecuencia[digito] += 1
    numero //= 10

for i in range(10):
    print(f"El dígito {i} aparece {frecuencia[i]} vez/veces.")
