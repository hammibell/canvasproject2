from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.configure(background = "light blue")
root.title("Canavs Project")

canvas = Canvas(width = 500, height = 500, highlightbackground = "green")
canvas.pack()

oldx = 50
oldy = 50
newx = 50
newy = 50

color_label = Label(root, text = "Choose Color")
color_label.place(relx = 0.3, rely = 0.5, anchor = CENTER)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "grey", "black"]

fillcolor = [colors]

dropdown_colors = ttk.Combobox(root, state = "readonly", values = "fillcolor", width = 5)
dropdown_colors.place(relx = 0.35, rely = 0.5, anchor = CENTER)

directions = ["startx", "starty", "endx", "endy"]
coordinates_values = directions

startx = ttk.Combobox(root, state = "readonly", values = "coordinate_values", width = 5)
coordinate_options.place(relx = 0.6, rely = 0.6, anchor = CENTER)

root.mainloop()