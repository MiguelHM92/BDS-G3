def sumar(n1,n2):
    resultado = n1 + n2
    return resultado

def sumar_con_mensaje(n1,n2):
    resultado = int(n1) + int(n2)
    print(f"SUMA CON MENSAJE: La suma de {n1} + {n2} es {resultado}")

n1 = input("Ingrese nro 1: ")
n2 = input("Ingrese nro 2: ")
suma = sumar(int(n1),int(n2))
print(f"La suma de {n1} + {n2} es {suma}")
