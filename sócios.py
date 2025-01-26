"""
programa que verifica se existem pessoas que são sócias de dois clubes
e se isso acontecer manda uma mensagem ao utilizador
"""
import numpy as np
socios_A=np.array(["Joaquim","Maria","João"])
socios_B=np.array(["Maria","Anónio","Carla"])
soma=0
for nome_A in socios_A:
    for nome_B in socios_B:
        if nome_A ==nome_B:
            print("A pessoa chamda")(nome_A)("é sócia de dois clubes")
    