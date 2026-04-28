# main.py
from games import stone_paper_scissors, dice_roll

def run_arcade():
    print("=== Welcome to the Python Arcade ===")
    
    while True:
        print("\n--- Game Menu ---")
        print("1. Play Stone-Paper-Scissors")
        print("2. Play Dice Roll Game")
        print("3. Exit Arcade")
        
        choice = input("Select a game to play (1-3): ")
        
        if choice == '1':
            stone_paper_scissors.play_sps()
        elif choice == '2':
            dice_roll.play_dice()
        elif choice == '3':
            print("\nThanks for playing! See you next time.")
            break
        else:
            print("[ERROR] Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    run_arcade()