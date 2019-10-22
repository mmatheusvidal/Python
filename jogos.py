import forca
import adivinhacao

print('##############################')
print('######### Seus Jogos #########')
print('##############################')

print('(1) Forca (2) Adivinhação')
jogo = int(input("qual jogo você quer jogar? "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar_adivinhacao()