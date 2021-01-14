
class Settings:
    """A class to store all settings for Blue Sky."""

    def __init__(self):
        """Initialize game settings."""
        self.bg_color = (135, 206, 250)
        # Rocket settings
        self.rocket_speed = 1.5
        self.rocket_limit = 3
        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (230, 15, 15)
        self.bullets_allowed = 3
        # UFO settings
        self.ufo_speed = 0.4
        self.fleet_drop_speed = 20
        self.fleet_direction = 1