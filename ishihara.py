class Ishihara:
    def __init__(self, imagem, respostas):
        self.imagem = imagem
        self.respostas = respostas  # {resposta: peso}

    def mostrar_imagem(self):
        # Lógica para mostrar a imagem usando uma interface gráfica (por exemplo, tkinter)
        pass

    def obter_resposta(self, resposta):
        return self.respostas.get(resposta, 0)