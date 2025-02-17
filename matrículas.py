"""
programa para registar as matriculas(segundos) de utilização  de um estacionamento
  O programa deve ler as matriculas separadas por,e os tempos em segundos separados por,
  NO máximo 10 matriculas
  """
import numpy as np
matriculas=input(("insira matriculas"))
tempos=input(("insira  os tempos de cada carro"))
maior=0


def Ler_dados():
  matriculas=input("insira  os tempos de cada carro separados por virgulos")
  tempos=input("insira todos os tempos separados por virgulas")
  tempos_separados=tempos.split(",")
  matriculas_separados=matriculas.split(",")
  print(matriculas_separadas,tempos_separados)
  matriculas_separadas = matriculas.split(",")
  tempos_separados = tempos.split(",")
  print(matriculas_separadas, tempos_separados)
  if len(matriculas_separadas) > 10:
    print("não pode inserir mais de 10 matriculas")
    return
  if len(tempos_separados) > 10:
    print("não pode inserir mais de 10 tempos")
    return
#verificar se

 
  for i in range(len(tempos_separados)):
    maior=matriculas_separadas[i].strip()
    #guardar os tempos
    tempos[i]=int(tempos_separados[i].strip())


def Maior_tempo(matriculas_separadas,tempos_separadas):
  maior[i]=0
  for i in range(10):
    if matriculas==[i]=="":
      break
    if tempos[i]>tempos[maior]:
      maior=i
    print(f"O tempo maior foi de {tempos[maior]} e corresponde à matricula {matriculas[maior]}")

    

def Média(tempos_separadas):
   media=0
   preenchidos=0
   for i in range(len(tempos_separadas)):
    if tempos[i]==0:
      break

    media=(media+i)/preenchidos
    return media
   

def mais_média(tempos_separados,media):
  maior_média=0
  for p in range(10):
    if tempos[p]==0:
      break
    if tempos[p]>media:
      print(f" O tempo maior do que a média é de{tempos[p]} e pertence à matricula {matriculas[p]}")

def vezes_estacionamento(matriculas):
  for m in range(len(matriculas)):
    contar=0
    for m2 in matriculas:
      if m2==matriculas:
        contar=+1
    if contar>1:
      print(f"A matricula{m}eseve estacionada{contar}vezes")
        


    

