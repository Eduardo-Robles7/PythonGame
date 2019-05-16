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

        #create enemy 
        self.ENEMY_SIZE = 50 
        self.ENEMY_COLOR = (255,0,0)
        self.enemy_pos = [random.randint(0,self.SCREEN_WIDTH-self.ENEMY_SIZE), 0]

        #set game speed
        self.clock = pygame.time.Clock()
        self.SPEED = 10

    def detect_collision(self,player_pos, enemy_pos):

        #player coordinate
        player_x = self.player_pos[0]
        player_y = self.player_pos[1]

        #enemy coodrinate
        enemy_x = self.enemy_pos[0]
        enemy_y = self.enemy_pos[1]

        if(enemy_x >= player_x and enemy_x < (player_x + self.PLAYER_SIZE)) or (player_x >= enemy_x and player_x < (enemy_x + self.ENEMY_SIZE)):
             if(enemy_y >= player_y and enemy_y < (player_y + self.PLAYER_SIZE)) or (player_y >= enemy_y and player_y < (enemy_y + self.ENEMY_SIZE)):
                 return True

        return False

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
                        if(x_coordinate > self.SCREEN_WIDTH-self.PLAYER_SIZE): #check if bigger than width
                            x_coordinate = self.SCREEN_WIDTH-self.PLAYER_SIZE #set it within bound

                    self.player_pos = [x_coordinate,y_coordinate] #update the coordinate for player

            self.screen.fill(self.BACKGROUND_COLOR)

            #set enemy position
            if self.enemy_pos[1] >= 0 and self.enemy_pos[1] < self.SCREEN_HEIGHT:
                self.enemy_pos[1] += self.SPEED
            else:
                self.enemy_pos[0] = random.randint(0,self.SCREEN_WIDTH - self.ENEMY_SIZE)
                self.enemy_pos[1] = 0

            #detect for collision
            if self.detect_collision(self.player_pos, self.enemy_pos):
                self.game_over = True #end the game 
                break

            #draw player
            pygame.draw.rect(self.screen, self.PLAYER_COLOR, (self.player_pos[0], self.player_pos[1], self.PLAYER_SIZE, self.PLAYER_SIZE))

            #draw enemy
            pygame.draw.rect(self.screen, self.ENEMY_COLOR, (self.enemy_pos[0], self.enemy_pos[1], self.ENEMY_SIZE, self.ENEMY_SIZE))

            self.clock.tick(30)
            pygame.display.update()



