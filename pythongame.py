from tkinter import *
import random

WIDTH=500
HEIGHT=500
F_Bvel=25
L_Rvel=25
foodcolor='red'
linecolor='#c0ccc2'
BACKGROUND_COLOR='#66bd73'
UNIT_BOX=25
temp_cord=[]
food_temp =None
score=0#because i have a head
direction='down'
speed =25
gamestop = FALSE
window=Tk()
window.config(width=WIDTH,height=HEIGHT)
canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg=BACKGROUND_COLOR)    
snake=canvas.create_rectangle(0,0,25,25,fill='#5342bd')
snakebody=[]
def board():
    for i in range(0,WIDTH,UNIT_BOX):
        canvas.create_line(i,0,i,HEIGHT,fill=linecolor)
    for i in range(0,HEIGHT,UNIT_BOX):
        canvas.create_line(0,i,WIDTH,i,fill=linecolor)
def food():
        global food_temp
        x= random.randint(0,19)*UNIT_BOX
        y=random.randint(0,19)*UNIT_BOX
        food_temp =canvas.create_oval(x,y,x+UNIT_BOX,y+UNIT_BOX,fill=foodcolor)
        return [x,y]
    

    
    
class movement(): 
       
     def move_fwd(event):
          global direction
          tcord=canvas.coords(snake)
          canvas.move(snake,0,-F_Bvel)
          body_movement(tcord)
          direction='top'
     def move_left(event):
          global direction
          tcord=canvas.coords(snake)
          canvas.move(snake,-F_Bvel,0)
          body_movement(tcord)
          direction='left'
     def move_right(event):
          global direction
          tcord=canvas.coords(snake)
          canvas.move(snake,F_Bvel,0)
          body_movement(tcord)
          direction='right'
     def move_back(event):
          global direction
          tcord=canvas.coords(snake)
          canvas.move(snake,0,F_Bvel)
          body_movement(tcord)
          direction='down'


def lose_game():
    
    gamecan = Canvas(window,width=500,height=200,bg='white')
    gamecan.place(x=0,y=150)
    gameover= Label(gamecan,text='Game Over',font=('HUMANOID',50),bg='white')
    gameover.place(x=80,y=50)
    window.after(2000,quit)
    
def Checkcollision():
    
    if( canvas.coords(snake)[0] <0 or canvas.coords(snake)[2]>WIDTH):
        lose_game()
    if(canvas.coords(snake)[1] <0 or canvas.coords(snake)[3]>HEIGHT):
        lose_game()
    midps=[(canvas.coords(snake)[0]+canvas.coords(snake)[2])/2,(canvas.coords(snake)[1]+canvas.coords(snake)[3])/2]
    for i in snakebody:
        midpt=[(canvas.coords(i)[0]+canvas.coords(i)[2])/2,(canvas.coords(i)[1]+canvas.coords(i)[3])/2]
        if(abs(midps[0]-midpt[0])<20 and abs(midps[1]-midpt[1])<20):
         """"
         print("midps-midpt in x"+str(abs(midps[0]-midpt[0])))
         print("midps-midpt in y"+str(abs(midps[1]-midpt[1])))
         print('i is '+str(snakebody.index(i)))
         """
        
         lose_game()
def move_cont():
    if(direction=='top'):
        tcord=canvas.coords(snake)
        canvas.move(snake,0,-speed)
        body_movement(tcord)
    elif(direction=='down'):
        tcord=canvas.coords(snake)
        canvas.move(snake,0,speed)
        body_movement(tcord)
    elif(direction=='left'):
        tcord=canvas.coords(snake)
        canvas.move(snake,-speed,0)
        body_movement(tcord)
    elif(direction=='right'):
        tcord=canvas.coords(snake)
        canvas.move(snake,speed,0)
        body_movement(tcord)
    
    window.after(120,move_cont)
    
def food_eaten():
    global score
    if(abs(canvas.coords(snake)[2]-canvas.coords(food_temp)[2])<5 and abs(canvas.coords(snake)[3]-canvas.coords(food_temp)[3])<5 ):
        canvas.delete(food_temp)
        food()
        score+=1
        snake_grow(score-1)
def body_movement(tcord):
     """"
     if(len(snakebody)!=0):
        print("this is working") 
        for j in range(4):
              canvas.coords(snakebody[0])[j]=coordinates[j]
        for i in range(1,len(snakebody)):
             for j in range(4):
              canvas.coords(snakebody[i])[j]=canvas.coords(snakebody[i-1])[j]
     """ 
     temp_cord=[]
     temp_cord2=[]
     if(len(snakebody)!=0):
         temp_cord=canvas.coords(snakebody[0])
         canvas.moveto(snakebody[0],tcord[0],tcord[1])
         for i in range(1,len(snakebody)):
             temp_cord2=canvas.coords(snakebody[i])
             canvas.moveto(snakebody[i],temp_cord[0],temp_cord[1])
             temp_cord=temp_cord2
     
                 
def snake_grow(i):
    if(i==0):
       square=canvas.create_rectangle(canvas.coords(snake)[0],canvas.coords(snake)[1]+25,canvas.coords(snake)[2],canvas.coords(snake)[3]+25,fill='#5342bd')
    else:
       square=canvas.create_rectangle(canvas.coords(snakebody[i-1])[0],canvas.coords(snakebody[i-1])[1]+25,canvas.coords(snakebody[i-1])[2],canvas.coords(snakebody[i-1])[3]+25,fill='#5342bd')
    snakebody.append(square)
        

def update():
    Checkcollision()
    food_eaten()
    
    
    window.after(10,update)


window.bind("<w>",movement.move_fwd)
window.bind("<a>",movement.move_left)
window.bind("<s>",movement.move_back)
window.bind("<d>",movement.move_right)
#board()
temp_cord=food()
update()
move_cont()




window.update()

canvas.pack()
window.mainloop()