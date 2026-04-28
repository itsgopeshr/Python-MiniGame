# games/dice_roll.py
import random

def play_dice():
    print("\n--- Dice Roll Game ---")
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)
    
    print("You rolled a:", user_roll)
    print("Computer rolled a:", comp_roll)
    
    if user_roll > comp_roll:
        print("[RESULT] You Win!")
    elif user_roll < comp_roll:
        print("[RESULT] Computer Wins!")
    else:
        print("[RESULT] It's a Draw!")