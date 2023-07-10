from tkinter import *
import tkinter.messagebox

class Venda:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master, padx=5, pady=5)
        self.container1.pack()
        self.lblpin = Label(self.container1, text='PIN', font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblpin.pack(side=LEFT)
        self.txtpin = Entry(self.container1, width=10, font=self.fonte)
        self.txtpin.pack(side=LEFT)
        self.btnbuscar = Button(self.container1, text='Buscar', font=self.fonte, width=10)
        self.btnbuscar['command'] = self.buscarVenda
        self.btnbuscar.pack(side=RIGHT, padx=10)

        self.container2 = Frame(master, padx=5, pady=5)
        self.container2.pack()
        self.lblproduto = Label(self.container2, text='Produto', font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblproduto.pack(side=LEFT)
        self.txtproduto = Entry(self.container2, width=10, font=self.fonte)
        self.txtproduto.pack(side=LEFT)

        self.container3 = Frame(master, padx=5, pady=5)
        self.container3.pack()
        self.lblvendedor = Label(self.container3, text='Vendedor(a)', font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblvendedor.pack(side=LEFT)
        self.txtvendedor = Entry(self.container3, width=10, font=self.fonte)
        self.txtvendedor.pack(side=LEFT)

        self.container4 = Frame(master, padx=5, pady=5)
        self.container4.pack()
        self.lblvalor = Label(self.container4, text='Valor Unitário', font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblvalor.pack(side=LEFT)
        self.txtvalor = Entry(self.container4, width=10, font=self.fonte)
        self.txtvalor.pack(side=LEFT)

        self.container5 = Frame(master, padx=5, pady=5)
        self.container5.pack()
        self.lblquantidade = Label(self.container5, text='Quantidade', font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblquantidade.pack(side=LEFT)
        self.txtquantidade = Entry(self.container5, width=10, font=self.fonte)
        self.txtquantidade.pack(side=LEFT)

        self.container6 = Frame(master, padx=5, pady=5)
        self.container6.pack()
        self.lblunidade = Label(self.container6, text='Unidade', font=self.fonte, width=10, anchor=E, justify=RIGHT)
        self.lblunidade.pack(side=LEFT)
        self.txtunidade = Entry(self.container6, width=10, font=self.fonte)
        self.txtunidade.pack(side=LEFT)

        self.container7 = Frame(master, padx=5, pady=5)
        self.container7.pack()
        self.btninserir = Button(self.container7, text='Inserir', font=self.fonte, width=10)
        self.btninserir['command'] = self.inserirVenda
        self.btninserir.pack(side=RIGHT, padx=10)

        self.container8 = Frame(master, padx=5, pady=5)
        self.container8.pack()
        self.btnalterar = Button(self.container7, text='Alterar', font=self.fonte, width=10)
        self.btnalterar['command'] = self.alterarVenda
        self.btnalterar.pack(side=RIGHT, padx=10)

        self.container9 = Frame(master, padx=5, pady=5)
        self.container9.pack()
        self.btnexcluir = Button(self.container9, text='Excluir', font=self.fonte, width=10)
        self.btnexcluir['command'] = self.excluirVenda
        self.btnexcluir.pack(side=RIGHT, padx=10)

    def buscarVenda(self):
        tkinter.messagebox.showinfo('Buscar', 'busca uma venda', icon='info')

    def inserirVenda(self):
        tkinter.messagebox.showinfo('Inserir', 'Insere uma venda', icon='info')

    def alterarVenda(self):
        tkinter.messagebox.showinfo('Alterar', 'Altera uma venda', icon='info')

    def excluirVenda(self):
        tkinter.messagebox.showinfo('Excluir', 'Excluir uma venda', icon='info')