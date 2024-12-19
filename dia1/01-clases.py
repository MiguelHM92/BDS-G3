class Automovil:
    # Creamos método constructor
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    # Métodos
    def encender(self):
        print('encender ' + self.marca)

    def avanzar(self):
        print('avanzar ' + self.marca)
    
    def acelerar(self):
        print('acelerar ' + self.marca)
    
    def frenar(self):
        print('frenar ' + self.marca)
    
## Creamos los objetos:
vw = Automovil(1970, 'CH-1234','Amarillo','Volkswagen')
vw.encender()
vw.acelerar()
vw.frenar()

tico = Automovil(1985, 'EJ-2345','Rojo','DAEWOO')
tico.encender()
tico.acelerar()
tico.frenar()

lb = Automovil(2023, 'LAB-2524','Azul','Lamborgini')
lb.encender()
lb.acelerar()
lb.frenar()
