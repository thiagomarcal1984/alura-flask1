class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

    @staticmethod
    def todos():
        usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
        usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
        usuario3 = Usuario("Guilherme Louro", "Cake", "pythonehvida")
        return {
            usuario1.nickname : usuario1, 
            usuario2.nickname : usuario2, 
            usuario3.nickname : usuario3, 
        }
