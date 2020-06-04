"""
Title: Bricks class
"""

from Sprites import Sprite

class Box(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(100, 30)


class Bricks(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.bricks = []

        #Put boxes in an array
        for i in range(7):

            self.bricks.append(Box(self.window))
        #Set position for each box in the array
        for i in range(len(self.bricks)):
            self.bricks[i].setPOS((i+0.2) * (self.bricks[i].getWidth() + 10), 15 )



    def blitBricks(self):
        for brick in self.bricks:
            self.window.blitSprite(brick)

    def getBricks(self):
        return self.bricks