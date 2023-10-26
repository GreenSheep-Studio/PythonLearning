from tkinter import *
from tkinter.messagebox import *
import winsound
from time import *
import random
import sys

tk=Tk()
tk.geometry("720x720")#窗口大小
tk.resizable(0,0)#锁定窗口
tk.title("MineGame")#标题
box=Canvas(tk,bg="black")
box.pack(fill = 'both',expand ='yes')
dell=0

area = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

image0=PhotoImage(file="photo\\0.jpg")
image1=PhotoImage(file="photo\\1.jpg")
image2=PhotoImage(file="photo\\2.jpg")
image3=PhotoImage(file="photo\\3.jpg")
image4=PhotoImage(file="photo\\4.jpg")
image5=PhotoImage(file="photo\\5.jpg")
image6=PhotoImage(file="photo\\6.jpg")
image7=PhotoImage(file="photo\\7.jpg")
image8=PhotoImage(file="photo\\8.jpg")
image9=PhotoImage(file="photo\\9.jpg")
image10=PhotoImage(file="photo\\10.jpg")
image11=PhotoImage(file="photo\\11.jpg")
#image12=PhotoImage(file="photo\\12.jpg")

def draw(map_key,keyy,keyx):
    global my_x,my_y,level,boxs
    if map_key==0:
        box.create_image(keyx,keyy,anchor=NW,image=image0)
    if map_key==1:
        box.create_image(keyx,keyy,anchor=NW,image=image1)
    if map_key==2:
        box.create_image(keyx,keyy,anchor=NW,image=image2)
    if map_key==3:
        box.create_image(keyx,keyy,anchor=NW,image=image3)
    if map_key==4:
        box.create_image(keyx,keyy,anchor=NW,image=image4)
    if map_key==5:
        box.create_image(keyx,keyy,anchor=NW,image=image5)
    if map_key==6:
        box.create_image(keyx,keyy,anchor=NW,image=image6)
    if map_key==7:
        box.create_image(keyx,keyy,anchor=NW,image=image7)
    if map_key==8:
        box.create_image(keyx,keyy,anchor=NW,image=image8)
    if map_key>=19 and map_key<=28:
        box.create_image(keyx,keyy,anchor=NW,image=image9)
    if map_key==-1:
        box.create_image(keyx,keyy,anchor=NW,image=image10)
    if map_key>=49 and map_key<=58:
        box.create_image(keyx,keyy,anchor=NW,image=image11)
    #if map_key==12:
    #    box.create_image(keyx,keyy,anchor=NW,image=image12)

def draw_map():
    global boxs
    box.update()
    for i in range(1,11):
        for j in range(1,11):
            draw(area[i][j],i*60,j*60)
    box.create_text(300,0,anchor=N,text="MineGame",fill="white",font=("",50))

def BornGame():
    for n in range(0,10):
        a = random.randint(1,10)
        b = random.randint(1,10)
        if area[a][b] != -1:
            area[a][b]-=1
    for i in range(1,11):
        for j in range(1,11):
            if area[i][j] == 0:
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if area[x][y] == -1:
                            area[i][j]+=1
    for i in range(1,11):
        for j in range(1,11):
            area[i][j]+=20


def ABOS(x,y):
    if area[x][y] == 0:
        for e in range(x-1,x+2):
            for f in range(y-1,y+2):
                if area[e][f] >= 20 and area[e][f] <= 28:
                    area[e][f]-=20
                    if area[e][f] == 0:
                        ABOS(e,f)
                    else:
                        break


def callBackLeft(event):
    y = event.x//60
    x = event.y//60

    if area[x][y] >= 19 and area[x][y] <= 28:
        area[x][y]-=20
        if area[x][y] == -1:
            sleep(1)
            sys.exit(0)

        ABOS(x, y)
        draw_map()



def callBackRight(event):
    y = event.x // 60
    x = event.y // 60
    if area[x][y] >= 19 and area[x][y] <= 28:
        area[x][y] += 30
        draw_map()

    elif area[x][y] >= 49 and area[x][y] <= 58:
        area[x][y] -=30
        draw_map()


def WinIf():
    m = 0
    for i in range(1,11):
        for j in range(1,11):
            if area[i][j] == 19:
                m+=1
                if m == 0:
                    sys.exit(0)


BornGame()
draw_map()
tk.bind("<Button-1>", callBackLeft)
tk.bind("<Button-3>", callBackRight)
WinIf()
tk.mainloop()