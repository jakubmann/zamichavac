#Array shuffler
import random
from tkinter import messagebox
from tkinter import *

def zamichat():
    T.delete('1.0', END)
    text_file = open("studenti.dat", "r")
    studenti = text_file.read().split(',')
    random.shuffle(studenti)
    for student in range(0, len(studenti)):
        T.insert(END, "%d     %s\n" % (student+1, studenti[student]))
    messagebox.showinfo("Hotovo","Studenti byli úspěšně zamícháni")


master = Tk()

w = 600
h = 650

ws = master.winfo_screenwidth()
hs = master.winfo_screenheight()


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

master.geometry('%dx%d+%d+%d' % (w, h, x, y))


master.winfo_toplevel().title("Zamíchávač Studentů V1.0")

T = Text(master, height = 40, width = 30)

B = Button(master, text = "Zamíchat studenty", command = zamichat)

B.pack()
T.pack()
master.mainloop()
