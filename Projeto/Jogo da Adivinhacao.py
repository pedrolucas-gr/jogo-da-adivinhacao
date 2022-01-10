import random
print('====================== \033[35mBEM-VINDO AO JOGO DA ADIVINHAÇÃO\033[m ======================')
print('Tente adivinhar o número entre 0 e 10 que eu estou pensando')
computador = random.randint(0, 10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é a sua tentativa? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('\033[32mVocê venceu, PARABÉNS\033[m')
print('Foram necessárias \033[37m{}\033[m tentativas para me vencer '.format(palpites))
