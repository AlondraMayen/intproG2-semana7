"""
Leer una palabra diferente a fin y convertirla a Mayuscula
"""

palabra= input("Dime una palabra: ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input ("Dime una palabra: ")
else:
    print("Adios...")