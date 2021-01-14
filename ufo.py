
import pygame
from pygame.sprite import Sprite


class Ufo(Sprite):
    """A class to represent a single UFO in the fleet."""

    def __init__(self, bs_game):
        """Initialize the UFO and set its starting position."""
        super().__init__()
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.screen_rect = bs_game.screen.get_rect()
        # Load the UFO image and set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()
        # Start each new UFO near the top right of the screen.
        self.rect.x = self.screen_rect.right - (2 * self.rect.width)
        self.rect.y = self.screen_rect.top + self.rect.height
        # Store the UFO's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if UFO is at edge of screen."""
        scren_rect = self.screen.get_rect()
        if self.rect.bottom >= scren_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Move the UFO to the left and up-down."""
        self.y -= (self.settings.ufo_speed * self.settings.fleet_direction)
        self.rect.y = self.y