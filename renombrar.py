import os
import stat

import tkinter as tk
from tkinter import filedialog, messagebox


def seleccionar_carpeta():
    ruta = filedialog.askdirectory(title="Seleccionar carpeta")
    entrada_carpeta.insert(0, ruta)


def renombrar_archivos():
    carpeta = entrada_carpeta.get()
    prefijo = entrada_prefijo.get()
    extensiones = tuple(entrada_extensiones.get().split(sep=','))

    archivos = []

    for file in os.listdir(carpeta):
        if file.endswith(extensiones):
            archivos.append(file)

    # Creación del archivo deshacer renombrado.sh
    ruta_deshacer = os.path.join(carpeta, "deshacer_renombrado.sh")

    with open(ruta_deshacer, "w", encoding="utf-8") as deshacer_mem:
        deshacer_mem.write("#!/bin/bash\n")
        # Generar los comandos en orden inverso
        for i, nombre_actual in reversed(list(enumerate(archivos, start=1))):
            extension_actual = os.path.splitext(nombre_actual)[1]
            nuevo_nombre = f"{prefijo}_{i}{extension_actual}"
            deshacer_mem.write(f'mv "{nuevo_nombre}" "{nombre_actual}"\n')
        deshacer_mem.write('rm -- "$0"\n')

    # Hacer el archivo ejecutable
    # Permisos de lectura, escritura y ejecución para el propietario, y lectura y ejecución para grupo y otros
    os.chmod(ruta_deshacer, 0o755)

    # Renombrar archivos
    for i, nombre_actual in enumerate(archivos, start=1):
        extension_actual = os.path.splitext(nombre_actual)[1]
        nuevo_nombre = f"{prefijo}_{i}{extension_actual}"
        ruta_actual = os.path.join(carpeta, nombre_actual)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        os.rename(ruta_actual, ruta_nueva)

    messagebox.showinfo("Renombrado Completo",
                        f"Renombrados {len(archivos)} archivos en la carpeta {carpeta} con el prefijo '{prefijo}'.\n\n"
                        f"Se ha creado un archivo 'deshacer_renombrado.sh' en la carpeta para revertir los cambios.")


# Ventana de aplicativo
ventana = tk.Tk()

ventana.title("Renombrado Completo")
ventana.geometry("400x260")
ventana.resizable(False, False)

tk.Label(ventana, text="Carpeta:").pack(pady=5)
frame_carpeta = tk.Frame(ventana)
frame_carpeta.pack(pady=5)

entrada_carpeta = tk.Entry(frame_carpeta, width=40)
entrada_carpeta.pack(side=tk.LEFT, padx=5)
tk.Button(frame_carpeta, text="Examinar",
          command=seleccionar_carpeta).pack(side=tk.LEFT)

tk.Label(ventana, text="Prefijo de los archivos:").pack(pady=5)
entrada_prefijo = tk.Entry(ventana, width=30)
entrada_prefijo.insert(0, "imagen_")
entrada_prefijo.pack(pady=5)

tk.Label(ventana, text="Extensiones (separadas por coma):").pack(pady=5)
entrada_extensiones = tk.Entry(ventana, width=30)
entrada_extensiones.insert(0, ".jpg,.jpeg,.png,.gif,.bmp")
entrada_extensiones.pack(pady=5)

tk.Button(ventana, text="Renombrar archivos",
          command=renombrar_archivos, bg="#04ba04", fg="white", padx=10).pack(pady=15)

ventana.mainloop()
