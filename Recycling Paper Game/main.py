
import pgzrun
import random

HEIGHT = 600
WIDTH = 800

center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
currentLevel = 1
finalLevel = 7
startspeed = 10
gameOver = False
gameComp = False
ITEMS = ["bag","battery","bottle","chips"]
items = []
animations = []

def displayMessage(heading,subheading):
    screen.draw.text(heading, fontsize = 60, center = center color = "white")
    screen.draw.text(subheading, fontsize = 30, center = (center_x,center_y + 30))

def draw():
    global items, currentlevel, gameover, gameComp
    screen.clear()
    screen.blit("bgimg",(0,0))
    if gameOver:
        displayMessage("You lose!","try again!")
    elif gameComp:
        displayMessage("You win!","congrats")
    else:
        for actor in items:
            actor.draw()

def getOptionToCreate(number_extraItems):
    pass

def makeItems(number_extraItems):
    itemsToCreate = getOptionToCreate(number_extraItems)
    newItems = createItems(itemsToCreate)
    layoutItems(newItems)

    return newItems

def update():
    global items
    if len(items) == 0:
        items = makeItems(currentLevel)

pgzrun.go