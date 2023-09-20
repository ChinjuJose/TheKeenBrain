from tkinter import *

root = Tk()
root.title("Test")
root.geometry("400x400")

name = "Ryan"
print(type(name))

messageLabel = Label(root,text="Good morning " + name)
messageLabel.pack()

root.mainloop()


