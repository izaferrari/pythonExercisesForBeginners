import random
while True:
    numeros = [1, 2, 3, 4, 5, 6]
    pergunta = int(input("escolha um numero de 1 ate 6: "))
    escolhaCorreta = random.choice(numeros)
    if pergunta == escolhaCorreta:
        print('PARABENS VOCE ACERTOU!!!')
    else:
        print("tente novamente.")