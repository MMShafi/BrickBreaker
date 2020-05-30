"""
Title: Pygame Window Frame for Brick Breaker
"""

import pygame

class Window:

    def __init__(self):
        self.title = "Brick Breaker"
        self.width = 800
        self.height = 600
        self.fps = 30
        self.screenDimensions = (self.width, self.height)
        self.background = (50, 50, 50)
        self.frame = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screenDimensions)
        self.screen.fill(self.background)
        self.caption =  pygame.display.set_caption(self.title)
        self.keysPressed = None

    # --- Modifier Methods --- #

    def updateScreen(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

    def clearScreen(self):
        self.screen.fill(self.background)

    #def blitSprite(self, sprite):

    def run(self):
        while True:
            ## --- INPUTS
            self.getEvents()
            ## --- PROCESSING

            # add sprite functions here

            ## --- OUTPUTS
            self.clearScreen()
            self.updateScreen()

    # --- Accessor Methods --- #

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.keysPressed = pygame.key.get_pressed()

    def getWidth(self):
        return self.screen.get_rect().width

    def getHeight(self):
        return self.screen.get_rect().height

    def getKeyPressed(self):
        return self.keysPressed

if __name__ == "__main__":
    pygame.init()
    window = Window()
    window.run()