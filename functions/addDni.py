from tkinter import Toplevel, Label, Button, Entry, CENTER
from tinkerconfigs import bindConfig
from database import database
# AddDni Functionality
fuente = ("Arial", 16 ,"bold")
class AddDniWindows(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Agregar DNI")
        self.geometry("400x220")
        self.config(bg="#ccc")
        dni = Entry(self, font=fuente, width=30)
        password = Entry(self, font=fuente, width=30)
        name = Entry(self, font=fuente, width=30)
        bindConfig(dni, 'DNI')
        bindConfig(password, 'Contraseña')
        bindConfig(name, 'Nombre')
        lbl_error = Label(self, fg="#f00", bg="#ccc", font=fuente, anchor=CENTER, justify=CENTER, text='')
        btn2 = Button(self,font=fuente, text='Agregar DNI', fg="#000", bg="#fff", padx=20,pady=10,command=lambda: addDniToDb(dni.get(), password.get(), name.get(), lbl_error, self))
        btn2.pack()
        lbl_error.pack(pady=10)
        self.focus()

def addDniToDb(dni, password, name, lbl_error, self):
    if(dni == 'DNI' or password == 'Contraseña' or name == 'Nombre' or dni == '' or password == '' or name == ''): return lbl_error.config(text='Por favor, complete los campos')
    database(dni, password, name).save()
    self.destroy()
    