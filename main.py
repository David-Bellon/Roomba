import cv2
from tkinter import *
from PIL import ImageTk, Image
from random import randint

def move_image():
    canvas.move(item, 1, 0)
    canvas.after(30, move_image)

def draw_scenario():
    max_left = 100
    max_rigth = 1700
    max_top = 100
    max_bottom = 900

    current_x = max_left
    current_y = max_top

    let_rigth = True
    let_left = False
    let_up = False
    let_down = False
    
    done = False

    #up = 0
    #down = 1
    #right = 2
    #left = 3
    room = []
    one_up = False
    move_left = False
    while not done:
        direction = randint(0, 3)

        if direction == 0 and let_up:
            distance = randint(50, 150)
            if (current_y - distance) > max_top:
                room.append(canvas.create_line(current_x, current_y, current_x, current_y - distance))
                current_y = current_y - distance
                one_up = True
                if let_left:
                    let_up = False
        elif direction == 1 and let_down:
            distance = randint(50, 150)
            if (current_y + distance) < max_bottom:
                room.append(canvas.create_line(current_x, current_y, current_x, current_y + distance))
                current_y = current_y + distance
                if let_rigth:
                    let_down = False
            else:
                let_down = False
                let_left = True
                let_up = False
        elif direction == 2 and let_rigth:
            distance = randint(50, 200)
            if (current_x + distance) < max_rigth:
                room.append(canvas.create_line(current_x, current_y, current_x + distance, current_y))
                current_x = current_x + distance
                if not move_left:
                    let_down = True
                    move_left = True
            else:
                let_rigth = False
                let_down = True
        elif direction == 3 and let_left:
            distance = randint(50, 200)
            if (current_x - distance) > max_left:
                room.append(canvas.create_line(current_x, current_y, current_x - distance, current_y))
                current_x = current_x - distance
                if not one_up:
                    let_up = True
            else:
                room.append(canvas.create_line(current_x, current_y, max_left, current_y))
                current_x = max_left
                room.append(canvas.create_line(current_x, current_y, current_x, max_top))
                current_y = max_top
                done = True
        
        
    

#resize image
img = cv2.imread(r"C:\Users\dadbc\Desktop\Phy\Repositorios\Roomba\robot.png")
img = cv2.resize(img, (30, 30))
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

#move_image()

root.mainloop()


