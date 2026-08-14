import random 

def verificar_autonomia_bike(capacidade_bateria:float, consumo: float)->str:
    autonomia_km = capacidade_bateria / consumo;
    if autonomia_km >= 50.0:
        # Regra determinística(Calculo exato)
        return f"PARA VIAGENS LONGA ({autonomia_km:1f}km)"
    return f"PARA VIAGENS URBANAS ({autonomia_km:1f}km)"

# Função que simula a abordagem Generativa Probabilística
# Estimativa da IA conversar com o cliente
def simular_estimativa(autonomia_base:float)->float:
    ruido = random.gauss(0, 3) # Variação de até 3km
    estimativa = autonomia_base + ruido
    return estimativa

# Simulação do cliente

bateria_wh = 500.0 # Bateria de 500 Wh (Watt Hora)
consumo_wh_km = 10.0 # Consumo médio de 10 Wh por km


autonomia_teorica = bateria_wh / consumo_wh_km


# Execução e exibição dos resultados
print("Determinístico:", verificar_autonomia_bike(bateria_wh, consumo_wh_km))
print(f"Generativo Simulado: {simular_estimativa(autonomia_teorica):1f}km")