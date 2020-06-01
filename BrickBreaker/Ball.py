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

    def getBallPaddleCollision(self, paddle):
        if paddle.getX() <= self.x +self.sprite.get_rect().width <= paddle.getX() + paddle.getWidth() + self.sprite.get_rect().width and paddle.getY()<= self.y + self.sprite.get_rect().height <=paddle.getY() + paddle.getHeight() + self.sprite.get_rect().height:
            return True
        else:
            return False


if __name__ == "__main__":
    from pygame import init
    from Window import Window
    from Paddle import Paddle
    from Bricks import *

    init()
    window = Window()
    ball = Ball(window)
    paddle = Paddle(window)
    box = Box(window)
    bricks = Bricks(window)

    while True:
        window.getEvents()
        ball.bounce()
        paddle.move(window.getKeyPressed())
        window.clearScreen()

        if ball.getBallPaddleCollision(paddle):
            window.blitSprite(box)

        window.blitSprite(ball)
        window.blitSprite(paddle)
        bricks.blitBricks()

        window.updateScreen()

