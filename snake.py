import pygame
pygame.init()
dis= pygame.display.set_mode((800,600))

pygame.display.set_caption('Snake by Kacper')

blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

x1 = 300
y1=300

x1_change = 0
y1_change = 0 

clock = pygame.time.Clock()

game_over = False
while not game_over:
    for click in pygame.event.get():
        if click.type==pygame.QUIT:
            game_over=True
        if click.type == pygame.KEYDOWN:
            if click.key== pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            elif click.key == pygame.K_RIGHT:
                x1_change=10
                y1_change=0
            elif click.key == pygame.K_DOWN:
                x1_change=0
                y1_change=10
            elif click.key == pygame.K_UP:
                x1_change=0
                y1_change=-10

    x1 +=x1_change
    y1 +=y1_change
    dis.fill(white) 
    pygame.draw.rect(dis,black,[x1,y1,10,10])

    pygame.display.update()

    clock.tick(20)


pygame.quit()
quit()