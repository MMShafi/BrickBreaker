"""
Title: Ball Sprite
"""

from Sprites import Sprite

class Ball(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(10, 10)
        self.setPOS(self.window.getWidth() / 2 - self.width / 2, self.window.getHeight()/2 - self.height/2)
        self.spd = 10
        self.score = 0

    # --- Modifier Methods --- #

    #Make ball bounce of the sides of the screen
    def bounce(self):
        self.x += self.dirX * self.spd
        if self.x > self.window.getWidth() - self.getWidth():
            self.x = self.window.getWidth() - self.getWidth()
            self.dirX = -1
        elif self.x < 0:
            self.x == 0
            self.dirX = 1

        self.y += self.dirY* self.spd
        if self.y <0:
            self.y ==0
            self.dirY =1

        #Game over if ball leaves bottom of screen
        elif  self.y > self.window.getHeight() - self.getHeight():
            print("Ball left bottom of the screen, Game Over")
            exit()


        self.pos = (self.x, self.y)

    #If ball hits a brick, score will be updates
    def updateScore(self):
        self.score+=1

    # --- Accessor methods --- #

    #Paddle and ball collision - ball will bounce back
    def getBallPaddleCollision(self, paddle):
        if paddle.getX() <= self.x +self.sprite.get_rect().width <= paddle.getX() + paddle.getWidth() + self.sprite.get_rect().width and paddle.getY()<= self.y + self.sprite.get_rect().height <=paddle.getY() + paddle.getHeight() + self.sprite.get_rect().height:

            self.y += self.dirY * self.spd
            self.y = paddle.getY() - self.getHeight()
            self.dirY = -1

        else:
            pass
    #Ball and brick collision - ball will bounce back
    def getBallBrickCollision(self, bricks):
        if bricks.getX() <= self.x +self.sprite.get_rect().width <= bricks.getX() + bricks.getWidth() + self.sprite.get_rect().width and bricks.getY()<= self.y + self.sprite.get_rect().height <= bricks.getY() + bricks.getHeight() + self.sprite.get_rect().height:

            self.y += self.dirY * self.spd
            self.y = (bricks.getY() + bricks.getHeight()) + self.getHeight()
            self.dirY = 1
            return True
        else:
            return False


    def getScore(self):
        return self.score
