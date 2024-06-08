from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import webbrowser 
#from Usuario import Usuario
from tkinter import Tk
#from Ishihara import Ishihara

class Documento(Usuario):
    def __init__(self, usuario, respostas, placas):
        self.usuario = usuario
        self.respostas = respostas
        self.placas = placas
        self.gerar_relatorio_pdf()
        
    def relatorio_usuario(self):
        webbrowser.open("ResultadoTeste.pdf")
        
    def gerar_relatorio_pdf(self):
        self.canvas = canvas.Canvas("ResultadoTeste.pdf", pagesize=letter)
        
        self.canvas.setFont("Helvetica-Bold", 24)
        self.canvas.drawString(200, 790, 'Resultados')

        # Aqui você precisa corrigir a obtenção dos valores do usuário
        self.nome = self.usuario.nome_var.get()
        self.sobrenome = self.usuario.sobrenome_var.get()
        self.data_nasc = self.usuario.data_var.get()
        self.tel = self.usuario.entry_tel.get()  # telefone não está como StringVar
        self.rua = self.usuario.rua_var.get()
        self.numero = self.usuario.numero_var.get()
        self.cep = self.usuario.entry_cep.get()  # CEP não está como StringVar
        self.bairro = self.usuario.bairro_var.get()
        self.cidade = self.usuario.cidade_var.get()

        self.canvas.setFont("Helvetica-Bold", 24)
        self.canvas.drawString(150, 790, self.nome + " " + self.sobrenome)
        self.canvas.drawString(150, 770, self.data_nasc)
        self.canvas.drawString(150, 750, self.tel)
        self.canvas.drawString(150, 730, self.rua)
        self.canvas.drawString(150, 710, self.numero)
        self.canvas.drawString(150, 690, self.cep)
        self.canvas.drawString(150, 670, self.bairro)
        self.canvas.drawString(150, 650, self.cidade)
        
        self.canvas.showPage()
        self.canvas.save()
        self.relatorio_usuario()


# Cria uma instância de Usuario
#usuario_teste = Usuario()

# Chama a classe Ishihara e passa a instância de Usuario
#Ishihara(usuario_teste)
