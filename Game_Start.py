import Data
import random
import Definitions

total_winnings = 0  
level = 0
lifelines_used = {"50:50": False, "Flip The Question": False, "Double Dip": False, "Ask The Expert": False} #By Default Values

def display_question(question_data, remaining_options=None):
    """__

    Args:
        question_data (dict): [questions, options, answer]
        remaining_options (list): _description_. Defaults to None.
    """
    print(" ➤ ",question_data["question"], end="\n\n")
    options = remaining_options if remaining_options else question_data["options"]
    for i in range(len(options)):
        option = options[i]
        print(f"👉 {i+1}. {option}")
        
def display_lifelines():
    """
    _Displays Lifeline_
    _Checks if that Lifeline hasn't been used._
    """
    print("\n ➤ Lifelines\n")
    for key, value in Data.lifeline[0].items():
        if not lifelines_used[value]:
            print(f"👉 {key} : {value}")
    
def get_statistics():
    """
    Returns:
        total_winnings, level : Returns The Total Winnings and Total Level Played
    """
    return total_winnings, level

def use_50_50(options, answer):
    """
    50:50: Eliminates two incorrect options.

    Args:
        options (list): Total options in that question
        answer (list): Correct Answer

    Returns:
        remaining_options : Rest Options Excluding Answer
    """
    remaining_options = [answer]
    while len(remaining_options) < 2:
        option = random.choice(options)
        if option != answer and option not in remaining_options:
            remaining_options.append(option)
    remaining_options.sort(key=options.index)
    return remaining_options

def use_flip_question():
    """
    Flips The Question

    Returns:
        more_questions: list[dict[str, Any]]
    """
    return random.choice(Data.more_questions)

def use_double_dip(question_data):
    """
    User can answer two times
    Args:
        question_data (dict): [questions, options, answer] 
    """
    first_attempt = int(input("Enter your first choice (1-4): ")) - 1
    if question_data["options"][first_attempt] == question_data["answer"]:
        return True
    else:
        second_attempt = int(input("Enter your second choice (1-4): ")) - 1
        return question_data["options"][second_attempt] == question_data["answer"]

def use_ask_the_expert(answer):
    """
    Answer Is Displayed Directly

    Args:
        answer (str): question_data["answer"]
    """
    print(f"\n🚨 The expert says the correct answer is: {answer} \n")

def main():
    global total_winnings, level 
    total_winnings = level = 0
    print("🔥 Welcome To Kaun Banega Crorepatii!! 🔥\n")
    
    # Getting the difficulty level from Definitions
    difficulty_level = Definitions.difficulty_level
    questions = getattr(Data, difficulty_level)
    
    # Shuffle The Questions
    random.shuffle(questions)
    
    #Fetches Question Data Based On The Difficulty Level
    for question_data in questions:
        remaining_options = None
        
        while True:
            display_question(question_data, remaining_options)
            display_lifelines()
            user_choice = input("\nEnter your choice (1-4) or (6-9) for lifelines: ")
            
            if user_choice.isdigit():
                user_choice = int(user_choice)
                
                if user_choice in range(1, 5):
                    selected_option = question_data["options"][user_choice - 1]
                    
                    # Checking user answer
                    if selected_option == question_data["answer"]:
                        total_winnings += Data.level_winnings[level]
                        print("\n✅️ Correct answer! You Won", Data.level_winnings[level], "points.\n")
                        level += 1
                        break
                    else:
                        print("🔴 Sorry, that's incorrect. The Correct answer was : ", question_data["answer"], "\n")
                        return total_winnings, level
                    
                elif user_choice == 6 and not lifelines_used["50:50"]:
                    remaining_options = use_50_50(question_data["options"], question_data["answer"])
                    lifelines_used["50:50"] = True
                    
                elif user_choice == 7 and not lifelines_used["Flip The Question"]:
                    question_data = use_flip_question()
                    lifelines_used["Flip The Question"] = True
                    remaining_options = None
                    
                elif user_choice == 8 and not lifelines_used["Double Dip"]:
                    if use_double_dip(question_data):
                        total_winnings += Data.level_winnings[level]
                        print("✅️ Correct answer! You Won", Data.level_winnings[level], "points.\n")
                        level += 1
                        lifelines_used["Double Dip"] = True
                        break
                    else:
                        print("😢 Sorry, both answers were incorrect. The correct answer was:", question_data["answer"], "\n")
                        lifelines_used["Double Dip"] = True
                        return total_winnings, level
                   
                elif user_choice == 9 and not lifelines_used["Ask The Expert"]:
                    use_ask_the_expert(question_data["answer"])
                    lifelines_used["Ask The Expert"] = True
                    
                else:
                    print("🔴 Invalid choice or lifeline already used. Please try again.")
                    
                
            else:
                print("🔴 Invalid input. Please enter a number.")
                continue
    
    return total_winnings, level
