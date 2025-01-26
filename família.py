import numpy as np
"""
programa para verificar se duas pessoas são da mesma família
 tendo em conta os dois últimos nomes
 """
nome1=np.input("insira o seu nome completo")
nome2=np.input("insira o seu nome completo")

def verificar_familia(nome1, nome2):
    if len(nome1) == len(nome2) - 1:
        return True
    else:
        return False
       

def verificar_familia(nome1, nome2):
    if len(nome1) == len(nome2) - 1:
        return True            
     