import datetime
import random
import time as t
import os

fecha = datetime.date.today()
print(f"Bienvenido {fecha}")

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar(segundos):
    for i in range(segundos, 0, -1):
        limpiar_pantalla()
        print(f"Espera {i} segundos...")
        t.sleep(1)
    limpiar_pantalla()

def adivinar(num_user, num_random):
    esperar(5)
    if num_user == num_random:
        t.sleep(1)
        print("¡Has adivinado correctamente!")
    else:
        print(f"Incorrecto. El número era {num_random}.")

def main():
    num_alea = random.randint(1, 10)
    resp = "s"
    
    while resp.lower() != 'n':
        try:
            num = int(input("Ingrese un número (1-10): "))
            if not 1 <= num <= 10:
                print("Por favor, ingrese un número entre 1 y 10.")
                continue
            adivinar(num, num_alea)
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            continue
        
        resp = input("¿Desea seguir jugando? [S = Sí | N = No | R = Reiniciar partida]: ").lower()
        if resp == 'r':
            num_alea = random.randint(1, 10)

main()
