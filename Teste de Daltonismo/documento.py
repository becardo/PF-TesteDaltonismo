import pandas as pd
import pdfkit
import webbrowser
from usuario import Usuario
from tkinter import tk
from ishihara import Ishihara

class Documento(Usuario, Ishihara):
    def __init__(self, usuario: list, respostas: list, placas: list) -> None:
        self.usuario = usuario
        self.respostas = respostas
        self.placas = placas
        self.gerar_relatorio_pdf()

    def relatorio_usuario(self) -> None:
        webbrowser.open("ResultadoTeste.pdf")

    def gerar_relatorio_pdf(self) -> None:

        self.nome = self.usuario[0].nome_var.get()
        self.sobrenome = self.usuario[0].sobrenome_var.get()
        self.data_nasc = self.usuario[0].data_var.get()
        self.tel = self.usuario[0].entry_tel.get() 
        self.email = self.usuario[0].rua_email.get()
        self.cpf = self.usuario[0].entry_cpf.get() 

        '''
        Criação do DataFrame com os dados do usuário
        '''
        dados_usuario = {
            'Nome': [self.nome],
            'Sobrenome': [self.sobrenome],
            'Data de Nascimento': [self.data_nasc],
            'Telefone': [self.tel],
            'E-mail': [self.email],
            'CPF': [self.cpf]
        }
        df_usuario = pd.DataFrame(dados_usuario)

        '''
        Criação do DataFrame com os resultados do teste
        '''
        dados_teste = []
        for i, resposta in enumerate(self.respostas):
            dados_teste.append({
                'Placa': i + 1,
                'Resposta': resposta,
                'Esperado': self.placas[i]['expected']
            })
        df_teste = pd.DataFrame(dados_teste)

        '''
        Salvando os DataFrames como arquivos HTML
        '''
        df_usuario.to_html('usuario.html', index=False)
        df_teste.to_html('teste.html', index=False)

        '''
        Gerando o arquivo PDF a partir do HTML
        '''
        with open('relatorio.html', 'w') as f:
            f.write('<h1>Resultados do Teste de Daltonismo</h1>')
            f.write('<h2>Dados do Usuário</h2>')
            with open('usuario.html', 'r') as usuario_html:
                f.write(usuario_html.read())
            f.write('<h2>Resultados do Teste</h2>')
            with open('teste.html', 'r') as teste_html:
                f.write(teste_html.read())

        '''
        Convertendo HTML para PDF
        '''
        pdfkit.from_file('relatorio.html', 'ResultadoTeste.pdf')

        self.relatorio_usuario()

if __name__ == "__main__":
    usuario = Usuario()
    documento = Documento(Usuario)
