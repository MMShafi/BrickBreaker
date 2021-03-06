"""
Title : Paddle Sprite
"""

from Sprites import Sprite
from pygame import K_d, K_a

class Paddle(Sprite):

    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(150, 25)
        self.setPOS(self.window.getWidth() / 2 - self.width / 2, self.window.getHeight() - (self.height +10))
        self.spd = 15

    # --- Modifier Methods --- #

    def move(self, keys):
        #Only need to move the paddle left and right , it had a set y position
        if keys[K_d] == 1:
            self.x += self.spd
        elif keys[K_a] == 1:
            self.x -= self.spd

        #Setting paddle boundaries
        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x< 0:
            self.x =0

        self.pos =(self.x, self.y)


