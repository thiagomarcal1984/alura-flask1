class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
    @staticmethod
    def todos():
        jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
        jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
        jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
        return [ jogo1, jogo2, jogo3]
