# Edição Definitiva

# Criador: João Pedro Bassetto Pulquério de Souza
# GitHub: https://github.com/Rigimon

# Importando Bibliotecas
import tkinter as tk
from tkinter import messagebox
import random

# Variaveis Globais
player = 1             # Identificar qual player está jogando
var = [[0,0,0],        # Tela em si
       [0,0,0],
       [0,0,0]]

# Resetar a tela sempre que trocar de modo
def Reset():
    global var
    var = [[0,0,0],
           [0,0,0],
           [0,0,0]]
    img1['text'] = '   '
    img2['text'] = '   '
    img3['text'] = '   '
    img4['text'] = '   '
    img5['text'] = '   '
    img6['text'] = '   '
    img7['text'] = '   '
    img8['text'] = '   '
    img9['text'] = '   '
    
# Identificar se acabou o jogo, com base nas possibilidades de vitória ou se n tiver mais espaço na tela
def fim():
    possibilidades = [[var[0][0],var[0][1],var[0][2]],
                      [var[1][0],var[1][1],var[1][2]],
                      [var[2][0],var[2][1],var[2][2]],
                      [var[0][0],var[1][0],var[2][0]],
                      [var[0][1],var[1][1],var[2][1]],
                      [var[0][2],var[1][2],var[2][2]],
                      [var[0][0],var[1][1],var[2][2]],
                      [var[0][2],var[1][1],var[2][0]]]
    for i in possibilidades:
        if mode_choice.get() == 1:
            if i == [1,1,1]:
                messagebox.showinfo('Resultado: ', 'Vitória')
                return True
            if i == [2,2,2]:
                messagebox.showinfo('Resultado: ', 'Derrota')
                return True
        else:
            if i == [1,1,1]:
                messagebox.showinfo('Resultado: ', '"O" Venceu')
                return True
            if i == [2,2,2]:
                messagebox.showinfo('Resultado: ', '"X" Venceu')
                return True
    if var[0][0] != 0 and var[0][1] != 0 and var[0][2] != 0 and var[1][0] != 0 and var[1][1] != 0 and var[1][2] != 0 and var[2][0] != 0 and var[2][1] != 0 and var[2][2] != 0:
        messagebox.showinfo('Resultado: ', 'Empate')
        return True
    return False

# Verificar onde o usuario ou a maquina escolheu para colocar seu simbolo na tela
def Verify():
    if var[0][0] != 0:
        if var[0][0] != 1:
            img1['text'] = 'X'
            img1['fg'] = 'red'
        else:
            img1['text'] = 'O'
            img1['fg'] = 'blue'

    if var[0][1] != 0:
        if var[0][1] != 1:
            img2['text'] = 'X'
            img2['fg'] = 'red'
        else:
            img2['text'] = 'O'
            img2['fg'] = 'blue'

    if var[0][2] != 0:
        if var[0][2] != 1:
            img3['text'] = 'X'
            img3['fg'] = 'red'
        else:
            img3['text'] = 'O'
            img3['fg'] = 'blue'

    if var[1][0] != 0:
        if var[1][0] != 1:
            img4['text'] = 'X'
            img4['fg'] = 'red'
        else:
            img4['text'] = 'O'
            img4['fg'] = 'blue'

    if var[1][1] != 0:
        if var[1][1] != 1:
            img5['text'] = 'X'
            img5['fg'] = 'red'
        else:
            img5['text'] = 'O'
            img5['fg'] = 'blue'

    if var[1][2] != 0:
        if var[1][2] != 1:
            img6['text'] = 'X'
            img6['fg'] = 'red'
        else:
            img6['text'] = 'O'
            img6['fg'] = 'blue'

    if var[2][0] != 0:
        if var[2][0] != 1:
            img7['text'] = 'X'
            img7['fg'] = 'red'
        else:
            img7['text'] = 'O'
            img7['fg'] = 'blue'

    if var[2][1] != 0:
        if var[2][1] != 1:
            img8['text'] = 'X'
            img8['fg'] = 'red'
        else:
            img8['text'] = 'O'
            img8['fg'] = 'blue'

    if var[2][2] != 0:
        if var[2][2] != 1:
            img9['text'] = 'X'
            img9['fg'] = 'red'
        else:
            img9['text'] = 'O'
            img9['fg'] = 'blue'
    cabo = fim()
    return cabo

