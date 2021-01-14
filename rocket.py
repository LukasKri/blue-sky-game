
import pygame


class Rocket:
    """A class to manage the rocket."""

    def __init__(self, bs_game):
        """Initialize the rocket and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()
        self.settings = bs_game.settings
        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        # Start the new rocket at the left side of the screen.
        self.rect.midleft = self.screen_rect.midleft
        # Store a decimal value for rocket's horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Movements flags.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flags."""
        if self.moving_up and self.rect.top > 0:
             self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        """Center the rocket on the screen."""
        self.rect.left = self.screen_rect.left
        self.x = float(self.rect.x)