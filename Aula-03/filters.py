
import re

def aplicar_filtros_deterministicos(texto_formulario, documentos_obrigatorios, orcamento_minimo):
    """
    Aplica filtros determinísticos estritos no formulário de preferências de turismo.
    Parâmetros:
        texto_formulario (str): O texto extraído do PDF.
        documentos_obrigatorios (list): Vistos/Documentos exigidos (ex: ["Passaporte Válido", "Visto americano"]).
        orcamento_minimo (float): Orçamento mínimo estipulado para o pacote de viagem.
    Retorna:
        tuple: (bool indicando aprovação, lista de motivos de reprovação se houver)
    """
    # Converte todo o texto para letras minúsculas para padronizar as buscas
    texto_lower = texto_formulario.lower()
    
    # Variável de controle assumindo que o cliente passou inicialmente
    aprovado = True
    
    # Lista para armazenar os motivos de eventuais desclassificações
    motivos_reprovacao = []
    
    # --- REGRA 1: Checagem de Documentação / Vistos Obrigatórios ---
    for doc in documentos_obrigatorios:
        doc_lower = doc.lower()
        
        # Verifica se o documento NÃO está mencionado no texto do formulário
        if doc_lower not in texto_lower:
            aprovado = False
            motivos_reprovacao.append(f"Documento ou visto obrigatório ausente: '{doc}'")
            
    # --- REGRA 2: Verificação de Orçamento Mínimo via Regex ---
    # Expressão regular para buscar padrões de valores financeiros (ex: "R$ 5.000", "5000 reais")
    padrao_orcamento = r'(?:r\$|\$)?\s*(\d{1,3}(?:\.\d{3})*|\d+)'
    correspondencias = re.findall(padrao_orcamento, texto_lower)
    
    # Converte os valores encontrados removendo pontos para inteiro
    valores_encontrados = []
    for val in correspondencias:
        val_limpo = val.replace('.', '')
        if val_limpo.isdigit():
            valores_encontrados.append(int(val_limpo))
            
    if valores_encontrados:
        maior_valor = max(valores_encontrados)
        # Se o maior valor monetário encontrado no formulário for menor que o requisito da agência
        if maior_valor < orcamento_minimo:
            aprovado = False
            motivos_reprovacao.append(f"Orçamento insuficiente: Informado R$ {maior_valor}, mas o pacote mínimo exige R$ {orcamento_minimo}.")

    # Retorna o status final da triagem e os motivos de corte
    return aprovado, motivos_reprovacao