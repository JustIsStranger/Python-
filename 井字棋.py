from tkinter import *
from tkinter import messagebox

w = Tk()
w.title('井字棋')

turn = 0
state = ['', '', '', '', '', '', '', '', '']
winner = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
game = True


def winner_check(p):
    global state, winner, game
    for i in winner:
        if((state[i[0]] == p) and (state[i[1]] == p) and (state[i[2]] == p)):
            string = '{}赢了！'.format(p)
            messagebox.showinfo('showinfo', string)
            game = False


def buttonClick(b, n):
    global turn, state, game

    if b['text'] == ' ' and game == True:
        if turn % 2 == 0:
            b['text'] = 'X'
            turn += 1
            state[n - 1] = 'X'
            winner_check('X')
        elif turn % 2 == 1:
            b['text'] = 'O'
            turn += 1
            state[n - 1] = 'O'
            player = 'X'
            winner_check('O')
    else:
        if game == False:
            messagebox.showinfo('showinfo', '游戏结束！开始新的游戏')
        elif b['text'] != ' ':
            messagebox.showinfo('showinfo', '这个方格被占用了')

    if turn > 8 and game == True:
        messagebox.showinfo('showinfo', "平局！")
        game = False
font = ('Helvetica', 20, 'bold')

b1 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b1, 1))
b1.grid(row=0, column=0)
b2 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b2, 2))
b2.grid(row=0, column=1)
b3 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b3, 3))
b3.grid(row=0, column=2)

b4 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b4, 4))
b4.grid(row=1, column=0)
b5 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b5, 5))
b5.grid(row=1, column=1)
b6 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b6, 6))
b6.grid(row=1, column=2)

b7 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b7, 7))
b7.grid(row=2, column=0)
b8 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b8, 8))
b8.grid(row=2, column=1)
b9 = Button(w, text=' ', width=4, height=2, font=font,command=lambda: buttonClick(b9, 9))
b9.grid(row=2, column=2)

boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
def new_game():
    global state, game, turn, boxes
    turn = 0
    state = ['', '', '', '', '', '', '', '', '']
    game = True
    for b in boxes:
        b['text'] = ' '
new = Button(w, text='新的游戏', command=new_game)
new.grid(row=3, column=1)

w.mainloop()
