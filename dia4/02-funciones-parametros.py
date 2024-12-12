# Parametros args y kwargs
def sumar_infinito(*args): # El asteristo permite que la cantidad de parámetros sea dinámica
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado

suma1 = sumar_infinito(1,2,3)
print(suma1)
suma2 = sumar_infinito(1,2)
print(suma2)

def calculadora(**kwargs):
    ope = kwargs.get('ope')
    n1 = kwargs.get('n1')
    n2 = kwargs.get('n2')

    if ope == "suma":
        resultado = n1 + n2
        print(f'La {ope} de {n1} y {n2} es {resultado}')
    elif ope == "resta":
        resultado = n1 - n2
        print(f'La {ope} de {n1} y {n2} es {resultado}')
    elif ope == "multiplicacion":
        resultado = n1 * n2
        print(f'La {ope} de {n1} y {n2} es {resultado}')
    elif ope == "division":
        resultado = n1 / n2
        print(f'La {ope} de {n1} y {n2} es {resultado}')
    else:
        print('No se encontro la operación solicitada')

calculadora(n1=5,n2=10,ope='suma')
calculadora(ope='resta',n1=3,n2=1)
calculadora(ope='multiplicacion',n1=10,n2=15)
