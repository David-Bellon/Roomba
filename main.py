from concurrent.futures import thread
import cv2
from tkinter import *
from PIL import ImageTk, Image
from random import randint
from enum import Enum
import threading

from matplotlib.pyplot import table


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
        self.knows = set()
        self.path = []

    def detecting_walls(self, right_walls, left_walls, up_walls, down_walls):

        cord_x = canvas.coords(item)[0]
        cord_y = canvas.coords(item)[1]

        self.x = cord_x
        self.y = cord_y


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

    def scan_room(self):
        for i in down_walls:
                if self.x + 15 >= i[0] and self.y >= i[1] and self.y <= i[3]:
                    self.knows.add((self.x + 15, self.y))
        for i in up_walls:
                if self.x - 15 <= i[0] and self.y <= i[1] and self.y >= i[3]:
                    self.knows.add((self.x - 15, self.y))
        for i in right_walls:
                if self.y - 15 <= i[1] and self.x >= i[0] and self.x <= i[2]:
                    self.knows.add((self.x, self.y - 15))
        for i in left_walls:
                if self.y + 15 >= i[1] and self.x <= i[0] and self.x >= i[2]:
                    self.knows.add((self.x, self.y + 15))
        

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
            pixels_y = randint(-4, -1)
        elif self.dir.name == "down_left":
            pixels_x = -1
            pixels_y = randint(1, 3)
        elif self.dir.name == "down_right":
            pixels_x = 1
            pixels_y = randint(1, 4)
        else:
            pixels_x = 1
            pixels_y = randint(-4, -1)

        canvas.move(item, pixels_x, pixels_y)
        canvas.after(10, self.move)
        self.path.append(canvas.coords(item))
        self.detecting_walls(right_walls, left_walls, up_walls, down_walls)
        self.scan_room()
        
        
        print(self.dir.name)
        print(canvas.coords(item))

    def draw_path(self):
        if var_roomba.get() == 0:
            canvas.delete("path")
        else:
            for i in self.path:
                canvas.create_oval(i[0], i[1], i[0], i[1], fill="Red", tags="path")

    def draw_scan(self):
        if var_scan.get() == 0:
            canvas.delete("scanned")
        else:
            for i in self.knows:
                canvas.create_oval(i[0], i[1], i[0], i[1], fill="Green", tags="scanned")

    def thread_move(self):
        x = threading.Thread(target=self.move)
        x.start()
    
    def thread_draw_scan(self):
        x = threading.Thread(target=self.draw_scan)
        x.start()
    
    def thread_draw_path(self):
        x = threading.Thread(target=self.draw_path)
        x.start()

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


def draw_obstacle():
    #Draw an object in a random wall with random size
    selected_wall = randint(1, 2)
    place_in = list()
    if selected_wall == 1:
        place_in = left_walls
    else:
        place_in = right_walls

    wall_to_place = place_in[randint(0, len(place_in) - 1)]

    position_x = 0
    position_y = 0

    if wall_to_place[0] < wall_to_place[2]:
        limit = wall_to_place[2]
        position_x = randint(wall_to_place[0], wall_to_place[2]) 
    else:
        limit = wall_to_place[0]
        position_x = randint(wall_to_place[2], wall_to_place[0]) 
    
    if wall_to_place[1] < wall_to_place[3]:
        position_y = randint(wall_to_place[1], wall_to_place[3]) 
    else:
        position_y = randint(wall_to_place[3], wall_to_place[1])

    start_x = position_x

    if selected_wall == 1:

        end_y = position_y

        incremenet_y = randint(30, 50)
        canvas.create_line(position_x, position_y, position_x, position_y - incremenet_y, tags="block")
        up_walls.append([position_x, position_y, position_x, position_y + incremenet_y])

        position_y = position_y - incremenet_y

        increment_x = randint(start_x, limit)
        canvas.create_line(position_x, position_y, increment_x, position_y, tags="block")
        right_walls.append([position_x, position_y, increment_x, position_y])

        position_x = increment_x

        canvas.create_line(position_x, position_y, position_x, end_y, tags="block")
        up_walls.append([position_x, position_y, position_x, end_y])
    else:

        end_y = position_y

        incremenet_y = randint(30, 50)
        canvas.create_line(position_x, position_y, position_x, position_y + incremenet_y, tags="block")
        down_walls.append([position_x, position_y, position_x, position_y + incremenet_y])

        position_y = position_y + incremenet_y

        increment_x = randint(start_x, limit)
        canvas.create_line(position_x, position_y, increment_x, position_y, tags="block")
        right_walls.append([position_x, position_y, increment_x, position_y])

        position_x = increment_x

        canvas.create_line(position_x, position_y, position_x, end_y, tags="block")
        up_walls.append([position_x, position_y, position_x, end_y])
    






def show_room():
    if var_scenario.get() == 0:
        canvas.delete("wall")
    else:
        for i in walls:
            canvas.create_line(i[0], i[1], i[2], i[3],tags="wall")


    

def set_walls_direction():
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

    return right_walls, left_walls, up_walls, down_walls


#Above are all functions
#-----------------------------------------------------------------------------------------#
#Real code



#resize image
path = r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png"
#img = cv2.imread(path)
#img = cv2.resize(img, (25, 25))
#cv2.imwrite(path, img)
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

right_walls, left_walls, up_walls, down_walls = set_walls_direction()

draw_obstacle()


roomba = Roomba()

#Checkbox to show or not the scenario
var_scenario = IntVar()
checkbox1 = Checkbutton(root, text= "Show Room", variable= var_scenario, command= show_room)
checkbox1.pack()
checkbox1.toggle()

#Checkbox for what roomba knows
var_roomba = IntVar()
checkbox2 = Checkbutton(root, text="Show last roomba path", variable= var_roomba, command=roomba.draw_path)
checkbox2.pack()

#Checkbox for scanned
var_scan = IntVar()
checkbox3 = Checkbutton(root, text="Scanned", variable= var_scan, command=roomba.draw_scan)
checkbox3.pack()

#Move image function
roomba.thread_move()

root.mainloop()


