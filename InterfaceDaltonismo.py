from abc import ABC, abstractmethod

class TesteDaltonismo(ABC):
    
    @abstractmethod
    def iniciar_teste(self) -> None:
        pass

    def habilitar_botao(self, botao: str, estado: str) -> None:
        """
        Habilita ou desabilita um botão baseado no nome do botão e no estado desejado.
        :param botao: Nome do botão a ser modificado ('bt_proxima' ou 'bt_gerar_pdf').
        :param estado: Estado desejado ('normal' ou 'disabled').
        """
        if hasattr(self, botao):
            getattr(self, botao).config(state=estado)
        else:
            raise ValueError(f"Botão desconhecido: {botao}")
