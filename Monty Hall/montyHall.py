import random 

def populaPortas(portas):
    indiceCarro =random.randint(0,2)
    portas[indiceCarro] = 1    
    return indiceCarro

def umaJogada(portas, portaEscolhida, trocaPorta=None):
  print('Portas: {}'.format(portas))
  print('Porta Escolhida: {}'.format(portaEscolhida))
  if trocaPorta:
    return portas[portaEscolhida] == 1
  return portas[portaEscolhida] == 1

def main():
    portas = [0,0,0]
    portaCarro = populaPortas(portas)
    portaRemovida = 0
    portaEscolhida = random.randint(0,2)
    while True:
      portaRemovida = random.randint(0,2)
      if portaRemovida != portaCarro and portaRemovida != portaEscolhida :
        portas.pop(portaRemovida)
        if portaRemovida
        break
    print('Resultado: {}'.format(umaJogada(portas, portaEscolhida)))

if __name__ =="__main__":
  main()

