import math
import random
import typing


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


def zeror(numero_jogadas: int, total_jogadas: int) -> float:
    return numero_jogadas/total_jogadas * 10 


class Machine:

    def __init__(self) -> None:
        self.contador_rodadas : int = 0
        self.jogadas_players : typing.List[str] = []

    def gerar_jogada(self) -> int:
        if self.contador_rodadas < 5:
            return random.randint(1,3)
        else:
            return self.gerar_jogada_com_pesos()
    
    def gerar_jogada_com_pesos(self) -> int:
        pesos = [1, 1, 1]
        jogadas_mais_frequentes = self.jogada_player_mais_frequente()
        for jogada in jogadas_mais_frequentes:
            if jogada == 1:
                pesos[1] = zeror(self.contar_vezes_player_escolheu(1), self.total_jogadas_player())
            elif jogada == 2:
                pesos[2] = zeror(self.contar_vezes_player_escolheu(2), self.total_jogadas_player())
            elif jogada == 3:
                pesos[0] = zeror(self.contar_vezes_player_escolheu(3), self.total_jogadas_player())

        print(f'pesos ->{pesos}')
        escolha_com_pesos = random.choices([1, 2, 3], weights = pesos)
        return int(escolha_com_pesos[0])
        
    def total_jogadas_player(self) -> int:
        return len(self.jogadas_players)

    def contar_vezes_player_escolheu(self, jogada: int) -> int:
        return self.jogadas_players.count(jogada)
    
    def jogada_player_mais_frequente(self) -> typing.List[int]:
        frequencia_jogadas = [
            self.contar_vezes_player_escolheu(1),
            self.contar_vezes_player_escolheu(2),
            self.contar_vezes_player_escolheu(3),
        ]
        maior_frequencia = max(frequencia_jogadas)
        jogadas_mais_frequentes = []
        for jogada, frequencia in enumerate(frequencia_jogadas, 1):
            if frequencia == maior_frequencia:
                jogadas_mais_frequentes.append(jogada)
        print(jogadas_mais_frequentes)
        return jogadas_mais_frequentes


    def guardar_jogada_player(self, jogada: str) -> None:
        self.jogadas_players.append(jogada)
    
    def adicionar_rodada(self) -> None:
        self.contador_rodadas += 1

def jokempo():
    machine = Machine()
    jogada_player = 0
    while jogada_player != 4:
        jogada_player = perguntar_jogada_do_player()
        machine.guardar_jogada_player(jogada_player)
        if jogada_player != 4:
            mostrar_resultado(jogada_player, machine.gerar_jogada())
            machine.adicionar_rodada()
    print('Até Logo!')


if __name__ == '__main__':
    jokempo()