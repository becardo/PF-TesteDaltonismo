import tkinter as tk
import subprocess
import sys
from tkcalendar import Calendar, DateEntry
from InterfaceDaltonismo import TesteDaltonismo

class Usuario(TesteDaltonismo):
    def __init__(self) -> None:
        self.janela_teste = tk.Tk()
        self.iniciar_teste()
        self.janela_teste.mainloop() 

    def configurar_validacao(self, entry: tk.Entry, tipo: str) -> None:
        '''
        Configura a validação para aceitar apenas caracteres numéricos ou letras.
        Para entrys que recebem entradas numéricas, caracteres como -, (, ), e . são permitidos.
        Para entrys que recebem entradas de letras, apenas caracteres como letras e "  " são permitos.
        '''
        def validar_entrada(action: str, value_if_allowed: str) -> bool:
            if action == '1': 
                try:
                    if tipo == 'numerico':
                        for char in value_if_allowed:
                            if not (char.isdigit() or char in "-()."):
                                raise ValueError

                    elif tipo == 'letras':
                        if not value_if_allowed.replace(" ","").isalpha():
                            raise ValueError
                except ValueError:
                    return False
            return True

        vcmd = (entry.register(validar_entrada), '%d', '%P')
        entry.config(validate='key', validatecommand=vcmd)

    def calendario(self) -> None:
        '''
        Cria um calendário para a data de nascimento do usuário.
        '''
        self.calendario = Calendar(self.frame, fg="gray75", bg="blue", font=("Times",'9','bold'), locale='pt_br')
        self.calendario.place(relx= 0.5, rely=0.1)
        self.calData = tk.Button(self.frame, text="Inserir Data", command= self.print_cal)
        self.calData.place(relx=0.6, rely=0.4, height=25, width=100)

    def print_cal(self) -> None:
        '''
        Imprime a data de nascimento do usuário no calendário. Em seguida, o calendário some.
        '''
        dataIni = self.calendario.get_date()
        self.calendario.destroy()
        self.entry_data.delete(0, tk.END)
        self.entry_data.insert(0, dataIni)
        self.calData.destroy()

    def iniciar_teste(self) -> None:
        '''
        Aqui estão todas as especificações gráficas de tela inicial do usuário:
        '''
        self.janela_teste.title("Teste de Daltonismo")
        self.janela_teste.geometry("800x600")
        self.janela_teste.configure(background= '#F0F8FF')

        self.frame = tk.Frame(self.janela_teste, bd=6, bg='#F0F8FF',
                           highlightbackground='#87CEEB', highlightthickness=3)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.label_cabecalho = tk.Label(
            self.frame, text="Ficha do Paciente", bg='#F0F8FF', fg='#191970', font=('arial', 18))
        self.label_cabecalho.place(relx=0.33, rely=0.01)

        '''
        Variáveis StringVar
        Essas informações serão obrigatórias. O usuário deve digitá-las para que tenha acesso ao teste.
        '''
        self._nome_var = tk.StringVar()
        self._sobrenome_var = tk.StringVar()
        self._data_var = tk.StringVar()
        self._tel_var = tk.StringVar()
        self.__email_var = tk.StringVar()
        self.__cpf_var = tk.StringVar()

        '''
        Monitoramento das variáveis:
        '''
        self._nome_var.trace("w", self.check_entradas)
        self._sobrenome_var.trace("w", self.check_entradas)
        self._data_var.trace("w", self.check_entradas)
        self._tel_var.trace("w", self.check_entradas)
        self.__email_var.trace("w", self.check_entradas)
        self.__cpf_var.trace("w", self.check_entradas)

        '''
        Label e Entry para as informações:
        '''
        self.label_nome = tk.Label(self.frame, text="Nome:* ",
                                bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_nome.place(relx=0.01, rely=0.15)

        self.entry_nome = tk.Entry(self.frame, textvariable=self._nome_var, font=('arial', 12))
        self.entry_nome.place(relx=0.085, rely=0.15, relwidth=0.85)
        self.configurar_validacao(self.entry_nome, 'letras')

        self.label_sobrenome = tk.Label(
            self.frame, text="Sobrenome:* ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_sobrenome.place(relx=0.01, rely=0.25)

        self.entry_sobrenome = tk.Entry(self.frame, textvariable=self._sobrenome_var, font=('arial', 12))
        self.entry_sobrenome.place(relx=0.14, rely=0.25, relwidth=0.8)
        self.configurar_validacao(self.entry_sobrenome, 'letras')

        self.label_data = tk.Button(self.frame, text="Data de Nascimento:* ",
                                bg='#F0F8FF', fg='#191970', font=('arial', 12), command= self.calendario)
        self.label_data.place(relx=0.01, rely=0.35)

        self.entry_data = tk.Entry(self.frame)
        self.entry_data.place(relx=0.3, rely=0.35, relwidth=0.25)

        self.label_cpf = tk.Label(self.frame, text="CPF:* ",
                               bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_cpf.place(relx=0.58, rely=0.35)

        self.entry_cpf = tk.Entry(self.frame,textvariable=self.__cpf_var, font=('arial', 12))
        self.entry_cpf.place(relx=0.65, rely=0.35, relwidth=0.29)
        self.configurar_validacao(self.entry_cpf, 'numerico')

        self.label_email = tk.Label(self.frame, text="E-mail:* ",
                               bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_email.place(relx=0.01, rely=0.45)

        self.entry_email = tk.Entry(self.frame, textvariable=self.__email_var, font=('arial', 12))
        self.entry_email.place(relx=0.09, rely=0.45, relwidth=0.85)

        self.label_tel = tk.Label(self.frame, text="Telefone/Celular:* ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_tel.place(relx=0.01, rely=0.55)

        self.entry_tel = tk.Entry(self.frame, textvariable=self._tel_var, font=('arial', 12))
        self.entry_tel.place(relx=0.18, rely=0.55, relwidth=0.25)
        self.configurar_validacao(self.entry_tel, 'numerico')

        self.label_aviso= tk.Label(self.frame, text="** Por favor, confira se os dados estão corretos antes de iniciar o teste.",bg='#F0F8FF', fg='#191970', font=('arial', 10))
        self.label_aviso.place(relx= 0.01, rely= 0.8)

        '''
        Botão para o inicio do teste:
        '''
        self.bt_iniciar = tk.Button(self.frame, text="Iniciar Teste", bd=4, bg='#4682B4', fg='#F5FFFA', activebackground='#B0E0E6', activeforeground='#4682B4', font=('arial', 12), command= self.iniciar_bt)
        self.bt_iniciar.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1)
        '''
        Desabilitar o botão inicialmente.
        '''
        self.habilitar_botao('bt_iniciar','disabled') 

    def check_entradas(self, *args: str) -> None:
        '''
         Verifica se os campos estão preenchidos.
        '''
        campos_obrigatorios = [
            self._nome_var.get(), 
            self._sobrenome_var.get(),
            self._tel_var.get(),
            self.__email_var.get(),
            self.__cpf_var.get()
        ]
        if all(campos_obrigatorios):
            self.habilitar_botao('bt_iniciar','normal')
        else:
            self.habilitar_botao('bt_iniciar','disabled')

    def iniciar_bt(self)-> None:
        '''
        Este método executa comando sys.executable, que abre a janela de execução do arquivo Ishihara.py e passa dos parâmetros do Usuário para Ishihara.
        '''
        subprocess.Popen([sys.executable, 'ishihara.py', '--nome',self._nome_var.get(), '--sobrenome',self._sobrenome_var.get(), '--data',self._data_var.get(), '--telefone',self._tel_var.get(),'--email', self.__email_var.get(),'--cpf', self.__cpf_var.get()])

'''
Inicializa a classe Usuario.
'''
Usuario()
