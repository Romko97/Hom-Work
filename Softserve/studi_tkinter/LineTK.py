from tkinter import *
import time
root = Tk()
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
# the line
# canvas.create_line(0,0,500,500)
# the rectangle
# x1=10
# y1=10
# x2=50
# y2=50
#     for a in range(4):
#         x1 = x2+5
#         x2 = x1+40
#         canvas.create_rectangle(x1,y1,x2,y2)
#canvas.create_rectangle(10,10,50,50)
# canvas.create_rectangle(10,10,50,50)
# canvas.create_rectangle(55,10,95,50)
# canvas.create_rectangle(100,10,140,50)
# canvas.create_rectangle(145,10,185,50)

def rectangles(width,height,number, fill_color ): 
    x1 = width
    y1 = height
    x2 = x1 + width
    y2 = y1 + height
    for i in range(1, number+1):
        x1 = x2+5
        x2 = x1+width
        canvas.create_rectangle(x1,y1,x2,y2, fill = fill_color)

rectangles(35,35,10,'gold')
a = 1
def addone(Event):
    global a 
    if Event.keysym == '1':
        a = 1
    elif Event.keysym == '2':
        a = 2
    elif Event.keysym == '3':
        a = 3
    elif Event.keysym == '4':
        a = 4
    elif Event.keysym == '5':
        a = 5
    elif Event.keysym == '6':
        a = 6
    elif Event.keysym == '7':
        a = 7
    elif Event.keysym == '8':
        a = 8
    elif Event.keysym == '9':
        a = 9
    elif Event.keysym == '0':
        a = 10
    else:
        print("no")
    return a 

def move_rectangles(Event):
    print(Event)
    if Event.keysym == 'Up':
        canvas.move(a,0,-3)
    elif Event.keysym == 'Down':
        canvas.move(a,0,3)
    elif Event.keysym == 'Left':
        canvas.move(a,-3,0)
    else:
        canvas.move(a,3,0)

canvas.bind_all("<KeyPress-1>", addone)
canvas.bind_all("<KeyPress-2>", addone)
canvas.bind_all("<KeyPress-3>", addone)
canvas.bind_all("<KeyPress-4>", addone)
canvas.bind_all("<KeyPress-5>", addone)
canvas.bind_all("<KeyPress-6>", addone)
canvas.bind_all("<KeyPress-7>", addone)
canvas.bind_all("<KeyPress-8>", addone)
canvas.bind_all("<KeyPress-9>", addone)
canvas.bind_all("<KeyPress-0>", addone)
canvas.bind_all("<KeyPress-Up>", move_rectangles)
canvas.bind_all("<KeyPress-Down>", move_rectangles)
canvas.bind_all("<KeyPress-Left>", move_rectangles)
canvas.bind_all("<KeyPress-Right>", move_rectangles)

root.update()
time.sleep(0.05)
root.mainloop()