class Usuario:
    __email = 'miguel@gmail.com'
    __password = '123456'

    def __init__(self):
        pass

    def login(self,email,password):
        if(self.__email == email and self.__password == password):
            print(f"Bienvenido {self.__email}")
        else:
            print('datos incorrectos')

print('LOGIN DE USUARIOS')
email = input('Ingrese Email: ')
password = input('Ingrese Password: ')

usuario = Usuario()
usuario.__password = password
usuario.login(email,password)