from tkinter import *
root = Tk()
convas = Canvas(root, width = 500, height = 500)
convas.pack()
# the line
# convas.create_line(0,0,500,500)
# the rectangle
# x1=10
# y1=10
# x2=50
# y2=50
#     for a in range(4):
#         x1 = x2+5
#         x2 = x1+40
#         convas.create_rectangle(x1,y1,x2,y2)
#convas.create_rectangle(10,10,50,50)
# convas.create_rectangle(10,10,50,50)
# convas.create_rectangle(55,10,95,50)
# convas.create_rectangle(100,10,140,50)
# convas.create_rectangle(145,10,185,50)
def rectangles(width,height,number ): 
    x1 = width
    y1 = height
    x2 = x1 + width
    y2 = y1 + height
    for i in range(1, number+1):
        x1 = x2+5
        x2 = x1+width
        convas.create_rectangle(x1,y1,x2,y2)

rectangles(50,50,5)

root.mainloop()