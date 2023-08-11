import random

# Gerar um numero aleatorio entre 1 e 100
num_aleatorio = random.randint(1, 100)
tentativas = 0
game = True
win = False

# Loop que solicita o paplpite
while True:

    while tentativas <= 10:
        palpite = int(input("Tente adivinhar o numero entre 1 e 100:"))
        tentativas +=1

        #verifica se o numero é igual
        if num_aleatorio > palpite:
            print('O numero é maior')
        elif num_aleatorio < palpite:
            print('O numero é menor')
        else:
            # Caso acerte Define a variaél win commo verdadeiro
            print('Parabéns, você acertou! em ', tentativas, " Tentativas") 
            win = True
            break
    
    if win:
        again = int(input("Gostaria de Jogar novamente ? 1 - Sim e 2 - Não   "))
        if again == 2:
            break
    else:
        print("Infelizmente você excedeu o numero de tentativas: ")
        again = int(input("Gostaria de Jogar novamente ? 1 - Sim e 2 - Não   "))
        if again == 2:
            break
    
    tentativas = 0