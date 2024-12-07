capitales = {
        'Perú':'Lima',
        'Ecuador':'Quito',
        'Chile':'Santiago',
        'Colombia':'Bogota'
}
""" 
pais = input('Ingrese el pais: ')
capital = capitales[pais]
print(f"La capital de {pais} es {capital}")
"""

pais = input('Ingrese el pais: ')
if pais in capitales:
    capital = capitales.get(pais)
    print(f'La capital de {pais} es {capital}')
    eliminar_capital = input('¿Desea eliminar la capital?(si,no)')
    if eliminar_capital == 'si':
        capitales.pop(pais,'NO EXISTE')
        print(capitales)
else:
    print(f'No se encontro la capital de {pais}')
    nueva_capital = input(f'Ingrese capital de {pais}: ')
    capitales.update({pais:nueva_capital})
    print(capitales)
