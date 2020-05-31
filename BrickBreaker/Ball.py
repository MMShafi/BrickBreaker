"""
Title: Ball Sprite
"""

from Sprites import Sprite

class Ball(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(10, 10)
        self.setPOS(self.window.getWidth() / 2 - self.width / 2, self.window.getHeight() - (self.height + 10))
        self.spd = 10

    def bounce(self):
        self.x += self.dirX * self.spd
        if self.x > self.window.getWidth() - self.getWidth():
            self.x = self.window.getWidth() - self.getWidth()
            self.dirX = -1
        elif self.x < 0:
            self.x == 0
            self.dirX = 1

        self.y += self.dirY* self.spd
        if self.y > self.window.getHeight() - self.getHeight():
            self.y =  self.window.getHeight() - self.getHeight()
            self.dirY = -1
        elif self.y <0:
            self.y ==0
            self.dirY =1


        self.pos = (self.x, self.y)



if __name__ == "__main__":
    from pygame import init
    from Window import Window

    init()
    window = Window()
    ball = Ball(window)

    while True:
        window.getEvents()
        ball.bounce()
        window.clearScreen()
        window.blitSprite(ball)
        window.updateScreen()

