import tkinter as tk
import subprocess
import sys
#from InterfaceDaltonismo import TesteDaltonismo
#from usuario import Usuario
#from ishihara import Ishihara

class Resultado():
    def __init__(self) -> None:
        self.janela = tk.Tk()
        self.iniciar_teste()
        self.janela.mainloop() 

    def iniciar_teste(self) -> None:
      '''
      Aqui estão todas as especificações gráficas de tela inicial do usuário:
      '''
      self.janela.title("Teste de Daltonismo")
      self.janela.geometry("800x600")
      self.janela.configure(background= '#F0F8FF')

      self.frame = tk.Frame(self.janela, bd=6, bg='#F0F8FF',
                         highlightbackground='#87CEEB', highlightthickness=3)
      self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

      self.label_cabecalho = tk.Label(
          self.frame, text="Resultado do teste: ", bg='#F0F8FF', fg='black', font=('arial', 12))
      self.label_cabecalho.place(relx=0.01, rely=0.01)

      self.bt_gerar_pdf = tk.Button(self.frame, text="Gerar PDF",bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 12), command= self.gerar_pdf)
      self.bt_gerar_pdf.place(relx= 0.4, rely=0.9)

    def gerar_pdf(self)-> None:
      '''
      Este método executa comando sys.executable, chama o arquivo documento.py para gerar o PDF com os resultados.
      '''
      subprocess.Popen([sys.executable, 'documento.py'])

Resultado()
