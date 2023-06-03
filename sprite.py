from pygame import*
from random import randint, shuffle

xcor_list = [90, 160, 240, 320]

k = [0,1,2,3]
shuffle(k)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dir = "left"

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 105:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 345:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Human(Player):
    def moving(self):
        if self.dir == "left":
            self.rect.x += 1
            if self.rect.x > 470:
                self.dir = "right"

        if self.dir == "right":
            self.rect.x -= 1
            if self.rect.x < 30:
                self.dir = "left"

class Enemy(GameSprite):
    def update(self, scroll_speed):
        self.rect.y -= scroll_speed
        if self.rect.y <= -115:
            self.rect.x = xcor_list[k[randint(0, 3)]]
            self.rect.y = randint(500, 800)



        #'''if self.rect.y <= 0:
            #self.rect.y = randint(700, 1200)'''
