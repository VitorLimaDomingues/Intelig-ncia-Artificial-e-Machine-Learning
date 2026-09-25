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
        ["Horas de Desenvolvimento", "16.0H"]
        ["Horas Perdidas(Bugs)", "4.5H"],
        ["Valor Líquido Gerado"]
    ]