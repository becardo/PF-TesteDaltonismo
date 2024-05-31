from fpdf import FPDF

class Documento:
    def __init__(self, usuario, respostas):
        self.usuario = usuario
        self.respostas = respostas

    def gerar_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt="Resultado do Teste de Daltonismo", ln=True, align="C")
        pdf.cell(200, 10, txt=str(self.usuario), ln=True, align="L")

        for idx, resposta in enumerate(self.respostas, start=1):
            pdf.cell(200, 10, txt=f"Lâmina {idx}: {resposta}", ln=True, align="L")

        # Salvar o PDF
        pdf.output("resultado.pdf")