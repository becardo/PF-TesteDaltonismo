class Usuario:
    def __init__(self, nome, idade, genero, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero}, Data de Nascimento: {self.data_nascimento}"