# Criador: João Pedro Bassetto Pulquério de Souza
# GitHub: https://github.com/Rigimon

# Importando Bibliotecas
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import random

# Resposta do computaor e verificação de vitória
def jokempo():

    try:
        if var.get() == 'pedra':
            textol = 'pedra'

        if var.get() == 'papel':
            textol = 'papel'

        if var.get() == 'tesoura':
            textol = 'tesoura'

        lista = ['pedra','papel','tesoura']
        resp = random.choice(lista)

        opcao = {'pedra':'tesoura',
                 'papel':'pedra',
                 'tesoura':'papel'}

        if opcao[textol] == resp:
            resultado = 'Vitória'
        elif textol == resp:
            resultado = 'Empate'
        else:
            resultado = 'Derrota'
        resposta["text"] = 'Oponente: ' + resp
        messagebox.showinfo('Resultado: ', resultado)
    except:
        messagebox.showinfo('Resultado: ', 'Escolha uma opção antes')

# Criação da Janela do jogo
janela = tk.Tk()
janela.title('Jokempo')
janela.resizable(False,False)
janela.config(background='LightSkyBlue')

# Dividindo os Frames do jogo, Frame -> Divisões de tela
op = ctk.CTkFrame(janela,fg_color='LightSkyBlue')
op.grid(row=0, padx=15,pady=5)

botao = tk.Frame(janela,background='LightSkyBlue')
botao.grid(row=2)

# Variavel para identificar qual a escolha do usuario
var = tk.StringVar()

# Escolha do usuario
Texto = ctk.CTkLabel(op, text='Escolha:',text_color='White').grid()
option = ctk.CTkOptionMenu(op, values=["pedra", "papel","tesoura"], variable=var).grid(padx=5,pady=5)

# Escolha do Computador
resposta = tk.Label(janela, text="")
resposta.grid(row=1)

# Botão para jogar
jogar = ctk.CTkButton(botao, text='Jogar',width=3, command=jokempo)
jogar.grid(column=0,row=1,padx=1,pady=3)

# Botão para fechar o jogo
sair = ctk.CTkButton(botao, text='Sair',width=3, command=janela.destroy)
sair.grid(column=1,row=1,padx=1,pady=3)

janela.mainloop()
