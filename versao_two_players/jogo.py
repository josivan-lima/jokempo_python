from machine import Machine
from player import Player

def jogo() -> None:

    formato_jogo = player_decide_formato_do_jogo()
    if formato_jogo == 2:
        jogo_two_players()
    else:
        jogo_one_player()
    
def jogo_one_player() -> None:
    p1 = Player('Player 1')
    machine = Machine()

    jogada_player = 0
    while True:
        jogada_player = p1.jogar()
        machine.memorizar_jogada_do_player(jogada_player)
        jogada_machine = machine.jogar()
        mostrar_resultado(jogada_player, jogada_machine)

def jogo_two_players() -> None:
    p1 = Player('Player 1')
    p2 = Player('Player 2')

    jogada_player1 = 0
    while True:
        jogada_player1 = p1.jogar()
        jogada_player2 = p2.jogar()
        mostrar_resultado(jogada_player1, jogada_player2, two_players=True)


def player_decide_formato_do_jogo() -> int:
    decisao_jogador = escolher_formato_jogo()
    return validar_formato_do_jogo(decisao_jogador)


def escolher_formato_jogo() -> str:
    return input('Decidir formato do jogo (1-One Player, 2-Two Players): ')


def validar_formato_do_jogo(formato: str) -> int:
    while formato_de_jogo_nao_eh_valido(formato):
        print('\nFormato não disponível!!!\n')
        formato = escolher_formato_jogo()
    return int(formato)


def formato_de_jogo_nao_eh_valido(formato:str) -> bool:
    formatos_validos = ['1', '2']
    return not formato.strip() in formatos_validos


def mostrar_resultado(jogada_player1: int, jogada_player2: int, two_players: bool=False):
    dict_jokempo = {
        1: 'Pedra',
        2: 'Papel',
        3: 'Tesoura'
    }
    jogada_que_ganha_ganha = {
        3:1,
        1:2,
        2:3
    }
    if two_players:
        mensagem = {
            'vitoria': f'Player 1:{dict_jokempo[jogada_player1]}\n'
                    f'Player 2:{dict_jokempo[jogada_player2]}\n'
                    'Player 1 Ganhou\n',
            'derrota': f'Player 1:{dict_jokempo[jogada_player1]}\n'
                    f'Player 2:{dict_jokempo[jogada_player2]}\n'
                    'Player 2 Ganhou\n',
            'empate': f'Player 1:{dict_jokempo[jogada_player1]}\n'
                    f'Player 2:{dict_jokempo[jogada_player2]}\n'
                    'Vocês Empataram\n',
        }
    else:
        mensagem = {
            'vitoria': f'Player:{dict_jokempo[jogada_player1]}\n'
                    f'Machine:{dict_jokempo[jogada_player2]}\n'
                    'Você Ganhou\n',
            'derrota': f'Player:{dict_jokempo[jogada_player1]}\n'
                    f'Machine:{dict_jokempo[jogada_player2]}\n'
                    'Você Perdeu\n',
            'empate': f'Player:{dict_jokempo[jogada_player1]}\n'
                    f'Machine:{dict_jokempo[jogada_player2]}\n'
                    'Você Empatou\n',
        }

    if jogada_player1 == jogada_player2:
        print(mensagem['empate'])
    elif jogada_player1 == jogada_que_ganha_ganha[jogada_player2]:
        print(mensagem['vitoria'])
    elif jogada_player2 == jogada_que_ganha_ganha[jogada_player1]:
        print(mensagem['derrota'])


if __name__ == "__main__":
    jogo()
