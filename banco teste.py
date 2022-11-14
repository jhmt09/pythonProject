import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import mysql.connector
from mysql.connector import errorcode


class Toplevel1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black'
        _tabfg2 = 'black'
        _tabbg1 = 'grey75'
        _tabbg2 = 'grey89'
        _bgmode = 'light'


        self.root = tk.Tk()
        self.root.geometry("600x450+258+102")
        self.root.minsize(120, 1)
        self.root.maxsize(1370, 749)
        self.root.resizable(1, 1)
        self.root.title("Login")
        self.root.configure(background="#00008a")
        self.root.configure(cursor="arrow")


        self.FrameCadastro = tk.Frame(self.root)
        self.FrameCadastro.place(relx=0.233, rely=0.089, relheight=0.833
                , relwidth=0.542)
        self.FrameCadastro.configure(relief='solid')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(relief="solid")
        self.FrameCadastro.configure(background="#b30059")
        self.FrameCadastro.configure(highlightcolor="#ffffff")

        self.Entry1 = tk.Entry(self.FrameCadastro)
        self.Entry1.place(relx=0.062, rely=0.427, height=20, relwidth=0.689)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.FrameCadastro, show='*')
        self.Entry2.place(relx=0.062, rely=0.587, height=20, relwidth=0.689)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label1Cadastro = tk.Label(self.FrameCadastro)
        self.Label1Cadastro.place(relx=0.338, rely=0.187, height=22, width=98)
        self.Label1Cadastro.configure(anchor='w')
        self.Label1Cadastro.configure(background="#d9d9d9")
        self.Label1Cadastro.configure(compound='left')
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {Arial} -size 14 -weight bold")
        self.Label1Cadastro.configure(foreground="#000000")
        self.Label1Cadastro.configure(text='''Login''')

        self.Label2 = tk.Label(self.FrameCadastro)
        self.Label2.place(relx=0.062, rely=0.347, height=21, width=64)
        self.Label2.configure(activeforeground="#eaeaea")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#eaeaea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 9 -weight bold -slant italic")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Usuário''')

        self.Label3 = tk.Label(self.FrameCadastro)
        self.Label3.place(relx=0.062, rely=0.507, height=21, width=64)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial} -size 9 -weight bold -slant italic")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Senha''')

        self.Button1Cadastro = tk.Button(self.FrameCadastro, command=self.LoginBackEnd)
        self.Button1Cadastro.place(relx=0.308, rely=0.693, height=34, width=107)
        self.Button1Cadastro.configure(activebackground="beige")
        self.Button1Cadastro.configure(activeforeground="#000000")
        self.Button1Cadastro.configure(background="#000097")
        self.Button1Cadastro.configure(compound='left')
        self.Button1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastro.configure(font="-family {Arial} -size 10 -weight bold")
        self.Button1Cadastro.configure(foreground="#000000")
        self.Button1Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastro.configure(highlightcolor="black")
        self.Button1Cadastro.configure(pady="0")
        self.Button1Cadastro.configure(text='''Logar''')

        self.Button2Cadastro = tk.Button(self.FrameCadastro, command=self.Cadastro)
        self.Button2Cadastro.place(relx=0.308, rely=0.827, height=34, width=107)
        self.Button2Cadastro.configure(activebackground="beige")
        self.Button2Cadastro.configure(activeforeground="#000000")
        self.Button2Cadastro.configure(background="#000093")
        self.Button2Cadastro.configure(compound='left')
        self.Button2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button2Cadastro.configure(font="-family {Arial} -size 10 -weight bold")
        self.Button2Cadastro.configure(foreground="#000000")
        self.Button2Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button2Cadastro.configure(highlightcolor="black")
        self.Button2Cadastro.configure(pady="0")
        self.Button2Cadastro.configure(text='''Cadastrar''')
        self.root.mainloop()



    def Cadastro(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40'  # X11 color: #666666
        _ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
        _ana2color = 'beige'  # X11 color: #f5f5dc
        _tabfg1 = 'black'
        _tabfg2 = 'black'
        _tabbg1 = 'grey75'
        _tabbg2 = 'grey89'
        _bgmode = 'light'

        self.root = tk.Tk()
        self.root.geometry("600x450+258+102")
        self.root.minsize(120, 1)
        self.root.maxsize(1370, 749)
        self.root.resizable(1, 1)
        self.root.title("Cadastro")
        self.root.configure(background="#00008a")
        self.root.configure(cursor="arrow")

        self.FrameCadastro = tk.Frame(self.root)
        self.FrameCadastro.place(relx=0.233, rely=0.089, relheight=0.833
                          , relwidth=0.542)
        self.FrameCadastro.configure(relief='solid')
        self.FrameCadastro.configure(borderwidth="2")
        self.FrameCadastro.configure(relief="solid")
        self.FrameCadastro.configure(background="#b30059")
        self.FrameCadastro.configure(highlightcolor="#ffffff")

        self.Entry1Cadastro = tk.Entry(self.FrameCadastro)
        self.Entry1Cadastro.place(relx=0.062, rely=0.427, height=20, relwidth=0.689)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(insertbackground="black")

        self.Entry2Cadastro = tk.Entry(self.FrameCadastro, show='*')
        self.Entry2Cadastro.place(relx=0.062, rely=0.587, height=20, relwidth=0.689)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(insertbackground="black")

        self.Label1Cadastro = tk.Label(self.FrameCadastro)
        self.Label1Cadastro.place(relx=0.338, rely=0.187, height=22, width=98)
        self.Label1Cadastro.configure(anchor='w')
        self.Label1Cadastro.configure(background="#d9d9d9")
        self.Label1Cadastro.configure(compound='left')
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font="-family {Arial} -size 14 -weight bold")
        self.Label1Cadastro.configure(foreground="#000000")
        self.Label1Cadastro.configure(text='''Cadastro''')

        self.Label2 = tk.Label(self.FrameCadastro)
        self.Label2.place(relx=0.062, rely=0.347, height=21, width=64)
        self.Label2.configure(activeforeground="#eaeaea")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#eaeaea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 9 -weight bold -slant italic")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Usuário''')

        self.Label3 = tk.Label(self.FrameCadastro)
        self.Label3.place(relx=0.062, rely=0.507, height=21, width=64)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial} -size 9 -weight bold -slant italic")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Senha''')

        self.Button2Cadastro= tk.Button(self.FrameCadastro, command=self.CadastrarBackEnd)
        self.Button2Cadastro.place(relx=0.308, rely=0.827, height=34, width=107)
        self.Button2Cadastro.configure(activebackground="beige")
        self.Button2Cadastro.configure(activeforeground="#000000")
        self.Button2Cadastro.configure(background="#000093")
        self.Button2Cadastro.configure(compound='left')
        self.Button2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button2Cadastro.configure(font="-family {Arial} -size 10 -weight bold")
        self.Button2Cadastro.configure(foreground="#000000")
        self.Button2Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button2Cadastro.configure(highlightcolor="black")
        self.Button2Cadastro.configure(pady="0")
        self.Button2Cadastro.configure(text='''Cadastrar''')
        self.root.mainloop()


    def CadastrarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get() + '\n')

            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry2Cadastro.get() + '\n')
            self.root.destroy()
        except:
            print('Há algo errado!')
    def LoginBackEnd(self):

        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))
        senhas = list(map(lambda x: x.replace('\n', ''), senhas))

        usuario = self.Entry1.get()
        senha = self.Entry2.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas [i]:
                print('usuario logado!')
                self.root.destroy()
                logado = True
                try:
                    net = mysql.connector.connect(host='localhost', database='projectg5', user='root',
                                                  password='@panzerpanzer3556')

                    consulta_sql = 'select*from detentos'
                    cursor = net.cursor()
                    cursor.execute(consulta_sql)
                    linhas = cursor.fetchall()
                    print('Numero total de registros retornados', cursor.rowcount)

                    print('Mostrando os Detentos cadastrados')
                    for linha in linhas:
                        print('=-' * 30)
                        print('Id', linha[0])
                        print('Nome', linha[1])
                        print('data de nascimento', linha[2])
                        print('Sexo', linha[3])
                        print('Endereço', linha[4])
                        print('RG', linha[5])
                        print('Situação', linha[6])
                        print('=-' * 30)




                except IOError as e:
                    print('Erro ao acessar tabela', e)
                finally:
                    if (net.is_connected()):
                        net.close()
                        cursor.close()
                        print('Conexão encerrada')

        if not logado:
            print('Usuario não cadastrado!')








Toplevel1()


