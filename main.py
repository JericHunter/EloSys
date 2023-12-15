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

"""def main():
    # Example usage
    player1 = Player(player_id=1, rating=1200)
    player2 = Player(player_id=2, rating=1000)

    # Simulate a match where player1 wins
    update_ratings(player1, player2)

    print(f"Player {player1.player_id} new rating: {player1.rating}")
    print(f"Player {player2.player_id} new rating: {player2.rating}")

if __name__ == "__main__":
    main()
"""
class Match:
    def __init__(self, player_a, player_b, result=None):
        """
        Initialize a Match instance.

        Parameters:
        - player_a: Player object for player A
        - player_b: Player object for player B
        - result: Result of the match (e.g., "win", "draw", "loss")
        """
        self.player_a = player_a
        self.player_b = player_b
        self.result = result
        self.processed = False  # Indicates whether the match result has been processed

    def process_match_result(self):
        """
        Process the match result and update player ratings.
        """
        if self.result is not None and not self.processed:
            # Calculate expected outcomes
            p_a, p_b = calculate_expected_outcome(self.player_a.rating, self.player_b.rating)

            # Update player ratings based on the result
            if self.result == "wins":
                self.player_a.rating, self.player_b.rating = update_ratings(self.player_a.rating, self.player_b.rating, p_a)
            elif self.result == "loss":
                self.player_b.rating, self.player_a.rating = update_ratings(self.player_b.rating, self.player_a.rating, p_b)

            # Set processed flag to True
            self.processed = True

    def __str__(self):
        """
        Return a string representation of the match.
        """
        winner = self.player_a if self.result == "wins" else self.player_b
        loser = self.player_b if self.result == "wins" else self.player_a

        return f"Match between {winner.player_id} (Winner) and {loser.player_id} (Loser) - Result: Player {winner.player_id} {self.result}"


# Example usage
player1 = Player(player_id=1, rating=1200)
player2 = Player(player_id=2, rating=1000)

# Create a Match instance
example_match = Match(player_a=player1, player_b=player2, result="wins")

# Display the match details using the __str__ method
print(example_match)