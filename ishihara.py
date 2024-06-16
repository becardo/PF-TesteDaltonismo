import tkinter as tk
from tkinter import ttk
from typing import Any, Dict, List
from PIL import Image, ImageTk
from InterfaceDaltonismo import TesteDaltonismo
import subprocess
import sys
#from documento import Documento

class Ishihara(TesteDaltonismo):
    def __init__(self) -> None:
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
        lista com as placas de Ishihara, opções e respostas esperadas para cada caso 
        '''
        self.tx_placa = tk.Label(self.scrollable_frame, text="Placa 1",background= '#F0F8FF')
        self.tx_placa.pack(pady=(10, 0))

        self.tx_imagem = tk.Label(self.scrollable_frame)
        self.tx_imagem.pack(pady=(10, 0))

        self.op_var = tk.StringVar()
        self.op_var.trace('w', self.selecionar_op)

        self.op_menu = ttk.Combobox(self.scrollable_frame, textvariable=self.op_var, state="readonly")
        self.op_menu.pack(pady=(10, 0))

        self.bt_proxima = tk.Button(self.scrollable_frame, text="Próxima",bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 10), command=self.px_imagem, state=tk.DISABLED)
        self.bt_proxima.pack(pady=(10, 0))

        self.tx_resultado = tk.Label(self.janela_teste, text="")
        self.tx_resultado.pack(pady=(10, 0))

        self.bt_finalizar = tk.Button(self.scrollable_frame, text="Finalizar teste", bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 10),command= self.janela_resultado, state=tk.DISABLED)
        self.bt_finalizar.pack(pady=(10, 0))

        self.mostrar_imagem(self.imagem_atual)

    def carregar_placas(self) -> List[Dict[str, Any]]:
        return [
            {"image": "ishihara/Ishihara01.png", "options": ["1", "2", "12"], "expected": {"normal": "12", "protanopia": "1", "deuteranopia": "2"}},
        ]

    def mostrar_imagem(self, index: int) -> None:
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
        if self.op_var.get(): 
            self.bt_proxima.config(state=tk.NORMAL)

    def px_imagem(self) -> None:
        escolha_usuario = self.op_var.get()
        self.resp_t.append(escolha_usuario)
        self.imagem_atual += 1
        self.mostrar_imagem(self.imagem_atual)

    def mostrar_resultados(self) -> None:
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

    def janela_resultado(self)-> None:
        '''
        Este método executa comando sys.executable, chama o arquivo documento.py para gerar o PDF com os resultados.
        '''
        subprocess.Popen([sys.executable, 'resultado.py'])


Ishihara()
