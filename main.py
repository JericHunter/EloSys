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

def update_ratings(winner, loser, k_factor=32):
    """
    Update the ratings of players based on the match outcome.
    """
    expected_outcome_winner = calculate_expected_outcome(winner.rating, loser.rating)
    expected_outcome_loser = 1 - expected_outcome_winner

    # Calculate rating changes
    rating_change_winner = k_factor * (1 - expected_outcome_winner)
    rating_change_loser = k_factor * (0 - expected_outcome_loser)

    # Update ratings
    winner.rating += rating_change_winner
    loser.rating += rating_change_loser