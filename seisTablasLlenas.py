from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

from generadorTablasIguales import tablasIguales

# Agrega el Encabezado bingo transformando el array numpy a una simple lista luego lo transforma en una tabla
class tablasLlenas():
    def __init__(self, pdf_file, num):
        self.tabla_Llena = tablasIguales()
        self.pdf_file = pdf_file
        self.estilo_cuerpo = ""
        self.estilo_info = ""
        self.content = []
        self.creacion_tablas(num)
        
    def asignar_tabla(self, arr):  
        nf = ["B", "I", "N", "G", "O"]
        data = arr.tolist()
        data.insert(0, nf)
        table = Table(data, colWidths=[40, 40, 40, 40, 40], rowHeights=[40, 30, 30, 30, 30, 30])  # Creación y asignación de tamaño de las tablas
        return table

    def tabla_resultado(self, i):
        i.tabla_llena()
        return i.tablaLlena

    def aplicar_estilos(self):
        # Aplicar estilos a las tablas
        self.estilo_cuerpo = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                            ('VALIGN', (2, 3), (2, 3), 'MIDDLE'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 28),#Tamaño del encabezado de las tablas
                            ('FONTSIZE', (0, 1), (-1, -1), 20),#Tamaño de los numeros
                            ('FONTSIZE', (2, 3), (2, 3), 10),#Tamaño de los numeros
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        self.estilo_info = TableStyle([('ALIGN', (0, 0), (-1,-1), 'LEFT'),
                            ('FONTSIZE', (0,0), (-1,-1), 16),
                            ('VALIGN', (0,0), (-1,-1),'TOP'),
                            ('BOX', (0, 0), (-1, -1), 2, colors.black),  # Borde exterior grueso
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

    def creacion_pdf(self):        
        #crea el documento
        self.document = SimpleDocTemplate(self.pdf_file, pagesize=letter,  
                                    leftMargin=10, rightMargin=10,
                                    topMargin=0, bottomMargin=10) #Tamaño del margen del pdf

    def creacion_tablas(self, num):
        self.aplicar_estilos()
        self.creacion_pdf()

        for i in range(num):
            self.tabla_Llena.tabla_principal()
            tb1= self.tabla_resultado(self.tabla_Llena)
            tb2= self.tabla_resultado(self.tabla_Llena)
            tb3= self.tabla_resultado(self.tabla_Llena)
            tb4= self.tabla_resultado(self.tabla_Llena)
            tb5= self.tabla_resultado(self.tabla_Llena)
            tb6= self.tabla_resultado(self.tabla_Llena)

            data_p = [["Organizado por:"],
                    ["Direccion:"],
                    ["Nota:"],
                    ["Fecha:"]]
            
            data_p = Table(data_p, colWidths=[580],rowHeights=[25, 25, 25, 25])
            data1 = self.asignar_tabla(tb1)
            data2 = self.asignar_tabla(tb2)
            data3 = self.asignar_tabla(tb3)
            data4 = self.asignar_tabla(tb4)
            data5 = self.asignar_tabla(tb5)
            data6 = self.asignar_tabla(tb6)

            data1.setStyle(self.estilo_cuerpo)
            data2.setStyle(self.estilo_cuerpo)
            data3.setStyle(self.estilo_cuerpo)
            data4.setStyle(self.estilo_cuerpo)
            data5.setStyle(self.estilo_cuerpo)
            data6.setStyle(self.estilo_cuerpo)
            data_p.setStyle(self.estilo_info)
            # Crear una tabla contenedora para alinear las tablas lado a lado con espaciado
            grupo_tablas = Table([[data1, Spacer(1, 0), data2], [data3, Spacer(1, 0), data4],[data5, Spacer(1, 0), data6]], colWidths=[300, 38, 210])

            # Crear el estilo del encabezado
            styles = getSampleStyleSheet()
            header_style = ParagraphStyle(name='CenteredHeader',
                                        parent=styles['Heading1'],
                                        alignment=1)  # 0=left, 1=center, 2=right

            # Crear el encabezado
            header = Paragraph("BINGO", header_style)
            # Crear el contenido del documento
            self.content.extend([header,Spacer(1,10), data_p, Spacer(1,20),grupo_tablas, PageBreak()])

        # Crear el documento PDF
        self.document.build(self.content)


        print(f"El archivo {self.pdf_file} ha sido creado.")

tablasLlenas("reporteTablasLlenas.pdf",5)