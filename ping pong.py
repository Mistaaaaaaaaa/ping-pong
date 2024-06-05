from typing import Any
from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
        def __init__(self,player_image,player_speed,player_x,player_y, size_x, size_y):
                super().__init__()
                self.image = transform.scale(image.load(player_image), (size_x, size_y))
                self.speed = player_speed
                self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
                self.size_x = size_x
                self.size_y = size_y
        def reset(self):
                window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
        def update_r(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_UP]:
                        self.rect.y -= self.speed
                if keys_pressed[K_DOWN]:
                        self.rect.y += self.speed
        def update_l(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_w]:
                    self.rect.y -= self.speed
                if keys_pressed[K_s]:
                    self.rect.y += self.speed
class enemy(GameSprite):
        def update(self):
                self.rect.x += self.speed
                global lost
                if self.rect.y > win_height:
                        self.rect.x = randint(80,win_width - 80)     
                        self.rect.y = 0
                        lost = lost + 1                    
                        
            
win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption("ping-pong")
background = transform.scale(
    image.load("tło.jpg"),
    (win_width, win_height)
)

platform_l = Player("platforma 1.jpg",10,650, win_height - 100, 50, 150)
platform_2 = Player("platforma 2.jpg",10,-5, win_height - 100, 50, 150)
pilki = sprite.Group()

       




#pętla gry 
clock = time.Clock()
FPS = 60
finish = False
game = True
while game:
        window.blit(background,(0,0))      
        
        
        
        for e in event.get():
                if e.type == QUIT:
                        game = False

        if finish != True:
               platform_l.update_r()
               platform_2.update_l()
               platform_l.reset()
               platform_2.reset()


               
                       


               display.update()

               
        
        
        
        
        
        clock.tick(FPS)
                        