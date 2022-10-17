import random

from zeror import zeror


class Machine:

    def __init__(self) -> None:
        self.jogadas_do_player = []
        self.funcao_otimizadora = zeror
    
    @property
    def args_funcao_otimizadora(self):
        return [self.jogadas_do_player]
    
    def jogar(self) -> int:
        if self.numero_de_rodadas() < 5:
            return self.gerar_jogada_aleatoria()
        else:
            return self.gerar_jogada_otimizada()

    def gerar_jogada_aleatoria(self) -> int:
        return random.randint(1,3)
    
    def gerar_jogada_otimizada(self) -> int:
        return self.otimizar_resultado()
    
    def otimizar_resultado(self) -> int:
        return self.funcao_otimizadora(*self.args_funcao_otimizadora)

    def numero_de_rodadas(self) -> int:
        return len(self.jogadas_do_player)        

    def memorizar_jogada_do_player(self, jogada_player: int) -> None:
        self.jogadas_do_player.append(jogada_player)
