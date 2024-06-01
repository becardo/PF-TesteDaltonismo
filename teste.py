import tkinter as tk
from usuario import Usuario
from ishihara import Ishihara
from documento import Documento

class Teste:
    def __init__(self, usuario, laminas):
        self.usuario = usuario
        self.laminas = laminas
        self.respostas = []

    def iniciar(self):
        # Lógica para iniciar o teste, iterar sobre as lâminas e registrar respostas
        pass

    def analisar_resultados(self):
        # Lógica para analisar os resultados e determinar o tipo de daltonismo
        pass

        doc = Documento(self.usuario, self.respostas)
        doc.gerar_pdf()

        #olha estou bem decepcionada com o github 
        # coisa chata isso
        #não chore Bibi