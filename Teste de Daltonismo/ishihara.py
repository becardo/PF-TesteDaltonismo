import subprocess
import sys
import argparse
import tkinter as tk
import sqlite3
from tkinter import ttk
from typing import Any, Dict, List
from PIL import Image, ImageTk
from InterfaceDaltonismo import TesteDaltonismo


class Ishihara(TesteDaltonismo):
    def __init__(self) -> None:
        '''
        Utilizando o módulo argparse, é possível passar parâmetros de Usuário para Ishihara. Os parâmetros que foram passados pelo subprocess.Popen no aquivo usuario.py são 'capturados' aqui para serem usados no arquivo ishihara.py.
        '''
        parser = argparse.ArgumentParser(description='Recebe argumentos para Ishihara')
        parser.add_argument('--nome', type=str, required=True, help='nome usuario')
        parser.add_argument('--sobrenome', type=str, required=True, help='sobrenome usuario')
        parser.add_argument('--data', type=str, required=True, help='data de nascimento')
        parser.add_argument('--telefone', type=str, required=True, help='telefone')
        parser.add_argument('--email', type=str, required=True, help='email')
        parser.add_argument('--cpf', type=str, required=True, help='cpf')

        self.dados_usuario = parser.parse_args()

        print(self.dados_usuario)

        '''
        Outros métodos e atributos de Ishihara:
        '''

        self.janela_teste = tk.Tk()
        self.ishihara_placas: List[Dict[str, Any]] = self.carregar_placas()
        self.resp_t: List[str] = []
        self.imagem_atual = 0
        self.iniciar_teste()
        self.janela_teste.mainloop()

    def iniciar_teste(self) -> None:
        '''
        Especificaçãoes da janela 
        '''
        self.janela_teste.title("Teste de Daltonismo")
        self.janela_teste.geometry("800x600")
        self.janela_teste.configure(background= '#F0F8FF')

        self.canvas = tk.Canvas(self.janela_teste, background='#F0F8FF')
        self.scrollbar = tk.Scrollbar(self.janela_teste, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="TFrame")

        self.style = ttk.Style()
        self.style.configure("TFrame", background='#F0F8FF')

        '''        
        Na estrutura abaixo, é associado um evento de configuração á scrollable_frame para que a barra de rolagem acompanhe
        o redimencionamento do Canvas
        '''
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        '''
        Cria uma janela dentro do Canvas, e configura ele para usar a barra de rolagem vetical. Dessa forma, a rolagem acompanha a 
        visualização do Canvas.
        '''
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(background='#F0F8FF', yscrollcommand=self.scrollbar.set)

        '''
        Posicionamento janela Canvas.
        '''
        self.canvas.pack(side="left", fill="both", expand=True, padx=150)
        self.scrollbar.pack(side="right", fill="y")

        '''
        Lista com as placas de Ishihara, opções e respostas esperadas para cada caso. 
        '''
        self.tx_placa = tk.Label(self.scrollable_frame, text="Placa 1")
        self.tx_placa.pack(pady=(10, 0))

        self.tx_imagem = tk.Label(self.scrollable_frame)
        self.tx_imagem.pack(pady=(10, 0))

        self.op_var = tk.StringVar()
        self.op_var.trace('w', self.selecionar_op)

        self.op_menu = ttk.Combobox(self.scrollable_frame, textvariable=self.op_var,state="readonly")
        self.op_menu.pack(pady=(10, 0))

        self.bt_proxima = tk.Button(self.scrollable_frame, text="Próxima",bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 10), command=self.px_imagem, state=tk.DISABLED)
        self.bt_proxima.pack(pady=(10, 0))

        self.tx_resultado = tk.Label(self.janela_teste, text="")
        self.tx_resultado.pack(pady=(10, 0))

        self.bt_finalizar = tk.Button(self.scrollable_frame, text="Gerar PDF", bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 10),command= self.janela_resultado, state=tk.DISABLED)
        self.bt_finalizar.pack(pady=(10, 0))

        self.mostrar_imagem(self.imagem_atual)

    def carregar_placas(self) -> List[Dict[str, Any]]:
        '''
        Neste método, são carregadas as placas de Ishihara, opções e respostas esperadas para cada caso. As placas estão presentes na pasta ishihara, no mesmo repositório que os demais arquivos do projeto.
        '''
        return [
            {"image": "ishihara/Ishihara01.png", "options": ["1", "2", "12", "Nada"], "expected": {"normal": "12", "protanopia": "12", "deuteranopia": "12", "tritanopia": "12"}},
            {"image": "ishihara/Ishihara02.png", "options": ["3", "6", "8","Nada"], "expected": {"normal": "8", "protanopia": "3", "deuteranopia": "3", "tritanopia": "8"}}, 
            {"image": "ishihara/Ishihara03.png", "options": ["3", "5", "6", "Nada"], "expected": {"normal": "6", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "12"}}, 
            {"image": "ishihara/Ishihara04.png", "options": ["10", "29", "70","Nada"], "expected": {"normal": "29", "protanopia": "70","deuteranopia": "70","tritanopia": "29"}},
            {"image": "ishihara/Ishihara05.jpg", "options": ["7", "57", "50","Nada"], "expected": {"normal": "57", "protanopia": "7","deuteranopia": "70","tritanopia": "57"}},
            {"image": "ishihara/Ishihara06.png", "options": ["2", "3", "5","Nada"], "expected": {"normal": "5", "protanopia": "2","deuteranopia": "2","tritanopia": "5"}},
            {"image": "ishihara/Ishihara07.png", "options": ["2", "3", "5","Nada"], "expected":{"normal": "3", "protanopia": "5","deuteranopia": "5","tritanopia": "3"}},
            {"image": "ishihara/Ishihara08.png", "options": ["13", "15", "17","Nada"], "expected":{"normal": "15", "protanopia": "17", "deuteranopia": "17","tritanopia": "15"}},
            {"image": "ishihara/Ishihara09.png", "options": ["11", "21", "74","Nada"], "expected":{"normal": "74", "protanopia": "21", "deuteranopia": "21","tritanopia": "74"}},
            {"image": "ishihara/Ishihara10.jpg", "options": ["0", "2", "Nada","3"], "expected":{"normal": "2", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "2"}},
            {"image": "ishihara/Ishihara11.jpg", "options": ["2", "6", "Nada","3"], "expected":{"normal": "6", "protanopia": "nada", "deuteranopia": "2","tritanopia": "6"}},
            {"image": "ishihara/Ishihara12.jpg", "options": ["31", "97", "Nada","91"], "expected":{"normal": "97", "protanopia": "Nada","deuteranopia": "91","tritanopia": "97"}},
            {"image": "ishihara/Ishihara13.png", "options": ["15", "45", "Nada","5"], "expected":{"normal": "45", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "45"}},
            {"image": "ishihara/Ishihara14.png", "options": ["3", "5", "Nada","0"], "expected":{"normal": "5", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "5"}},
            {"image": "ishihara/Ishihara15.png", "options": ["1", "7", "Nada","2"], "expected":{"normal": "7", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "7"}},
            {"image": "ishihara/Ishihara16.png", "options": ["16", "26", "Nada","6"], "expected":{"normal": "16", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "16"}},
            {"image": "ishihara/Ishihara17.png", "options": ["13", "73", "Nada","10"], "expected":{"normal": "73", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "73"}},
            {"image": "ishihara/Ishihara18.png", "options": ["5", "3", "Nada","Abstrato de cores"], "expected":{"normal": "Abstrato de cores", "protanopia": "Nada","deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara19.jpg", "options": ["1", "2", "Nada","Abstrato de cores"], "expected":{"normal": "Abstrato de cores", "protanopia": "Nada","deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara20.png", "options": ["5", "45", "Nada","Abstrato de cores"], "expected":{"normal": "Abstrato de cores", "protanopia": "Nada","deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara21.jpg", "options": ["13", "73", "Nada","Abstrato de cores"], "expected":{"normal": "Abstrato de cores", "protanopia": "Nada","deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara22.png", "options": ["2", "Nada", "26","20"], "expected":{"normal": "26", "protanopia": "20", "deuteranopia": "2","tritanopia": "26"}},
            {"image": "ishihara/Ishihara23.png", "options": ["2", "4", "42","Nada"], "expected":{"normal": "42", "protanopia": "42", "deuteranopia": "4","tritanopia": "42"}},
            {"image": "ishihara/Ishihara24.jpg", "options": ["3", "5", "35","Nada"], "expected":{"normal": "35", "protanopia": "3", "deuteranopia": "35","tritanopia": "35"}},
            {"image": "ishihara/Ishihara25.jpg", "options": ["6", "9", "96","Nada"], "expected":{"normal": "96", "protanopia": "9", "deuteranopia": "96","tritanopia": "96"}},
            {"image": "ishihara/Ishihara26.png", "options": ["Duas linhas de cores diferentes", "Duas linhas da mesma cor", "Duas linhas", "Uma linha"], "expected":{"normal": "Duas linhas de cores diferentes", "protanopia": "Duas linhas de cores diferentes", "deuteranopia": "Uma linha","tritanopia": "Duas linhas da mesma cor"}},
            {"image": "ishihara/Ishihara27.jpg", "options": ["Uma linha", "Uma linha e bolinhas", "Duas linhas","Nada"], "expected":{"normal": "Duas linhas", "protanopia": "Uma linha", "deuteranopia": "Uma linha e bolinhas","tritanopia": "Uma linha e bolinhas"}},
            {"image": "ishihara/Ishihara28.jpg", "options": ["Uma linha", "Nada", "Abstrato de cores"], "expected":{"normal": "Abstrato de cores", "protanopia": "Nada","deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara29.png", "options": ["Uma linha", "Nada", "Abstrato de cores"], "expected":{"normal": "Abstrato de cores", "protanopia": "Nada","deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara30.png", "options": ["Uma linha", "Um numero", "Nada"], "expected":{"normal": "Uma linha", "protanopia": "Nada", "deuteranopia": "Nada","tritanopia": "Abstrato de cores"}},
            {"image": "ishihara/Ishihara31.jpg", "options": ["Uma linha", "Um numero", "Nada"], "expected":{"normal": "Uma linha", "protanopia": "Nada","deuteranopia": "Uma linha","tritanopia": "Uma linha"}},
            {"image": "ishihara/Ishihara32.png", "options": ["Uma linha", "Um numero", "nada"], "expected":{"normal": "Uma linha", "protanopia": "Nada" , "deuteranopia": "Nada","tritanopia": "Uma linha"}},
            {"image": "ishihara/Ishihara33.jpeg", "options": ["Uma linha", "Um numero", "Nada"], "expected":{"normal": "Uma linha", "protanopia": "Nada" , "deuteranopia": "Nada","tritanopia": "Uma linha"}},
            {"image": "ishihara/Ishihara35.png", "options": ["Nada", "Dois traços", "Uma linha"], "expected":{"normal": "Uma linha", "protanopia": "Nada" , "deuteranopia": "Dois traços","tritanopia": "Uma linha"}},
            {"image": "ishihara/Ishihara36.jpeg", "options": ["Uma linha", "Nada", "Um numero"], "expected":{"normal": "Uma linha", "protanopia": "Nada" , "deuteranopia": "Uma linha","tritanopia": "Uma linha"}},
            {"image": "ishihara/Ishihara37.png", "options": ["Uma curva", "Nada", "Uma linha"], "expected":{"normal": "Uma linha", "protanopia": "Uma curva" , "deuteranopia": "Nada","tritanopia": "Uma linha"}},
            {"image": "ishihara/Ishihara38.png", "options": ["Uma_linha","Nada","Um_numero"],"expected": {"normal": "Uma_linha", "protanopia": "Uma_linha", "deuteranopia":"Uma_linha","tritanopia":"Uma_linha"}},
        ]

    def mostrar_imagem(self, index: int) -> None:
        '''
        Este método é responsável por mostrar a imagem correspondente ao índice fornecido. Ele chama o método mostrar_resultados para computar e analisar a resposta do usuário. O método habilitar_botao é chamado e o bt_proxima é habilitado apenas se for selecionada uma resposta. Já o bt_finalizar só é habilitado após a última lâmina ser respondida.
        '''
        if index >= len(self.ishihara_placas):
            self.mostrar_resultados()
            self.habilitar_botao('bt_proxima','disabled')
            self.habilitar_botao('bt_finalizar','normal')
            return

        plate = self.ishihara_placas[index]

        '''
        Carrega a imagem.
        '''
        image = Image.open(plate["image"])
        image = image.resize((450, 450), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        '''
        Atualiza o rótulo da imagem.
        '''
        self.tx_imagem.config(image=photo)
        self.tx_imagem.image = photo 

        '''
        Atualiza o rótulo da placa.
        '''
        self.tx_placa.config(text=f"Placa {index + 1}")

        '''
        Atualiza as opções da caixa de seleção.
        '''
        self.op_menu['values'] = plate["options"]
        self.op_var.set("") # Reseta a seleção.
        self.bt_proxima.config(state=tk.DISABLED)

    def selecionar_op(self, *args: Any) -> None:
        '''
        Verifica se a opção foi selecionada e, se sim, o botão bt_proxima é habilitado.
        '''
        if self.op_var.get(): 
            self.bt_proxima.config(state=tk.NORMAL)

    def px_imagem(self) -> None:
        '''
        Este método é responsável por mostrar a próxima imagem, acrescentando +1 ao índice e chamando o método mostrar_imagem, passando como parâmetro o índice atualizado. 
        '''
        escolha_usuario = self.op_var.get()
        self.resp_t.append(escolha_usuario)
        self.imagem_atual += 1
        self.mostrar_imagem(self.imagem_atual)

    def mostrar_resultados(self) -> None:
        '''
        Este método é responsável por mostrar os resultados do usuário. Ele conta as respostas dos diferentes tipos de daltonismo e da visão normal, e determina um prognóstico com base nas contagens. 
        O método faz isso através da comparação das respostas do usuário com as respostas esperadas, e exibe um resultado correspondente.
        '''
        normal_count = 0
        protanopia_count = 0
        deuteranopia_count = 0
        tritanopia_count = 0

        resul_ = []

        for i, escolha_usuario in enumerate(self.resp_t):
            expected = self.ishihara_placas[i]["expected"]
            if escolha_usuario == expected.get("normal"):
                normal_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Normal)")
            elif escolha_usuario == expected.get("protanopia"):
                protanopia_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Protanopia)")
            elif escolha_usuario == expected.get("deuteranopia"):
                deuteranopia_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Deuteranopia)")
            elif escolha_usuario == expected.get("tritanopia"):
                tritanopia_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Tritanopia)")

        if protanopia_count > deuteranopia_count and protanopia_count > normal_count and protanopia_count > tritanopia_count:
            diagnostico = "Protanopia"
        elif deuteranopia_count > protanopia_count and deuteranopia_count > normal_count and deuteranopia_count > tritanopia_count:
            diagnostico = "Deuteranopia"
        elif tritanopia_count > protanopia_count and tritanopia_count > normal_count and tritanopia_count > normal_count:
            diagnostico = "Tritanopia"
        elif normal_count > protanopia_count and normal_count > deuteranopia_count and normal_count > tritanopia_count:
            diagnostico = "Visão Normal"
        else:
            diagnostico = "Indeterminado"

        resul_.append(f"\nPrognóstico Final: {diagnostico}")

        self.tx_resultado.config(text="\n".join(resul_))
        self.salvar_dados(diagnostico)

    def salvar_dados(self, diagnostico):
      '''
      Este método salva os dados do usuário, incluindo o prognóstico final, em um bando de dados SQLite pacientes.db e cria, se não existi, uma tabela com colunas que receberão as informações do usuário, incluindo o prognóstico.
      Com cursor.execute, ele insere os dados do usuário no banco de dados.
      '''
      conn = sqlite3.connect('pacientes.db')
      cursor = conn.cursor()
        
      cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,        
            cpf TEXT NOT NULL,
            diagnostico TEXT
          )
      ''')

      conn.commit()

      cursor.execute('''
            INSERT INTO pacientes (nome, sobrenome, data_nascimento, telefone,  email, cpf, diagnostico) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self.dados_usuario.nome, self.dados_usuario.sobrenome, self.dados_usuario.data,self.dados_usuario.telefone,self.dados_usuario.email, self.dados_usuario.cpf, diagnostico))

      conn.commit()

    def janela_resultado(self)-> None:
        '''
        Este método executa comando sys.executable, chama o arquivo documento.py para gerar o PDF com os resultados.
        '''
        self.mostrar_resultados()
        subprocess.Popen([sys.executable, 'documento.py'])

Ishihara()
