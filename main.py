import cv2
from tkinter import *
from PIL import ImageTk, Image
from random import randint
from enum import Enum


walls = []


class Roomba():

    class direction(Enum):
        up = 1
        down = 2
        right = 3
        left = 4
        up_left = 5
        up_right = 6
        down_right = 7
        down_left = 8


    def __init__(self):
        self.x = canvas.coords(item)[0]
        self.y = canvas.coords(item)[1]
        self.dir = self.direction["up_right"]

    def detecting_walls(self):
        #identify wall direction
        right_walls = []
        left_walls = []
        up_walls = []
        down_walls = []

        for wall in walls:
            if wall[0] != wall[2]:
                #move on x-axis
                if wall[0] < wall[2]:
                    right_walls.append(wall)
                else:
                    left_walls.append(wall)
            elif wall[1] < wall[3]:
                down_walls.append(wall)
            else:
                up_walls.append(wall)
    

        cord_x = canvas.coords(item)[0]
        cord_y = canvas.coords(item)[1]

        collision = False

        if self.dir.name == "right" or self.dir.name == "down_right" or self.dir.name == "up_right":
            for i in down_walls:
                if cord_x + 15 >= i[0] and cord_y >= i[1] and cord_y <= i[3]:
                    collision = True
        if self.dir.name == "left" or self.dir.name == "down_left" or self.dir.name == "up_left":
            for i in up_walls:
                if cord_x - 15 <= i[0] and cord_y <= i[1] and cord_y >= i[3]:
                    collision = True
        if self.dir.name == "up" or self.dir.name == "up_right" or self.dir.name == "up_left":
            for i in right_walls:
                if cord_y - 15 <= i[1] and cord_x >= i[0] and cord_x <= i[2]:
                    collision = True
        if self.dir.name == "down" or self.dir.name == "down_left" or self.dir.name == "down_right":
            for i in left_walls:
                if cord_y + 15 >= i[1] and cord_x <= i[0] and cord_x >= i[2]:
                    collision = True
        
        if collision:
            current_direction = self.dir.value
            new_direction = randint(1, 8)
            while new_direction == current_direction:
                new_direction = randint(1, 8)
            
            self.dir = self.direction(new_direction)

    def move(self):

        pixels_x = 0
        pixels_y = 0
        if self.dir.name == "up":
            pixels_x = 0
            pixels_y = -1
        elif self.dir.name == "down":
            pixels_x = 0
            pixels_y = 1
        elif self.dir.name == "left":
            pixels_x = -1
            pixels_y = 0
        elif self.dir.name == "right":
            pixels_x = 1
            pixels_y = 0
        elif self.dir.name == "up_left":
            pixels_x = -1
            pixels_y = -1
        elif self.dir.name == "down_left":
            pixels_x = -1
            pixels_y = 1
        elif self.dir.name == "down_right":
            pixels_x = 1
            pixels_y = 1
        else:
            pixels_x = 1
            pixels_y = -1

        canvas.move(item, pixels_x, pixels_y)
        canvas.after(1, self.move)

        self.detecting_walls()
        print(self.dir.name)
        print(canvas.coords(item))



def draw_scenario():

    #Start drawing scenario for random room
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
    #end Drawing room


    #place the roomba next to a random wall
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
    
    global item

    item = canvas.create_image(x_roomba, y_roomba, image= image)

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
path = r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png"
img = cv2.imread(path)
img = cv2.resize(img, (25, 25))
cv2.imwrite(path, img)
#end resize

#create window
root = Tk()
root.geometry("1000x700")
root.minsize(1000, 700)
root.maxsize(1000, 700)

#set image and canvas

width = 80
height = 80
canvas = Canvas(width=width, height=height, bg="white")
canvas.pack(expand=1, fill=BOTH)
image = ImageTk.PhotoImage(Image.open(path))

#draw the scenario and the roomba
draw_scenario()

roomba = Roomba()

#Checkbox to show or not the scenario
var = IntVar()
checkbox = Checkbutton(root, text= "Show Room", variable= var, command= check)
checkbox.pack()
checkbox.toggle()


#Move image function
roomba.move()

root.mainloop()


