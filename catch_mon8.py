import pygame

width = 510
height = 480
blue_color = (97, 159, 182)

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
    
    stop_game = False
    while not stop_game:

        
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        # pygame.display.update()
        background_img()
        hero.screen_pos()
        monster.screen_pos()
        if loop_sum <= 120:
            monster.move_east()
        elif loop_sum > 120 and loop_sum <= 240:
            monster.move_southwest
        elif loop_sum > 240 and loop_sum <= 360:
            monster.move_north()
        elif loop_sum > 360 and loop_sum <= 480:
            monster.move_northwest()
        elif loop_sum > 480 and loop_sum <= 600:
            monster.move_south()
        elif loop_sum > 600 and loop_sum <= 720:
            monster.move_northeast()
        elif loop_sum > 720 and loop_sum <= 840:
            monster.move_west()
        elif loop_sum > 840 and loop_sum <= 960:
            monster.move_southeast()
        else:
            loop_sum = 0

        print monster.x, monster.y
        
        loop_sum += 1
        
        
        




        # Draw background
        # background_img()
        # screen.fill(blue_color)
        # background_image = pygame.image.load('images/background.png')
        # screen.blit(background_image, (0, 0))
        
        


        # # Game display
        # hero.screen_pos(monster)
        # monster.screen_pos(hero)

        # pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
