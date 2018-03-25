from Tkinter import *
import os
import deleteScript

root = Tk()


#def printName(event):
e = Entry(root)
e.pack()
def runScript():
    ID = e.get()
    os.system(deleteScript.deletRecord(ID))#"./deleteScript.py ID")

button = Button(root, text = "Issue", command = lambda : runScript())
button.pack()



root.geometry("400x300");


#T = Text(root, height=1, width=30)
#T.place(x = 100, y = 100)
root.mainloop()
