"""
O Sr. Joaquim tem um restaurante muito popular é preciso de ajuda a gerir a fila dee clientes
    Pretende-se criar um programa para registar os nomes dos clientes em espera e de cada vez retirar o 1º da fila
    menu:1.Entrada 2.Saída 3. Consultar fila 4. Terminar
"""
import numpy as np
n_máx=10
def Entrada(fila):
#função para adicionar um nome no final da fila
    #ler o nome
    nome=input("insira um nome")
    #procurar o último nome da fila
    q=0
    for posição  in range(n_máx):
     if fila[posição]=="":
        
    #avisar se a fila está cheia
        if q==n_máx:
            print("A fila está cheia")
#inserir o nome
    fila[posição]=nome
    print("a sua posição na fila é de {posição}")
        



def Saída(fila,posição):
 #função para tirar o 1º nome da fila
    #verificar se a fila está vazia
    if fila[posição(0)]=="":
        print("a fila está vazia")
    #retirar o 1º nome da fila
    print(f"{fila[0]} pode entrar na fila")
    fila[0] = ""
    #puxar o resto dos nomes uma posição á frente
    for i  in range(n_máx-1):
        fila[i]=fila[i+1]
        fila[n_máx-1]#limpar a última posição do array

       

def Consultar_fila(fila,posição):
#função para ver a fila
    #verificar se a fila está vazio
    if fila[posição(0)]=="":
        print("a fila está vazia")
    #listar os nomes da fila de espera
    for  k in range(n_máx):
        if fila[posição]=="":
            break

    #avisar se a fila está cheia
    if fila[posição]=="":
        fil_cheia=False

def main():
    op=int(input("insira a opção da operção a realizar"))
    fila = np.zeros(n_máx, dtype="U20")
    while op!=4:
        print("1.Entrada/2.Saída/3.Consultar fila/Terminar")
        if op==1:
            Entrada(fila)
        if op ==2:
            Saída(fila)
        if op==3:
            Consultar_fila(fila)
        if op==4:
            break
    