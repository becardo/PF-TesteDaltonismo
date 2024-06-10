from abc import ABC, abstractmethod
from tkinter import *

class TesteDaltonismo(ABC):
    def __init__(self):
        super().__init__()
        self.janela_teste = Tk()
        self.setup_janela()
        
    def setup_janela(self):
        self.janela_teste.title("Teste de Daltonismo")
        self.janela_teste.geometry("800x600")
        self.janela_teste.configure(background= '#F0F8FF')
        
    @abstractmethod
    def iniciar_teste(self):
        pass
