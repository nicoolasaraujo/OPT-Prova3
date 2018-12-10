import random as R

NE=1000
ORCAMENTO = 0

def umaJogadaMoedaViciada(vicio, L=3):
  s = 0
  gasto = 0
  while not abs(s) == L:
    r = R.random()
    if r < vicio:
      s -= 1
    elif r >= vicio:
      s += 1
    gasto += 1
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
  s = 0
  gasto = 0
  while ((not abs(s) == L)): #continua jogando até que a diferença seja maior que L e possua capInicial[0]
    r = R.randint(0, 1)
    if r == 0:
      s -= 1
    elif r == 1:
      s += 1
    gasto += 1
    if capInicial > 0: #quando o capital tiver acabado o seu valor não deve mais ser drecementado, porque o "crédito" será contabilizado no gasto
      capInicial -=1
  return 8-gasto + capInicial # o resultado final será o quanto ele ganhou + o capital inicial

def umaJogadaOrcamento(orcamento,L=2):
  s = 0
  gasto = 0
  while ((not abs(s) == L) and (orcamento > 0)): #continua jogando até que a diferença seja maior que L e possua capInicial[0]
    r = R.randint(0, 1)
    if r == 0:
      s -= 1
    elif r == 1:
      s += 1
    gasto += 1
    orcamento -=1
  if(abs(s) == L):
    return 0
  return 1
  
def main():
  '''diferença de 3'''
  print('Vai executar diferença de 3')
  exp = [umaJogada() for _ in range(NE)]
  print(str(sum(exp)/(NE*1.0)))  

  # '''diferença de 2'''
  # print('Vai executar diferença de 2')
  # exp = [umaJogada(2) for _ in range(NE)]
  # print(str(sum(exp)/(NE*1.0)))  

  # '''Diferença 3 e capInicial'''
  # print('Diferença 3 e capInicial')
  # for capInicial in range(3, 9): 
  #   capInicial = int(capInicial) 
  #   print('Capital Inicial: {}'.format(capInicial))
  #   exp = [umaJogadaCapInicial(capInicial) for _ in range(NE)]
  #   print(str(sum(exp)/(NE*1.0)))  
  
  for i in range(1,26):
    print('Orçamento: {}'.format(i), end="\t")
    exp = [umaJogadaOrcamento(i) for _ in range(NE)]
    print(str(sum(exp)))
  
  # print(umaJogadaMoedaViciada(0.5))

    # exp = [umaJogadaMoedaViciada(0.8) for _ in range(NE)]
    # print(str((sum(exp)/(NE*1.0))))
    ultimaNegativa = None
    percVicio = 0.5
    pontoMudanca = None
    for i in range(1, 51):
      tempPerc = percVicio + i/100
      exp = [umaJogadaMoedaViciada(tempPerc) for _ in range(NE)]
      vlr = sum(exp)/(NE*1.0)
      print('Percentual: {} \tResultado: {}'.format(round(tempPerc, 2),vlr))
      if vlr < 0:
        ultimaNegativa = tempPerc
        pontoMudanca = None
      else:
        if ultimaNegativa and not pontoMudanca:
          pontoMudanca = tempPerc
      print('-------------------')

    if ultimaNegativa:
      print(pontoMudanca) 

if __name__ =="__main__":
  main()


