import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Call the run_game() function to start the game.
# run_game()



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    
    # Create an instance of the Settings class.
    ai_settings = Settings()
    
    # Create the game window.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Start the main loop for the game.
    while True:
        # Your game logic goes here.
        
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Call the run_game() function to start the game.
if __name__ == "__main__":
    # run_game()




 def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    
    # Create an instance of the Settings class.
    ai_settings = Settings()
    
    # Create the game window.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create a ship.
    ship = Ship(screen)
    
    # Start the main loop for the game.
    while True:
        # Your game logic goes here.
        
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        
        # Draw the ship at its current location.
        ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Call the run_game() function to start the game.
if __name__ == "__main__":
    # run_game()
    





 def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    
    # Create an instance of the Settings class.
    ai_settings = Settings()
    
    # Create the game window.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create a ship.
    ship = Ship(ai_settings, screen)
    
    # Start the main loop for the game.
    while True:
        # Check for and respond to events.
        gf.check_events(ship)
        ship.update()
        
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        
        # Your game logic goes here.
        
        # Draw the ship at its current location.
        ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Call the run_game() function to start the game.
if __name__ == "__main__":
    run_game()



