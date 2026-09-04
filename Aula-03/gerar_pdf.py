from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def criar_pdf():
    nome_arquivo = "formulario.pdf"
    
    # Cria o documento PDF na pasta atual
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter
    
    # Escreve as informações que o leitor de PDF vai capturar
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, altura - 50, "AGENCIA DE TURISMO - FORMULARIO DE CLIENTE")
    
    c.setFont("Helvetica", 11)
    c.drawString(50, altura - 90, "------------------------------------------------------------------------------------------------")
    c.drawString(50, altura - 120, "Nome do Cliente: Wellington Cidade")
    c.drawString(50, altura - 150, "Interesse Principal: Viagem internacional cultural (Europa)")
    c.drawString(50, altura - 180, "Documentacao Apresentada: Possui Passaporte Valido.")
    c.drawString(50, altura - 210, "Orcamento Disponivel Informado: R$ 8.500")
    c.drawString(50, altura - 240, "Preferencias Adicionais: Foco em roteiros historicos, museus e gastronomia.")
    c.drawString(50, altura - 270, "------------------------------------------------------------------------------------------------")
    
    # Salva o arquivo no disco
    c.save()
    print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado na pasta.")

if __name__ == "__main__":
    criar_pdf()
