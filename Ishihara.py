import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#from Documento import Documento


_janela_ishihara = Tk() # Criando a variavel para inicializar a janela Ishihara.

class Ishihara():
    def __init__(self):
        super().__init__()
        self._janela_ishihara = _janela_ishihara
        self._teste_ishi()
        
        _janela_ishihara.mainloop()
        
    def _teste_ishi(self):
        # Neste método é realizado toda a configuração da janela, das imagens, gabaritos e tratamento
        # das respostas do usuário. 
        
        self._janela_ishihara.title("Teste de Ishihara")
        self._janela_ishihara.geometry("800x600")
        self._janela_ishihara.configure(background= '#F0F8FF')
        self._canvas = tk.Canvas(_janela_ishihara, background= '#F0F8FF') # Criação de uma wigdget Canvas dentro da janela Ishihara, para colocar as imagens.
        self._scrollbar = tk.Scrollbar(_janela_ishihara, orient="vertical", command=self._canvas.yview) # Criação da barra de rolagem.
        self._scrollable_frame = ttk.Frame(self._canvas, style= "TFrame")
        
        # Apenas para mudar a cor do fundo do Canvas.
        self._style = ttk.Style()
        self._style.configure("TFrame", background= '#F0F8FF')

        # Na estrutura abaixo, é associado um evento de configuração á scrollable_frame para que a barra de rolagem acompanhe
        # o redimencionamento do Canvas
        self._scrollable_frame.bind(
            "<Configure>",
            lambda e: self._canvas.configure(
                scrollregion=self._canvas.bbox("all")
            )
        )

        # Cria uma janela dentro do Canvas, e configura ele para usar a barra de rolagem vetical. Dessa forma, a rolagem acompanha a 
        # visualização do Canvas.
        self._canvas.create_window((0, 0), window=self._scrollable_frame, anchor="nw")
        self._canvas.configure(background= '#F0F8FF', yscrollcommand=self._scrollbar.set)
        
        # Posicionamento janela Canvas.
        self._canvas.pack(side="left", fill="both", expand=True,padx= 150)
        self._scrollbar.pack(side="right", fill="y")

        # lista com as placas de Ishihara, opções e respostas esperadas para cada caso 
        self._ishihara_placas = [
            {"image": "ishihara/Ishihara01.png", "options": ["1", "2", "12"], "expected": {"normal": "12", "protanopia": "1", "deuteranopia": "2"}},
            {"image": "ishihara/Ishihara02.png", "options": ["3", "6", "8"], "expected": {"normal": "8", "protanopia": "3"}},
            {"image": "ishihara/Ishihara03.png", "options": ["3", "5", "6"], "expected": {"normal": "6", "protanopia": "5"}},
            {"image": "ishihara/Ishihara04.png", "options": ["10", "29", "70"], "expected": {"normal": "29", "protanopia": "70"}},
            {"image": "ishihara/Ishihara05.jpg", "options": ["35", "57", "66"], "expected": {"normal": "57", "protanopia": "35"}},
            {"image": "ishihara/Ishihara06.png", "options": ["2", "3", "5"], "expected": {"normal": "5", "protanopia": "2"}},
            {"image": "ishihara/Ishihara07.png", "options": ["2", "3", "5"], "expected":{"normal": "3", "protanopia": "5"}},
            {"image": "ishihara/Ishihara08.png", "options": ["13", "15", "17"], "expected":{"normal": "15", "protanopia": "17"}},
            {"image": "ishihara/Ishihara09.png", "options": ["11", "21", "74"], "expected":{"normal": "74", "protanopia": "21"}},
            {"image": "ishihara/Ishihara10.jpg", "options": ["1", "2", "nada"], "expected":{"normal": "2", "protanopia": "1", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara11.jpg", "options": ["3", "6", "nada"], "expected":{"normal": "6", "protanopia": "3", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara12.jpg", "options": ["31", "97", "nada"], "expected":{"normal": "97", "protanopia": "31", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara13.png", "options": ["15", "45", "nada"], "expected":{"normal": "45", "protanopia": "15", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara14.png", "options": ["3", "5", "nada"], "expected":{"normal": "5", "protanopia": "3", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara15.png", "options": ["1", "7", "nada"], "expected":{"normal": "7", "protanopia": "1", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara16.png", "options": ["16", "26", "nada"], "expected":{"normal": "16", "protanopia": "26", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara17.png", "options": ["13", "73", "nada"], "expected":{"normal": "73", "protanopia": "13", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara18.png", "options": ["5", "3", "nada"], "expected":{"normal": "nada", "protanopia": "5"}},
            {"image": "ishihara/Ishihara19.jpg", "options": ["1", "2", "nada"], "expected":{"normal": "nada", "protanopia": "2"}},
            {"image": "ishihara/Ishihara20.png", "options": ["5", "45", "nada"], "expected":{"normal": "nada", "protanopia": "45"}},
            {"image": "ishihara/Ishihara21.jpg", "options": ["13", "73", "nada"], "expected":{"normal": "nada", "protanopia": "73"}},
            {"image": "ishihara/Ishihara22.png", "options": ["2", "6", "26"], "expected":{"normal": "26", "protanopia": "6", "deuteranopia": "2"}},
            {"image": "ishihara/Ishihara23.png", "options": ["2", "4", "42"], "expected":{"normal": "42", "protanopia": "2", "deuteranopia": "4"}},
            {"image": "ishihara/Ishihara24.jpg", "options": ["3", "5", "35"], "expected":{"normal": "35", "protanopia": "5", "deuteranopia": "3"}},
            {"image": "ishihara/Ishihara25.jpg", "options": ["6", "9", "96"], "expected":{"normal": "96", "protanopia": "6", "deuteranopia": "9"}},
            {"image": "ishihara/Ishihara26.png", "options": ["roxo", "vermelho", "roxo e vermelho"], "expected":{"normal": "roxo e vermelho", "protanopia": "roxo", "deuteranopia": "vermelho"}},
            {"image": "ishihara/Ishihara27.jpg", "options": ["roxo", "vermelho", "roxo e vermelho"], "expected":{"normal": "roxo e vermelho", "protanopia": "roxo", "deuteranopia": "vermelho"}},
            {"image": "ishihara/Ishihara28.jpg", "options": ["uma linha", "um número", "nada"], "expected":{"normal": "nada", "protanopia": "uma linha"}},
            {"image": "ishihara/Ishihara29.png", "options": ["uma linha", "um número", "nada"], "expected":{"normal": "nada", "protanopia": "uma linha"}},
            {"image": "ishihara/Ishihara30.png", "options": ["uma linha verde ou azul", "um número", "nada"], "expected":{"normal": "uma linha verde ou azul", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara31.jpg", "options": ["uma linha verde ou azul", "um número", "nada"], "expected":{"normal": "uma linha verde ou azul", "protanopia": "nada"}},
            {"image": "ishihara/Ishihara32.png", "options": ["uma linha", "uma linha laranja", "nada"], "expected":{"normal": "uma linha laranja", "protanopia": "nada" , "protanopia": "uma linha"}},
            {"image": "ishihara/Ishihara33.jpeg", "options": ["uma linha", "uma linha laranja", "nada"], "expected":{"normal": "uma linha laranja", "protanopia": "nada" , "protanopia": "uma linha"}},
            {"image": "ishihara/Ishihara34.jpg", "options": ["uma linha azul/verde/amarela", "uma linha verde/vermelha", "uma linha lilas"], "expected":{"normal": "uma linha azul/verde/amarela", "protanopia": "uma linha verde/vermelha" , "protanopia": "uma linha lilas"}},
            {"image": "ishihara/Ishihara35.png", "options": ["uma linha azul/verde/amarela", "uma linha verde/azul", "uma linha lilas"], "expected":{"normal": "uma linha azul/verde/amarela", "protanopia": "uma linha verde/azul" , "protanopia": "uma linha lilas"}},
            {"image": "ishihara/Ishihara36.jpeg", "options": ["uma linha lilas/laranja", "uma linha verde/azul", "uma linha lilas"], "expected":{"normal": "uma linha lilas/laranja", "protanopia": "uma linha verde/azul" , "protanopia": "uma linha lilas"}},
            {"image": "ishihara/Ishihara37.png", "options": ["uma linha lilas/laranja", "uma linha verde/azul", "uma linha lilas"], "expected":{"normal": "uma linha lilas/laranja", "protanopia": "uma linha verde/azul" , "protanopia": "uma linha lilas"}},
            {"image": "ishihara/Ishihara38.png", "options": ["uma linha laranja", "uma linha"], "expected": {"normal": "uma linha laranja", "protanopia": "uma linha", "deuteranopia": "uma linha"}},
        ]

        self._resp_t = []
        self._imagem_atual = 0

        # criando os widgets
        self._tx_placa = tk.Label(self._scrollable_frame, text="Placa 1")
        self._tx_placa.pack(pady=(10, 0))

        self._tx_imagem = tk.Label(self._scrollable_frame)
        self._tx_imagem.pack(pady=(10, 0))

        self._op_var = tk.StringVar()
        self._op_var.trace('w', self._selecionar_op)
        
        self._op_menu = ttk.Combobox(self._scrollable_frame, textvariable=self._op_var, state="readonly")
        self._op_menu.pack(pady=(10, 0))

        self._bt_proxima = tk.Button(self._scrollable_frame, text="Próxima", command=self._px_imagem, state=tk.DISABLED)
        self._bt_proxima.pack(pady=(10, 0))

        self._tx_resultado = tk.Label(_janela_ishihara, text="")
        self._tx_resultado.pack(pady=(10, 0))
        
        self._bt_gerar_pdf = tk.Button(self._scrollable_frame, text="Gerar Documento PDF", state= tk.DISABLED)
        self._bt_gerar_pdf.pack(pady=(10, 0))

        # Exibe a primeira imagem.
        self._mostrar_imagem(self._imagem_atual)

    def _mostrar_imagem(self, index):
        if index >= len(self._ishihara_placas):
            self._mostrar_resultados()
            self._bt_proxima.config(state= tk.DISABLED)
            self._bt_gerar_pdf.config(state= tk.NORMAL)
            return

        plate = self._ishihara_placas[index]

        # Carrega a imagem.
        image = Image.open(plate["image"])
        image = image.resize((450, 450), Image.Resampling.LANCZOS)  # tamanho padrão a imagem para tamanho da janela -50
        photo = ImageTk.PhotoImage(image)

        # Atualiza o rótulo da imagem.
        self._tx_imagem.config(image=photo)
        self._tx_imagem.image = photo  # manetm uma referência da imagem pra não dar erro

        # Atualiza o rótulo da placa.
        self._tx_placa.config(text=f"Placa {index + 1}")

        # Atualiza as opções da caixa de seleção.
        self._op_menu['values'] = plate["options"]
        self._op_var.set("")  # Reseta a seleção.
        self._bt_proxima.config(state=tk.DISABLED)
        
    def _selecionar_op(self, *args):
        if self._op_var.get():  # Se uma opção estiver selecionada
            self._bt_proxima.config(state=tk.NORMAL)  # Habilitar o botão "Próxima"

    def _px_imagem(self):
        escolha_usuario = self._op_var.get()
        self._resp_t.append(escolha_usuario)
        self._imagem_atual += 1
        self._mostrar_imagem(self._imagem_atual)

    def _mostrar_resultados(self):
        normal_count = 0
        protanopia_count = 0
        deuteranopia_count = 0

        resul_ = []

        for i, escolha_usuario in enumerate(self._resp_t):
            expected = self._ishihara_placas[i]["expected"]
            if escolha_usuario == expected.get("normal"):
                normal_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Normal)")
            elif escolha_usuario == expected.get("protanopia"):
                protanopia_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Protanopia)")
            elif escolha_usuario == expected.get("deuteranopia"):
                deuteranopia_count += 1
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Deuteranopia)")
            else:
                resul_.append(f"Placa {i+1}: {escolha_usuario} (Resposta Inválida)")

        # gera o diagnóstico 
        if protanopia_count > deuteranopia_count and protanopia_count > normal_count:
            diagnostico = "Protanopia"
        elif deuteranopia_count > protanopia_count and deuteranopia_count > normal_count:
            diagnostico = "Deuteranopia"
        elif normal_count > protanopia_count and normal_count > deuteranopia_count:
            diagnostico = "Visão Normal"
        else:
            diagnostico = "Indeterminado"

        resul_.append(f"\nDiagnóstico Final: {diagnostico}")

        self._tx_resultado.config(text="\n".join(resul_))
        
    #def gerar_pdf(self):
      # Documento.gerar_relatorio_pdf(self.resp_t, self.ishihara_placas)

Ishihara()
