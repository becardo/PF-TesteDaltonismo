import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Ishihara:
    def __init__(self, master):
        self.master = master
        self.master.title("Teste de Ishihara")

        self.window_width = 600
        self.window_height = 700
        self.master.geometry(f"{self.window_width}x{self.window_height}")
        
        self.canvas = tk.Canvas(master)
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
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
        self.ishihara_plates = [
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

        self.user_responses = []
        self.current_index = 0

        # criando os widgets
        self.plate_label = tk.Label(self.scrollable_frame, text="Placa 1")
        self.plate_label.pack(pady=(10, 0))

        self.image_label = tk.Label(self.scrollable_frame)
        self.image_label.pack(pady=(10, 0))

        self.option_var = tk.StringVar()
        self.option_var.trace('w', self.option_selected)
        
        self.option_menu = ttk.Combobox(self.scrollable_frame, textvariable=self.option_var, state="readonly")
        self.option_menu.pack(pady=(10, 0))

        self.next_button = tk.Button(self.scrollable_frame, text="Próxima", command=self.next_image, state=tk.DISABLED)
        self.next_button.pack(pady=(10, 0))

        self.results_label = tk.Label(master, text="")
        self.results_label.pack(pady=(10, 0))

        # exibe a primeira imagem
        self.show_image(self.current_index)

    def show_image(self, index):
        if index >= len(self.ishihara_plates):
            self.show_results()
            self.next_button.config(state=tk.DISABLED)
            return

        plate = self.ishihara_plates[index]

        # carrega a imagem
        image = Image.open(plate["image"])
        image = image.resize((self.window_width - 50, self.window_width - 50), Image.Resampling.LANCZOS)  # tamanho padrão a imagem para tamanho da janela -50
        photo = ImageTk.PhotoImage(image)

        # atualiza o rótulo da imagem
        self.image_label.config(image=photo)
        self.image_label.image = photo  # manetm uma referência da imagem pra não dar erro

        # atualiza o rótulo da placa
        self.plate_label.config(text=f"Placa {index + 1}")

        # atualiza as opções da caixa de seleção
        self.option_menu['values'] = plate["options"]
        self.option_var.set("")  # reseta a seleção
        self.next_button.config(state=tk.DISABLED)
        
    def option_selected(self, *args):
        if self.option_var.get():  # Se uma opção estiver selecionada
            self.next_button.config(state=tk.NORMAL)  # Habilitar o botão "Próxima"

    def next_image(self):
        response = self.option_var.get()
        self.user_responses.append(response)
        self.current_index += 1
        self.show_image(self.current_index)

    def show_results(self):
        normal_count = 0
        protanopia_count = 0
        deuteranopia_count = 0

        results = []

        for i, response in enumerate(self.user_responses):
            expected = self.ishihara_plates[i]["expected"]
            if response == expected.get("normal"):
                normal_count += 1
                results.append(f"Placa {i+1}: {response} (Normal)")
            elif response == expected.get("protanopia"):
                protanopia_count += 1
                results.append(f"Placa {i+1}: {response} (Protanopia)")
            elif response == expected.get("deuteranopia"):
                deuteranopia_count += 1
                results.append(f"Placa {i+1}: {response} (Deuteranopia)")
            else:
                results.append(f"Placa {i+1}: {response} (Resposta Inválida)")

        # gera o diagnóstico 
        if protanopia_count > deuteranopia_count and protanopia_count > normal_count:
            diagnosis = "Protanopia"
        elif deuteranopia_count > protanopia_count and deuteranopia_count > normal_count:
            diagnosis = "Deuteranopia"
        elif normal_count > protanopia_count and normal_count > deuteranopia_count:
            diagnosis = "Visão Normal"
        else:
            diagnosis = "Indeterminado"

        results.append(f"\nDiagnóstico Final: {diagnosis}")

        self.results_label.config(text="\n".join(results))


if __name__ == "__main__":
    root = tk.Tk()
    app = Ishihara(root)
    root.mainloop()
