saldo = 1000
depositos = 0
retiros = 0

while True:
    print(f"\nSaldo actual: ${saldo}")
    print("1. Depósito")
    print("2. Retiro")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        depositos += 1
        print(f"Has depositado ${deposito}. Nuevo saldo: ${saldo}")
        
    elif opcion == '2':
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            retiros += 1
            print(f"Has retirado ${retiro}. Nuevo saldo: ${saldo}")
        else:
            print("Saldo insuficiente.")
    
    elif opcion == '3':
        print(f"\nGracias por usar el cajero. Depósitos realizados: {depositos}, Retiros realizados: {retiros}.")
        break
    
    else:
        print("Opción inválida. Intente nuevamente.")
