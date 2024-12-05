bandera = "si"
while(bandera == "si"):
    print("=================== CALCULADORA CON PYTHON ==================")
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    operacion = int(input("""Ingrese el tipo de operación
                    1) SUMA
                    2) RESTA
                    3) MULTIPLICACIÓN
                    4) DIVISIÓN
                    INGRESE OPCIÓN: """))
    if(operacion == 1):
        resultado = numero1 + numero2
        print(f"La suma de {numero1} + {numero2} es {resultado}")
    elif(operacion == 2):
        resultado = numero1 - numero2
        print(f"La resta de {numero1} - {numero2} es {resultado}")
    elif(operacion == 3):
        resultado = numero1 * numero2
        print(f"La multiplicación de {numero1} * {numero2} es {resultado}")
    elif(operacion == 4):
        resultado = numero1 / numero2
        print(f"La división de {numero1} / {numero2} es {resultado}")
    else:
        print("La operación no existe")
    
    bandera = input("¿Desea continuar...?(si/no): ")


