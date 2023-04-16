from tkinter import *
from tkinter import colorchooser

x, y = 0, 0
color = None
outline = 'black'
sizeVal = 1

w = Tk()
w.title("绘画")
w.state('zoomed')
w.rowconfigure(0, weight = 1)
w.columnconfigure(0, weight = 1)

canvas = Canvas(w, background = 'white')
canvas.grid(row = 0, column = 0, sticky = "NSEW")

def draw_line(event):
    global x, y, sizeVal
    canvas.create_line((x, y, event.x, event.y), fill = outline, width = sizeVal)
    x, y = event.x, event.y

def draw_square(event):
    global x,y, sizeVal
    canvas.create_rectangle((x, y, event.x, event.y), outline = outline, fill = color, width = sizeVal)
    x,y = event.x, event.y

def draw_circle(event):
    global x, y, sizeVal
    canvas.create_oval((x, y, event.x, event.y), outline = outline, fill = color, width = sizeVal)
    x, y = event.x, event.y

def select(options):
    if options == 1:
        canvas.unbind("<ButtonRelease-1>")
        canvas.bind('<B1-Motion>', draw_line)
    if options == 2:
        canvas.unbind("<B1-Motion>")
        canvas.bind('<ButtonRelease-1>', draw_line)
    elif options == 3:
        canvas.unbind("<B1-Motion>")
        canvas.bind('<ButtonRelease-1>', draw_square)
    elif options == 4:
        canvas.unbind("<B1-Motion>")
        canvas.bind('<ButtonRelease-1>', draw_circle)



def position(event):
    global x, y
    x, y = event.x, event.y

def changeSize(size):
    global sizeVal
    sizeVal = size

def set_line_color():
    global outline
    getColor = colorchooser.askcolor(title = "选择颜色")
    outline = getColor[1]

def set_fill_color():
    global color
    getColor = colorchooser.askcolor(title = "选择颜色")
    color = getColor[1]

def clear_screen():
    canvas.delete('all')
canvas.bind('<Button-1>', position)

main = Menu(w)
menu1 = Menu(main)
main.add_cascade(label = '绘画选项', menu = menu1)
menu1.add_command(label = '笔', command = lambda: select(1))
menu1.add_command(label = '线', command = lambda: select(2))
menu1.add_command(label = '矩形', command = lambda: select(3))
menu1.add_command(label = '圆', command = lambda: select(4))

menu2 = Menu(main)
main.add_cascade(label = '选择尺寸', menu = menu2)
menu2.add_command(label = '1', command = lambda: changeSize(1))
menu2.add_command(label = '5', command = lambda: changeSize(5))
menu2.add_command(label = '10', command = lambda: changeSize(10))
menu2.add_command(label = '15', command = lambda: changeSize(15))
menu2.add_command(label = '20', command = lambda: changeSize(20))
menu2.add_command(label = '25', command = lambda: changeSize(25))

menu3 = Menu(main)
main.add_cascade(label = '选择颜色', menu = menu3)
menu3.add_command(label = '线条颜色', command = set_line_color)
menu3.add_command(label = '填充颜色', command = set_fill_color)

menu4 = Menu(main)
main.add_cascade(label = '清空', menu = menu4)
menu4.add_command(label = '清空', command = clear_screen)

w.config(menu = main)
w.mainloop()
