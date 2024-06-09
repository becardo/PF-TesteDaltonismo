from abc import ABC, abstractmethod
from tkinter import *

class TesteDaltonismo(ABC):
    def __init__(self):
        super().__init__()
        self._janela_teste = Tk()
        self._setup_janela()
        
    def _setup_janela(self):
        self._janela_teste.title("Teste de Daltonismo")
        self._janela_teste.geometry("800x600")
        self._janela_teste.configure(background= '#F0F8FF')
        
    @abstractmethod
    def iniciar_teste(self):
        pass
