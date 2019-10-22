import random

def jogar_adivinhacao():

    print('###########################################')
    print('######### Meu Jogo de Adivinhação #########')
    print('###########################################')

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('Escolha a dificuldade: (1) Fácil (2) Médio (3) Díficl')
    nivel = int(input('Escolha o nivel de dificuldade: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for tentativa in range(1, total_tentativas + 1):
        print('Tentativa: {} de {}'.format(tentativa, total_tentativas))

        chute_str = input('Digite um numero entre 1 e 100: ')
        print('Você digitou ', chute_str)

        chute = int(chute_str)
        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Voce Acertou! e fez {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou, seu chute foi maior!')
            elif(menor):
                print('Voce Errou, seu chute foi menor')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
    print('Fim do jogo')
    print(numero_secreto)

if(__name__== "__main__"):
    jogar_adivinhacao()