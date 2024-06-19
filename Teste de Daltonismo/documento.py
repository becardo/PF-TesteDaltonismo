import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime
import webbrowser

class Documento():
    # Função para formatar a data de nascimento
    # Tentamos formatar a data de nascimento para o formato dd/mm/aaaa para que a mesma fosse exibida corretamente no PDF. Devido algum erro ela não apareceu e decidimos retirar a informação data de nascimento do PDF, mas deixamos a lógica pensada aqui.
    def formatar_data(data_nascimento):
        try:
            return datetime.strptime(data_nascimento, '%Y-%m-%d').strftime('%d/%m/%Y')
        except ValueError:
            return data_nascimento  
    
    def gerar_pdf(dados_usuario):
        '''
        Aqui é gerado o PDF com os dados do último usuário adicionado ao banco de dados.
        '''
        nome = dados_usuario['_nome_var']
        pdf_file = f"Resultado_{nome}.pdf"
    
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        elements = []
    
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        title_style.fontSize = 20
        title_style.alignment = 1  # Centralizar o texto
    
        normal_style = styles['Normal']
        normal_style.fontSize = 12
    
        elements.append(Paragraph("Resultado do Teste de Daltonismo", title_style))
        elements.append(Spacer(1, 0.5 * inch))
    
        user_info = [
            f"Nome: {dados_usuario['_nome_var']} {dados_usuario['_sobrenome_var']}",
            f"CPF: {dados_usuario['__cpf_var']}",
            f"Telefone: {dados_usuario['_tel_var']}",
            f"E-mail: {dados_usuario['__email_var']}"
        ]
    
        for info in user_info:
            elements.append(Paragraph(info, normal_style))
            elements.append(Spacer(1, 0.2 * inch))
    
        # Adiciona espaço extra entre E-mail e Resultado
        elements.append(Spacer(1, 0.4 * inch))
    
        additional_info = [
            f"Resultado: {dados_usuario['diagnostico']}",
            "Este resultado é apenas um PROGNÓSTICO, e não exclui a necessidade de consulta com um profissional oftalmologista.",
            "Caso seu resultado tenha sido Protanopia, Deuteranopia ou Tritanopia, procure um médico e leve estes resultados para avaliação profissional."
        ]
    
        for info in additional_info:
            elements.append(Paragraph(info, normal_style))
            elements.append(Spacer(1, 0.2 * inch))
    
        doc.build(elements)
    
        webbrowser.open(pdf_file)
    
    conn = sqlite3.connect('pacientes.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM pacientes ORDER BY id DESC LIMIT 1')
    ultimo_usuario = cursor.fetchone()
    
    conn.close()
    
    if ultimo_usuario:
        colunas = ['id', '_nome_var','_sobrenome_var', 'diagnostico', '_tel_var', '__email_var', '__cpf_var','diagnostico']
        dados_usuario = dict(zip(colunas, ultimo_usuario))
    
        print("Dados do usuário recuperados:", dados_usuario)
        gerar_pdf(dados_usuario)
        
    else:
        print("Nenhum usuário encontrado no banco de dados.")

Documento()
