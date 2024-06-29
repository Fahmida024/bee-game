import pgzrun
import random
WIDTH=600
HEIGH=500
score=0
gameover=False
bee=Actor("img3")
bee.pos=100,100
flower=Actor('img2')
flower.pos=200,150
def draw():
    screen.blit('img5',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(score),color='Red',center=(50,40))
    if gameover ==True:
        screen.fill('red')
        screen.draw.text('Youre final score=' +str(score), color='pink',center=(250,200),fontsize=50)

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    if bee.colliderect(flower):
        placeFlower()
        score=score+10



def placeFlower():
    flower.x=random.randint(50,550)
    flower.y=random.randint(50,450)

def timeUp():
    global gameover
    gameover=True

clock.schedule(timeUp,20.0)




    







pgzrun.go()

