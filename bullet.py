
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the rocket."""

    def __init__(self, bs_game):
        """Create a bullet object at the rocket's current position."""
        super().__init__()
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midright = bs_game.rocket.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right of the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)