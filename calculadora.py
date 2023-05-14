from tkinter import *
from tkinter import ttk
root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.fone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.variaveis()
        iid = len(self.listaCli.get_children())
        if self.codigo or self.nome or self.fone or self.cidade:
            self.listaCli.insert(parent='', index='end', values=(self.codigo, self.nome, self.fone, self.cidade), iid=iid)      
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()
        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n,'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2) 
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis()
        self.limpa_tela()
        for n in self.listaCli.selection():
            self.listaCli.delete(n)
            self.listaCli.update_idletasks()   
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()
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
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão Buscar
        self.buscar = Button(self.frame_1, text="Buscar", font=('verdana', 10, 'bold'))
        self.buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão Novo
        self.novo = Button(self.frame_1, text="Novo", font=('verdana', 10, 'bold'), command=self.add_cliente)
        self.novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ###Criação do botão Alterar
        self.alterar = Button(self.frame_1, text="Alterar", font=('verdana', 10, 'bold'))
        self.alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
       
        ###Criação do botão Apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar", font=('verdana', 10, 'bold'), command=self.deleta_cliente)
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ## Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código", font=('verdana', 10, 'bold'), bg='#B4B2A2')
        self.lb_codigo.place(relx=0.05, rely= 0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do nome
        self.lb_codigo = Label(self.frame_1, text="Nome", font=('verdana', 10, 'bold'), bg='#B4B2A2')
        self.lb_codigo.place(relx=0.05, rely=0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85)
       
        ## Criação da label e entrada do telefone
        self.lb_codigo = Label(self.frame_1, font=('verdana', 10, 'bold'), text="Telefone", bg='#B4B2A2')
        self.lb_codigo.place(relx=0.05, rely=0.60)
        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        ## Criação da label e entrada da cidade
        self.lb_codigo = Label(self.frame_1, text="Cidade", font=('verdana', 10, 'bold'), bg='#B4B2A2')
        self.lb_codigo.place(relx=0.5, rely=0.6)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
Application()