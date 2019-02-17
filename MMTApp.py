import tkinter as tk

HEIGHT = 700
WIDTH = 800
root = tk.Tk() #initiation

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Browse")
button.pack()

root.mainloop() #end
