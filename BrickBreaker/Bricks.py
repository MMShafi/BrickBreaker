"""
Title: Bricks class
"""

from Sprites import Sprite
from Window import Window

class Box(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(100, 30)
        self.setPOS(self.window.getWidth()/2 - self.width/2, self.window.getHeight()/2 - self.height)


class Bricks:

    def __init__(self):
        self.window = Window()
        self.bricks = []

        for i in range(7):
            self.bricks.append(Box(self.window))

        for i in range(len(self.bricks)):
            self.bricks[i].setPOS((i+0.2) * (self.bricks[i].getWidth() + 10), 15 )

    def blitBricks(self):
        for brick in self.bricks:
            self.window.blitSprite(brick)


if __name__ == "__main__":
    from pygame import init
    from Window import Window
    from Paddle import Paddle
    from Ball import Ball

    init()
    window = Window()
    ball = Ball(window)
    paddle = Paddle(window)
    bricks = Bricks()

    while True:
        window.getEvents()

        ball.bounce()
        paddle.move(window.getKeyPressed())

        window.clearScreen()
        window.blitSprite(ball)
        window.blitSprite(paddle)
        bricks.blitBricks()

        window.updateScreen()


