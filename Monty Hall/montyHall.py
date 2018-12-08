import random 

NE = 10

def selecionaCarro(portas):
    indiceCarro = random.randint(0,2)
    portas[indiceCarro] = 1    
    return indiceCarro

def umaJogada(portas, portaEscolhida, trocaPorta=None):
  if trocaPorta:
    if portas[portaEscolhida] == 0: #se trocou de porta, a porta escolhida anteriormente deverá ser igual a zero
      return 1
  elif portas[portaEscolhida] == 1: #se ele não trocou de porta, ele ganha se a porta escolhida for 1
    return 1
  return 0


def main():
  rodadaSemTroca = []
  rodadaComTroca = []

  for _ in range(NE):
    portas = {0:0, 1:0, 2:0}
    portaCarro = selecionaCarro(portas)
    portaRemovida = 0
    portaEscolhida = random.randint(0,2)

    while True:
      portaRemovida = random.randint(0,2)
      if portaRemovida != portaCarro and portaRemovida != portaEscolhida :
        portas.pop(portaRemovida)
        break

    rodadaSemTroca.append(umaJogada(portas, portaEscolhida))
    rodadaComTroca.append(umaJogada(portas, portaEscolhida, trocaPorta=True))
  
  print('Não trocou de porta: {}'.format(sum(rodadaSemTroca)/(NE*1.0)))
  print('Trocou de porta: {}'.format(sum(rodadaComTroca)/(NE*1.0)))


if __name__ =="__main__":
  main()
