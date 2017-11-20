import pygame
import random
import math

width = 510
height = 480
blue_color = (97, 159, 182)

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# creates background
def background_img():
    screen.fill(blue_color)
    background_image = pygame.image.load('images/background.png')
    screen.blit(background_image, (0, 0))
    pygame.display.update()


# create classes
class Fighters(object):
    def __init__(self, name, x, y, dir_x, dir_y, image):
        self.name = name
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.image = image

    # the following creates movement for the fighter
    def move_east(self):
        if self.x < width:
            self.x += self.dir_x
        else:
            self.x = 0

    def move_northeast(self):
        self.move_north()
        self.move_east()
                        
    def move_north(self):
        if self.y > 0:
            self.y -= self.dir_y
        else:
            self.y = 480

    def move_northwest(self):
        self.move_north()
        self.move_west()

    def move_west(self):
        if self.x > 0:
            self.x -= self.dir_x
        else:
            self.x = 510

    def move_southwest(self):
        self.move_south()
        self.move_west()

    def move_south(self):
        if self.y < height:
            self.y += self.dir_y
        else:
            self.y = 0  

    def move_southeast(self):
        self.move_south()
        self.move_east()     

class Hero(Fighters):
    def screen_pos(self):
        screen.blit(self.image, (self.x, self.y))
        # screen.blit(combatant.image, (combatant.x, combatant.y))
        pygame.display.update()

class Monster(Fighters):
    def screen_pos(self):
        screen.blit(self.image, (self.x, self.y))
        # screen.blit(combatant.image, (combatant.x, combatant.y))
        pygame.display.update()


def main():
    
    
    # Game initialization
    hero_image_value = pygame.image.load('images/hero.png')
    monster_image_value = pygame.image.load('images/monster.png')
    hero = Hero('You', 240, 220, 0, 0, hero_image_value)
    monster = Monster('monster', 125, 350, 5, 5, monster_image_value)
    loop_sum = 0
    rand_num = random.randint(1,9)
    
    stop_game = False
    while not stop_game:

        
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        background_img()
        hero.screen_pos()
        monster.screen_pos()
        
        # allows the hero to move from arrow key input
        if event.type == pygame.KEYDOWN:
            # adding or subtracting 60, 30 pixels for the bushes
            if event.key == KEY_DOWN and hero.y < (480 - 60):
                hero.y += 3
            elif event.key == KEY_UP and hero.y > 30:
                hero.y -= 3
            elif event.key == KEY_LEFT and hero.x > 30:
                hero.x -= 3
            elif event.key == KEY_RIGHT and hero.x < (510 - 60):
                hero.x += 3
        
        if loop_sum <= 120:
            if rand_num == 1:
                monster.move_east()
            elif rand_num == 2:
                monster.move_southwest()
            elif rand_num == 3:
                monster.move_north()
            elif rand_num == 4:
                monster.move_northwest()
            elif rand_num == 5:
                monster.move_south()
            elif rand_num == 6:
                monster.move_northeast()
            elif rand_num == 7:
                monster.move_west()
            else: 
                monster.move_southeast()
        else:
            loop_sum = 0
            rand_num = random.randint(1,9)

        # collision detection
        if hero.x + 32 < monster.x:
            pass
        elif monster.x + 32 < hero.x:
            pass
        elif hero.y + 32 < monster.y:
            pass
        elif monster.y + 32 < hero.y:
            pass
        else:
            prompt_cont = raw_input("You've caught the monster!  Would you like to continue? ")
            hero.x += 50
            hero.y += 50

        print monster.x, monster.y
        
        loop_sum += 1
        
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
