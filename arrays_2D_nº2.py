"""
Defenir uma matriz 5,3 e preencher com a multiplicação do indice da e da coluna correspondente
"""
import numpy as np
matriz=np.zeros((5,3)),dtype="i"

#ciclo para percorrer as linhas
for l in  range(matriz.shape[0]):
    for c in range(matriz.shape[1]):
        matriz[l,c]=l*c
