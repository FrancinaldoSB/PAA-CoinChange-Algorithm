# --------------------------------------------------------------------------------------------------- #

'''
Bibliotecas necessárias e variáveis globais
'''

from guloso_e_backtracking import algoritmo_guloso, algoritmo_backtracking
import matplotlib.pyplot as plt
import numpy as np
import time as t
import random
import math
import pandas as pd
import seaborn as sns
import os
import tracemalloc

MOEDAS = [i for i in range(1,15)]
MOEDAS2 = [i for i in range(1,45)]
VALOR = 10

# --------------------------------------------------------------------------------------------------- #

'''
Metrificação e plotagem dos gráficos
'''

def tempos_guloso(lista_moedas, valor, n_execucoes):
    tempos = []
    for _ in range(n_execucoes):
        inicio = t.time()
        _ = algoritmo_guloso(lista_moedas, valor)
        fim = t.time()
        res = fim - inicio
        tempos.append(res)
    tempos_mili = [res * 1_000 for res in tempos]
    return tempos_mili
    
def memoria_guloso(lista_moedas, valor):
    tracemalloc.start()
    _ = algoritmo_guloso(lista_moedas, valor)
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    
    return mem_atual, mem_pico
    
def tempos_backtracking(lista_moedas, valor, n_execucoes, total_moedas=0):
    tempos = []
    for _ in range(n_execucoes):
        inicio = t.time()
        _ = algoritmo_backtracking(lista_moedas, valor, total_moedas)
        fim = t.time()
        res = fim - inicio
        tempos.append(res)
    tempos_mili = [res * 1_000 for res in tempos]
    return tempos_mili

def memoria_guloso(lista_moedas, valor, total_moedas=0):
    tracemalloc.start()
    _ = algoritmo_backtracking(lista_moedas, valor, total_moedas)
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    
    return mem_atual, mem_pico

def plotar_tempos(tempos):    
    plt.figure(figsize=(10,6))
    plt.plot(tempos[0], label='Algoritmo Guloso', marker='o', linestyle='--', color='black')
    plt.plot(tempos[1], label='Backtracking', marker='s', linestyle='--', color='green')
    
    plt.title(f'Comparacao de Tempo de Execucao para o Primeiro Cenário')
    plt.xlabel('Número da execução', fontsize=12)
    plt.ylabel('Tempo (milissegundos)', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
# --------------------------------------------------------------------------------------------------- #
    
'''
Cenário 1: 15 moedas
'''

cenario1_guloso = tempos_guloso(MOEDAS, VALOR, 20)
cenario1_backtracking = tempos_backtracking(MOEDAS, VALOR, 20)
tempos_cenarios = [cenario1_guloso, cenario1_backtracking]

plotar_tempos(tempos_cenarios)

# --------------------------------------------------------------------------------------------------- #
    
'''
Cenário 1: 45 moedas
'''

cenario1_guloso = tempos_guloso(MOEDAS2, VALOR, 20)
cenario1_backtracking = tempos_backtracking(MOEDAS2, VALOR, 20)
tempos_cenarios = [cenario1_guloso, cenario1_backtracking]

plotar_tempos(tempos_cenarios)