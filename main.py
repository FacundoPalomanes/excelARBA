from tkinter import Tk, Label, Button, CENTER
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os 

load_dotenv()

def main():
    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("App sencilla para el IVA")
    ventana.config(bg="#000")
    fuente = ("Arial", 16 ,"bold")
    lbl = Label(ventana,fg="#fff", bg="#000", font=fuente,anchor=CENTER,
                justify=CENTER,text='Queres hacer el trabajo de iva?')
    lbl.pack(pady=40)


    btn = Button(ventana,font=fuente, text='Ejecutar accion', fg="#fff", bg="#000", padx=20,pady=10,command=mainCode)
    btn.pack()

    ventana.mainloop()
    

def mainCode():
    print('this print is for not get error of any line in the mainCode def')
    #here should be the part of ARCA and AFIP
    #emailPerson()

#print()

def emailPerson():
    # Configuración del correo
    remitente = "facpalomanes@gmail.com"
    destinatario = "x@example.com"
    asunto = "Excel trabajo de IVA"
    cuerpo = "Aca iria adjuntado los dos archivos excel." # en el cuerpo habria q fijarse como adjuntar archivos

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Configurar la conexión SMTP
    try:
        servidor_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Para Gmail, usa SSL
        print(remitente)
        servidor_smtp.login(remitente, os.getenv("password"))
        servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
        servidor_smtp.quit()
        print("Correo electrónico enviado con éxito")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


main()