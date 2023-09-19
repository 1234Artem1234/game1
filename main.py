from pygame import *
from random import randint
class all(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image=transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class player(all):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if self.rect.x > 0 and self.x_speed<0 or self.rect.x < wight-80  and self.x_speed>0:
            self.rect.x += self.x_speed
        if self.rect.y > 0 and self.y_speed<0 or self.rect.y < 420 and self.y_speed>0:
            self.rect.y += self.y_speed     
class Bullet(all):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
window = display.set_mode((1366, 728))
window.fill((0, 125, 126))
display.set_caption('labirint')
run = True
blue = (0, 125, 125)
wight =1366
haight = 728
win = all('win.jpg', wight, haight, 0, 0)
player2 = player('123.jpg', 100, 10, 400, haight-50, 0, 0)
ball = Bullet('ball.png', 15, 15, 400, 100, 0, 5)
walls = sprite.Group()
for i in range(wight//20):
    wall1 = all('123.jpg', 20, 20, 20*i, 0)
    walls.add(wall1)
for i in range(wight//20):
    wall1 = all('123.jpg', 20, 20, 20*i, 20)
    walls.add(wall1)
for i in range(wight//20):
    wall1 = all('123.jpg', 20, 20, 20*i, 40)
    walls.add(wall1)
lines = sprite.Group()
lose = all('lose.jpeg', wight, haight, 0, 0)
line1 = all('123.jpg', wight, 20, 0, -20)
line2 = all('123.jpg', 20, haight, -20, 0)
line3 = all('123.jpg', 20, haight, wight, 0)
line4 = all('123.jpg', wight, 20, 0, haight-10)
lines.add(line1)
lines.add(line2)
lines.add(line3)
lines.add(line4)
balls = sprite.Group()
players = sprite.Group()
balls.add(ball)
players.add(player2)
finish = True
touch = True
count = 1
while run:
    if touch and finish:
        if count % 10 == 0:
            ball.y_speed += 1
        window.fill((0, 125, 126))
        players.draw(window)
        balls.draw(window)
        walls.draw(window)
        lines.draw(window) 
        for e in event.get():
            if e.type ==QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    player2.x_speed = 8 
                elif e.key == K_LEFT:
                    player2.x_speed = -8      
            elif e.type == KEYUP:   
                if e.key == K_RIGHT:
                    player2.x_speed = 0     
                elif e.key == K_LEFT:
                    player2.x_speed = 0
        if sprite.groupcollide(players, balls, False, False):
                ball.y_speed = ball.y_speed*(-1)
                ball.x_speed = randint(1, 10)-5
        if sprite.groupcollide(walls, balls, True, False):
            ball.y_speed = ball.y_speed*(-1)
            ball.x_speed = randint(1, 10)-5
            count += 1
        if sprite.collide_rect(line2, ball):
            ball.y_speed = ball.y_speed*(1)
            ball.x_speed = ball.x_speed*(-1) + 1
        if sprite.collide_rect(line4, ball):
            touch = False
        if sprite.collide_rect(line3, ball):
            ball.y_speed = ball.y_speed*(1)
            ball.x_speed = ball.x_speed*(-1) - 2
        if sprite.collide_rect(line1, ball):
            finish = False 
        player2.update() 
        ball.update()      
        time.delay(10)
        display.update()  
    elif not touch:
        while not touch and run:
            window.fill((0, 125, 126))
            lose.reset()
            for e in event.get():
                if e.type ==QUIT:
                    run = False
            time.delay(50)
            display.update()
    elif not finish:
        while not finish and run:
            window.fill((0, 125, 126))
            win.reset()
            for e in event.get():
                if e.type ==QUIT:
                    run = False
            time.delay(50)
            display.update()