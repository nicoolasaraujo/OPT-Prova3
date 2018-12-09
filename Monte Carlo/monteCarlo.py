import random
import math

NE = 10000000

def defineCoordenadas():
    y = random.randrange(0, 100050)
    x = random.randrange(0, 100050)
    return x,y

def executaMonteCarlo():
    x,y = defineCoordenadas()
    z = math.sin(x/50000) + math.cos(y/30000)
    return z

def main():
    '''Execução Monte Carlo Simples'''
    exp = [executaMonteCarlo() for _ in range(NE)]
    print(str(max(exp)))



if __name__ =="__main__":
  main()
