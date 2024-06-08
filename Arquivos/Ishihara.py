import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Arquivos import Documento


janela_ishihara = Tk()

class Ishihara(Documento):
    def __init__(self):
        super().__init__()
        self.janela_ishihara = janela_ishihara
        self.espec_janela()
        
        janela_ishihara.mainloop()
        
    def espec_janela(self):
        self.janela_ishihara.title("Teste de Ishihara")

        self.largura_janela = 800
        self.altura_janela = 600
        self.janela_ishihara.geometry(f"{self.largura_janela}x{self.altura_janela}")
        
        self.canvas = tk.Canvas(janela_ishihara)
        self.scrollbar = tk.Scrollbar(janela_ishihara, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # lista com as placas de Ishihara, opções e respostas esperadas para cada caso 
        self.ishihara_placas = [
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
            # fiz só com 33 placas, mas tem que colocar as 38 placas do pdf
        ]

        self.resp_t = []
        self.imagem_atual = 0

        # criando os widgets
        self.tx_placa = tk.Label(self.scrollable_frame, text="Placa 1")
        self.tx_placa.pack(pady=(10, 0))

        self.tx_imagem = tk.Label(self.scrollable_frame)
        self.tx_imagem.pack(pady=(10, 0))

        self.op_var = tk.StringVar()
        self.op_var.trace('w', self.selecionar_op)
        
        self.op_menu = ttk.Combobox(self.scrollable_frame, textvariable=self.op_var, state="readonly")
        self.op_menu.pack(pady=(10, 0))

        self.bt_proxima = tk.Button(self.scrollable_frame, text="Próxima", command=self.px_imagem, state=tk.DISABLED)
        self.bt_proxima.pack(pady=(10, 0))

        self.tx_resultado = tk.Label(janela_ishihara, text="")
        self.tx_resultado.pack(pady=(10, 0))
        
        self.bt_gerar_pdf = tk.Button(self.scrollable_frame, text="Gerar Documento PDF", state= tk.DISABLED, command= self.gerar_pdf)
        self.bt_gerar_pdf.pack(pady=(10, 0))

        # exibe a primeira imagem
        self.mostrar_imagem(self.imagem_atual)

    def mostrar_imagem(self, index):
        if index >= len(self.ishihara_placas):
            self.msotrar_resultados()
            self.bt_proxima.config(state= tk.DISABLED)
            self.bt_gerar_pdf.config(state= tk.NORMAL)
            return

        plate = self.ishihara_placas[index]

        # carrega a imagem
        image = Image.open(plate["image"])
        image = image.resize((self.largura_janela - 350, self.largura_janela - 350), Image.Resampling.LANCZOS)  # tamanho padrão a imagem para tamanho da janela -50
        photo = ImageTk.PhotoImage(image)

        # atualiza o rótulo da imagem
        self.tx_imagem.config(image=photo)
        self.tx_imagem.image = photo  # manetm uma referência da imagem pra não dar erro

        # atualiza o rótulo da placa
        self.tx_placa.config(text=f"Placa {index + 1}")

        # atualiza as opções da caixa de seleção
        self.op_menu['values'] = plate["options"]
        self.op_var.set("")  # reseta a seleção
        self.bt_proxima.config(state=tk.DISABLED)
        
    def selecionar_op(self, *args):
        if self.op_var.get():  # Se uma opção estiver selecionada
            self.bt_proxima.config(state=tk.NORMAL)  # Habilitar o botão "Próxima"

    def px_imagem(self):
        escolha_usuario = self.op_var.get()
        self.resp_t.append(escolha_usuario)
        self.imagem_atual += 1
        self.mostrar_imagem(self.imagem_atual)

    def msotrar_resultados(self):
        normal_count = 0
        protanopia_count = 0
        deuteranopia_count = 0

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

        self.tx_resultado.config(text="\n".join(resul_))
        
    def gerar_pdf(self):
        Documento()


Ishihara()
