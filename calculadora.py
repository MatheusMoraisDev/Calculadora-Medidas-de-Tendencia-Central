from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

root = Tk()

class Funcs:
    def limpa_tela(self):
        self.valor_entry.delete(0, END)
        self.frequencia_entry.delete(0, END)

    def variaveis(self):
        self.valor = self.valor_entry.get()
        self.frequencia = self.frequencia_entry.get()

    def add_valor(self):
        self.variaveis()
        if self.valor or self.frequencia:
            if self.valor.isdigit() and self.frequencia.isdigit():
                self.select_lista()
                self.limpa_tela()
            else:
                messagebox.showerror("Erro", "Insira somente números!")
        else:
            messagebox.showerror("Erro", "Insira alguma coisa!")
    def select_lista(self):
        self.variaveis()
        if self.valor or self.frequencia:
            iid = len(self.listaCli.get_children())
            self.calc_freq_acumulada()
            self.listaCli.insert(
                parent="",
                index="end",
                values=(self.valor, self.frequencia, self.freq_acumulada),
                iid=iid,
            )

    def calc_freq_acumulada(self):
        self.variaveis
        coluna_valores = []
        try:
            for item in self.listaCli.get_children():
                valor = self.listaCli.item(item, "values")[1]
                coluna_valores.append(int(valor))
            self.soma_freq = sum(coluna_valores)
            self.freq_acumulada = self.soma_freq + int(self.frequencia)
        except:
            self.freq_acumulada = self.frequencia

    def atualizar_freq_acumulada(self):
        items = self.listaCli.get_children()
        freq_acumulada = 0
        for item in items:
            freq_absoluta = int(self.listaCli.item(item, "values")[1])
            freq_acumulada += freq_absoluta
            self.listaCli.item(item, values=(self.listaCli.item(item, "values")[0], freq_absoluta, freq_acumulada))

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()
        self.freq_acumulada_entry = []
        for n in self.listaCli.selection():
            col1, col2, col3 = self.listaCli.item(n, "values")
            self.valor_entry.insert(END, col1)
            self.frequencia_entry.insert(END, col2)

    def deleta_valor(self):
        self.variaveis()
        self.limpa_tela()
        for n in self.listaCli.selection():
            self.listaCli.delete(n)
            self.listaCli.update_idletasks()
        self.atualizar_freq_acumulada()

    def calcular_media(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, "values")
            coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        df[2] = df[0] * df[1]
        media = df[2].sum() / df[1].sum()
        return media

    def calcular_moda(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, "values")
            coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        moda = df[1].max()
        classe_modal = df.loc[df[1] == moda]
        return int(classe_modal[0])

    def calcular_desvioPadrao(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, "values")
            coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        df[2] = df[0] * df[1]
        media = df[2].sum() / df[1].sum()
        mediaElevada = ((df[0] ** 2) * df[1]).sum() / df[1].sum()
        desvioPadrao = (mediaElevada - ((media) ** 2)) ** 0.5
        return desvioPadrao

    def calcular_mediana(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, "values")
            coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        n = df[1].sum()
        if n % 2 == 0:
            mediana = df[1].sum() / 2
        else:
            mediana = (df[1].sum() + 1) / 2
        return int(mediana)

    def calcular_coeficienteDeVariacao(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, "values")
            coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        coeficiente = (self.calcular_desvioPadrao() / self.calcular_media()) *100
        return coeficiente

    def calcular_amplitude_total(self):
        coluna_valores = []
        for item in self.listaCli.get_children():
            valor = self.listaCli.item(item, "values")
            coluna_valores.append(valor)
        df = pd.DataFrame(coluna_valores)
        df.drop(columns=[2], inplace=True)
        df[0] = df[0].apply(lambda x: int(x))
        df[1] = df[1].apply(lambda x: int(x))
        return int(df[0].max() - df[0].min())

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
        self.root.title("Calculadora de Medidas de Tendências Central")
        self.root.configure(background="#ffffff")
        self.root.geometry("788x550")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bg="#ffffff")
        self.frame_1.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.7)
        self.frame_3 = Frame(self.root, bg="#ffffff")
        self.frame_3.place(relx=0.02, rely=0.68, relwidth=0.96, relheight=0.30)

    def widgets_frame1(self):
        ###Criação do Título da Página
        self.lb_titulo = Label(
            self.frame_1, text="Calculadora - Medidas de Tendência Central", font=("verdana", 14, "bold"), bg="#ffffff"
        )
        self.lb_titulo.place(relx=0.17, rely=0.07)
        ###Criação do botão Limpar
        self.bt_limpar = Button(
            self.frame_1,
            text="Limpar",
            font=("verdana", 10, "bold"),
            command=self.limpa_tela,
        )
        self.bt_limpar.place(relx=0.88, rely=0.85, relwidth=0.1, relheight=0.1)

        ###Criação do botão Novo
        self.novo = Button(
            self.frame_1,
            text="Novo",
            font=("verdana", 10, "bold"),
            command=self.add_valor,
        )
        self.novo.place(relx=0.02, rely=0.2, relwidth=0.1, relheight=0.1)

        ## Criação da label e entrada do valor
        self.lb_valor = Label(
            self.frame_1, text="Valor", font=("verdana", 10, "bold"), bg="#ffffff"
        )
        self.lb_valor.place(relx=0.19, rely=0.2)
        
        self.valor_entry = Entry(self.frame_1, background="#D9D9D9")
        self.valor_entry.place(relx=0.19, rely=0.25, relwidth=0.1, relheight=0.05)

        ## Criação da label e entrada da frequência
        self.lb_frequencia = Label(
            self.frame_1, font=("verdana", 10, "bold"), text="Frequência", bg="#ffffff"
        )
        self.lb_frequencia.place(relx=0.35, rely=0.2)
        self.frequencia_entry = Entry(self.frame_1,  background="#D9D9D9")
        self.frequencia_entry.place(relx=0.35, rely=0.25, relwidth=0.1, relheight=0.05)

    def lista_frame2(self):
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Custom.Treeview", fieldbackground="#D9D9D9", background="#D9D9D9", forebackground='#D9D9D9')
        self.listaCli = ttk.Treeview(self.frame_1, height=3, column=("col1", "col2", "col3", "col4"), style="Custom.Treeview")
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Valor")
        self.listaCli.heading("#2", text="Frequência Absoluta")
        self.listaCli.heading("#3", text="Frequência Acumulada")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=100)
        self.listaCli.column("#2", width=300)
        self.listaCli.column("#3", width=300)
        self.listaCli.place(relx=0.02, rely=0.4, relwidth=0.94, relheight=0.4)
        self.scrollLista = Scrollbar(self.frame_1, orient="vertical")
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.95, rely=0.4, relwidth=0.03, relheight=0.4)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def widgets_frame3(self):
        self.bt_media = Button(
            self.frame_3,
            text="Média",
            font=("verdana", 10, "bold"),
            command=lambda: self.exibir_resultado(self.calcular_media()),
        )
        self.bt_media.place(relx=0.06, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_mediana = Button(
            self.frame_3,
            text="Mediana",
            font=("verdana", 10, "bold"),
            command=lambda: self.exibir_resultado(self.calcular_mediana()),
        )
        self.bt_mediana.place(relx=0.17, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_moda = Button(
            self.frame_3,
            text="Moda",
            font=("verdana", 10, "bold"),
            command=lambda: self.exibir_resultado(self.calcular_moda()),
        )
        self.bt_moda.place(relx=0.28, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_desvio_padrao = Button(
            self.frame_3,
            text="Desvio Padrão",
            font=("verdana", 10, "bold"),
            command=lambda: self.exibir_resultado(self.calcular_desvioPadrao()),
        )
        self.bt_desvio_padrao.place(relx=0.39, rely=0.1, relwidth=0.15, relheight=0.15)
        self.bt_coef_variacao = Button(
            self.frame_3,
            text="Coeficiente de Variação",
            font=("verdana", 10, "bold"),
            command=lambda: self.exibir_resultado(self.calcular_coeficienteDeVariacao()),
        )
        self.bt_coef_variacao.place(relx=0.55, rely=0.1, relwidth=0.23, relheight=0.15)
        
        self.bt_amp_total = Button(
            self.frame_3,
            text="Amplitude Total",
            font=("verdana", 10, "bold"),
            command=lambda: self.exibir_resultado(self.calcular_amplitude_total()),
        )
        self.bt_amp_total.place(relx=0.79, rely=0.1, relwidth=0.16, relheight=0.15)

        self.resultado_label = Label(
            self.frame_3,
            font=("verdana", 10, "bold"),
        )
        self.resultado_label.place(relx=0.39, rely=0.4, relwidth=0.20, relheight=0.15)
        
        self.bt_limpar = Button(
            self.frame_3,
            text="Apagar",
            font=("verdana", 10, "bold"),
            command=self.deleta_valor,
        )
        self.bt_limpar.place(relx=0.44, rely=0.7, relwidth=0.1, relheight=0.15)

    def exibir_resultado(self, resultado):
        self.resultado_label.config(text="Resultado: {:.4f}".format(resultado))


Application()