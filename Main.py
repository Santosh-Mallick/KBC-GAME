import Definitions
import Menu

Definitions.clear_console()

global fn_name, ln_name

print("\nEnter Your Full Name (First Name & Last Name) : ", end ="")
f_name = input().strip() #Input FullName
if len(f_name.split()) == 2: #Checks Whether User Has Entered Full Name or Not.
    fn_name, ln_name = f_name.split()
else:
    print("Invalid input. Please enter your full name (First Name Last Name): ")
        
birth_year = int(input("Enter your birth year (YYYY): ")) #Input Birth Year
age = 2024-birth_year
if age < 13:
    print("Sorry, you must be at least 13 years old to proceed.")
    exit()
elif age >= 90:
    print("Too old or Invalid Age")
else:
    print("Please Type your Birth Year Correctly.")
            
print(f"\nLoading....")

Definitions.clear_console()

print(f"Welcome {f_name.title()}😉,\n\n")

print("We're thrilled to have you join us on this incredible journey.")
print("KBC offers something special for everyone.")
print(f"Best of luck {fn_name.title()}, and let's play Kaun Banega Crorepatiii!\n")

print("Press Enter Key To Continue...")


while True:
    #Checking If User Pressed ENTER Key Or Not
    user_input = input()
    if user_input == "":
        break
    else:
        print("🔴 Wrong key pressed. Please press Enter key to continue...")

#To Clear Console
Definitions.clear_console()
#Importing Menu Section
Menu.Home()