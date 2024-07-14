import random

def adivinhação(): #Função para adivinhação

    numero_secreto = random.randint(1, 10)
    tentativas = 0
    max_tenteativas = 5

    print('\nJogo de adivinhação!')

    while tentativas < max_tenteativas:

        papite = int(input('\nAdivinhe um numero de 1 a 10: '))

        if numero_secreto == papite:
            print('\nParábens, você acertou o número!') 
            break
        elif papite > numero_secreto:
            print('\nTente um número menor!')
        else:
            print('\nTente um número maior!')

        tentativas += papite

        if tentativas == max_tenteativas:
            print('\nTentativas esgotadas, tente novamente mais tarde!')

adivinhação()
