def jogar_forca():
    print('#####################################')
    print('######### Meu Jogo de Forca #########')
    print('#####################################')

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_' for a in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input('Qual letra?')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você Ganhou!')
    else:
        print('Você Perdeu!')

    print('Fim do jogo')

if(__name__== '__main__'):
    jogar_forca()
