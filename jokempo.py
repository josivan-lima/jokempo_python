import math
import random

player = int(input('Escolha uma opção (1, 2, 3 ou 4)\n1 - Pedra\n2 - Papel\n\
3 - Tesoura\n4 - Sair\n'))

while player >= 5 or player <= 0:
    print ('\nValor fora das opções!!!\n')
    player = int(input('Escolha uma opção (1, 2, 3 ou 4)\n1 - Pedra\n2 - Papel\n\
3 - Tesoura\n4 - Sair\n'))

machine = random.randint(1,3)

dict_jokempo = {1:'Pedra', 2:'Papel', 3:'Tesoura'}

count = 0
moves_player =[]
rep = []
moves_rep = []
pesos = [1, 1, 1]
while player !=4:
    count += 1
    moves_player.append(player)
    if player == machine:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê empatou!\n')
    elif player == 1 and machine == 3:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê ganhou!\n')
    elif player == 2 and machine == 1:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê ganhou!\n')
    elif player == 3 and machine == 2:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê ganhou!\n')
    elif player == 3 and machine == 1:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê perdeu!\n')
    elif player == 1 and machine == 2:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê perdeu!\n')
    elif player == 2 and machine == 3:
        print(f'Sua jogada -> {dict_jokempo[player]}\nJogada da máquina -> \
{dict_jokempo[machine]}\nVocê perdeu!\n')
    player = int(input('Escolha uma opção (1, 2, 3 ou 4)\n1 - Pedra\n2 - Papel\n\
3 - Tesoura\n4 - Sair\n'))
    if player >= 5 or player <= 0:
        print ('\nValor fora das opções!!!\n')
        player = int(input('Escolha uma opção (1, 2, 3 ou 4)\n1 - Pedra\n2 - Papel\n\
3 - Tesoura\n4 - Sair\n'))
    if count >= 5:
        #print('JOGADAS ->', moves_player)
        for x in moves_player:
            rep.append(moves_player.count(x))
        #print (rep)

        moves_max = max(rep)
        for j in range(len(moves_player)):
            if moves_max == rep[j]:
                moves_rep.append([moves_player[j], rep[j]])
        #print (moves_rep)
                                 
        for i in moves_rep: #Aplicação do ZeroR
            if i[0] == 1:
                pesos[0] = i[1]/len(moves_player)*10
            elif i[0] == 2:
                pesos[1] = i[1]/len(moves_player)*10
            elif i[0] == 3:
                pesos[2] = i[1]/len(moves_player)*10
        #print (pesos)
        machine = random.choices([1, 2, 3], weights = pesos)
        machine = int(machine[0])
        if player >= 5 or player <= 0:
            print ('\nValor fora das opções!!!\n')

    rep = []
    moves_rep = []
    pesos = [1, 1, 1]
    
        
if player == 4:
    print('Até Logo!')

