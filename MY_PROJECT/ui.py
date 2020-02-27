from tkinter import *

root = Tk()

root.geometry('300x300')
root.title("Calendar")

topFrame=Frame(root)
topFrame.pack(side=LEFT)
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text='button1',fg="red",bg="blue")
button2 = Button(topFrame,text='button2',fg="red")
button3 = Button(topFrame,text='button3',fg="red")
button4 = Button(bottomFrame,text='button4',fg="red")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)


root.mainloop()