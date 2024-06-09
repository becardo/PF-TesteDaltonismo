import tkinter as tk
import subprocess
import sys

class Usuario():
    def __init__(self):
        self.janela_usuario = tk.Tk()
        self.espec_tela()
        self.janela_usuario.mainloop()  # Loop para manter a janela do usuario aberta.

    def espec_tela(self):
        # Aqui estão todas as especificações gráficas de tela inicial do usuário:
        self.janela_usuario.title("Teste/Prognóstico para Daltonismo")
        self.janela_usuario.configure(background='#ADD8E6')
        self.janela_usuario.geometry("800x600")
        self.janela_usuario.resizable(True, True)
        self.janela_usuario.minsize(width=800, height=600)

        self.frame = tk.Frame(self.janela_usuario, bd=6, bg='#F0F8FF',
                           highlightbackground='#87CEEB', highlightthickness=3)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.label_cabecalho = tk.Label(
            self.frame, text="Ficha do Paciente", bg='#F0F8FF', fg='#191970', font=('arial', 18))
        self.label_cabecalho.place(relx=0.33, rely=0.01)

        # Variáveis StringVar
        # Essas informações serão obrigatórias. O usuário deve digitá-las para que tenha acesso ao teste.
        self._nome_var = tk.StringVar()
        self._sobrenome_var = tk.StringVar()
        self._data_var = tk.StringVar()
        self._tel_var = tk.StringVar()
        self.__rua_var = tk.StringVar()
        self.__numero_var = tk.StringVar()
        self.__bairro_var = tk.StringVar()
        self.__cidade_var = tk.StringVar()
        self.__cep_var = tk.StringVar()

        # Monitoramento das variáveis
        self._nome_var.trace("w", self.check_entradas)
        self._sobrenome_var.trace("w", self.check_entradas)
        self._data_var.trace("w", self.check_entradas)
        self._tel_var.trace("w", self.check_entradas)
        self.__rua_var.trace("w", self.check_entradas)
        self.__numero_var.trace("w", self.check_entradas)
        self.__bairro_var.trace("w", self.check_entradas)
        self.__cidade_var.trace("w", self.check_entradas)
        self.__cep_var.trace("w", self.check_entradas)

        # Label e Entry para as informações:
        self.label_nome = tk.Label(self.frame, text="Nome:* ",
                                bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_nome.place(relx=0.01, rely=0.15)

        self.entry_nome = tk.Entry(self.frame, textvariable=self._nome_var, font=('arial', 12))
        self.entry_nome.place(relx=0.085, rely=0.14, relwidth=0.85)

        self.label_sobrenome = tk.Label(
            self.frame, text="Sobrenome:* ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_sobrenome.place(relx=0.01, rely=0.25)

        self.entry_sobrenome = tk.Entry(self.frame, textvariable=self._sobrenome_var, font=('arial', 12))
        self.entry_sobrenome.place(relx=0.14, rely=0.24, relwidth=0.8)

        self.label_data = tk.Label(self.frame, text="Data de Nascimento:* ",
                                bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_data.place(relx=0.01, rely=0.35)

        self.entry_data = tk.Entry(self.frame, textvariable=self._data_var, font=('arial', 12))
        self.entry_data.place(relx=0.23, rely=0.34, relwidth=0.25)

        self.label_tel = tk.Label(self.frame, text="Telefone/Celular: ",
                               bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_tel.place(relx=0.48, rely=0.35)

        self.entry_tel = tk.Entry(self.frame,textvariable=self._tel_var, font=('arial', 12))
        self.entry_tel.place(relx=0.65, rely=0.34, relwidth=0.28)

        self.label_endereco = tk.Label(
            self.frame, text="Endereço: ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_endereco.place(relx=0.01, rely=0.45)

        self.label_rua = tk.Label(self.frame, text="Rua:* ",
                               bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_rua.place(relx=0.01, rely=0.55)

        self.entry_rua = tk.Entry(self.frame, textvariable=self.__rua_var, font=('arial', 12))
        self.entry_rua.place(relx=0.065, rely=0.54, relwidth=0.7)

        self.label_numero = tk.Label(
            self.frame, text="N°:* ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_numero.place(relx=0.79, rely=0.55)

        self.entry_numero = tk.Entry(self.frame, textvariable=self.__numero_var, font=('arial', 12))
        self.entry_numero.place(relx=0.85, rely=0.54, relwidth=0.1)

        self.label_bairro = tk.Label(self.frame, text="Bairro:* ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_bairro.place(relx=0.01, rely=0.65)
        
        self.entry_bairro = tk.Entry(self.frame, textvariable=self.__bairro_var, font=('arial', 12))
        self.entry_bairro.place(relx=0.085, rely=0.64, relwidth=0.25)

        self.label_cidade = tk.Label(self.frame, text="Cidade:* ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_cidade.place(relx=0.35, rely=0.65)
        
        self.entry_cidade = tk.Entry(self.frame, textvariable=self.__cidade_var, font=('arial', 12))
        self.entry_cidade.place(relx=0.45, rely=0.64, relwidth=0.25)

        self.label_cep = tk.Label(self.frame, text="CEP: ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_cep.place(relx=0.70, rely=0.65)
        
        self.entry_cep = tk.Entry(self.frame, textvariable=self.__cep_var, font=('arial', 12))
        self.entry_cep.place(relx=0.78, rely=0.64, relwidth=0.17)
        
        self.label_aviso= tk.Label(self.frame, text="** Por favor, confira se os dados estão corretos antes de iniciar o teste.",bg='#F0F8FF', fg='#191970', font=('arial', 10))
        self.label_aviso.place(relx= 0.01, rely= 0.8)
        
        # Botão para o inicio do teste:
        self.bt_iniciar = tk.Button(self.frame, text="Iniciar Teste", bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 12), command=self.iniciar_teste)
        self.bt_iniciar.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1)
        self.bt_iniciar.config(state=tk.DISABLED) # Desabilitar o botão inicialmente.
    
    def check_entradas(self, *args):
        # Verifica se os campos estão preenchidos.
        campos_obrigatorios = [
            self._nome_var.get(), 
            self._sobrenome_var.get(), 
            self._data_var.get(),
            self._tel_var.get(),
            self.__rua_var.get(),
            self.__numero_var.get(),
            self.__bairro_var.get(),
            self.__cidade_var.get(),
            self.__cep_var.get()
        ]
        if all(campos_obrigatorios):
            self.bt_iniciar.config(state=tk.NORMAL)
        else:
            self.bt_iniciar.config(state=tk.DISABLED)

    def iniciar_teste(self):
        # Este método executa comando sys.executable, que abre a janela de execução do arquivo Ishihara.py.
        # self.janela_usuario.destroy() # Faz com que a janela Usuario feche.
        subprocess.Popen([sys.executable, "Ishihara.py"])

# Inicializar a classe Usuario.
Usuario()
