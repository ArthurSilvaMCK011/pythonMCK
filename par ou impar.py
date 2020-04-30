#JOGO PAR OU IMPAR

import random

resposta= int(input("Vamos jogar par ou impar? Digite 1 para sim e 0 para não: "))
if resposta == 1:
    print("Vamos la!")
    npessoa= int(input("Digite um número de 1 a 10: "))
    if npessoa > 10 :
        print(" Vishhhh, número invalido, tenta denovo!")
    elif npessoa <= 10 :
        escolha= int(input("Digite zero para par e um para impar: "))
        maq= (random.randrange(0, 11))
        print("O número escolhido por você for: ", npessoa)
        print("O numero escolhido por mim foi: ", maq)
        resultado= npessoa + maq
        if resultado % 2 == 0 and escolha == 0 :
            print("Você escolheu par e a soma dos números deu par. Parabéns você me venceu!")
        elif resultado % 2 == 0 and escolha == 1 :
            print("Você escolheu impar e a soma dos números deu par. Eu venci dessa vez!")
        elif resultado % 2 == 1 and escolha == 0 :
            print( "Você escolheu par e a soma dos números deu impar. Eu venci dessa vez!")
        elif resultado % 2 == 1 and escolha == 1 :
            print("Você escolheu impar e a soma dos números deu impar. Parabéns você me venceu!")
elif resposta == 0 :
    print("Poxa! tudo bem, podemos jogar mais tarde.")
    
    
        
