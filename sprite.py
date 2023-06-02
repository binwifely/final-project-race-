from pygame import*
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dir = "left"

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 110:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 340:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
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



        #'''if self.rect.y <= 0:
            #self.rect.y = randint(700, 1200)'''
