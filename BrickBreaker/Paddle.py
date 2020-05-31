"""
Title : Paddle Sprite
"""

from Sprites import Sprite
from pygame import K_d, K_a

class Paddle(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(200, 25)
        self.setPOS(self.window.getWidth() / 2 - self.width / 2, self.window.getHeight() - (self.height +10))
        self.spd = 10

    def move(self, keys):
        if keys[K_d] == 1:
            self.x += self.spd
        elif keys[K_a] == 1:
            self.x -= self.spd

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x< 0:
            self.x =0

        self.pos =(self.x, self.y)

if __name__ == "__main__":
    from pygame import init
    from Window import Window

    init()
    window = Window()
    paddle = Paddle(window)

    while True:
        window.getEvents()
        paddle.move(window.getKeyPressed())
        window.clearScreen()
        window.blitSprite(paddle)
        window.updateScreen()
