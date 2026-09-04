from reader import extrair_texto_pdf
from filters import aplicar_filtros_deterministicos
from cliente import analisar_perfil_com_ia

def executar_pipeline_agencia_turismo():
    """
    Orquestra o fluxo de atendimento e planejamento automatizado da agência de turismo.
    """
    print("=== SISTEMA INTELIGENTE DE ROTEIROS (AGÊNCIA DE TURISMO) ===")
    
    # ---------------------------------------------------------
    # CONFIGURAÇÕES DA AGÊNCIA E PACOTE
    # ---------------------------------------------------------
    documentos_exigidos = ["Passaporte Valido"]
    orcamento_minimo_exigido = 4000
    catalogo_destinos = (
        "Pacotes Disponíveis: "
        "1. Praias do Nordeste (Foco em descanso e resort, valor estimado R$ 4.500). "
        "2. Europa Cultural - Paris e Roma (Foco em história e museus, valor estimado R$ 9.000)."
    )
    
    # Caminho simulado do arquivo PDF do formulário do cliente
   
    caminho_pdf = "formulario.pdf"
    
    # ---------------------------------------------------------
    # PASSO 1: LEITURA E EXTRAÇÃO DO PDF
    # ---------------------------------------------------------

    print(f"\n[Passo 1] Lendo o formulário do cliente do arquivo: {caminho_pdf}...")
    
    # Tenta extrair o texto de um arquivo PDF real na pasta
    texto_formulario = extrair_texto_pdf(caminho_pdf)
    
    # Se o PDF não existir na pasta ou estiver vazio, usa o texto simulado para a aula não parar
    if not texto_formulario.strip():
        print("-> Aviso: Arquivo PDF não encontrado na pasta. Usando dados simulados para a demonstração.")
        texto_formulario = (
            "Cliente: Wellington Cidade. "
            "Interesse: Viagem internacional cultural. "
            "Documentação: Possui Passaporte Valido. "
            "Orçamento disponível informado: R$ 8.500."
        )
    else:
        print("-> Texto extraído com sucesso do arquivo PDF real!")

    # ---------------------------------------------------------
    # PASSO 2: APLICAÇÃO DOS FILTROS DETERMINÍSTICOS
    # ---------------------------------------------------------
    print("\n[Passo 2] Aplicando filtros determinísticos (Regras Rígidas de Orçamento/Documento)...")
    aprovado_regras, motivos_reprovacao = aplicar_filtros_deterministicos(
        texto_formulario, 
        documentos_exigidos, 
        orcamento_minimo_exigido
    )
    
    # Valida se passou na triagem rígida
    if not aprovado_regras:
        print("-> Status: REPROVADO na triagem determinística.")
        print("-> Motivos da desclassificação:")
        for motivo in motivos_reprovacao:
            print(f"   - {motivo}")
        print("-> Processo encerrado. Nenhum recurso de IA foi consumido.")
        return

    print("-> Status: APROVADO na triagem determinística! Prosseguindo para a IA criar o roteiro...")

    # ---------------------------------------------------------
    # PASSO 3 & 4: CAMADA GENERATIVA E CONTROLE DE TOKENS
    # ---------------------------------------------------------
    print("\n[Passo 3 & 4] Acionando Camada Generativa (IA) e monitorando tokens...")
    
    try:
        roteiro_personalizado, relatorio_tokens = analisar_perfil_com_ia(
            texto_formulario, 
            catalogo_destinos
        )
        
        # Exibe os resultados da análise generativa
        print("\n==================================================")
        print("       ROTEIRO PERSONALIZADO GERADO PELA IA       ")
        print("==================================================")
        print(roteiro_personalizado)
        
        # Exibe o relatório de consumo computacional
        print("\n==================================================")
        print("         RELATÓRIO DE CONSUMO E TOKENS            ")
        print("==================================================")
        print(f"• Modelo Utilizado          : {relatorio_tokens['modelo']}")
        print(f"• Tokens de Entrada (Prompt): {relatorio_tokens['tokens_entrada']}")
        print(f"• Tokens de Saída (Output)  : {relatorio_tokens['tokens_saida']}")
        print(f"• Total de Tokens Consumidos: {relatorio_tokens['tokens_totais']}")
        print("==================================================")
        
    except Exception as e:
        print(f"[Erro Crítico] Falha ao executar a camada generativa: {e}")

if __name__ == "__main__":
    executar_pipeline_agencia_turismo()