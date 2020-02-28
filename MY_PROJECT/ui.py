from tkinter import *

root = Tk()

root.geometry('300x300')
root.title("Calendar")

topFrame=Frame(root)
topFrame.pack(side=LEFT)
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

b1 = Button(topFrame,text='button1',fg="red",bg='gold')
b2 = Button(topFrame,text='button2',fg="red",bg='gold')
b3 = Button(topFrame,text='button3',fg="red",bg='gold')
b4 = Button(bottomFrame,text='button4',fg="red",bg='gold')
b1.pack()
b2.pack()
b3.pack()
b4.pack()


class Change():
    def __init__(self,):
        self['text'] = "Changed"
        self['bg'] = '#000000'
        self['activebackground'] = '#555555'
        self['fg'] = '#ffffff'
        self['activeforeground'] = '#ffffff'



d1 = Change

def Changef():
    b2['text'] = "Changed"
    b2['bg'] = '#000000'
    b2['activebackground'] = '#555555'
    b2['fg'] = '#ffffff'
    b2['activeforeground'] = '#ffffff'
b3.config(command=Changef)

root.mainloop()