from tkinter import Canvas, Frame, Toplevel, Scrollbar, Label, Button, Entry
import csv
from current_dni import set_current_dni
from database import database
header_font = ("Arial", 14 ,"bold")
font = ("Arial", 13 ,"bold")
#Show Dnis Windows
class ShowDnis(Toplevel):
    def __init__(self, dni_var ,master=None):
        super().__init__(master)
        self.dni_var = dni_var
        self.title("Mostrar Dnis")
        self.geometry("1000x400")
        self.config(bg="#ccc")

        self.scroll_canvas = Canvas(self, bg="#ccc")
        self.frame = Frame(self.scroll_canvas, bg="#ccc")
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.scroll_canvas.pack(side="left", fill="both", expand=True)
        self.scroll_canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        self.data = []
        self.load_data()

    def load_data(self):
        self.data = []

        # Encabezados
        header_dni = Label(self.frame, text="DNI", font=header_font, bg="#bbb", width=15)
        header_pass = Label(self.frame, text="Contraseña", font=header_font, bg="#bbb", width=15)
        header_name = Label(self.frame, text="Nombre", font=header_font, bg="#bbb", width=15)
        header_dni.grid(row=0, column=0, padx=5, pady=5)
        header_pass.grid(row=0, column=1, padx=5, pady=5)
        header_name.grid(row=0, column=2, padx=5, pady=5)
        
        data = database('','','').show()
        if data:
            for index, (dni, password, name) in enumerate(data, start=1):
                self.data.append((dni, password, name))
                self.add_row(index, dni, password, name)


    def add_row(self, index, dni, password, name):
        Label(self.frame, text=dni, font=font, bg="#ccc", width=20).grid(row=index, column=0, padx=5, pady=2)
        Label(self.frame, text=password, font=font, bg="#ccc", width=20).grid(row=index, column=1, padx=5, pady=2)
        Label(self.frame, text=name, font=font, bg="#ccc", width=20).grid(row=index, column=2, padx=5, pady=2)

        Button(self.frame, text="✏️ Editar", font=font, command=lambda d=dni, p=password, n=name: self.edit_entry(d, p, n)).grid(row=index, column=3, padx=5)
        Button(self.frame, text="❌ Erase", font=font, command=lambda d=dni: self.erase_entry(d)).grid(row=index, column=4, padx=5)
        Button(self.frame, text="✅ Usar", font=font, command=lambda d=dni, p=password,n=name: self.use_this_dni(d,p,n)).grid(row=index, column=5, padx=5)

    def use_this_dni(self, dni, password, name):
        set_current_dni(dni, password, name)
        self.dni_var.set(f'Nombre: {name}')
        self.destroy()

    def erase_entry(self, dni):
        # Elimina el DNI del archivo
        self.data = [row for row in self.data if row[0] != dni]

        # Sobrescribe el CSV
        with open('local_database.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

        # Refresca vista
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.load_data()

    def edit_entry(self, dni, password, name):
        top = Toplevel(self)
        top.title("Editar entrada")
        top.geometry("300x200")

        Label(top, text="Nuevo DNI:").pack(pady=5)
        dni_entry = Entry(top)
        dni_entry.insert(0, dni)
        dni_entry.pack()

        Label(top, text="Nueva contraseña:").pack(pady=5)
        pass_entry = Entry(top)
        pass_entry.insert(0, password)
        pass_entry.pack()
        
        Label(top, text="Nuevo nombre:").pack(pady=5)
        name_entry = Entry(top)
        name_entry.insert(0, name)
        name_entry.pack()

        def save_edit():
            new_dni = dni_entry.get()
            new_pass = pass_entry.get()
            new_name = name_entry.get()
            self.data = [(new_dni, new_pass, new_name) if d == dni else (d, p, n) for d, p, n in self.data]

            with open('local_database.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in self.data:
                    writer.writerow(row)

            top.destroy()
            for widget in self.frame.winfo_children():
                widget.destroy()
            self.load_data()

        Button(top, text="Guardar", command=save_edit).pack(pady=10)
