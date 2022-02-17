import cv2
from tkinter import *
from PIL import ImageTk, Image

def move_image():
    canvas.move(item, 1, 0)
    canvas.after(30, move_image)

def draw_scenario():
    
    canvas.create_line(60, 100, 400, 100)
    canvas.create_line(400, 100, 400, 120)
    

#resize image
img = cv2.imread(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png")
img = cv2.resize(img, (50, 50))
cv2.imwrite(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png", img)

#end resize
root = Tk()
root.geometry("1920x1080")

image = ImageTk.PhotoImage(Image.open(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png"))
width = 80
height = 80
canvas = Canvas(width=width, height=height, bg="white")
canvas.pack(expand=1, fill=BOTH)
x = (width) / 2.0
y = (height) / 2.0
item = canvas.create_image(x, y, image= image)
draw_scenario()
move_image()

root.mainloop()


