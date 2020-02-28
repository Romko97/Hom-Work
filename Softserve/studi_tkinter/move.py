from tkinter import *
import time
root = Tk()
convas = Canvas(root, width = 500, height = 500)
convas.pack()
convas.create_rectangle(10,10,50,50)
for x in range(60):
    convas.move(1,0,5)
    root.update()
    time.sleep(0.05)

root.mainloop()