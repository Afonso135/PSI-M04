"""
Criar uma agenda que regista os nomes por ordem alfabetica.
    Guardar o onome e a data de nascimento das pessoas ordenadas por ordem crescente do nome
    menu:1.Adicionar contacto 2.listar contactos 3.pesquisar 4. terminar
"""
import numpy as np
N_MÁX=10
contactos=np.zeros(N_MÁX,dtype="U30")



def Adicionar(contactos,nome):
    """
    função para adicionar um novo contacto à agenda
    """
    #verificar se está vazio
    if contactos[0]=="":
        contactos=nome
        return 
    #verificar se está cheio
    if contactos[N_MÁX-1]!="":
        print("Agenda cheia")
        return
    #procurar a posição do novo contacto
    for posição in range(N_MÁX):
        if nome<contactos[posição] or contactos[posição]=="":
            break
    #avançar uma posição
    for i in range(N_MÁX-1,posição,-1):
        contactos[i]=contactos[i-1]
        #inserir contacto
        contactos[posição]=nome



def Listar(contactos):
    """
    Lista todos os contatos na agenda
    """
    for nome in contactos:
        if nome=="":
            partes=nome.split("-")
        print(f"nome: {partes[0]}, data_nascimento: {partes[1]}")



def Pesquisar(contactos,nome):
    "Recebe o array de contactos e o nome a pesquisar"
    inicio=0
    fim=len(contactos)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        parrtes=contactos[meio]
        valor_meio=contactos[meio]
        if nome in valor_meio:
            print(valor_meio)
            return
        if nome in valor_meio:
            inicio=meio+1
        else:
            fim=meio-1
        print("o nº não existe")

def main():
    contactos=np.zero(N_MÁX,"U30")
    op=0
    while op!=4:
        print("1.Adicionar contacto/2.Listar/3.Pesquisar/Terminar")
        if op=="1":
            nome=input("insira o nome do contacto a adicionar")
            data=input("insira a sua data de nascimento:")
            Adicionar(contactos,nome+"-"*data)
        if op=="2":
            Listar(contactos)
        if op=="3":
            Pesquisar()
        if op=="4":
            break
    