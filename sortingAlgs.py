from tkinter import *
from tkinter import ttk 
import random 

root = Tk()
root.title('Sorting Algorithm Visualization')
root.maxsize(900,600)
root.config(bg='black')

selected_alg = StringVar()

def Generate():
    print('Alg Selected: ' + selected.alg.get())

UI_frame = Frame(root,width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)



root.mainloop()