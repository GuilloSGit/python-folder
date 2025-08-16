import os
from docx2pdf import convert
from tkinter import Tk, filedialog, messagebox

root = Tk()
root.withdraw()

carpeta_entrada = filedialog.askdirectory(
    title="Selecciona la carpeta de entrada")

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".docx"):
        ruta_DOCX = os.path.join(carpeta_entrada, archivo)
        try:
            convert(ruta_DOCX)
            print(f"Convertido: {ruta_DOCX}")
        except Exception as e:
            print(f"Error al convertir {ruta_DOCX}: {e}")
