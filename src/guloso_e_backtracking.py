# Se você tiver moedas de valores [1, 3, 4] e quiser formar o valor 6, a combinação ideal seria:

# 1 moeda de 3 + 1 moeda de 3 = 2 moedas

# ou 1 moeda de 4 + 1 moeda de 1 + 1 moeda de 1 = 3 moedas
# A resposta ideal é 2 moedas

lista = [1, 3, 4]

valor = 6

# Algoritmo Guloso
# O algoritmo guloso tenta sempre usar a maior moeda possível, o que pode não levar à solução ótima em todos os casos.
def algoritmo_guloso(moedas, valor):
    moedas.sort(reverse=True) 
    total_moedas = 0
    for moeda in moedas:
        while valor >= moeda:
            valor -= moeda
            total_moedas += 1
    return total_moedas if valor == 0 else -1

resultado_guloso = algoritmo_guloso(lista, valor)
# print(f"Resultado Guloso: {resultado_guloso}")

# Algoritmo Backtracking
# O algoritmo de backtracking tenta todas as combinações possíveis de moedas para encontrar a solução ótima.
def algoritmo_backtracking(moedas, valor, total_moedas=0):
    if valor == 0:
        return total_moedas
    if valor < 0 or not moedas:
        return float('inf')  

    usar_moeda = algoritmo_backtracking(moedas, valor - moedas[0], total_moedas + 1)

    nao_usar_moeda = algoritmo_backtracking(moedas[1:], valor, total_moedas)
    return min(usar_moeda, nao_usar_moeda)

resultado_backtracking = algoritmo_backtracking(lista, valor)
# print(f"Resultado Backtracking: {resultado_backtracking if resultado_backtracking != float('inf') else -1}")