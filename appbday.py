from tkinter import *
from datetime import datetime
from tkinter import messagebox
import tkinter

class Bday:
    cor_fundo = '#13633B'
    cor_botao = '#2BE387'

    def __init__(self):
        self.root = root
        self.widgets()
        self.config_tela()

        root.mainloop()

    def config_tela(self):
        self.root.title('Niver Calculator')
        self.root.geometry('600x600')
        self.root.resizable(False,False)
        self.root.iconbitmap('Aniversário app\\niver.ico')
        self.root.configure(bg=self.cor_fundo)

    def widgets(self):
        txt1 = Label(root, text='Calculadora',bg=self.cor_fundo,fg='black',font='Arial 39 bold')
        txt1.place(x=150,y=40)

        txt2 = Label(root, text='de',bg=self.cor_fundo,fg='black',font='Arial 22 bold')
        txt2.place(x=280,y=96)

        txt3 = Label(root, text='Aniversário',bg=self.cor_fundo,fg='black',font='Arial 27 bold')
        txt3.place(x=200,y=129)

        txt4 = Label(root, text='Dia:',bg=self.cor_fundo,fg='black',font='Arial 18 bold')
        txt4.place(x=186, y=270)
        self.entr1 = Entry(root, bg='white', fg='black', font='Arial 22 bold', border=0)
        self.entr1.place(x=186, y=300, width=255, height= 42)
        '''self.entr1.insert(tkinter.END, '2')'''#Insere um Texto no Entry

        txt5 = Label(root, text='Mês:',bg=self.cor_fundo,fg='black',font='Arial 18 bold')
        txt5.place(x=186, y=350)
        self.entr2 = Entry(root, bg='white', fg='black', font='Arial 22 bold', border=0)
        self.entr2.place(x=186, y=380, width=255, height= 42)
        '''self.entr2.insert(tkinter.END, '12')'''#Insere um Texto no Entry

        btn1 = Button(root, text='Ver!', bg=self.cor_botao, fg='black', font='Arial 22 bold', command=self.verbday, border=0)
        btn1.place(x=230, y=500, width=171, height=45)

    def verbday(self):

        try:
            dia = int(self.entr1.get())
            mes = int(self.entr2.get())
            ano = datetime.now().year



            if mes >= datetime.now().month:
                data = datetime.strptime(f'{dia + 1}/{mes}/{ano}','%d/%m/%Y')
                if dia <= datetime.now().day and mes == datetime.now().month:
                    data = datetime.strptime(f'{dia}/{mes}/{ano + 1}','%d/%m/%Y')
            elif mes < datetime.now().month:
                data = datetime.strptime(f'{dia}/{mes}/{ano + 1}','%d/%m/%Y')
                

            data_atual = datetime.now()
            dia_bday = data - data_atual

            messagebox.showinfo(title='Quantos dias faltam?', message=f'Faltam {dia_bday.days} dias para o seu aniversário!')

        except:
            messagebox.showinfo(title='Algo deu errado!', message='Você não digitou ou colocou algo errado, tente novamente')


root = Tk()
Bday()
