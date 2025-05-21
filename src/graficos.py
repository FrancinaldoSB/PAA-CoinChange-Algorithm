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

MOEDAS = [i for i in range(1,16)]
MOEDAS2 = [i for i in range(1,46)]
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

def memoria_backtracking(lista_moedas, valor, total_moedas=0):
    tracemalloc.start()
    _ = algoritmo_backtracking(lista_moedas, valor, total_moedas)
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    
    return mem_atual, mem_pico

def plotar_tempos(tempos, cenario):    
    plt.figure(figsize=(10,6))
    plt.plot(tempos[0], label='Algoritmo Guloso', marker='o', linestyle='--', color='black')
    plt.plot(tempos[1], label='Backtracking', marker='s', linestyle='--', color='green')
    
    plt.title(f"Comparacao de tempo de execução para o {'primeiro' if cenario == 1 else 'segundo'} cenário")
    plt.xlabel('Número da execução', fontsize=12)
    plt.ylabel('Tempo (milissegundos)', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def plotar_memorias(memoriag, memoriab, total_moedas):
    labels = ['Memória atual', 'Memória de pico']
    x = np.arange(len(labels))
    largura = 0.35
    
    fig, ax = plt.subplots(figsize=(8,6))
    
    paleta = [sns.color_palette("pastel")[0], sns.color_palette("pastel")[4]]
    
    barra1 = ax.bar(x - largura/2, memoriag, largura, label='Algoritmo Guloso', color=paleta[0])
    barra2 = ax.bar(x + largura/2, memoriab, largura, label='Backtracking', color=paleta[1])
    
    ax.set_ylabel('Memória (KB)')
    ax.set_title(f'Uso de memória por algoritmo (Quantidade {total_moedas})')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    for barra in [barra1, barra2]:
        for b in barra:
            height = b.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(b.get_x() + b.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
            
    plt.tight_layout()
    plt.show()

# --------------------------------------------------------------------------------------------------- #
    
'''
Cenário 1: 15 moedas
'''

cenario1_guloso = tempos_guloso(MOEDAS, VALOR, 20)
cenario1_backtracking = tempos_backtracking(MOEDAS, VALOR, 20)
tempos_cenarios = [cenario1_guloso, cenario1_backtracking]

atualg, picog = memoria_guloso(MOEDAS, VALOR)
atualb, picob = memoria_backtracking(MOEDAS, VALOR)
memoriag = [atualg / 1024, picog / 1024]
memoriab = [atualb / 1024, picob / 1024]

plotar_memorias(memoriag, memoriab, len(MOEDAS))
plotar_tempos(tempos_cenarios, 1)

# --------------------------------------------------------------------------------------------------- #
    
'''
Cenário 1: 45 moedas
'''

cenario1_guloso = tempos_guloso(MOEDAS2, VALOR, 20)
cenario1_backtracking = tempos_backtracking(MOEDAS2, VALOR, 20)
tempos_cenarios = [cenario1_guloso, cenario1_backtracking]

plotar_memorias(memoriag, memoriab, len(MOEDAS2))
plotar_tempos(tempos_cenarios, 2)