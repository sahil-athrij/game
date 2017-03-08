
import pygame
import random
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bg  = white

cell = 10
fps = 20
displayw = 800
displayh = 600
delete= 'yes'
evildelete = 'yes'
UP = 'up'
DOWN = "down"
RIGHT = "right"
LEFT = "left"
gotfood = 'yes'
foodcount = '0'
evilcount ='0'
evilgotfood = 'no'
level = 1
gotfood2 = 'no'
delete2 = 'yes'
foodcount2 = '0'
direction2='still'
def food():
    
    randomxy = random.randrange(0,70)
    randomyx = random.randrange(0,50)
    bewcell = [{'x':randomxy,'y':randomyx}]
    
    return bewcell


foodpos = food()
deadzone = []


def whatNext():
    for event in pygame.event.get([KEYDOWN, KEYUP,QUIT]):
    
        if event.type == KEYDOWN:
            continue

        return event.key
    


def maketextobjs(text,font,tcolor):
    textsurface = font.render(text,True,tcolor)
    return textsurface, textsurface.get_rect()

def score(text,color,location):
    smalltext = pygame.font.Font('freesansbold.ttf',20)
    typtextsurf, typtextrect = maketextobjs(text,smalltext,color)
    typtextrect.center = location
    setDisplay.blit(typtextsurf, typtextrect)
    pygame.display.update()
    fpsTime.tick()

    


def message(text,color):
    smalltext = pygame.font.Font('freesansbold.ttf',20)
    largetext = pygame.font.Font('freesansbold.ttf',150)

    titletextsurf, titletextrect = maketextobjs(text,largetext,color)
    titletextrect.center = (int(displayw/2),int(displayh/2))
    setDisplay.blit(titletextsurf,titletextrect)

    typtextsurf, typtextrect = maketextobjs('press any key to continue',smalltext,black)
    typtextrect.center = (int(displayw/2),int(displayh/2)+120)
    setDisplay.blit(typtextsurf, typtextrect)
    pygame.display.update()
    fpsTime.tick()

    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.quit()

        pygame.display.update()
        fpsTime.tick()

    rungame()


