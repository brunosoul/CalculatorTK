# Author: Bruno Souza Faria
#
# Date: 25/04/19
# version: 0.0.1
#
# A simple calculator with two operands (x + y) and
# four diferents operators (+, -, *, /).
#


from tkinter import *
from functools import partial

BG = {'num':'light gray', 'func':'gray', 'iqual':'black'}
FG = {'num':'black','iqual':'white'}


def result():
    operands = ['+', '-', '*', '/']
    num1,num2,op = '','',''
    next = False
    for i in str(tela['text']):
        if not next:
            if i.isnumeric():
                num1 = num1+i
            elif i in operands:
                op = str(i)
                next = True
        else:
            if i.isnumeric():
                num2 = num2+i

    soma.set(eval('{}{}{}'.format(int(num1), op, int(num2))))
    escreve.set('')

def write(e):
    escreve.set('{}{}'.format(escreve.get(), str(e['text'][0])))

def erase():
    escreve.set(escreve.get()[:len(escreve.get())-1])


janela = Tk()
fila = Frame(janela)
fila.pack(side='top')
fila1 = Frame(janela)
fila1.pack(side='top')
fila2 = Frame(janela)
fila2.pack(side='top')
fila3 = Frame(janela)
fila3.pack(side='top')
fila4 = Frame(janela)
fila4.pack(side='top')

escreve = StringVar(janela)
soma = DoubleVar(janela)

separador = Label(fila, text=' ')
separador.pack()

bt1 = Button(fila1, width=5, text='1')
bt1['command'] = partial(write, bt1)
bt1['bg'] = BG['num']

bt2 = Button(fila1, width=5, text='2')
bt2['command'] = partial(write, bt2)
bt2['bg'] = BG['num']

bt3 = Button(fila1, width=5, text='3')
bt3['command'] = partial(write, bt3)
bt3['bg'] = BG['num']

bt4 = Button(fila2, width=5, text='4')
bt4['command'] = partial(write, bt4)
bt4['bg'] = BG['num']

bt5 = Button(fila2, width=5, text='5')
bt5['command'] = partial(write, bt5)
bt5['bg'] = BG['num']

bt6 = Button(fila2, width=5, text='6')
bt6['command'] = partial(write, bt6)
bt6['bg'] = BG['num']

bt7 = Button(fila3, width=5, text='7')
bt7['command'] = partial(write, bt7)
bt7['bg'] = BG['num']

bt8 = Button(fila3, width=5, text='8')
bt8['command'] = partial(write, bt8)
bt8['bg'] = BG['num']

bt9 = Button(fila3, width=5, text='9')
bt9['command'] = partial(write, bt9)
bt9['bg'] = BG['num']

bt10 = Button(fila4, width=5, text='0')
bt10['command'] = partial(write, bt10)
bt10['bg'] = BG['num']

bt11 = Button(fila1, width=5, text='+')
bt11['command'] = partial(write, bt11)
bt11['bg'] = BG['func']

bt12 = Button(fila2, width=5, text='-')
bt12['command'] = partial(write, bt12)
bt12['bg'] = BG['func']

bt13 = Button(fila3, width=5, text='*')
bt13['command'] = partial(write, bt13)
bt13['bg'] = BG['func']

bt14 = Button(fila4, width=5, text='C')
bt14['command'] = erase
bt14['bg'] = BG['iqual']
bt14['fg'] = FG['iqual']

bt15 = Button(fila4, width=5, text='=')
bt15['command'] = result
bt15['bg'] = BG['iqual']
bt15['fg'] = FG['iqual']

bt16 = Button(fila4, width=5, text='/')
bt16['command'] = partial(write, bt16)
bt16['bg'] = BG['func']

for i in range (1,17):
    eval("bt{}.pack(side='left')".format(i))

tela = Button(janela, width=32, textvar=escreve)
tela.pack()

resultado = Button(janela, width=28, textvar=soma, font=('Times',12), text='Result')
resultado.pack()

janela.geometry('280x200')
janela.title('Calculator')
janela.mainloop()