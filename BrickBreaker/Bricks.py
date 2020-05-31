"""
Title: Bricks class
"""

from Sprites import Sprite

class Bricks(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(125, 45)
        self.setPOS(self.window.getWidth()/2 - self.width/2, self.window.getHeight()/2 - self.height)


if __name__ == "__main__":
    from pygame import init
    from Window import Window
    from Paddle import Paddle
    from Ball import Ball

    init()
    window = Window()
    ball = Ball(window)
    paddle = Paddle(window)
    brick = Bricks(window)

    while True:
        window.getEvents()

        ball.bounce()
        paddle.move(window.getKeyPressed())

        window.clearScreen()
        window.blitSprite(ball)
        window.blitSprite(paddle)
        window.blitSprite(brick)
        window.updateScreen()


