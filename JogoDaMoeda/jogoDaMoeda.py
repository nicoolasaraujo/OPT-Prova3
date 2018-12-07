import random as R
# import threading from threading
def umaJogadaMoedaViciada(L=3):
  s = 0
  gasto = 0
  while not abs(s) == L:
    r = R.random()
    if r < 0.61:
      s -= 1
      # print('Cara')
    elif r >= 0.61:
      s += 1
      # print('Coroa')
    gasto += 1
  # print(8-gasto)
  return 8-gasto

def umaJogada(L=3):
  s = 0
  gasto = 0
  while not abs(s) == L:
    r = R.randint(0, 1)
    if r == 0:
      s -= 1
    elif r == 1:
      s += 1
    gasto += 1
  return 8-gasto

def umaJogadaCapInicial(capInicial,L=3):
  print('Capital Inicial: ' + str(capInicial))
  s = 0
  gasto = 0
  while ((not abs(s) == L) & (capInicial[0] > 0) ): #continua jogando até que a diferença seja maior que L e possua capInicial[0]
    r = R.randint(0, 1)
    if r == 0:
      s -= 1
    elif r == 1:
      s += 1
    gasto += 1
    capInicial[0] -=1

  if (not abs(s) == L):
    return gasto * (-1)

  return 8-gasto

def main():
  NE=1000
  '''diferença de 3'''
  print('Vai executar diferença de 3')
  exp = [umaJogada() for _ in range(NE)]
  print(str(sum(exp)/(NE*1.0)))  

  '''diferença de 2'''
  print('Vai executar diferença de 2')
  exp = [umaJogada(2) for _ in range(NE)]
  print(str(sum(exp)/(NE*1.0)))  

  '''Diferença 3 e capInicial'''
  print('Diferença 3 e capInicial')
  capInicial = 5 
  # print(capInicial[0])
  exp = [umaJogadaCapInicial(capInicial) for _ in range(NE)]
  print(str(sum(exp)/(NE*1.0)))  

if __name__ =="__main__":
  main()