# Acão do Player, onde ele escolhe jogar
def PlayerAction(i,j):
    global player
    if mode_choice.get() == 1:
        if fim() == False:
            while True:
                if var[i][j] == 0:
                    var[i][j] = 1
                    cabo = Verify()
                    if cabo == False:
                        ComputerAction()
                        break
                else:
                    break
    else:
        if fim() == False:
            while True:
                if player % 2 == 1:
                    if var[i][j] == 0:
                        var[i][j] = 1
                        cabo = Verify()
                        player += 1
                        break
                    else:
                        break
                else:
                    if var[i][j] == 0:
                        var[i][j] = 2
                        cabo = Verify()
                        player += 1
                        break
                    else:
                        break

# Ação do Computador, onde ele escolhe jogar
def ComputerAction():
    possibilidades = [[var[0][0],var[0][1],var[0][2]],
                      [var[1][0],var[1][1],var[1][2]],
                      [var[2][0],var[2][1],var[2][2]],
                      [var[0][0],var[1][0],var[2][0]],
                      [var[0][1],var[1][1],var[2][1]],
                      [var[0][2],var[1][2],var[2][2]],
                      [var[0][0],var[1][1],var[2][2]],
                      [var[0][2],var[1][1],var[2][0]]]
    linha = {0:[0,0,0],
             1:[1,1,1],
             2:[2,2,2],
             3:[0,1,2],
             4:[0,1,2],
             5:[0,1,2],
             6:[0,1,2],
             7:[0,1,2]}
    
    coluna = {0:[0,1,2],
              1:[0,1,2],
              2:[0,1,2],
              3:[0,0,0],
              4:[1,1,1],
              5:[2,2,2],
              6:[0,1,2],
              7:[2,1,0]}
    
    if dificult.get() == 1:
        while True:
            i = random.randrange(0,3)
            j = random.randrange(0,3)
            if var[i][j] == 0:
                var[i][j] = 2
                break
            if var[0][0] != 0 and var[0][1] != 0 and var[0][2] != 0 and var[1][0] != 0 and var[1][1] != 0 and var[1][2] != 0 and var[2][0] != 0 and var[2][1] != 0 and var[2][2] != 0:
                break
    if dificult.get() == 2:
        while True:
            max = False
            for i, possibilidade in enumerate(possibilidades):                                 # i -> indice da possibilidade, possibilidade -> valor dentro de possibilidades de acordo com o indice
                j = str(possibilidade[0])+str(possibilidade[1])+str(possibilidade[2])          # j -> junção dos valores de possibilidades como string
                if j.count('1') == 2 and j.find('0') != -1:
                    pos = j.find('0')
                    pos_i = linha[i][pos]
                    pos_j = coluna[i][pos]
                    var[pos_i][pos_j] = 2
                    max = True
                    break
            if max == False:
                while True:
                    i = random.randrange(0,3)
                    j = random.randrange(0,3)
                    if var[i][j] == 0:
                        var[i][j] = 2
                        break
                    if var[0][0] != 0 and var[0][1] != 0 and var[0][2] != 0 and var[1][0] != 0 and var[1][1] != 0 and var[1][2] != 0 and var[2][0] != 0 and var[2][1] != 0 and var[2][2] != 0:
                        break
            break
    if dificult.get() == 3:
        while True:
            max = False                                                                            # max -> Identificar se o if foi feito
            primeiro = False                                                                       # primeiro -> parar o codigo caso o for tenha sido feito com sucesso
            if max == False:
                for i, possibilidade in enumerate(possibilidades):                                 # i -> indice da possibilidade, possibilidade -> valor dentro de possibilidades de acordo com o indice
                    j = str(possibilidade[0])+str(possibilidade[1])+str(possibilidade[2])          # j -> junção dos valores de possibilidades como string
                    if j.count('2') == 2 and j.find('0') != -1:
                        pos = j.find('0')
                        pos_i = linha[i][pos]
                        pos_j = coluna[i][pos]
                        var[pos_i][pos_j] = 2
                        max = True
                        primeiro = True
                        break
                if primeiro == True:
                    break
            if max == False:
                for i, possibilidade in enumerate(possibilidades):
                    j = str(possibilidade[0])+str(possibilidade[1])+str(possibilidade[2])
                    if j.count('1') == 2 and j.find('0') != -1:
                        pos = j.find('0')
                        pos_i = linha[i][pos]
                        pos_j = coluna[i][pos]
                        var[pos_i][pos_j] = 2
                        max = True
                        primeiro = True
                        break
                if primeiro == True:
                    break
            if max == False:
                while True:
                    i = random.randrange(0,3)
                    j = random.randrange(0,3)
                    if var[i][j] == 0:
                        var[i][j] = 2
                        break
                    if var[0][0] != 0 and var[0][1] != 0 and var[0][2] != 0 and var[1][0] != 0 and var[1][1] != 0 and var[1][2] != 0 and var[2][0] != 0 and var[2][1] != 0 and var[2][2] != 0:
                        break
                break
    Verify()

