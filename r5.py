#coding:utf-8
import tkinter as tk

#window
root = tk.Tk()
root.geometry("600x500")

#canvas
canvas = tk.Canvas(root, width = 600, height = 400, bg = "blue")
canvas.place(x=0, y=0)

#circle
canvas.create_oval(300 -20, 200 - 20, 300 + 20, 200 + 20, tag = "hm")
#line
canvas.create_line(300, 220, 300, 250, tag = "hm")
canvas.create_line(300, 227, 330, 215, tag = "hm")
canvas.create_line(300, 227, 270, 215, tag = "hm")
canvas.create_line(300, 250, 325, 290, tag = "hm")
canvas.create_line(300, 250, 275, 290, tag = "hm")

def move():
    canvas.move("hm", 5, 0)
    canvas.after(100,move)

move()

root.mainloop()