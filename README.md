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


## Example Gameplay
   ```bash
Enter Your Full Name (First Name & Last Name) : Harsh Yadav
Enter your birth year (YYYY): 2005

Welcome Harsh Yadav😉,


We're thrilled to have you join us on this incredible journey.
KBC offers something special for everyone.
Best of luck Thejas, and let's play Kaun Banega Crorepatiii!

Press Enter Key To Continue...

🔥 Welcome To Kaun Banega Crorepatii!! 🔥

⭐ 1. Start
⭐ 2. Statistics
⭐ 3. Settings
⭐ 4. Exit game


➤ Choose an Option From 1-4: 1

Starting the game...
Press Enter to continue...

🔥 Welcome To Kaun Banega Crorepatii!! 🔥

 ➤  What is the capital of France?

👉 1. Berlin
👉 2. Paris
👉 3. London
👉 4. Rome

 ➤ Lifelines

👉 6 : 50:50
👉 7 : Flip The Question
👉 8 : Double Dip
👉 9 : Ask The Expert

Enter your choice (1-4) or (6-9) for lifelines: 2

✅️ Correct answer! You Won 10000 points.

 ➤  Which of the following is a type of bird?

👉 1. Sparrow
👉 2. Lion
👉 3. Elephant
👉 4. Tiger

 ➤ Lifelines

👉 6 : 50:50
👉 7 : Flip The Question
👉 8 : Double Dip
👉 9 : Ask The Expert

Enter your choice (1-4) or (6-9) for lifelines: 8
Enter your first choice (1-4): 2
Enter your second choice (1-4): 1
✅️ Correct answer! You Won 20000 points.

 ➤  What is the chemical symbol for water?

👉 1. H2O
👉 2. CO2
👉 3. O2
👉 4. N2

 ➤ Lifelines

👉 6 : 50:50
👉 7 : Flip The Question
👉 9 : Ask The Expert

Enter your choice (1-4) or (6-9) for lifelines: 6
 ➤  What is the chemical symbol for water?

👉 1. H2O
👉 2. O2

 ➤ Lifelines

👉 7 : Flip The Question
👉 9 : Ask The Expert

Enter your choice (1-4) or (6-9) for lifelines: 1

✅️ Correct answer! You Won 30000 points.

 ➤  Who is the main character in the book 'Alice in Wonderland'?

👉 1. Alice
👉 2. Bob
👉 3. Charlie
👉 4. David

 ➤ Lifelines

👉 7 : Flip The Question
👉 9 : Ask The Expert

Enter your choice (1-4) or (6-9) for lifelines: 9

🚨 The expert says the correct answer is: Alice 

 ➤  Who is the main character in the book 'Alice in Wonderland'?

👉 1. Alice
👉 2. Bob
👉 3. Charlie
👉 4. David

 ➤ Lifelines

👉 7 : Flip The Question

Enter your choice (1-4) or (6-9) for lifelines: 1

✅️ Correct answer! You Won 50000 points.

 ➤  Who is the author of the book 'Harry Potter'?

👉 1. J.K. Rowling
👉 2. J.R.R. Tolkien
👉 3. C.S. Lewis
👉 4. Dr. Seuss

 ➤ Lifelines

👉 7 : Flip The Question

Enter your choice (1-4) or (6-9) for lifelines: 7
 ➤  How will the internet be used after we conquer Big Data?

👉 1. To transform the current technological context and how we communicate on the web
👉 2. To increase surveillance and control
👉 3. To create more jobs
👉 4. To reduce inequality

 ➤ Lifelines


Enter your choice (1-4) or (6-9) for lifelines: 3
🔴 Sorry, that's incorrect. The Correct answer was :  To transform the current technological context and how we communicate on the web 

You won a total of 110000 points!
