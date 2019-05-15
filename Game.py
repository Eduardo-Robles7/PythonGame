import pygame
import random
import sys

class Game:

    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.BACKGROUND_COLOR = (0,0,0) #black color
        self.PLAYER_COLOR = (0,0,255) #blue color
        self.PLAYER_SIZE = 50
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.player_pos = [self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT-2*self.PLAYER_SIZE]
        self.game_over = False
        

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    x_coordinate = self.player_pos[0]
                    y_coordinate = self.player_pos[1]

                    if event.key == pygame.K_LEFT:
                        x_coordinate -= self.PLAYER_SIZE #get new coordinate
                        if(x_coordinate < 0): #check if smaller than the width
                            x_coordinate = 0  #set it within bound

                    elif event.key == pygame.K_RIGHT:
                        x_coordinate += self.PLAYER_SIZE #get new coordinate
                        if(x_coordinate > self.SCREEN_WIDTH-50): #check if bigger than width
                            x_coordinate = self.SCREEN_WIDTH-50 #set it within bound

                    self.player_pos = [x_coordinate,y_coordinate] #update the coordinate for player

            self.screen.fill(self.BACKGROUND_COLOR)
            pygame.draw.rect(self.screen, self.PLAYER_COLOR, (self.player_pos[0], self.player_pos[1], self.PLAYER_SIZE, self.PLAYER_SIZE))
            pygame.display.update()



