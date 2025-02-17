"""
Programa para ler as notas de 10 alunos em 5 disciplinas e calcular a media de cada aluno
e a media de cada disciplina
"""
import numpy as np
notas=np.zeros([1,2,3,4,5,6,7,8,9,10,[1,2,3,4,5]])

def ler_dados(notas):
    for l in range(notas.shape[0]):
        for c in range(notas.shape[1]):
            notas[l,c]=input(f"introduza a nota do aluno{l+1} na{c+1}")


def média_aluno(notas):
    media=0
    soma=0
    for l in range(notas.shape[0]):
        for c in range(notas.shape[1]):
              media=soma/notas.shape[1]



def média_discpilna(notas):
    media=0
    soma=0
    for i in range(notas.shape[1]):
        for l in range(notas.shape[0]):
            media=soma/notas.shape[0]