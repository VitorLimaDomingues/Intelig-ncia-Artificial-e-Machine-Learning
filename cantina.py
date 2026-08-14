# Uma cantina da fiap precisa analisar a capacidade de produção de salgados
# (como coxinhas e empadas) a partir da quantidade de massa disponível 
# em estoque e da quantidade média de massa utilizada por unidade. 
# Além da conta exata (determinística), a cantina utiliza um assistente de 
# IA para simular a estimativa de demanda dos alunos 
# no intervalo (probabilística/generativa).

import random

def tempo_encomenda(tempo_sugerido:float, tempo_disponivel:float, fator_folga:float = 1)->dict:
    """Aplica um Guardrail no tempo estimo pela IA para encomendas da cantina,
    garantindo uma margem de segurança(folga) no cronograma da cozinha
    """

    # Calcular quanas vezes o tempo disponível é maior do que o tempo previsto pela IA

    fator_folga_obtido = tempo_disponivel / tempo_sugerido

    valido = fator_folga_obtido >= fator_folga

    return{
        "Tempo Sugerido":tempo_sugerido,
        "Folga":round(fator_folga_obtido,2),
        "Status_Produto": "Aceito" if valido else "Rejeitado"
    }

# Valores da encomenda
tempo_sugerido_ia = 45.0
tempo_disponivel = 50.0


# Executa a operação (Guardrail)
resultado_encomenda = tempo_encomenda(tempo_sugerido_ia, tempo_disponivel)

# Exibe o resultado no console
print("Resultado da validação da encomenda", resultado_encomenda)