import math
import random


def mostrar_resultado(player:int, machine:int) -> None:
    resultado = {
    'empate': f'Sua jogada -> {dict_jokempo[player]}\n'
              f'Jogada da máquina -> {dict_jokempo[machine]}\n'
              'Você empatou!\n',
    'vitoria':f'Sua jogada -> {dict_jokempo[player]}\n'
              f'Jogada da máquina -> {dict_jokempo[machine]}\n'
              'Você ganhou!\n',
    'derrota':f'Sua jogada -> {dict_jokempo[player]}\n'
              f'Jogada da máquina -> {dict_jokempo[machine]}\n'
              'Você perdeu!\n'
              }
    
    if player == machine:
        print(resultado['empate'])
    elif player == 1 and machine == 3:
        print(resultado['vitoria'])
    elif player == 2 and machine == 1:
        print(resultado['vitoria'])
    elif player == 3 and machine == 2:
        print(resultado['vitoria'])
    elif player == 3 and machine == 1:
        print(resultado['derrota'])
    elif player == 1 and machine == 2:
        print(resultado['derrota'])
    elif player == 2 and machine == 3:
        print(resultado['derrota'])


def escolha_do_jogador_nao_for_valida(escolha: int) -> bool:
    escolhas_validas = [1,2,3,4] 
    return escolha not in escolhas_validas


player = int(input('Escolha uma opção (1, 2, 3 ou 4)\n1 - Pedra\n2 - Papel\n\
3 - Tesoura\n4 - Sair\n'))

while escolha_do_jogador_nao_for_valida(player):
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
    mostrar_resultado(player, machine)
    print(machine)
    player = int(input('Escolha uma opção (1, 2, 3 ou 4)\n1 - Pedra\n2 - Papel\n\
3 - Tesoura\n4 - Sair\n'))
    while escolha_do_jogador_nao_for_valida(player):
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
                pesos[1] = i[1]/len(moves_player)*10
            elif i[0] == 2:
                pesos[2] = i[1]/len(moves_player)*10
            elif i[0] == 3:
                pesos[0] = i[1]/len(moves_player)*10
        #print (pesos)
        machine = random.choices([1, 2, 3], weights = pesos)
        machine = int(machine[0])

    rep = []
    moves_rep = []
    pesos = [1, 1, 1]
    
        
if player == 4:
    print('Até Logo!')

