import math
import time
import random

# Define the Game
class Game:
    def __init__(self, target_score=10):
        self.target_score = target_score

    def is_terminal(self, score):
        return score >= self.target_score

    def utility(self, score, maximizing_player):
        # Returns -1 for a loss, +1 for a win, and 0 otherwise
        if self.is_terminal(score):
            return -1 if maximizing_player else 1
        return 0

    def get_possible_moves(self, score):
        # Players can only add 1 or 2 to the current score
        return [score + 1, score + 2]

# MiniMax Function with Optimization
def minimax(game, score, maximizing_player, depth=5):
    if depth == 0 or game.is_terminal(score):
        return game.utility(score, maximizing_player)

    if maximizing_player:
        max_eval = -math.inf
        for new_score in game.get_possible_moves(score):
            eval = minimax(game, new_score, False, depth - 1)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for new_score in game.get_possible_moves(score):
            eval = minimax(game, new_score, True, depth - 1)
            min_eval = min(min_eval, eval)
        return min_eval

# AI Decision Function
def ai_move(game, current_score, depth):
    # AI chooses its move using minimax
    best_move = None
    best_value = -math.inf  # Start with the worst case for maximizing player
    
    for move in game.get_possible_moves(current_score):
        move_val = minimax(game, move, False, depth)
        if move_val > best_value:
            best_value = move_val
            best_move = move
            
    return best_move

# Main Game Function
if __name__ == "__main__":
    target_score = 10
    game = Game(target_score)

    current_score = 0
    depth = 5  # Limit recursion depth
    maximizing_player = True  # Player goes first

    print(f"Welcome to the game! Try to avoid reaching the target score of {target_score}.\n")

    # Game loop
    while not game.is_terminal(current_score):
        if maximizing_player:
            # User's turn
            print(f"Current score: {current_score}")
            try:
                user_move = int(input("Choose to add 1 or 2 to the current score: "))
                if user_move not in [1, 2]:
                    print("Invalid move. Please choose 1 or 2.")
                    continue
                current_score += user_move
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        else:
            # AI's turn with "thinking" simulation
            print("\nAI is thinking...")
            time.sleep(1)  # Simulate AI thinking time
            
            # AI makes its move
            if current_score >= target_score - 2:
                # If the current score is close to target, AI makes a safer move
                ai_move_choice = random.choice(game.get_possible_moves(current_score))
            else:
                ai_move_choice = ai_move(game, current_score, depth)

            print(f"AI chooses to add {ai_move_choice - current_score}. New score: {ai_move_choice}")
            current_score = ai_move_choice

        maximizing_player = not maximizing_player  # Switch turns

    # Output result
    print("\nGame Over!")
    if maximizing_player:
        print("AI wins!")
    else:
        print("Congratulations! You win!")
