import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf


import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()



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
        # Check for and respond to events.
        gf.check_events()
        
        # Update the screen with the ship.
        gf.update_screen(ai_settings, screen, ship)
        
# Call the run_game() function to start the game.
if __name__ == "__main__":
    run_game()

