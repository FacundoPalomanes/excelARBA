import os
from pathlib import Path

def erase_files(dni):
    # Archivos a adjuntar (poné tus rutas reales acá)
    downloads_path = Path.home() / "Downloads"
    sell_file = downloads_path / f"Comprobantes de Ventas - CUIT {dni}.xlsx"
    buy_file = downloads_path / f"Comprobantes de Compras - CUIT {dni}.xlsx"
    buy_file_updated = downloads_path / f"Compras_modificado_{dni}.xlsx"
    sell_file_updated = downloads_path / f"Ventas_modificadas_{dni}.xlsx"
    erase_file(buy_file)
    erase_file(buy_file_updated)
    erase_file(sell_file)
    erase_file(sell_file_updated)

def erase_file(file):
     if os.path.exists(file):
        os.remove(file)
        print(f"Archivo '{file}' eliminado.")
     else:
        print(f"El archivo '{file}' no existe.")