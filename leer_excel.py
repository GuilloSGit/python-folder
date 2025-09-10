import os
import pandas as pd
import dotenv

dotenv.load_dotenv()
smtp_password_env=os.getenv("GMAIL_APP_PASSWORD")

# leer el archivo xlsx
df=pd.read_excel("/Users/guillermoandrada/Documents/python-docs/nombres_propios_frecuentes_anio_sexo_provincia_2012_2024.xlsx")

# filtrar nombre > 12000
nombre_filtrado=df[df["cantidad"]>=500]

# ordenar por nombre y cantidad donde provincia_id!=99
nombre_filtrado=nombre_filtrado[nombre_filtrado["provincia_id"]!=99] # total_pais

# Usar la columna 'nombre_provincia' que ya existe en los datos
nombres_provincias=nombre_filtrado[['provincia_id', 'nombre_provincia']].drop_duplicates()
provincias=dict(zip(nombres_provincias['provincia_id'], nombres_provincias['nombre_provincia']))

# Agrupar por provincia y contar la cantidad de nombres únicos
nombres_por_provincia=nombre_filtrado.groupby('provincia_id')['nombre'].nunique()

# Crear una Serie con los nombres de las provincias
nombres_provincias=nombres_por_provincia.index.map(provincias)
nombres_por_provincia.index=nombres_provincias
nombres_por_provincia=nombres_por_provincia.sort_values(ascending=False)

# Crear el gráfico
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
nombres_por_provincia.plot(kind='bar')
plt.title('Cantidad de nombres únicos por provincia')
plt.xlabel('Provincia')
plt.ylabel('Cantidad de Nombres Únicos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Guardar el gráfico
ruta_grafico = "/Users/guillermoandrada/Documents/python-docs/output/nombres_por_provincia.png"
plt.savefig(ruta_grafico)
plt.close()

# Ordenar los datos para el archivo de salida
nombre_filtrado = nombre_filtrado.sort_values(by=["provincia_id","nombre","cantidad"], ascending=[True, True, True])

# guardar en nvo xlsx
os.makedirs("/Users/guillermoandrada/Documents/python-docs/output", exist_ok=True)
salida_xlsx="/Users/guillermoandrada/Documents/python-docs/output/nombres_filtrados.xlsx"
nombre_filtrado.to_excel(salida_xlsx, index=False)

# Crear un archivo de texto simple en lugar de TXT
salida_txt = "/Users/guillermoandrada/Documents/python-docs/output/nombres_filtrados.txt"
with open(salida_txt, 'w') as f:
    f.write(nombre_filtrado.to_string())

# enviar el reporte por email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

# configurar el servidor SMTP
smtp_server="smtp.gmail.com"
smtp_port=587
smtp_user="guillermoandrada@gmail.com"
smtp_password=smtp_password_env

# crear el mensaje
msg=MIMEMultipart()
msg["From"]="guillermoandrada@gmail.com"
msg["To"]="guillermoandrada@gmail.com"
msg["Subject"]="Reporte de nombres filtrados"

# El cuerpo del mensaje ahora se manejará más adelante

# Agregar el archivo de texto
with open(salida_txt, "rb") as attachment:
    part = MIMEApplication(attachment.read(), Name=os.path.basename(salida_txt))
    part["Content-Disposition"] = f"attachment; filename={os.path.basename(salida_txt)}"
    msg.attach(part)

# Crear el mensaje HTML con la imagen incrustada
html = """
<html>
    <body>
        <p style="font-size: 16px;max-width: 700px;">Se adjunta el reporte de nombres únicos de todas las provincias, se quitaron los totales del país</p>
        <br><br>
        <div style="max-width: 700px; margin: 0 auto;">
            <img src="cid:grafico_provincias" style="width: 100%; height: auto;" alt="Gráfico de provincias"/>
        </div>
    </body>
</html>
"""

# Adjuntar el HTML al mensaje
msg.attach(MIMEText(html, 'html'))

# Adjuntar la imagen
with open(ruta_grafico, 'rb') as img:
    img_part = MIMEImage(img.read())
    img_part.add_header('Content-ID', '<grafico_provincias>')
    img_part.add_header('Content-Disposition', 'inline', filename=os.path.basename(ruta_grafico))
    msg.attach(img_part)

# enviar el correo
try:
    server=smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, msg["To"], msg.as_string())
    server.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print("Error al enviar el correo:", e)

