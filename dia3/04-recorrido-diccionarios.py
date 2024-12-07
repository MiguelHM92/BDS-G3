capitales = {
        'Perú':'Lima',
        'Ecuador':'Quito',
        'Chile':'Santiago',
        'Colombia':'Bogota'
}

print('='*50 + 'RECORRIDO POR CLAVES')
# Recorrido por claves
for clave in capitales.keys():
    print(clave)

print('='*50 + 'RECORRIDO POR VALORES')
# Recorrido por valores
for valor in capitales.values():
    print(valor)

print('='*50 + 'RECORRIDO POR CLAVE, VALOR')
# Recorrido por clave, valor
for clave,valor in capitales.items():
    print(f'La capital de {clave} es {valor}')


