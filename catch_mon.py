import pygame

def main():
    width = 510
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    
    class Fighters(object):
        def __init__(self, name):
            self.name = name

    class Hero(Fighters):
        def screen_pos(self):
            hero_image = pygame.image.load('images/hero.png')        
            screen.blit(hero_image, (240, 220))

    class Monster(Fighters):
        def screen_pos(self):
            hero_image = pygame.image.load('images/monster.png')        
            screen.blit(hero_image, (125, 350))

    # Game initialization
    hero = Hero('You')
    monster = Monster('monster')

    stop_game = False
    while not stop_game:

        
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        background_image = pygame.image.load('images/background.png')
        screen.blit(background_image, (0, 0))
        
        


        # Game display
        hero.screen_pos()
        monster.screen_pos()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
