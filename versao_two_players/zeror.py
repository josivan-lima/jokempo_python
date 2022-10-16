import random


def zeror(jogadas_do_player):
    pesos = [1, 1, 1]
    jogadas_mais_frequentes_player = get_jogadas_mais_frequentes_player(jogadas_do_player)
    for jogada, frequencia in jogadas_mais_frequentes_player.items():
            peso_jogada = funcao_zeror(frequencia, total_jogadas_player(jogadas_do_player))
            if jogada == 1:
                pesos[1] = peso_jogada
            elif jogada == 2:
                pesos[2] = peso_jogada
            elif jogada == 3:
                pesos[0] = peso_jogada
    jogada_otimizada = random.choices([1, 2, 3], weights = pesos)
    return int(jogada_otimizada[0])

def total_jogadas_player(jogadas):
    return len(jogadas)

def funcao_zeror(numero_de_jogadas, total_de_jogadas):
    return numero_de_jogadas/total_de_jogadas * 10 

def gerar_frequencia_de_jogadas(jogadas):
    return [
            contar_vezes_player_escolheu(1, jogadas),
            contar_vezes_player_escolheu(2, jogadas),
            contar_vezes_player_escolheu(3, jogadas),
        ]

def get_jogadas_mais_frequentes_player(jogadas):
    frequencia_jogadas = gerar_frequencia_de_jogadas(jogadas)
    maior_frequencia = max(frequencia_jogadas)
    jogadas_mais_frequentes = {}
    for jogada, frequencia in enumerate(frequencia_jogadas, 1):
        if frequencia == maior_frequencia:
            jogadas_mais_frequentes[jogada] = frequencia
    return jogadas_mais_frequentes

def contar_vezes_player_escolheu(jogada, jogadas):
    return jogadas.count(jogada)