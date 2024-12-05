#RETO 1 : CREAR UN PROGRAMA QUE PUEDA CONVERTIR MONEDAS
#DE SOLES A DOLARES O DE DOLARES A SOLES, USE CONDICIONALES
#Y BUCLES Y AL FINAL EL PROGAMA DEBE PREGUNTAR SI DFESEA
#CONTINUAR, SI NO , SALE RECIEN DEL PROGRAMA

bandera = "Si"
while(bandera == "Si"):
    print("<<<<<<<<< CONVERTIDOR DE MONEDA >>>>>>>>>")
    modeda = float(input("Ingrese la cantidad a convertir: "))
    tasa = float(input("Ingrese la tasa de conversión: "))
    
    conversion = int(input("""Ingrese la conversión que desea realizar:
                    1) Soles a Dólares
                    2) Dólares a Soles
                    INGRESE UNA OPCIÓN: """))
    if(conversion == 1):
        soles = modeda / tasa
        print(f"El equivalente de {modeda} soles es {soles} dólares")
    elif(conversion == 2):
        dolares = modeda * tasa
        print(f"El equivalente de {modeda} dólares es {dolares} soles")
    else:
        print("La opción ingresada no existe")
    
    bandera = input("¿Desea continuar con la conversión? (Si/No): ")

