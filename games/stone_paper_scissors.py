# games/stone_paper_scissors.py
import random

def play_sps():
    opts = ["stone", "paper", "scissors"]
    comp_choice = random.choice(opts)
    
    print("\n--- Stone, Paper, Scissors ---")
    user_input = input("Enter 'stone', 'paper', or 'scissors': ").lower()
    
    if user_input not in opts:
        print("[ERROR] Invalid choice. You lose this round by default!")
        return
        
    print("Computer chose:", comp_choice)
    
    if user_input == comp_choice:
        print("[RESULT] It's a Tie!")
    elif (user_input == "stone" and comp_choice == "scissors") or \
         (user_input == "paper" and comp_choice == "stone") or \
         (user_input == "scissors" and comp_choice == "paper"):
        print("[RESULT] Congratulations, You Win!")
    else:
        print("[RESULT] Computer Wins! Better luck next time.")