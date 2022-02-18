import cv2
from tkinter import *
from PIL import ImageTk, Image
from random import randint

def move_image():
    canvas.move(item, 1, 0)
    canvas.after(100, move_image)
    print(canvas.coords(item))

def draw_scenario():

    walls = []
    x = randint(120, 500)
    canvas.create_line(100, 100, x, 100)
    walls.append([100, 100, x, 100])

    y = randint(40, 300)
    canvas.create_line(x, 100, x, y)
    walls.append([x, 100, x, y])

    canvas.create_line(x, y, 900, y)
    walls.append([x, y, 900, y])

    x =900
    canvas.create_line(x, y, x, 600)
    walls.append([x, y, x, 600])

    y = 600
    x1 = randint(400, 900)
    canvas.create_line(x, y, x1, y)
    walls.append([x, y, x1, y])

    x = x1
    y1 = randint(500, y)
    canvas.create_line(x, y, x, y1)
    walls.append([x, y, x, y1])

    y = y1
    canvas.create_line(x, y, 100, y)
    walls.append([x, y, 100, y])

    x = 100
    canvas.create_line(x, y, x, 100)
    walls.append([x, y, x, 100])
    None
    

#resize image
img = cv2.imread(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png")
img = cv2.resize(img, (30, 30))
cv2.imwrite(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png", img)

#end resize
root = Tk()
root.geometry("1000x700")
root.minsize(1000, 700)
root.maxsize(1000, 700)

image = ImageTk.PhotoImage(Image.open(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png"))
width = 80
height = 80
canvas = Canvas(width=width, height=height, bg="white")
canvas.pack(expand=1, fill=BOTH)
x = (width) / 2.0
y = (height) / 2.0
item = canvas.create_image(x, y, image= image)
draw_scenario()

#move_image()

root.mainloop()


