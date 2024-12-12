import numpy as np
"""
i-inteiros
f-reais
b-boleanos
s-strings
u- unicode string
m-datatime
i-inteiros
"""
nomes=np.empty(10,dtype="U20")
for i in range(len(nomes)):
    nomes[i]=input("introduza o nome")
    print(nomes)
    