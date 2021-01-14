
import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from rocket import Rocket
from bullet import Bullet
from ufo import Ufo


class BlueSky:
    """Makes a Pygame window with a blue background."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Blue Sky")
        self.stats = GameStats(self)
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_ufos()        
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and key releases."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.rocket.screen_rect.right:
                self.bullets.remove(bullet)
        self._check_bullet_ufo_collisions()

    def _check_bullet_ufo_collisions(self):
        """Respond to bullet-UFO collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.ufos, True, True)
        if not self.ufos:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_ufos(self):
        """Update the position of all UFOs in the fleet."""
        self._check_fleet_edges()
        self.ufos.update()
        # Look for UFO-rocket collisions.
        if pygame.sprite.spritecollideany(self.rocket, self.ufos):
            self._rocket_hit()
        self._check_ufos_left()

    def _rocket_hit(self):
        """Respond to the rocket being hit by an UFO."""
        if self.stats.rockets_left > 0:
            # Decrement rockets left.
            self.stats.rockets_left -= 1
            # Get rid of any remaining UFOS and bullets.
            self.ufos.empty()
            self.bullets.empty()
            # Create a new fleet and center the rocket.
            self._create_fleet()
            self.rocket.center_rocket()
            sleep(1)
        else:
            self.stats.game_active = False

    def _check_ufos_left(self):
        """Check if any UFOS have reached the left side of the sceen."""
        screen_rect = self.screen.get_rect()
        for ufo in self.ufos.sprites():
            if ufo.rect.left <= screen_rect.left:
                self._rocket_hit()
                break

    def _create_fleet(self):
        """Create the fleet of UFO."""
        # Create an UFO and find the number of UFOs in a row.
        ufo = Ufo(self)
        ufo_width, ufo_height = ufo.rect.size
        rocket_width = self.rocket.rect.width
        available_space_x = (self.settings.screen_width - 
                                (3 * ufo_width) - rocket_width)
        number_ufo_x = available_space_x // (2 * ufo_width)
        # Determine the number of rows of UFOs that fit on the screen.
        available_space_y = self.settings.screen_height - (2 * ufo_height)
        number_rows = available_space_y // (2 * ufo_height)
        # Create the full fleet of UFOs.
        for row_number in range(number_rows):
            for ufo_number in range(number_ufo_x):
                self._create_ufo(ufo_number, row_number)

    def _create_ufo(self, ufo_number, row_number):
        """Create and UFO and place it in the row."""
        ufo = Ufo(self)
        ufo_width, ufo_height = ufo.rect.size
        ufo.x = 5 * ufo_width + 2 * ufo_width * ufo_number
        ufo.rect.x = ufo.x
        ufo.y = ufo_height + 2 * ufo_height * row_number
        ufo.rect.y = ufo.y
        self.ufos.add(ufo)

    def _check_fleet_edges(self):
        """Respond appropriately if any UFO reached an edge."""
        for ufo in self.ufos.sprites():
            if ufo.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for ufo in self.ufos.sprites():
            ufo.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ufos.draw(self.screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()