from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from venda import Venda

APP_TITLE = 'Meu Sistema'
root = Tk()

def showJanela(event=None):
    window = tkinter.Toplevel(root)
    window.title('Registro de Vendas')
    window.geometry('500x500')
    window.transient(root)
    Venda(window)
    root.wait_window(window)
    
def showSobre(event=None):
    tkinter.messagebox.showinfo('Sobre', 
                                '{}{}'.format(APP_TITLE, 'Meu Sistema Gráfico\ncom Python e Tkinter'))


def sair(event=None):
    if tkinter.messagebox.askokcancel("Sair", "Deseja realmente sair??"):
        root.destroy()

def montarMenu(event=None):
    menu_bar = Menu(root)
    arc_menu = Menu(menu_bar, tearoff=0)
    aux_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Arquivo', underline=0, menu=arc_menu)
    menu_bar.add_cascade(label='Ajuda', underline=0, menu=aux_menu)
    root.config(menu=menu_bar)

    arc_menu.add_command(label='Venda', compound='left', command=showJanela)
    arc_menu.add_separator()
    arc_menu.add_command(label='Sair', compound='left', command=sair)

    aux_menu.add_command(label='Sobre', compound='left', command=showSobre)

def principal():
    montarMenu()
    root.protocol("WM_DELETE_WINDOW", sair)
    root.title(APP_TITLE)
    root.geometry("600x600")
    root.mainloop()

if __name__ == '__main__':
    principal()