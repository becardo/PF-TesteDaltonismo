from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from Usuario import Usuario
import webbrowser 

class Documento(Usuario):
    def __init__(self,usuario):
        self.usuario = Usuario()
        
    def relatorio_usuario(self):
        webbrowser.open("ResultadoTeste.pdf")
        
    def gerar_relatorio_pdf(self):
        self.canvas = canvas.Canvas("ResultadoTeste.pdf")
        
        self.usuario.variaveis()
        
        self.canvas.setFont("Helvetica-Bold", 24)
        self.canvas.drawString(200, 790, 'Resultados')

        ### essas identações eu vou mudar dps q estiver conseguindo vizualizar o pdf
        self.canvas.setFont("Helvetica-Bold", 24)
        self.canvas.drawString(50, 790, 'Nome: ')
        self.canvas.drawString(50, 770, 'Data de Nascimento: ')
        self.canvas.drawString(50, 750, 'Telefone/ Celular: ')
        self.canvas.drawString(50, 730, 'Rua: ')
        self.canvas.drawString(50, 710, 'N°: ')
        self.canvas.drawString(50, 690, 'CEP: ')
        self.canvas.drawString(50, 670, 'Bairro: ')
        self.canvas.drawString(50, 650, 'Cidade: ')
        
        self.canvas.setFont("Helvetica-Bold", 24)
        self.canvas.drawString(150, 790, self.nome + self.sobrenome)
        self.canvas.drawString(150, 770, self.data)
        self.canvas.drawString(150, 750, self.tel)
        self.canvas.drawString(150, 730, self.rua)
        self.canvas.drawString(150, 710, self.numero)
        self.canvas.drawString(150, 690, self.cep)
        self.canvas.drawString(150, 670, self.bairro)
        self.canvas.drawString(150, 650, self.cidade)
        
        
        self.canvas.showPage()
        self.canvas.save()
        self.relatorio_usuario()
        
Documento()
