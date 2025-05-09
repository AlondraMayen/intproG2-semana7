frase = input("Ingrese una frase: ")

contador = 0
en_palabra = False

for caracter in frase:
    if caracter != " " and not en_palabra:
        contador += 1
        en_palabra = True
    elif caracter == " ":
        en_palabra = False

print(f"La frase contiene {contador} palabra(s).")