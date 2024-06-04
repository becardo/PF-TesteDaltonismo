from tkinter import *
from Documento import Documento

janela_usuario = Tk()

class Usuario(Documento):
    def __init__(self):
        self.janela_usuario = janela_usuario
        self.espec_tela()

        janela_usuario.mainloop()

    def variaveis(self):
        self.nome= self.entry_nome.get()
        self.sobrenome= self.entry_sobrenome.get()
        self.data= self.entry_data.get()
        self.tel= self.entry_tel.get()
        self.rua= self.entry_rua.get()
        self.numero= self.entry_numero.get()
        self.bairro= self.entry_bairro.get()
        self.cidade= self.entry_cidade.get()
        self.cep= self.entry_cep.get()
    
    def espec_tela(self):
        # Aqui estão todas as especificações gráficas de tela inicial do usuário:
        self.janela_usuario.title("Teste/Prognóstico para Daltonismo")
        self.janela_usuario.configure(background='#ADD8E6')
        self.janela_usuario.geometry("800x500")
        self.janela_usuario.resizable(True, True)
        self.janela_usuario.minsize(width=700, height=400)

        self.frame = Frame(self.janela_usuario, bd=6, bg='#F0F8FF',
                           highlightbackground='#87CEEB', highlightthickness=3)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.label_cabecalho = Label(
            self.frame, text="Ficha do Paciente", bg='#F0F8FF', fg='#191970', font=('arial', 18))
        self.label_cabecalho.place(relx=0.33, rely=0.01)

        # Label e Entry para as informações:
        self.label_nome = Label(self.frame, text="Nome: ",
                                bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_nome.place(relx=0.01, rely=0.15)

        self.entry_nome = Entry(self.frame, font=('arial', 12))
        self.entry_nome.place(relx=0.08, rely=0.14, relwidth=0.85)
        ###
        self.label_sobrenome = Label(
            self.frame, text="Sobrenome: ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_sobrenome.place(relx=0.01, rely=0.25)

        self.entry_sobrenome = Entry(self.frame, font=('arial', 12))
        self.entry_sobrenome.place(relx=0.13, rely=0.24, relwidth=0.8)
        ###
        self.label_data = Label(self.frame, text="Data de Nascimento: ",
                                bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_data.place(relx=0.01, rely=0.35)

        self.entry_data = Entry(self.frame, font=('arial', 12))
        self.entry_data.place(relx=0.21, rely=0.34, relwidth=0.25)
        ###
        self.label_tel = Label(self.frame, text="Telefone/Celular: ",
                               bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_tel.place(relx=0.48, rely=0.35)

        self.entry_tel = Entry(self.frame, font=('arial', 12))
        self.entry_tel.place(relx=0.65, rely=0.34, relwidth=0.28)
        ###
        self.label_endereco = Label(
            self.frame, text="Endereço: ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_endereco.place(relx=0.01, rely=0.45)
        ###
        self.label_rua = Label(self.frame, text="Rua: ",
                               bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_rua.place(relx=0.01, rely=0.55)

        self.entry_rua = Entry(self.frame, font=('arial', 12))
        self.entry_rua.place(relx=0.06, rely=0.54, relwidth=0.7)
        ###
        self.label_numero = Label(
            self.frame, text="N°: ", bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_numero.place(relx=0.79, rely=0.55)

        self.entry_numero = Entry(self.frame, font=('arial', 12))
        self.entry_numero.place(relx=0.83, rely=0.54, relwidth=0.1)
        ###
        self.label_bairro = Label(self.frame, text="Bairro: ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_bairro.place(relx=0.01, rely=0.65)
        
        self.entry_bairro = Entry(self.frame, font=('arial', 12))
        self.entry_bairro.place(relx=0.08, rely=0.64, relwidth=0.25)
        ###
        self.label_cidade = Label(self.frame, text="Cidade: ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_cidade.place(relx=0.35, rely=0.65)
        
        self.entry_cidade = Entry(self.frame, font=('arial', 12))
        self.entry_cidade.place(relx=0.43, rely=0.64, relwidth=0.25)
        ###
        self.label_cep = Label(self.frame, text="CEP: ",bg='#F0F8FF', fg='#191970', font=('arial', 12))
        self.label_cep.place(relx=0.70, rely=0.65)
        
        self.entry_cep = Entry(self.frame, font=('arial', 12))
        self.entry_cep.place(relx=0.76, rely=0.64, relwidth=0.17)
        
        self.label_aviso= Label(self.frame, text="** Por favor, confira se os dados estão corretos antes de inicar o teste.**",bg='#F0F8FF', fg='#191970', font=('arial', 10))
        self.label_aviso.place(relx= 0.01, rely= 0.8)
        
        # Botão para o inicio do teste:
        self.bt_iniciar = Button(self.frame, text= "Iniciar Teste", bd= 4, bg= '#4682B4', fg= '#F5FFFA', activebackgroun= '#B0E0E6', activeforegroun= '#4682B4', font= ('arial',12))
        self.bt_iniciar.place(relx= 0.4, rely= 0.85, relwidth= 0.15, relheight= 0.1)


Usuario()
