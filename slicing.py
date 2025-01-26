"""
Slicing-Permite ter acesso a subconjuntos de uma sequência ou coleção
sintaxe:sequencia[início:fim:passo]
inicio- a posição do primeiro a incluir
fim- é a posição onde termina o slice NÃO É INCLUI
passo-intervalo entre os elementos a inclui no slice
"""

nome="Mário silva"
nome_5letas=nome[0:5:1]#copia as lettras da posição 0 a 4
nome_5letas=nome[:5:1]#copa as primeiras 5 letras
print(nome_5letas)
nome_ultimas_letras=nome[7:]#copia as letras da posição 7 até ao fim
print(nome_ultimas_letras)
nome_invertido=nome[::-1]# inverter a string
print(nome_invertido)
nome_2_2_letras=nome[::2]
print(nome_2_2_letras)
print(nome[-1])#ultima letra da string
apelido=nome[13:7:-1]
print(apelido)

import numpy as np
nomes=np.array(["Joaquim","maria","antónio","augusto","césar"])
#mostrar todos nomes por ordem inversa
nomes_inverso=nomes[::-1]
#mostrar os dois ultimos nomes
nomes_2_ultimos=nomes[len(nomes)-2:]
#mostrar o 1º,o 3º e o 5º
print(nomes[::2]) 
