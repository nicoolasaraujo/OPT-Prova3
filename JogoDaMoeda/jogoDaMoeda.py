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

def umaJogadaCapInicial(capInicial,L=3):
  s = 0
  gasto = 0
  while ((not abs(s) == L)): #continua jogando até que a diferença seja maior que L
    r = R.randint(0, 1)
    if r == 0:
      s -= 1
    elif r == 1:
      s += 1
    gasto += 1
    if capInicial > 0:
      capInicial -= 1
  return 8-gasto + capInicial # o resultado final será o quanto ele ganhou + o capital inicial

def umaJogadaOrcamento(saldo_aplicado, L=2):
  s = 0
  gasto = 0
  while ((not abs(s) == L) and (saldo_aplicado > 0)): #continua jogando até que a diferença seja maior que L e possua saldo
    r = R.randint(0, 1)
    if r == 0:
      s -= 1
    elif r == 1:
      s += 1
    gasto += 1
    saldo_aplicado -=1
  
  if (saldo_aplicado <= 0) and (not abs(s) == L): # quando sair do while caso não tenha dinheiro, então quer dizer que quebrou
    return saldo_aplicado

  return 8-gasto + saldo_aplicado

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

def simulaCapitalInicial(L=3):
  
  for capInicial in range(3, 25):
    resultados = [] 
    saldo = capInicial 
    for _ in range(0, NE):
      nroTentativa = 0
      saldo = capInicial
      while nroTentativa < 10:
        saldo = umaJogadaCapInicial(saldo)
        nroTentativa += 1
      resultados.append(saldo)

    print('Capital Inicial: {} \t Média: {}'.format(capInicial, sum(resultados)/(NE*1.0)))
  print('-------------------')

def simulaMoedaViciada():
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
  if ultimaNegativa:
    print(pontoMudanca) 
    print('-------------------')

def simulaDiferenca2():
  print('Vai executar diferença de 2')
  exp = [umaJogada(2) for _ in range(NE)]
  print(str(sum(exp)/(NE*1.0))) 
  print('-------------------')

def simulaOrcamento():
  for capital in range(1, 26):
    quebras = 0
    saldo = capital
    for _ in range (0, NE):
      nroTentativa = 0
      saldo = capital
      while saldo > 0 and nroTentativa < 2: 
        saldo = umaJogadaOrcamento(saldo) 
        nroTentativa += 1 
      if saldo <= 0:
          quebras += 1
    
    print('Orcamento: {} \t Quebras: {}'.format(capital, quebras))
  print('-------------------')

def main():
  # simulaDiferenca2()
  simulaCapitalInicial()
  # simulaMoedaViciada()
  # simulaOrcamento()

if __name__ =="__main__":
  main()


