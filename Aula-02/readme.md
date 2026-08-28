# Aula de IA e Machine Learning - 28/08/2026

**Modelos Generativos Funcionam (Tokens, Embeddings, Contexto)**

tokens são processados em espaços vetoriais de alta dimensão (Embeddings), onde proximidade geométrica reflete afinidade semântica.
A limitação da Janela de Contexto determina quanto histórico o modelo consegue processar simultaneamente.  

A Alucinação Técnica ocorre porque o objetivo de treinamento do modelo é maximizar a probabilidade da sequência de palavras subsequente, sem acesso direto a um motor de cálculo numérico ou verificação 
de fatos em tempo real.

**Tokens:** São os pedaços mínimos de texto (palavras ou caracteres) em que o modelo divide uma informação 
para conseguir processá-la.

**Embeddings:** São as representações numéricas (vetores) desses tokens, que traduzem o seu significado 
e a relação semântica com outras palavras.

**Contexto:** É o volume total de informação (janela de memória) que a IA consegue considerar de uma 
só vez para entender e gerar uma resposta coerente.