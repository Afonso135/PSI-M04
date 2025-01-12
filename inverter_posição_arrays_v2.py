import numpy as np
invertido=np.zero(5)
NR_elementos=5
for i in range(5):
 nomes=np.empty(NR_elementos,dtype="U20")
nomes[i]=input("introduza um nome")
#criar um array
nomes_invertidos=np.empty(NR_elementos),dtype="U20"
#preencher o array invertendo as suas posições
for i in range(NR_elementos):
 k=NR_elementos-1
 nomes_invertidos[k]=nomes[i]
 k=k-1

 #mostrar os dois arrays
print(nomes,nomes_invertidos)