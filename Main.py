from Voice import audioToText
from FileIO import readBible
from Passage import passageFinder
from tkinter import *
import tkinter.messagebox

def getText():
    global w
    passage = w.get()
    print (passage)
    return passage


bible = readBible("ESV")
root = Tk()

topFrame = Frame(root, width = 300, height = 500)
topFrame.pack()

w = Entry(topFrame)
voiceButton = Button(topFrame, text = "Voice Search", fg = "blue")
textButton = Button(topFrame, text = "Text Search", fg = "red", command = getText)
w.grid(row = 2, column = 1)
voiceButton.grid(row = 1, column = 1)
textButton.grid(row = 3, column = 1)
#passage = "James 5 vs 1 to 5"
#print(passageFinder(bible, passage))
root.mainloop()
#passage = audioToText()
