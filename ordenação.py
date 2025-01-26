"""
implementar o algoritmo de ordenação bubble sort
"""
import numpy as np
números = np.array([29, 10, 14, 37, 14, 14])
def bubble_sort(vetor):
    tamanho=len(vetor)
    for i in range (tamanho):
        for j in range(0,tamanho-1):
            if vetor[j<vetor[j+1]]:
                t=vetor[j]
                vetor[j]=vetor[j+1]
                vetor[j+1]=t


