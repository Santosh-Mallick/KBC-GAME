import Definitions

menu_options = {
    1: Definitions.start,
    2: Definitions.statistics,
    3: Definitions.settings,
    4: Definitions.exit_game
}

def Home():
    while True:
        Definitions.clear_console()
        print("🔥 Welcome To Kaun Banega Crorepatii!! 🔥\n")
        for key, value in menu_options.items():
            print(f"⭐ {key}. {value.__name__.capitalize().replace('_', ' ')}")

        try:
            choice = int(input("\n\n➤ Choose an Option From 1-4: "))
            if choice in menu_options:
                menu_options[choice]()
            else:
                print("🔴 Invalid option. Please choose a number from 1 to 4.")
                input("Press Enter to try again...")
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to try again...")
