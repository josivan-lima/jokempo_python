from getpass import getpass


class Player:

    def __init__(self, nome) -> None:
        self.nome = nome
    
    def jogar(self) -> int:
        jogada = self.escolhe_jogada()
        jogada_validada = self.validar_jogada(jogada)
        if jogada_validada == 4:
            self.sair_do_jogo()
        return jogada_validada
    
    def escolhe_jogada(self) -> str:
        return getpass(f'{self.nome} escolha sua jogada (1-Pedra, 2-Papel, 3-Tesoura ou 4-Sair): ')
    
    def validar_jogada(self, jogada: str) -> int:
        while self.jogada_nao_eh_valida(jogada):
            print('\nValor fora das opções!!!\n')
            jogada = self.escolhe_jogada()
        return int(jogada)

    def jogada_nao_eh_valida(self, jogada: str) -> bool:
        jogadas_validas = ['1', '2', '3', '4']
        return not jogada.strip() in jogadas_validas
    
    def sair_do_jogo(self) -> None:
        print('Até Logo!')
        exit()