import os
import Game_Start

all_time_total_winnings = 0
difficulty_level = "easy_questions"  # Default difficulty level

def clear_console():
    '''
    Function To Clear Console.
    '''
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux (os.name is 'posix')
        os.system('clear')

def start():
    global all_time_total_winnings  
    clear_console()
    print("Starting the game...")
    input("Press Enter to continue...")
    clear_console()
    total_winnings = Game_Start.main()  
    all_time_total_winnings += int(total_winnings[0])
    print(f"You won a total of {total_winnings[0]} points!")
    input("Press Enter to return to the main menu...")
    
def statistics():
    global all_time_total_winnings  
    clear_console()
    print("STATISTICS\n")
    total_winnings, level = Game_Start.get_statistics()  
    print(">> Total Levels Played in last match : ", level)
    print(">> Your Total Points in the last match : ", total_winnings)
    print(">> All Time Total Points : ", all_time_total_winnings,"\n")
    input("Press Enter to return to the main menu...")

def settings():
    global difficulty_level
    clear_console()
    print("SETTINGS")
    print("Choose Difficulty level")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    try:
        opt = int(input("Enter your choice (1-3): "))
        if opt == 1:
            difficulty_level = "easy_questions"
        elif opt == 2:
            difficulty_level = "medium_questions"
        elif opt == 3:
            difficulty_level = "hard_questions"
        else:
            print("Invalid option. Please choose a number from 1 to 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    input("Press Enter to return to the main menu...")

def exit_game():
    clear_console()
    exit()
