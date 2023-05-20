from tkinter import *
from tkinter import ttk
import pandas as pd
root = Tk()

class Funcs():
    def limpa_tela(self):
        self.valor_entry.delete(0,END)
        self.frequencia_entry.delete(0,END)
    def variaveis(self):
        self.valor = self.valor_entry.get()
        self.frequencia = self.frequencia_entry.get()
    def add_valor(self):
        self.variaveis()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):    
        self.variaveis()
        iid = len(self.listaCli.get_children())
        if self.valor and self.frequencia:
            self.calc_freq_acumulada()
            self.listaCli.insert(parent='', index='end', values=(self.valor, self.frequencia, self.freq_acumulada), iid=iid)
    '''def calc_freq_relativa(self):
    self.variaveis()
    try:
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, 'values')[1]
            coluna_valores.append(int(valor))
        self.soma_freq = sum(coluna_valores)
        self.frequencia_int = int(self.frequencia)
        self.freq_relativa = (self.frequencia_int / self.soma_freq) * 100
    except:
        self.freq_relativa = 0  '''
    def calc_freq_acumulada(self):
        self.variaveis
        coluna_valores = []
        try:
            for item in self.listaCli.get_children():
                valor = self.listaCli.item(item, 'values')[1]
                coluna_valores.append(int(valor))
            self.soma_freq = sum(coluna_valores)
            self.freq_acumulada = self.soma_freq + int(self.frequencia)
        except:
            self.freq_acumulada = self.frequencia
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()
        self.freq_acumulada_entry = []
        for n in self.listaCli.selection():
            col1, col2, col3 = self.listaCli.item(n,'values')
            self.valor_entry.insert(END, col1) 
            self.frequencia_entry.insert(END, col2)
    def deleta_valor(self):
        self.variaveis()
        self.limpa_tela()
        for n in self.listaCli.selection():
            self.listaCli.delete(n)
            self.listaCli.update_idletasks()
    def calcular_media(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
                valor = self.listaCli.item(item, 'values')
                coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        df[2] = df[0] * df[1]
        print(df[2].sum() / df[1].sum())
    def calcular_moda(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
                valor = self.listaCli.item(item, 'values')
                coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        moda = df[1].max()
        classe_modal = df.loc[df[1] == moda]
        print(int(classe_modal[0]))
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()
        self.widgets_frame3()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#53524B')
        self.root.geometry("788x1000")
        self.root.resizable(True, True)
        self.root.maxsize(width = 900, height= 700)
        self.root.minsize(width= 500, height= 400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bg='#B4B2A2' )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight= 0.30)
        self.frame_2 = Frame(self.root, bg='#B4B2A2')
        self.frame_2.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.30)
        self.frame_3 = Frame(self.root, bg='#B4B2A2')
        self.frame_3.place(relx=0.02, rely=0.68, relwidth=0.96, relheight=0.30)
    def widgets_frame1(self):
        ###Criação do botão Limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", font=('verdana', 10, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.07, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão Novo
        self.novo = Button(self.frame_1, text="Novo", font=('verdana', 10, 'bold'), command=self.add_valor)
        self.novo.place(relx=0.19, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão Apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar", font=('verdana', 10, 'bold'), command=self.deleta_valor)
        self.bt_limpar.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.15)
    
        ## Criação da label e entrada do valor
        self.lb_codigo = Label(self.frame_1, text="valor", font=('verdana', 10, 'bold'), bg='#B4B2A2')
        self.lb_codigo.place(relx=0.07, rely=0.35)
        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx=0.07, rely=0.45, relwidth=0.85, relheight=0.12)
       
        ## Criação da label e entrada do telefrequencia
        self.lb_codigo = Label(self.frame_1, font=('verdana', 10, 'bold'), text="Frequência", bg='#B4B2A2')
        self.lb_codigo.place(relx=0.07, rely=0.60)
        self.frequencia_entry = Entry(self.frame_1)
        self.frequencia_entry.place(relx=0.07, rely=0.7, relwidth=0.85, relheight=0.12)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Valor")
        self.listaCli.heading("#2", text="Frequência Absoluta")
        self.listaCli.heading("#3", text="Frequência Acumulada")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=100)
        self.listaCli.column("#2", width=300)
        self.listaCli.column("#3", width=300)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def widgets_frame3(self):
        self.bt_media = Button(self.frame_3, text="Média", font=('verdana', 10, 'bold'), command=self.calcular_media)
        self.bt_media.place(relx=0.07, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_mediana = Button(self.frame_3, text="Mediana", font=('verdana', 10, 'bold'))
        self.bt_mediana.place(relx=0.19, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_moda = Button(self.frame_3, text="Moda", font=('verdana', 10, 'bold'), command= self.calcular_moda)
        self.bt_moda.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_desvio_padrao = Button(self.frame_3, text="Desvio Padrão", font=('verdana', 10, 'bold'))
        self.bt_desvio_padrao.place(relx=0.50, rely=0.1, relwidth=0.15, relheight=0.15)
        self.bt_coef_variacao = Button(self.frame_3, text="Coeficiente de Variação", font=('verdana', 10, 'bold'))
        self.bt_coef_variacao.place(relx=0.67, rely=0.1, relwidth=0.25, relheight=0.15)
Application()

### Atualização do projeto