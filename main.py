from pygame import*
from button import Button
from sprite import GameSprite
from sprite import Player
from random import randint
from sprite import Human
window = display.set_mode((500, 500))
clock = time.Clock()
kills = 0
scroll_speed = 3

game = True
run = False
road = image.load('road.png')
font.init()
font = font.SysFont('Helvetica', 24)

play = Button(130, 100, 240, 90, 'start_button.png')   
exit = Button(130, 300, 240, 90, 'quit_button.png')


car = Player('car.png', 250, 10, 50, 100, 5)

car1 = GameSprite('car1.png', 250, 100, 50, 100, 0)

human1 = Human('human1.png', 30, 100, 30, 30, randint(1,3))
human2 = Human('human2.png', 470, 250, 30, 30, randint(1,3))
human3 = Human('human3.png', 30, 400, 30, 30, randint(1,3))


humans = [human1, human2, human3]

road = transform.scale(road, (500, 500))
road_width = road.get_width()
tiles = 2
scroll = 0
speed = 10

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif exit.draw(window):
            game = False

        if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                run = not run
    
    if run:
        for i in range(0, tiles):
            window.blit(road, (0, i * road_width + scroll))
        scroll -= scroll_speed

        if abs(scroll) > road_width:
            scroll = 0
        
        for i in humans:
            if i.rect.colliderect(car.rect):
                i.rect.x = 1000
                kills += 1

        points = font.render('вбивства:' + str(kills), True, (100, 0, 255))
        window.blit(points, (100, 50))
        car.draw(window)
        car.move()
        car1.draw(window)
        human1.draw(window)
        human1.moving()
        human2.draw(window)
        human2.moving()
        human3.draw(window)
        human3.moving()
    else:
        window.blit(road, (0, 0))
        if play.draw(window):
            run = True
        if exit.draw(window):
            run = False
    display.update()
    clock.tick(60)

