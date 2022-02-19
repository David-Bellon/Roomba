import cv2
from tkinter import *
from PIL import ImageTk, Image
from random import randint

walls = []

def move_image():
    canvas.move(item, 1, 0)
    canvas.after(100, move_image)
    print(canvas.coords(item))

def draw_scenario():

    x = randint(120, 500)
    canvas.create_line(100, 100, x, 100, tags="wall")
    walls.append([100, 100, x, 100])

    y = randint(40, 300)
    canvas.create_line(x, 100, x, y, tags="wall")
    walls.append([x, 100, x, y])

    canvas.create_line(x, y, 900, y, tags="wall")
    walls.append([x, y, 900, y])

    x =900
    canvas.create_line(x, y, x, 600, tags="wall")
    walls.append([x, y, x, 600])

    y = 600
    x1 = randint(400, 700)
    canvas.create_line(x, y, x1, y, tags="wall")
    walls.append([x, y, x1, y])

    x = x1
    y1 = randint(500, y)
    canvas.create_line(x, y, x, y1, tags="wall")
    walls.append([x, y, x, y1])

    y = y1
    canvas.create_line(x, y, 100, y, tags="wall")
    walls.append([x, y, 100, y])

    x = 100
    canvas.create_line(x, y, x, 100, tags="wall")
    walls.append([x, y, x, 100])

    select_wall = randint(0, 7)
    change_x = 0
    change_y = 0
    if select_wall == 0 or select_wall == 2:
        change_y = 25
    elif select_wall == 4 or select_wall == 6:
        change_y = -25
    elif select_wall == 3 or select_wall == 1:
        change_x = -25
    elif select_wall == 7 or select_wall == 5:
        change_x = 25


    if walls[select_wall][2] > walls[select_wall][0]:
        x_roomba = randint(walls[select_wall][0], walls[select_wall][2]) + change_x
    else:
        x_roomba = randint(walls[select_wall][2], walls[select_wall][0]) + change_x

    if  walls[select_wall][1] > walls[select_wall][3]:
        y_roomba = randint(walls[select_wall][3], walls[select_wall][1]) + change_y
    else:
        y_roomba = randint(walls[select_wall][1], walls[select_wall][3]) + change_y
    
    item = canvas.create_image(x_roomba, y_roomba, image= image)

    return item

def check():
    if var.get() == 0:
        canvas.delete("wall")
    else:
        for i in walls:
            canvas.create_line(i[0], i[1], i[2], i[3],tags="wall")
    


#Above are all functions
#-----------------------------------------------------------------------------------------#
#Real code



#resize image
img = cv2.imread(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png")
img = cv2.resize(img, (25, 25))
cv2.imwrite(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png", img)
#end resize

#create window
root = Tk()
root.geometry("1000x700")
root.minsize(1000, 700)
root.maxsize(1000, 700)

#set image and canvas
image = ImageTk.PhotoImage(Image.open(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png"))
width = 80
height = 80
canvas = Canvas(width=width, height=height, bg="white")
canvas.pack(expand=1, fill=BOTH)
x = (width) / 2.0
y = (height) / 2.0

#draw the scenario and the roomba
item = draw_scenario()

#Checkbox to show or not the scenario
var = IntVar()
checkbox = Checkbutton(root, text= "Show Room", variable= var, command= check)
checkbox.pack()
checkbox.toggle()


#Move image function
#move_image()

root.mainloop()


