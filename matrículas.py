"""
programa para registar as matriculas(segundos) de utilização  de um estacionamento
  O programa deve ler as matriculas separadas por,e os tempos em segundos separados por,
  NO máximo 10 matriculas
  """
import numpy as np
matriculas=input(("insira matriculas"))
tempos=input(("insira  os tempos de cada carro"))
maior=0


def estatistica(matriculas,tempos):