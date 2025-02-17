"""
Introdução aos arrays de duas dimensões ou matrizes
"""
import numpy as np

arr=np.array([[1,2,3],[3,5,0]])

print(arr)#1º elemento
print(arr[0,0])#último elemento
print(arr[1,2])

#percorrer todos os relementos da matriz
for i in range(2):
    for c in range(3):
        print(arr[i,c])

#nº de linhas
print(f"Nº de linhas da matriz:",arr.shape[0])
#nº de colunas
print(f"Nº de linhas da matriz:",arr.shape[1])