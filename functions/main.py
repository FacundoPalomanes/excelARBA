from tkinter import StringVar, Tk, Label, Button, CENTER
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from tinkerconfigs import tinkerConfig
from addDni import AddDniWindows
from showDnis import ShowDnis
from current_dni import get_current_dni
from afip import afip
from send_email import emailPerson  
from excel import excel
from erase_files import erase_files

load_dotenv()
ventana = Tk()
fuente = ("Arial", 16 ,"bold")

def main():
    tinkerConfig(ventana)

    dni, password, name = get_current_dni()
    dni_var = StringVar()
    if dni and password and name:
        dni_var.set(f"Nombre: {name}")
    else:
        dni_var.set("Nombre: Ninguno seleccionado")
    dni_lbl = Label(ventana, fg="#000", bg="#ccc", font=fuente, anchor=CENTER, justify=CENTER, textvariable=dni_var)
    dni_lbl.pack(pady=10)
    
    mainFunctionButton = Button(ventana,font=fuente, text='Hacer Excel', fg="#000", bg="#fff", padx=40,pady=10,command=mainCode)
    mainFunctionButton.pack(pady=10)

    addDniButton = Button(ventana,font=fuente, text='Agregar Cuenta', fg="#000", bg="#fff", padx=40,pady=10,command=AddDniWindows)
    addDniButton.pack(pady=10)

    listAccounts = Button(ventana,font=fuente, text='Mostrar Lista', fg="#000", bg="#fff", padx=40,pady=10,command=lambda: ShowDnis(dni_var))
    listAccounts.pack(pady=10)
    
    ventana.mainloop()

def mainCode():
    dni, password, name = get_current_dni()
    afip(dni, password)
    excel(dni)
    emailPerson(name,dni)
    erase_files(dni)

if(__name__ == "__main__"):
    main()