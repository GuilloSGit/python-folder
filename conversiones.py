import os
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from tkinter import Tk, filedialog, messagebox

root=Tk()
root.withdraw()

carpeta_entrada = filedialog.askdirectory(title="Selecciona la carpeta de entrada")

def docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    
    # Configuración de márgenes y formato
    margin = 72  # 1 pulgada = 72 puntos
    line_height = 14
    y_position = height - margin
    
    # Configuración de fuente
    font_name = 'Helvetica'
    font_size = 12
    c.setFont(font_name, font_size)
    
    # Función para verificar si hay espacio suficiente
    def check_page_break(required_lines=1):
        nonlocal y_position
        if y_position < margin + (line_height * required_lines):
            c.showPage()
            y_position = height - margin
            c.setFont(font_name, font_size)
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            y_position -= line_height  # Espacio entre párrafos
            continue
            
        # Dividir el texto en líneas que quepan en el ancho de la página
        max_width = width - (2 * margin)
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, font_name, font_size) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        # Verificar si hay suficiente espacio para el párrafo
        check_page_break(len(lines) + 1)
        
        # Dibujar cada línea
        for line in lines:
            c.drawString(margin, y_position, line)
            y_position -= line_height
        
        # Espacio después del párrafo
        y_position -= line_height * 0.5
    
    c.save()

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".docx"):
        ruta_DOCX = os.path.join(carpeta_entrada, archivo)
        ruta_PDF = os.path.splitext(ruta_DOCX)[0] + '.pdf'
        try:
            docx_to_pdf(ruta_DOCX, ruta_PDF)
            messagebox.showinfo("Conversión exitosa", f"Se convirtió {archivo} a PDF")
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir {archivo}: {str(e)}")
