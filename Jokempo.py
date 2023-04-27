# Criador: João Pedro Bassetto Pulquério de Souza
# GitHub: https://github.com/Rigimon

# Importando Bibliotecas
import tkinter as tk
from tkinter import messagebox
import random

# Resposta do computaor e verificação de vitória
def jokempo():

    try:
        if var.get() == 1:
            textol = 'pedra'

        if var.get() == 2:
            textol = 'papel'

        if var.get() == 3:
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

# Dividindo os Frames do jogo, Frame -> Divisões de tela
op = tk.LabelFrame(janela, text='Escolha:')
op.grid(row=0, padx=15)

botao = tk.Frame(janela)
botao.grid(row=2)

# Variavel para identificar qual a escolha do usuario
var = tk.IntVar()
var.set(0)

# Escolha do usuario
pedra = tk.Radiobutton(op, text='pedra', variable=var, value=1).grid(column=0, row=2)
papel = tk.Radiobutton(op, text='papel', variable=var, value=2).grid(column=1, row=2)
tesoura = tk.Radiobutton(op, text='tesoura', variable=var, value=3).grid(column=2, row=2)

# Escolha do Computador
resposta = tk.Label(janela, text="")
resposta.grid(row=1)

# Botão para jogar
jogar = tk.Button(botao, text='Jogar', command=jokempo)
jogar.grid(column=0,row=1)

# Botão para fechar o jogo
sair = tk.Button(botao, text='Sair', command=janela.destroy)
sair.grid(column=1,row=1)

janela.mainloop()
