from reportlab.lib.pagesizes import letter
from reportlab.lib.platypus import SimpleDocTemplate,Paragraph,Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def gerar_pdf(filename="relatorio.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, topMargin=40, bottomMargin=40)

    styles = getSampleStyleSheet()
    story=[]

    story.append(Paragraph("<b>Relatório de Entrega:</b> Módulo de exportação,", styles['Hending1']))

    dados=[
        ["Métrica", "Valor"],
        ["Horas de Desenvolvimento", "16.0H"],
        ["Horas Perdidas(Bugs)", "4.5H"],
        ["Valor Líquido Gerado"]
    ]

    tabela = table(dados,colWidths=[250, 250])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1D293B")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,0), colors.HexColor("#acbdSe1")),
        ('ROWBACKGROUND', (0,0), (-1, 0), [colors.white, colors.HexColor("#F8FAFC")])
    ]))

    story.append(tabela)