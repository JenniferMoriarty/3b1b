
#3Blue1Brown counting puzzle
#https://www.youtube.com/watch?v=HEfHFsfGXjs&ab_channel=3Blue1Brown
import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("3b1b counting puzzle")
clock = pygame.time.Clock()

collisions = 0

box1x = 50
box1y = 750
v1x = 0
b1Size = 50
mass1 = 1

box2x = 200
box2y = 700
v2x = -1
b2Size = 100
mass2 = 100 #this code stops working if this is larger than 100!

while True:
    clock.tick(60)
   
    #check for keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

   
    #physics--------------------
           
    #bounce off left edge
    if box1x < 0:
        v1x *= -1
        collisions +=1
        print(collisions)
    if box2x <0:
        v2x *=-1
   
    #bounce off each other (simple version, assuming always the same weight)
    #if box1x + b1Size > box2x:
    #    temp = v1x
    #    v1x = v2x
    #    v2x = temp
    #    collisions +=1
    #    print(collisions)
   
    #bounce off each other, take mass into account
    #equations gotten from here: http://hyperphysics.phy-astr.gsu.edu/hbase/colsta.html#c5
    if box1x + b1Size > box2x:
        new_v2x = ((2*mass1)/(mass1+mass2))*v1x - ((mass1-mass2)/(mass1 + mass2))*v2x
        new_v1x = ((mass1-mass2)/(mass1+mass2))*v1x + ((2*mass2)/(mass1+mass2))*v2x
       
        v2x = new_v2x
        v1x = new_v1x
        collisions +=1
        print(collisions)
       
       
    #update box position
    box1x += v1x
    box2x += v2x
   

   
    #render section    
    screen.fill((0,0,0))
   
    pygame.draw.rect(screen, (255, 0, 255), (box1x, box1y, b1Size, b1Size))
    pygame.draw.rect(screen, (255, 255, 255), (box2x, box2y, b2Size, b2Size))
   
    pygame.display.flip()
   
pygame.quit()
