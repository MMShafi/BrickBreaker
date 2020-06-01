"""
Title: Bricks class
"""

from Sprites import Sprite


class Box(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(100, 30)
        self.setPOS(0, 0)


class Bricks(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.bricks = []


        for i in range(7):
            self.bricks.append(Box(self.window))

        for i in range(len(self.bricks)):
            self.bricks[i].setPOS((i+0.2) * (self.bricks[i].getWidth() + 10), 15 )

    def blitBricks(self):
        for brick in self.bricks:
            self.window.blitSprite(brick)

    def getBricks(self):
        return self.bricks




'''
if __name__ == "__main__":
    from pygame import init
    from Window import Window
    from Paddle import Paddle
    from Ball import Ball

    init()
    window = Window()
    ball = Ball(window)
    paddle = Paddle(window)
    bricks = Bricks(window)

    while True:
        window.getEvents()

        ball.bounce()
        paddle.move(window.getKeyPressed())

        window.clearScreen()
        window.blitSprite(ball)
        window.blitSprite(paddle)
        bricks.blitBricks()

        window.updateScreen()

'''
