from Window import Window
from Paddle import Paddle
from Bricks import *
from Ball import Ball

class Engine:
    def __init__(self):
        self.window = Window()
        self.paddle = Paddle(self.window)
        self.bricks = Bricks(self.window)
        self.ball = Ball(self.window)
        self.running = True
        self.check = True



    def run(self):
        while self.running:
            # --- Inputs --- #
            self.window.getEvents()

            # --- Processing --- #
            self.ball.bounce()
            self.paddle.move(self.window.getKeyPressed())
            self.ball.getBallPaddleCollision(self.paddle)

            for brick in self.bricks.getBricks(): #Checks collision for all the brick
               if self.ball.getBallBrickCollision(brick):
                   self.check = False
                   self.bricks.getBricks().pop(self.check)
                   self.ball.updateScore()
                   print("Score:%s" % (self.ball.getScore()))

                   if len(self.bricks.getBricks()) ==0:
                       self.check = False
                       exit()



            # --- Outputs --- #
            self.window.clearScreen()

            self.window.blitSprite(self.ball)
            self.window.blitSprite(self.paddle)
            self.bricks.blitBricks()

            self.window.updateScreen()


