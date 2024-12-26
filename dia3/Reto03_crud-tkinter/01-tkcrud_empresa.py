from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector

class EmpresaTk:

    def __init__(self,app):
        # Configuración de la pantalla:
        self.app = app
        self.app.title('Administrador de Empresas')
        self.app.geometry('840x480')

        # Connección con la base de datos:
        self.data = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='datag3'
        )

        self.cursor = self.data.cursor()

        # Creación de cuadro "Registrar":
        frame = LabelFrame(self.app, text='Registrar nueva empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

        # Etiquetas y cuadros de texto:
        # a) RUC:
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)

        # b) Razón Social:
        lb_razsocial = Label(frame, text='Razón Social')
        lb_razsocial.grid(row=2, column=0)
        self.txt_razsocial = Entry(frame)
        self.txt_razsocial.grid(row=2, column=1)

        # c) Email:
        lb_email = Label(frame, text='Email')
        lb_email.grid(row=3, column=0)
        self.txt_email = Entry(frame)
        self.txt_email.grid(row=3,column=1)

        btn_insertar = Button(frame, text='Insertar', command=self.insertar_empresas)
        btn_insertar.grid(row=4, columnspan=2, sticky=W+E)

        # Grilla para las empresas:
        self.tree = Treeview(self.app, columns=('RUC','Razon Social','Email'))
        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.tree.heading('#0', text='id')
        self.tree.heading('RUC', text='RUC')
        self.tree.heading('Razon Social', text='Razon Social')
        self.tree.heading('Email', text='Email')

        self.cargar_empresas()
    
    def cargar_empresas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.cursor.execute("SELECT id, nro_ruc, razon_social, email FROM empresa ORDER BY id")
        for row in self.cursor.fetchall():
            self.tree.insert('',0,text=row[0],values=(row[1],row[2],row[3]))
    
    def insertar_empresas(self):
        nueva_empresa = (
            self.txt_ruc.get(),
            self.txt_razsocial.get(),
            self.txt_email.get()
        )

        query = "INSERT INTO empresa(nro_ruc, razon_social, email) VALUES(%s,%s,%s)"
        self.cursor.execute(query,nueva_empresa)
        self.data.commit()
        self.cargar_empresas()

app = Tk()
app_empresa = EmpresaTk(app)
app.mainloop()


