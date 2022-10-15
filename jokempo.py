import math
import random


def mostrar_resultado(player:int, machine:int) -> None:
    dict_jokempo = {1:'Pedra', 2:'Papel', 3:'Tesoura'}
    
    mensagem_de_resultado = {
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
        print(mensagem_de_resultado['empate'])
    elif player == 1 and machine == 3:
        print(mensagem_de_resultado['vitoria'])
    elif player == 2 and machine == 1:
        print(mensagem_de_resultado['vitoria'])
    elif player == 3 and machine == 2:
        print(mensagem_de_resultado['vitoria'])
    elif player == 3 and machine == 1:
        print(mensagem_de_resultado['derrota'])
    elif player == 1 and machine == 2:
        print(mensagem_de_resultado['derrota'])
    elif player == 2 and machine == 3:
        print(mensagem_de_resultado['derrota'])


def escolha_eh_int(escolha: str) -> bool:
    try:
        escolha = int(escolha)
        return True
    except ValueError as e:
        print ('\nValor fora das opções!!!\n')
        return False


def escolha_esta_entre_as_opcoes_validas(escolha: str) -> bool:
    opcoes_validas = ['1','2','3','4']
    return escolha.strip() in opcoes_validas


def escolha_do_jogador_eh_valida(escolha: str) -> bool:
    return escolha_eh_int(escolha) and escolha_esta_entre_as_opcoes_validas(escolha)


def perguntar_jogada_do_player() -> int:
    mensagem_de_escolha = 'Escolha uma opção (1, 2, 3 ou 4)\n'\
                          '1 - Pedra\n'\
                          '2 - Papel\n'\
                          '3 - Tesoura\n'\
                          '4 - Sair\n'
    escolha = input(mensagem_de_escolha)
    while not escolha_do_jogador_eh_valida(escolha):
        print ('\nValor fora das opções!!!\n')
        escolha = input(mensagem_de_escolha)    
    return int(escolha)
    
def jokempo():
    player = perguntar_jogada_do_player()
    machine = random.randint(1,3)

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
        player = perguntar_jogada_do_player()
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
        
    print('Até Logo!')


if __name__ == '__main__':
    jokempo()