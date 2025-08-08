from tkinter import PhotoImage

# Tinker and bind configs to make it look prettier
def tinkerConfig(ventana):
    ventana.geometry("500x325")
    ventana.title("App sencilla para el IVA")
    icon = PhotoImage(file='assets/afip.png') # Cargar imagen
    ventana.wm_iconphoto(True, icon) # Mostrar icono
    ventana.config(bg="#ccc")
    
def bindConfig(entry, placeholder):
    entry.insert(0, placeholder)
    entry.configure(state='disabled')
    entry.bind('<Button-1>', lambda x: on_focus_in(entry))
    entry.bind(
    '<FocusOut>', lambda x: on_focus_out(entry, placeholder))
    entry.pack(pady=10)

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')
