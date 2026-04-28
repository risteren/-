from pygame import*

window = display.set_mode((700, 500))
window.fill((107, 142, 35))
clock = time.Clock()
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
           self.rect.y += self.speed
    def  updates(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
           self.rect.y += self.speed
    
player1 = Player('racket.png', 5, 250, 4, 20, 110)
player2 = Player('racket.png', 675, 250, 4, 20, 110)
ball = GameSprite('tenis_ball.png', 350, 250, 3, 30, 30)



while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        
        
    if not finish:
        window.fill((107, 142, 35))
        player1.reset()
        player1.update()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(60)

