from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 880:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 880:
            self.rect.y += self.speed

win = display.set_mode((1920, 1080))
display.set_caption('Windows 12')
bg = transform.scale(image.load('windows.jpg'), (1920, 1080))
lose = transform.scale(image.load('Bsodwindows10.png'), (1920, 1080))
clock = time.Clock()
fps = 8

microsoft = Player('microsoft.png', 40, 500, 50, 200, 50)
gates = Player('Gates.jpg', 1830, 500, 50, 200, 50)
lose = GameSprite('Bsodwindows10.png', 0, 0, 1920, 1080, 0)
ball = GameSprite('ball.png', 1000, 500, 10, 15, 50)
speed_x = 50
speed_y = 50

mixer.init()
startup = mixer.Sound('windows-11-startup.mp3')
lose_sound = mixer.Sound('windows-foreground.mp3')
startup.play()

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        win.blit(bg, (0, 0))
        microsoft.update_l()
        gates.update_r()
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
        if sprite.collide_rect(microsoft, ball) or sprite.collide_rect(gates, ball):
            speed_x *= -1
        if ball.rect.y < 0 or ball.rect.y > 1030:
            speed_y *= -1
        microsoft.reset()
        gates.reset()
        ball.reset()
        if ball.rect.x >= (gates.rect.x + 80):
            finish = True
            lose.reset()
            lose_sound.play()
        if ball.rect.x <= (microsoft.rect.x - 80):
            finish = True
            lose.reset()
            lose_sound.play()
    else:
        finish = False
        microsoft.rect.x = 40
        microsoft.rect.y = 500
        gates.rect.x = 1830
        gates.rect.y = 500
        ball.rect.x = 1000
        ball.rect.y = 500
        time.delay(5000)
        startup.play()
    clock.tick(fps)
    display.update()