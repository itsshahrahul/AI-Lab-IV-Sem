from itertools import permutations

def solve_cryptarithm():
    # Define the words and the final equation
    words = ["SEND", "MORE"]
    result = "MONEY"
    
    # Get all unique letters
    unique_letters = set("".join(words) + result)
    assert len(unique_letters) <= 10, "Too many unique letters!"
    
    # Define the positions for letters in the final equation
    def to_number(word, assignment):
        return sum(assignment[letter] * (10 ** i) for i, letter in enumerate(word[::-1]))
    
    for perm in permutations(range(10), len(unique_letters)):
        assignment = dict(zip(unique_letters, perm))
        
        # Check the leading digit constraint
        if assignment["S"] == 0 or assignment["M"] == 0:
            continue
        
        # Check if the equation holds
        send = to_number("SEND", assignment)
        more = to_number("MORE", assignment)
        money = to_number("MONEY", assignment)
        
        if send + more == money:
            print(f"SEND + MORE = MONEY: {send} + {more} = {money}")
            return assignment  # Solution found

solution = solve_cryptarithm()
if solution:
    print("Solution:", solution)
else:
    print("No solution found.")
