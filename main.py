from pygame import*
from button import Button
from sprite import GameSprite
from sprite import Player
from random import randint, shuffle
from sprite import Human
from sprite import Enemy
window = display.set_mode((500, 500))
clock = time.Clock()
kills = 0
scroll_speed = 2
speed = 5
x_list = [90, 160, 240, 320]


game = True
run = False
road = image.load('road.png')
font.init()
font = font.SysFont('Helvetica', 24)

play = Button(130, 100, 240, 90, 'start_button.png')   
exit = Button(130, 300, 240, 90, 'quit_button.png')


car = Player('car.png', 250, 10, 50, 100, speed)

l = [0,1,2,3]
shuffle(l)

car1 = Enemy('car1.png', x_list[l[0]], randint(500, 600), 95, 115, scroll_speed)
car2 = Enemy('car2.png', x_list[l[1]], randint(500, 600), 95, 115, scroll_speed)
car3 = Enemy('car3.png', x_list[l[2]], randint(500, 600), 90, 110, scroll_speed)

cars = sprite.Group()

cars.add(car1)
cars.add(car2)
cars.add(car3)

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

        #points = font.render('вбивства:' + str(kills), True, (100, 0, 255))
        #window.blit(points, (100, 50))
        car.draw(window)
        car.move()
        cars.draw(window)
        cars.update(scroll_speed)

        if sprite.spritecollideany(car, cars):
            scroll_speed = 0
            speed = 0
        '''human1.draw(window)
        human1.moving()
        human2.draw(window)
        human2.moving()
        human3.draw(window)
        human3.moving()'''
    else:
        window.blit(road, (0, 0))
        if play.draw(window):
            run = True
        if exit.draw(window):
            run = False
    display.update()
    clock.tick(60)

