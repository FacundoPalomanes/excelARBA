import os

FILE = "current_dni.txt"

def set_current_dni(dni, password, name):
    with open(FILE, 'w') as f:
        f.write(f"{dni},{password},{name}")

def get_current_dni():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            data = f.read().strip()
            if "," in data:
                dni, password, name = data.split(",", 2)
                return dni, password, name
            else:
                return data, None, None
    return None, None, None
