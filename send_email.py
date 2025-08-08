from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import os 
import smtplib

def emailPerson(name, dni):
    # Configuración del correo
    remitente = os.getenv("sender")
    destinatario = os.getenv("receiver")  # Cambié de "password" a "receiver" para que sea el destinatario real
    asunto = f"Excel trabajo de IVA {name}"
    cuerpo = f"Adjunto los dos archivos Excel de {name} generados."

    # Archivos a adjuntar (poné tus rutas reales acá)
    downloads_path = Path.home() / "Downloads"
    archivo_compras = downloads_path / f"Compras_modificado_{dni}.xlsx"
    archivo_ventas = downloads_path / f"Ventas_modificadas_{dni}.xlsx"

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Función auxiliar para adjuntar archivos
    def adjuntar_archivo(ruta_archivo):
        if not ruta_archivo.exists():
            print(f"[ADVERTENCIA] No se encontró el archivo: {ruta_archivo}")
            return
        with open(ruta_archivo, "rb") as adj:
            parte = MIMEBase("application", "octet-stream")
            parte.set_payload(adj.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename={ruta_archivo.name}")
        mensaje.attach(parte)

    # Adjuntar los dos Excel
    adjuntar_archivo(archivo_compras)
    adjuntar_archivo(archivo_ventas)

    # Configurar la conexión SMTP y enviar
    try:
        servidor_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        servidor_smtp.login(remitente, os.getenv("password"))
        servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
        servidor_smtp.quit()
        print("[OK] Correo electrónico enviado con éxito")
    except Exception as e:
        print(f"[ERROR] Error al enviar el correo: {e}")