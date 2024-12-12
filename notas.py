import numpy as np

#constnte com o valor do nº de alunos
NR_ALUNOS=10
#defenir o array
notas=np.zeros(10)

#ler as notas
for n in range(NR_ALUNOS):
    notas[n]=int(input("nota:"))
    print(notas)

#calcular a média
soma=0
soma=soma+notas[n]

média=soma/NR_ALUNOS
print(f"a média dos alunos foi{média}")

for n in range(NR_ALUNOS):
    if notas[n]>média:
        print(f"a nota{notas} do aluno nº{n+1}é superior à média")



