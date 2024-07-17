# Kaun Banega Crorepatii (KBC) Game

## Introduction
Welcome to the Kaun Banega Crorepatii (KBC) game, A Python console-based quiz game inspired by the popular Indian TV show! Players answer multiple-choice questions to win points, with the help of various lifelines.

## Requirements
- Python 3.x
- A terminal or command prompt

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Santosh-Mallick/KBC-GAME.git

2. **Navigate to the Game Directory:**
   ```bash
   cd kbc-game

3. **Running the Game**
   ```bash
   python Main.py

## Game Structure

The game consists of multiple-choice questions where players can use lifelines to help them answer correctly. The available lifelines are:

- 50:50: Eliminates two incorrect options.
- Flip The Question: Replaces the current question with a new one.
- Double Dip: Allows the player to attempt answering the question twice.
- Ask The Expert: Provides the expert's opinion on the correct answer.

## How to Play
1. **Start the Game:**
Upon running the game, you'll be greeted with a welcome message and the first question.

2. **Answering Questions:**

- Each question has four options.
- Enter the number corresponding to your choice (1-4).
3. **Using Lifelines:**

Enter the number corresponding to the lifeline:
- 6 for 50:50
- 7 for Flip The Question
- 8 for Double Dip
- 9 for Ask The Expert
- Follow the prompts for the chosen lifeline.
4. **Winning and Losing:**

Answer correctly to win points and proceed to the next level.
Incorrect answers end the game.
## Code Structure
- Main.py: Entry point of the game.
- Menu.py: Handles the game menu and options.
- Game_Start.py: Main game logic, including question handling and lifelines.
- Data.py: Contains the questions and lifelines data.
- Definitions.py: Definitions and configurations for the game. 
