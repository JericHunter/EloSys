import math
class Player:
    def __init__(self, player_id, rating=1000, username=None):
        self.player_id = player_id
        self.rating = rating
        self.username = username

def calculate_expected_outcome(player_a_rating, player_b_rating):
    """
    Calculate the expected outcome of a match between two players.
    """
    exponent = (player_b_rating - player_a_rating) / 400.0
    return 1 / (1 + math.pow(10, exponent))