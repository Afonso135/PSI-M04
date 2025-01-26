#programa para criar uma agenda de contactos

def menu():
    print("1.Adicionar/n2.Listar todos/3.Pesquisar/n4.Apagar/n5.Editar/n6.Trminar")

def Adicionar(nomes,emails,números):


def Listar_todos(nomes,emails,números):
    print(nomes)



def Apagar(nomes,emails,números):
    apagar=input("qual o nome a apagar")
    if apagar in nomes[i]:
        for i in range():



def Editar(nomes,emails,números):
#função que pesquisa um contacto pelo nome e permite mudar os dados
    nome=input("insira um nome")

    for i in range(nr_contactos):
        if nome in nomes[i]:
            print(f"Dados de Contacto:{nomes[i]}-{emails[i]}-{números}[i]")
            op=input("Pretende editar estes dados?")
            if op=="S":
                  continue
            novo_nome=input("insira um nome ou deixe em branco")
            novo_email=input("insira um noome ou deixe em branco")
            novo_número=input("insira um número ou deixe em branco")
            if novo_nome.strip()!="":
                nomes[i]=novo_nome.strip()
            if novo_nome.strip()!="":
                emails[i]=novo_email.strip()
            if novo_nome.strip()!="":
                números[i]=novo_número.strip()
            
def Terminar():
    