
class GameStats:
    """Track statistics for Blue Sky."""
   
    def __init__(self, bs_game):
        """Initialize statistics."""
        self.settings = bs_game.settings
        self.reset_stats()
        # Start Blue Sky in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rockets_left = self.settings.rocket_limit