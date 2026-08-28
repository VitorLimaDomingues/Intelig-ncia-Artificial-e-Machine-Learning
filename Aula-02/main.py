# Função para calcular o custo estimado por caracter do prompt

def tokens_custo(texto:str, custo_por_tokens: float=0.0015)->dict:
    """
        Estimativa aproximada baseada na média de 3.2 caracteres por token em português.
    """

    total_caracteres = len(texto)
    tokens_estimado = max(int(total_caracteres / 3.2), 1)
    custo_estimado = (tokens_estimado / 1000 * custo_por_tokens)

    return {
        "Caracteres": total_caracteres,
        "Tokens Estimados": tokens_estimado,
        "Custo":f"{custo_estimado:6f}"
    }

especificacao = "Olá, meu nome é vitor de lima domingues."
print("Resultado", tokens_custo(especificacao))