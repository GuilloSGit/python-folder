import os
import shutil

# Ruta donde están los archivos a ordenar
ruta = input("Introduce la ruta de la carpeta a ordenar: ")

if not os.path.exists(ruta):
    print("La ruta especificada no existe.")
    exit()

# Verificar si la ruta es un directorio
if not os.path.isdir(ruta):
    print("La ruta especificada no es un directorio.")
    exit()

# Crear carpetas para cada tipo de archivo si no existen
tipos_archivos = ["Imágenes", "DocumentosPDF", "DocumentosTxt",
                  "ArchivosComprimidos", "Música", "Vídeos", "Ejecutables", "DocumentosExcel", "JSON"]

# Crear las carpetas si no existen
for carpeta in tipos_archivos:
    ruta_carpeta = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Mover los archivos a las carpetas correspondientes
for archivo in os.listdir(ruta):
    if archivo.endswith(('.jpg', '.gif', '.png', '.jpeg')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "Imágenes", archivo))
    elif archivo.endswith('.pdf'):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "DocumentosPDF", archivo))
    elif archivo.endswith(('.txt', '.doc', '.docx')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "DocumentosTxt", archivo))
    elif archivo.endswith(('.zip', '.rar', '.tar')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "ArchivosComprimidos", archivo))
    elif archivo.endswith(('.mp3', '.wav')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "Música", archivo))
    elif archivo.endswith(('.mp4', '.avi', 'webm', '.mov')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "Vídeos", archivo))
    elif archivo.endswith(('.exe', '.msi', '.dmg')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "Ejecutables", archivo))
    elif archivo.endswith(('.csv', '.xls', '.xlsx')):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "DocumentosExcel", archivo))
    elif archivo.endswith('.json'):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "JSON", archivo))
    else:
        # Si es una  carpeta de las que estoy creando, no imprimir nada
        if archivo in tipos_archivos:
            print(f"{archivo} - Archivo reconocido")
        else:
            print(f"{archivo} - Archivo no reconocido, no se moverá.")
