import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Ishihara:
    def __init__(self, master):
        self.master = master
        self.master.title("Teste de Ishihara")

        # lista com as placas de Ishihara, opções e respostas esperadas para cada caso 
        self.ishihara_plates = [
            {"image": "ishihara/Ishihara01.png", "options": ["1", "2", "12"], "expected": {"normal": "12", "protanopia": "1", "deuteranopia": "2"}},
            {"image": "ishihara/Ishihara02.png", "options": ["3", "6", "8"], "expected": {"normal": "8", "protanopia": "3"}},
            {"image": "ishihara/Ishihara03.png", "options": ["3", "5", "6"], "expected": {"normal": "6", "protanopia": "5"}},
            # fiz só com 3 placas, mas tem que colocar as 38 placas do pdf
        ]

        self.user_responses = []
        self.current_index = 0

        # criando os widgets
        self.plate_label = tk.Label(master, text="Placa 1")
        self.plate_label.pack()

        self.image_label = tk.Label(master)
        self.image_label.pack()

        self.option_var = tk.StringVar()
        self.option_menu = ttk.Combobox(master, textvariable=self.option_var)
        self.option_menu.pack()

        self.next_button = tk.Button(master, text="Próxima", command=self.next_image)
        self.next_button.pack()

        self.results_label = tk.Label(master, text="")
        self.results_label.pack()

        # exibe a primeira imagem
        self.show_image(self.current_index)

    def show_image(self, index):
        if index >= len(self.ishihara_plates):
            self.show_results()
            return

        plate = self.ishihara_plates[index]

        # carrega a imagem
        image = Image.open(plate["image"])
        photo = ImageTk.PhotoImage(image)

        # atualiza o rótulo da imagem
        self.image_label.config(image=photo)
        self.image_label.image = photo  # manetm uma referência da imagem pra não dar erro

        # atualiza o rótulo da placa
        self.plate_label.config(text=f"Placa {index + 1}")

        # atualiza as opções da caixa de seleção
        self.option_menu['values'] = plate["options"]
        self.option_var.set("")  # reseta a seleção

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
