from typing import *
from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
        def __init__(self,player_image,player_x,player_y,player_speed, size_x, size_y):
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
win_width = 600
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption("ping-pong")
background = transform.scale(
    image.load("tło.jpg"),
    (win_width, win_height)
)

platform_l = Player("platforma 1.jpg",30,200,4,50,150)
platform_2 = Player("platforma 2.jpg",520,200,4,50,150)
ball = GameSprite("piłkaaaaa.png",200, 200, 4, 50, 50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
       'PLAYER 1 LOSES!', True, (180,0,0)
)                          
lose2 = font1.render(
       'PLAYER 2 LOSES!', True, (180,0,0)
)                                              



speed_x = 3
speed_y = 3
#pętla gry 
clock = time.Clock()
FPS = 60
finish = False
game = True
while game:
             
        
        
        
        for e in event.get():
                if e.type == QUIT:
                        game = False

        if finish != True:
               window.blit(background,(0,0)) 
               ball.rect.x += speed_x
               ball.rect.y += speed_y
               platform_l.update_r()
               platform_2.update_l()
               if ball.rect.y > win_height - 50 or ball.rect.y < 0:
                      speed_y *= -1
               if sprite.collide_rect(platform_l, ball )or sprite.collide_rect(platform_2, ball):
                        speed_x *= -1 
               if ball.rect.x <0 : 
                        finish = True
                        window.blit(lose1, (200,200))
               if ball.rect.x > win_width - 50: 
                        finish = True
                        window.blit(lose2, (200,200))


               
                       

               platform_l.reset()
               platform_2.reset()
               ball.reset() 
        display.update()

               
        
        
        
        
        
        clock.tick(FPS)
                        