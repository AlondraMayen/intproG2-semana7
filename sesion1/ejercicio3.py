cadena = input("Ingrese una cadena de texto: ").lower()  

cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for letra in cadena:
    if letra == 'a':
        cont_a += 1
    elif letra == 'e':
        cont_e += 1
    elif letra == 'i':
        cont_i += 1
    elif letra == 'o':
        cont_o += 1
    elif letra == 'u':
        cont_u += 1

print("Cantidad de vocales:")
print(f"A: {cont_a}")
print(f"E: {cont_e}")
print(f"I: {cont_i}")
print(f"O: {cont_o}")
print(f"U: {cont_u}")