def rungame():
    global gotfood
    global foodpos
    global deadzone
    global foodcount
    global direction
    global delete
    global olddir
    global level
    global evilsnake
    global evilcount
    global evilgotfood
    global evildelete
    global gotfood2
    global direction2
    global delete2
    global foodcount2
    startx =3
    starty = 3
    y_velold = 0
    x_velold = 0
    y_vel = 0
    x_vel = 0
    ey_vel = 0
    ex_vel = 0
    y_vel2 = 0
    x_vel2 = 0
    cord = [{'x':startx,'y':starty}]
    evilsn = [{'x':10,'y':10}]
    cord2 =[{'x':40,'y':40}]
    evildelete = 'yes'
    evilcord1 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord2 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord3 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord4 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord5 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord6 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord7 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord8 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
    evilcord9 = [{'x':displayw/(2*cell),'y':displayh/(2*cell)}]
        
    direction = 'still'
    isalive = 'yes'
    isalive2 = 'yes'
    

    evilsn = [{'x':10,'y':10}]

    while True:
        while isalive == 'yes':
            deadzone = []
            
            for event in pygame.event.get():
                score(foodcount,blue,(30,30))
                score(foodcount2,red,(700,30))
                if event.type == QUIT:
                    pygame.quit()
                    sys.quit()

                
                elif event.type == KEYDOWN:
                    if event.key == K_a:
                        direction2 = LEFT
                    elif event.key == K_w:
                        direction2 = UP
                    elif event.key == K_d:
                        direction2 = RIGHT
                    elif event.key == K_s:
                        direction2 = DOWN
                        
                    if event.key == K_LEFT:
                        direction = LEFT
                    elif event.key == K_UP:
                        direction = UP
                    elif event.key == K_RIGHT:
                        direction = RIGHT
                    elif event.key == K_DOWN:
                        direction = DOWN
                        
                    
                    

                
                y_velold = y_vel
                x_velold = x_vel

                    
                if direction == UP:
                    y_vel = -1
                    x_vel = 0
                elif direction == DOWN:
                    y_vel = +1
                    x_vel = 0
                elif direction == RIGHT:
                    y_vel = 0
                    x_vel = +1                    
                elif direction == LEFT:
                    y_vel = 0
                    x_vel = -1         
                
            newcell = {'x':cord[0]['x']+x_vel,'y':cord[0]['y']+y_vel}
                    

            if delete == 'yes':
                del cord[-1]
            if gotfood == 'yes' or evilgotfood =='yes':
                foodpos = food()

                
            cord.insert(0,newcell)
            setDisplay.fill(bg)

            currentpos = [newcell['x'],newcell['y']]
            foodcheck = [foodpos[0]['x'],foodpos[0]['y']]
            
            if level == 1:
                
                evilMove(evilcord1)
                evilMove(evilcord2)
                evilMove(evilcord3)
                evilMove(evilcord4)
                evilMove(evilcord5)
                evilMove(evilcord6)
                evilMove(evilcord7)
                evilMove(evilcord8)
                evilMove(evilcord9)
                    

                    
                drawCell(cord,black,0)
                    
                drawCell(evilcord1,red,0)
                drawCell(evilcord2,red,0)
                drawCell(evilcord3,red,0)
                drawCell(evilcord4,red,0)
                drawCell(evilcord5,red,0)
                drawCell(evilcord6,red,0)
                drawCell(evilcord7,red,0)
                drawCell(evilcord8,red,0)
                drawCell(evilcord9,red,0)
                drawCell(foodpos,green,0)

                currentpos = [newcell['x'],newcell['y']]
                foodcheck = [foodpos[0]['x'],foodpos[0]['y']]
                    

                for eachcord in deadzone:
                    if eachcord in cord :
                        if len(cord) ==1:
                            isalive = 'no'
                        else:
                            del cord[-1]

                            
            if level == 2:
                global evildelete
                currentpos = [newcell['x'],newcell['y']]
                foodcheck = [foodpos[0]['x'],foodpos[0]['y']]
                if len(evilsn)>=1 :
                    if len(evilsn) <= len(cord):
                        evilsn[0]['x'] = int(evilsn[0]['x'])
                        evilsn[0]['y'] = int(evilsn[0]['y'])
                        if (evilsn[0]['x']< foodcheck[0]) :
                            ey_vel =0
                            ex_vel = +1
                        if evilsn[0]['x'] > foodcheck[0]:
                            ey_vel = 0
                            ex_vel = -1
                        
                        if (evilsn[0]['y']>foodcheck[1]):
                            ey_vel = -1
                            ex_vel = 0                   
                        if evilsn[0]['y']<foodcheck[1]:
                            ey_vel = +1
                            ex_vel = 0


                    elif len(evilsn)>len(cord):
                        if (evilsn[0]['x']< cord[-1]['x']) :
                            ey_vel =0
                            ex_vel = +.5
                        if evilsn[0]['x'] > cord[-1]['x']:
                            ey_vel = 0
                            ex_vel = -.5

                        
                        if (evilsn[0]['y']>cord[-1]['y']):
                            ey_vel = -.5
                            ex_vel = 0                   
                        if evilsn[0]['y']<cord[-1]['y']:
                            ey_vel = +.5
                            ex_vel = 0

                     

                    newecell = {'x':evilsn[0]['x']+ex_vel,'y':evilsn[0]['y']+ey_vel}
                    if evildelete == 'yes':
                        del evilsn[-1]
                    

                    

                    evilsn.insert(0,newecell)
                    currentevilpos = [newecell['x'],newecell['y']]

                    if foodcheck == currentevilpos:
                        evilgotfood = 'yes'
                        evilcount = str(int(foodcount)+1)
                        evildelete = 'no'
                    else:
                        evilgotfood = 'no'
                        evildelete = 'yes'
                    if len(evilsn)<=len(cord):
                        drawCell(evilsn,blue,0)
                    if len(evilsn)>len(cord):
                        drawCell(evilsn,red,0)


                    for i in evilsn:
                        if i in cord:
                            if len(evilsn)<=len(cord):
                                del evilsn[-1]
                                delete = 'no'
                            elif len(evilsn)>len(cord) and len(cord)>1:
                                del cord[-1]
                                evildelete = 'no'
                            else:
                                isalive = 'no'

                else :
                    level +=1
                    foodcount = '0'

                
                                

                    
                
               
                drawCell(cord,black,0)
                drawCell(foodpos,green,0)

            if level == 3 and isalive2 =='yes':

                

                    
                    

                    
                y_velold2 = y_vel2
                x_velold2 = x_vel2

                        
                if direction2 == UP:
                    y_vel2 = -1
                    x_vel2 = 0
                elif direction2 == DOWN:
                    y_vel2 = +1
                    x_vel2 = 0
                elif direction2 == RIGHT:
                    y_vel2 = 0
                    x_vel2 = +1                    
                elif direction2 == LEFT:
                    y_vel2 = 0
                    x_vel2 = -1         
                    
                newcell2 = {'x':cord2[0]['x']+x_vel2,'y':cord2[0]['y']+y_vel2}
                        

                if delete2 == 'yes':
                    del cord2[-1]
                if gotfood2 == 'yes' or evilgotfood =='yes':
                    foodpos = food()

                    
                cord2.insert(0,newcell2)
                
                if (newcell2['x'] < 0 or newcell2['y']< 0 or newcell2['x']>displayw/cell or newcell2['y']> displayh/cell):
                    isalive = 'no'
                    foodcount2 = '0'

                currentpos2 = [newcell2['x'],newcell2['y']]

                if foodcheck == currentpos2:
                    gotfood2 = 'yes'
                    foodcount2 = str(int(foodcount2)+1)
                    delete2 = 'no'
                else:
                    gotfood2 = 'no'
                    delete2 = 'yes'

                drawCell(cord2,blue,0)
                drawCell(cord,black,0)
                drawCell(foodpos,green,0)
                
                

                
            if newcell in cord[1:] and direction <> 'still' and ((y_velold + y_vel) <> 0) and ((x_velold + x_vel) <> 0):
                if len(cord) == 1:
                    isalive = 'no'
                    foodcount  = '0'
                else:
                    del cord[-1]

                    


            score(foodcount,blue,(30,30))
            score(foodcount2,red,(700,30))
            pygame.display.update()
            fpsTime.tick(fps)

            if (newcell['x'] < 0 or newcell['y']< 0 or newcell['x']>displayw/cell or newcell['y']> displayh/cell):
                isalive = 'no'
                foodcount = '0'

                    
            if foodcheck == currentpos:
                gotfood = 'yes'
                foodcount = str(int(foodcount)+1)
                delete = 'no'
            else:
                gotfood = 'no'
                delete = 'yes'
            
            if int(foodcount)==20:
                foodcount = '0'
                level+=1
                
           
        message('you died',red)
        



def evilMove(evilguy):
    evilcords = []

    randomx = random.randrange(-1,2)
    randomy = random.randrange(-1,2)
    
    
    newcell = {'x':evilguy[0]['x']+randomx,'y':evilguy[0]['y']+randomy}
    if (newcell['x'] < 0 or newcell['y']< 0 or newcell['x']>displayw/cell or newcell['y']> displayh/cell):
        newcell = {'x':displayw/(2*cell),'y':displayh/(2*cell)}
    del evilguy[-1]
    evilguy.insert(0,newcell)

    evilcords.append(newcell['x'])
    evilcords.append(newcell['y'])
    deadzone.append({'x':newcell['x'],'y':newcell['y']})


        
def drawCell(cord,ccolor,size):
    for i in cord:
        x = i['x']*cell
        y = i['y']*cell
        makecell = pygame.Rect(x,y,cell+size,cell+size)
        pygame.draw.rect(setDisplay,ccolor,makecell)



   



while True:
    global fpsTime
    global setDIsplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((displayw,displayh))
    pygame.display.set_caption("snake's revenge")
    rungame()
