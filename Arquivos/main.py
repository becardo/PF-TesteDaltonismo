import tkinter as tk
from tkinter import simpledialog
from usuario import Usuario
from ishihara import Ishihara
from teste import Teste

def main():
    # Inicialização da interface gráfica
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Obter informações do usuário
    nome = simpledialog.askstring("Nome", "Qual é o seu nome?")
    idade = simpledialog.askinteger("Idade", "Qual é a sua idade?")
    genero = simpledialog.askstring("Gênero", "Qual é o seu gênero?")
    data_nascimento = simpledialog.askstring("Data de Nascimento", "Qual é a sua data de nascimento?")

    usuario = Usuario(nome, idade, genero, data_nascimento)

    # Carregar lâminas de Ishihara
    laminas = []
    for i in range(1, 35):
        imagem = f"imagens/lamina_{i}.png"
        respostas = {"resposta1": 1, "resposta2": 2, "resposta3": 3, "resposta4": 4}  # Substituir com respostas reais
        laminas.append(Ishihara(imagem, respostas))

    # Iniciar o teste
    teste = Teste(usuario, laminas)
    teste.iniciar()

    # Analisar resultados
    teste.analisar_resultados()

    # Gerar documento PDF com os resultados
    teste.gerar_documento()

if __name__ == "__main__":
    main()