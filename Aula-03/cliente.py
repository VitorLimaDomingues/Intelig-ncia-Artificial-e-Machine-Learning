from token_tracker import calcular_tokens

def analisar_perfil_com_ia(texto_formulario, catalogo_destinos):
    """
    Simula o envio do formulário e catálogo para um modelo generativo, gerando um roteiro 
    fictício didático e calculando rigorosamente os tokens de entrada e saída.
    Parâmetros:
        texto_formulario (str): O texto completo extraído do formulário do cliente.
        catalogo_destinos (str): As opções de pacotes disponíveis na agência.
    Retorna:
        tuple: (str com o roteiro gerado pela IA simulada, dict com o relatório detalhado de tokens)
    """
    # Define o nome do modelo simulado para fins de relatório
    modelo_utilizado = "gpt-4o-mini-simulado"
    
    # Configura o System Prompt (Instrução de papel que define o contexto do modelo)
    prompt_sistema = (
        "Você é um Consultor de Viagens Sênior de uma agência de turismo de luxo, "
        "especializado em criar roteiros personalizados alinhados às preferências e orçamento dos clientes."
    )
    
    # Configura o User Prompt (A janela de contexto que injeta os dados dinâmicos da execução)
    prompt_usuario = f"""
    Com base nas preferências do cliente descritas abaixo e no catálogo de destinos da agência, 
    crie um mini roteiro de viagens personalizado e uma estimativa de passeios.
    
    --- CATÁLOGO DE DESTINOS DA AGÊNCIA ---
    {catalogo_destinos}
    
    --- FORMULÁRIO DE PREFERÊNCIAS DO CLIENTE ---
    {texto_formulario}
    """
    
    # --- CONCEITO DE CONTEXTO E TOKENS DE ENTRADA ---
    # Tudo o que é enviado para o modelo (System + User) forma a "Janela de Contexto".
    # Calculamos exatamente quantos tokens essa entrada consome.
    texto_total_entrada = prompt_sistema + prompt_usuario
    tokens_entrada = calcular_tokens(texto_total_entrada, modelo_utilizado)
    
    # --- SIMULAÇÃO DA RESPOSTA DO MODELO GENERATIVO ---
    # Em vez de chamar uma API na nuvem, geramos uma resposta estruturada baseada no contexto.
    texto_resposta = (
        "--- ROTEIRO EXCLUSIVO GERADO PELA IA (SIMULAÇÃO DIDÁTICA) ---\n\n"
        "Olá,Wellington ! Com base no seu formulário e no seu orçamento de R$ 8.500, "
        "selecionamos o pacote ideal do nosso catálogo: **Europa Cultural - Paris e Roma**.\n\n"
        "**Cronograma Sugerido:**\n"
        "• **Dias 1 a 4 (Paris):** Visita guiada ao Museu do Louvre, caminhada romântica às margens do Sena e jantar bistrô.\n"
        "• **Dias 5 a 8 (Roma):** Tour histórico pelo Coliseu, Vaticano e Fontana di Trevi.\n\n"
        "*Parecer do Consultor:* Perfil perfeitamente alinhado com a documentação em dia e orçamento compatível!"
    )
    
    # --- CONCEITO DE TOKENS DE SAÍDA ---
    # Medimos quantos tokens a resposta gerada pelo modelo consumiu
    tokens_saida = calcular_tokens(texto_resposta, modelo_utilizado)
    
    # --- RELATÓRIO DE COMPUTACIONAL DE TOKENS ---
    # Consolida as métricas para demonstrar o custo computacional da operação
    relatorio_tokens = {
        "modelo": modelo_utilizado,
        "tokens_entrada": tokens_entrada,
        "tokens_saida": tokens_saida,
        "tokens_totais": tokens_entrada + tokens_saida
    }
    
    # Retorna o roteiro simulado e o dicionário completo de tokens
    return texto_resposta, relatorio_tokens

# Frase de entrada para processamento
texto = "A inteligência artificial aprende com dados"

# 1. Divide a frase em uma lista de palavras individuais utilizando os espaços
palavras = texto.split()

# 2. Inicializa um dicionário vazio que armazenará os agrupamentos
agrupamento = {}

# 3. Itera sobre cada palavra extraída do texto
for palavra in palavras:
    # Obtém a quantidade de caracteres da palavra atual
    tamanho = len(palavra)
    
    # Se o tamanho ainda não existe como chave no dicionário, cria uma lista vazia para ele
    if tamanho not in agrupamento:
        agrupamento[tamanho] = []
        
    # Adiciona a palavra na lista correspondente ao seu tamanho
    agrupamento[tamanho].append(palavra)

def atualizar_estoque(estoque: dict, vendas: list) -> dict:
    """Atualiza o saldo de produtos no estoque com base nas vendas efetuadas."""
    # Percorre cada tupla (produto, quantidade) presente na lista de vendas
    for produto, qtd_vendida in vendas:
        # Verifica se o produto vendido existe no cadastro do estoque
        if produto in estoque:
            # Checa se há saldo disponível suficiente para dar baixa
            if estoque[produto] >= qtd_vendida:
                # Subtrai a quantidade vendida do saldo atual do produto
                estoque[produto] -= qtd_vendida
                print(f" Venda de {qtd_vendida}x '{produto}' realizada com sucesso.")
            else:
                # Avisa que a quantidade em estoque é inferior à solicitada
                print(f" Estoque insuficiente de '{produto}'. Disponível: {estoque[produto]}, Solicitado: {qtd_vendida}.")
        else:
            # Avisa se o produto informado na venda não consta no dicionário
            print(f" Produto '{produto}' não cadastrado no estoque.")
            
    # Retorna o dicionário com o saldo do estoque atualizado após as operações
    return estoque











