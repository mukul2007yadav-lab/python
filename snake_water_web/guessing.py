import random
def get_game_result(user_choice_str):
    # 1. Update the input map to accept both inputs
    choice_map = {
        "S": 1, "SNAKE": 1,
        "G": 0, "GUN": 0,
        "W": -1, "WATER": -1
    }
    
    # 2. Keep the reverse map pointing to the names
    reverse_map = {1: "Snake", 0: "Gun", -1: "Water"}
    
    user_key = user_choice_str.upper()
    you = choice_map.get(user_key)
    
    if you is None:
        return f"Error: I don't recognize '{user_choice_str}'"

    # The rest of your logic remains unchanged
    computer = random.choice([0, 1, -1])
    
    comp_name = reverse_map[computer]
    you_name = reverse_map[you]

    if computer == you:
        result = "Game draw!! Try again."
    elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
        result = "You lose!!"
    else:
        result = "You win!!"
        
    return f"You chose {you_name}, Computer chose {comp_name}. {result}"