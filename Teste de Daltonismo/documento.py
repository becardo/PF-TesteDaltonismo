import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Função para formatar a data de nascimento
def formatar_data(data_nascimento):
    try:
        return datetime.strptime(data_nascimento, '%Y-%m-%d').strftime('%d/%m/%Y')
    except ValueError:
        return data_nascimento  # Retornar a data original se não puder ser formatada

# Função para gerar PDF com os dados do último usuário adicionado
def gerar_pdf(dados_usuario):
    c = canvas.Canvas("usuario.pdf", pagesize=letter)
    width, height = letter

    # Adicionar texto ao PDF
    c.drawString(100, height - 120, f"Nome: {dados_usuario['_nome_var']}")
    c.drawString(100, height - 140, f"Sobrenome: {dados_usuario['_sobrenome_var']}")
    c.drawString(100, height - 200, f"E-mail: {dados_usuario['__email_var']}")
    c.drawString(100, height - 180, f"Data de Nascimento: {dados_usuario['_data_var']}")
    c.drawString(100, height - 160, f"CPF: {dados_usuario['__cpf_var']}")
    c.drawString(100, height - 220, f"Telefone: {dados_usuario['_tel_var']}")
    c.drawString(100, height - 240, f"Diagnóstico: {dados_usuario['diagnostico']}")

    # Salvar o PDF
    c.save()

# Conectar ao banco de dados
conn = sqlite3.connect('pacientes.db')
cursor = conn.cursor()

# Pegar o último ID adicionado
cursor.execute('SELECT * FROM pacientes ORDER BY id DESC LIMIT 1')
ultimo_usuario = cursor.fetchone()

# Fechar a conexão
conn.close()

# Transformar o resultado em um dicionário
colunas = ['id','_nome_var', '_sobrenome_var', '_data_var', '_tel_var', '__email_var',  '__cpf_var', 'diagnostico']
dados_usuario = dict(zip(colunas, ultimo_usuario))
# Formatar a data de nascimento
dados_usuario['_data_var'] = formatar_data(dados_usuario['_data_var'])
# Gerar o PDF com os dados do último usuário adicionado
gerar_pdf(dados_usuario)
