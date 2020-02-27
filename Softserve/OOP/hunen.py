from tkinter import *
class Human:
    def __init__(self, age, sex):
        self.age=age
        self.sex=sex
    def speak(self):
        return f"Hello, i am {self} and {self.age} and {self.sex}"
        
man = Human(24,"man")
root = Tk()
def speak():
    print(2+2)
btn = Button(root, text="clik me", command=speak)
btn.pack()
root.mainloop()