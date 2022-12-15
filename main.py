# from src.backEnd import resistorCalculator 
import pygame
from src.displays import*

# initiation
pygame.init() # initializes all pygame modules
win=pygame.display.set_mode((800,400))
pygame.display.set_caption('Resistor Calculator'.upper())

running=True
mouse=pygame.mouse.get_pos()
white=(255,255,255)
windowType = 0 # 0 means the main menu is open, 1 means selecting colour menu is open

def chooseBandsNum() : # check if one of the squares is clicked on
    global chosen
    chosen = 0
    mouse=pygame.mouse.get_pos()
    if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300: 
        chosen = 3
    elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300: 
        chosen = 4
    elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300: 
        chosen = 5
    if chosen == 0: return # if the click was not on any squares
    global windowType
    windowType = 1

def returnToMenu(): #check if a colour is chosen, or if the cancel button is pressed
    mouse=pygame.mouse.get_pos()
    if mouse[0]>20 and mouse[0]<170 and mouse[1]>20 and mouse[1]<60: 
        global windowType
        windowType = 0

def checkSelectedBand(chosen):
    mouse=pygame.mouse.get_pos()

    if chosen==3:
        if mouse[0]>200 and mouse[0]<330 and mouse[1]>90 and mouse[1]<310:
            selected=1
        elif mouse[0]>325 and mouse[0]<435 and mouse[1]>90 and mouse[1]<310:
            selected=2
        elif mouse[0]>450 and mouse[0]<560 and mouse[1]>90 and mouse[1]<310:
            selected=3
        else:
            return
    
    elif chosen==4:
        return

    elif chosen==5:
        return

    print(selected)

# main program
while running:

    for event in pygame.event.get(): 
        
        if event.type==pygame.QUIT: 
            running=False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if windowType == 0: # if in menu, check which 'bands' button chosen
                chooseBandsNum()
            
            elif windowType == 1: # if in 'bands' page, check if 'return to menu' button chosen
                returnToMenu()
                
                if chosen == 3:
                    checkSelectedBand(chosen)

                elif chosen == 4: print("nothing yet")
                else: print("nothing yet")

    if windowType == 0: 
        menu(win)

    elif windowType == 1:
        if chosen == 3:
            thirdBand(win,white)

        elif chosen == 4:
            fourthBand(win,white)

        else:
            fifthBand(win,white)

    pygame.display.update() 
    