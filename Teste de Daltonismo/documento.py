import pandas as pd
import pdfkit
from usuario import Usuario
from ishihara import Ishihara

class Documento(Usuario, Ishihara):
    def __init__(self) -> None:
        super().__init__()

    def gerar_relatorio_pdf(self):
        # Obter os dados do usuário do objeto Usuario
        dados_usuario = {
            'Nome': [self._nome_var.get()],
            'Sobrenome': [self._sobrenome_var.get()],
            'Data de Nascimento': [self._data_var.get()],
            'Telefone': [self._tel_var.get()],
            'E-mail': [self.__email_var.get()],
            'CPF': [self.__cpf_var.get()]
        }
        df_usuario = pd.DataFrame(dados_usuario)

        # Obter os resultados do teste de Ishihara do objeto Ishihara
        dados_teste = []
        for i, resposta in enumerate(self.resp_t):
            dados_teste.append({
                'Placa': i + 1,
                'Resposta': resposta,
                'Esperado': self.ishihara_placas[i]['expected']['normal']
            })
        df_teste = pd.DataFrame(dados_teste)

        # Salvar os DataFrames como arquivos HTML
        df_usuario.to_html('usuario.html', index=False)
        df_teste.to_html('teste.html', index=False)

        # Gerar o arquivo PDF a partir do HTML
        with open('relatorio.html', 'w') as f:
            f.write('<h1>Resultados do Teste de Daltonismo</h1>')
            f.write('<h2>Dados do Usuário</h2>')
            with open('usuario.html', 'r') as usuario_html:
                f.write(usuario_html.read())
            f.write('<h2>Resultados do Teste</h2>')
            with open('teste.html', 'r') as teste_html:
                f.write(teste_html.read())

        pdfkit.from_file('relatorio.html', 'ResultadoTeste.pdf')

# Inicializa a classe GerarPDF
Documento()
