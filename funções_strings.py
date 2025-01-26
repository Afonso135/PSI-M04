texto=" olá mundo "

tamanho=len(texto)# obter o tamanho da string
print(tamanho)

texto=texto.upper()# converter as letras para maiúsculas
print(texto)
texto=texto.lower()#converter as letras para maiúsculas
print(texto)

texto=texto.capitalize()# devolve a string com a 1ª letra maiúsculo
print(texto)

texto=texto.strip()#devolve a string sem espaços em brancos
print(texto)

texto=texto.replace("","-")# devolve a string substituindo o primeiro parâmetro pelo segundo
print(texto)

texto=texto.isdigit#devolve verdadeiro se todas as letras sem números
print(texto)

frase="olá mundo, o computador é um torradeira"
palavras=frase.split("") # devolve uma lista com as partes da str separadas por o caracter indicado
print(palavras)

posição=frase.index("m")# devolve a posição da str,mas se não existir dá erro
print(posição)

posição=frase.find("m")# devolve a posião da str, se não encontra devolve -1
if posição==1:
    print("não encontrei")
else:
    print("encontrei"+str(posição))
código=ord("a")
print(código)
#devolve a letra correspondente
letra=chr(97)