from Controller import Instagem
from tkinter import *


main = Tk()
var = IntVar()

class Iniciar():
    def inicia(self):
        selection = var.get()
        self.bot = Instagem()
        self.linkfoto()

        if selection == 1:
            self.marcarAmigos()
        else:
            self.comenta()
            a = Instagem()
            a.threading()

    def linkfoto(self):
        self.bot.Postagem(self.LinkInstagram.get())

    def comenta(self):
        qTd = int(self.QtdComentarios.get())
        iVcS = int(self.IntervaloComentariosSeg.get())
        self.bot.Comenta(qTd, iVcS)

    def marcarAmigos(self):
        AqTd = int(self.QtdComentarios.get())
        AiVcS = int(self.IntervaloComentariosSeg.get())

        self.bot.Marca_Amigo(AqTd, AiVcS)

class Aplicacao(Iniciar):
    def __init__(self):
        self.main = main
        self.principal()
        self.frame()
        self.botao()
        main.mainloop()

    def principal(self):
        self.main.title('Boot comentario instagram')
        self.main.geometry('800x500')
        self.main.resizable(False, False)

    def frame(self):
        self.framePrincipal = Frame(self.main, bg='#F8F8FF', highlightbackground='black')
        self.framePrincipal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def botao(self):
        Label(self.framePrincipal, text='Link do instagram', bg='white', fg='#B22222').place(relx=0.08, rely=0.20)
        self.LinkInstagram = Entry(self.framePrincipal)
        self.LinkInstagram.place(relx=0.30, rely=0.20, width=500)
        Label(self.framePrincipal,text='Quantidade de comentarios' ,bg='white',fg='#B22222').place(relx=0.08,rely=0.30)
        self.QtdComentarios=Entry(self.framePrincipal)
        self.QtdComentarios.place(relx=0.35,rely=0.30 ,width=50)

        Label(self.framePrincipal,text='Marcar amigo ?',bg='white',fg='#B22222').place(relx=0.08,rely=0.35)

        Radiobutton(self.framePrincipal,text='Sim' ,bg='white',fg='#B22222',variable=var,value=1).place(relx=0.30,rely=0.35)
        Radiobutton(self.framePrincipal, text='Nao', bg='white', fg='#B22222',variable=var,value=2).place(relx=0.40, rely=0.35)

        Label(self.framePrincipal, text='Intervalo entre comentarios em Segundos', bg='white',fg='#B22222').place(relx=0.08, rely=0.40)
        self.IntervaloComentariosSeg=Entry(self.framePrincipal)
        self.IntervaloComentariosSeg.place(relx=0.45, rely=0.40,width=50)
        self.Btniniciar = Button(self.main, text='Iniciar' ,command=self.inicia)
        self.Btniniciar.place(relx=0.2, rely=0.60, width=100, height=30)
        self.Btnsair = Button(self.main, text='Sair' ,command=self.main.destroy)
        self.Btnsair.place(relx=0.40, rely=0.60, width=100, height=30)
Aplicacao()