# Criação da Janela do jogo
janela = tk.Tk()
janela.title('Jogo da Velha')

# Dividindo os Frames dos jogos, Frame -> Divisões de tela
op = tk.LabelFrame(janela, text='Jogo da Velha', labelanchor='n', font=50)   # Frame Principal
op.grid(row=1, padx=5, pady=3)

frame = tk.Frame(op)                       # Frame da tela do jogo em si
frame.grid(row=0,column=0,padx=10,pady=5)

# Menu Superior
menu_button = tk.Menu(janela)
janela.config(menu=menu_button)

## Adicionando o menu de modos
modo = tk.Menu(menu_button)
menu_button.add_cascade(label='Modo', menu=modo)
mode_choice = tk.IntVar()    # variavel para identificar o modo que o usuario escolheu
mode_choice.set(1)
modo.add_radiobutton(label='single player',variable=mode_choice,value=1,command=Reset)
modo.add_radiobutton(label='Multiplayer',variable=mode_choice,value=2,command=Reset)

## Adicionando o menu de dificuldade
dificuldade = tk.Menu(menu_button)
menu_button.add_cascade(label='Dificuldade', menu=dificuldade)
dificult = tk.IntVar()        # variavel para identificar a dificuldade que o usuario escolheu
dificult.set(1)
dificuldade.add_radiobutton(label='Facil',variable=dificult,value=1,command=Reset)
dificuldade.add_radiobutton(label='Medio',variable=dificult,value=2,command=Reset)
dificuldade.add_radiobutton(label='Dificil',variable=dificult,value=3,command=Reset)

# Frames da Tela
## Linha Superior
y1 = tk.LabelFrame(frame)
y1.grid(row=0,column=0)
y2 = tk.LabelFrame(frame)
y2.grid(row=0,column=1)
y3 = tk.LabelFrame(frame)
y3.grid(row=0,column=2)
## Linha Central
y4 = tk.LabelFrame(frame)
y4.grid(row=1,column=0)
y5 = tk.LabelFrame(frame)
y5.grid(row=1,column=1)
y6 = tk.LabelFrame(frame)
y6.grid(row=1,column=2)

## Linha Inferior
y7 = tk.LabelFrame(frame)
y7.grid(row=2,column=0)
y8 = tk.LabelFrame(frame)
y8.grid(row=2,column=1)
y9 = tk.LabelFrame(frame)
y9.grid(row=2,column=2)

# Tela
## Linha Superior
img1 = tk.Button(y1,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(0,0)])
img1.grid()
img2 = tk.Button(y2,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(0,1)])
img2.grid()
img3 = tk.Button(y3,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(0,2)])
img3.grid()

## Linha Central
img4 = tk.Button(y4,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(1,0)])
img4.grid()
img5 = tk.Button(y5,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(1,1)])
img5.grid()
img6 = tk.Button(y6,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(1,2)])
img6.grid()

## Linha Inferior
img7 = tk.Button(y7,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(2,0)])
img7.grid()
img8 = tk.Button(y8,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(2,1)])
img8.grid()
img9 = tk.Button(y9,text='   ', font=('Arial',30), height=1, width=2, command=lambda:[PlayerAction(2,2)])
img9.grid()

# Deixar a tela aberta
janela.mainloop()
