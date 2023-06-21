#coding:utf-8
import tkinter as tk

#window
root = tk.Tk()
root.geometry("600x500")

#canvas
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x=0, y=0)

#circle
canvas.create_oval(300 -20, 200 - 20, 300 + 20, 200 + 20)
#line
canvas.create_line(300, 220, 300, 250)
canvas.create_line(300, 227, 330, 215)
canvas.create_line(300, 227, 270, 215)
canvas.create_line(300, 250, 325, 290)
canvas.create_line(300, 250, 275, 290)

root.mainloop()
