import random
import math
import time

NE = 10000
RESTRICAOX = 99953
RESTRICAOY = 100015

def defineCoordenadas():
  y = random.randrange(0, RESTRICAOY)
  x = random.randrange(0, RESTRICAOX)
  return x,y

def executaMonteCarlo(x=None, y=None):
  if not x and not y:
    x,y = defineCoordenadas()
  z = math.sin(x/50000) + math.cos(y/30000)
  return z

def randomWalk():
  x,y = defineCoordenadas()
  z = executaMonteCarlo()
  while True:
    direcao = random.choice(['NORTE', 'SUL', 'LESTE','OESTE'])
    if direcao == 'NORTE':
      y += random.randint(0, (RESTRICAOY - y))
    elif direcao == 'SUL':
      y -= random.randint(0,  y)
    elif direcao == 'LESTE':
      x += random.randint(0, RESTRICAOX - x)
    elif direcao == 'OESTE':
      x -= random.randint(0,  x)
  
    novoZ = executaMonteCarlo(x,y)
    if z >= novoZ:
      break
    else:
      z = novoZ
  return z

def main():

  print('Execução Monte Carlo Simples')
  tempoInicio = time.time()  
  '''Execução Monte Carlo Simples'''
  exp = [executaMonteCarlo() for _ in range(NE)]
  print(str(max(exp)))
  print('Tempo despendido {}'.format(time.time() - tempoInicio))
  print('---------------------------------------')

  print('Execução Monte random walk')
  tempoInicio = time.time()
  '''Execução Monte random walk'''
  exp = [randomWalk() for _ in range(NE)]
  print(str(max(exp)))
  print('Tempo despendido {}'.format(time.time() - tempoInicio))
  print('---------------------------------------')
  
if __name__ =="__main__":
  main()
