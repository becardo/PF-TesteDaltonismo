from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

import webbrowser 

class Documento():
    def relatorio_usuario(self):
        webbrowser.open("ResultadoTeste.pdf")
        
    def gerar_relatorio_usuario(self):
        self.c = canvas.Canvas("ResultadoTeste.pdf")
        
        self.variaveis()
