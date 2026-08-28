def validar_senha(senha:str)-> bool:
    """
        Verifica se uma senha cumpre aos requisitos mínimos de comprimento dos caracteres
    """

    tamanho_minimo = len(senha) >= 8

    maisculo = any(char.isupper() for char in senha)

    numero = any(char.isdigit() for char in senha)

    return tamanho_minimo and maisculo and numero

print("Senha", validar_senha("Senha123"))

print("Senha", validar_senha("senha3145"))

print("Senha", validar_senha("minhasenha3333"))