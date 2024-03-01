from random import randint
import csv

# Prompt user to either roll dice / premade dice set or create / view table
# Need function to create, save, and retrieve local data
# CSV file?

def main():

    # Main loop should be initial options, then after picking and
    # resolving an option you are asked to select another option
    # or quit

    # Choice to function dictionary
    choice_dict = {
        'dice': dice, # Complete!
        'dice set': dice_set, # Next
        'view tables': view_table
    }
    
    while True:

        choice = str(input(
            """Welcome to Dice Roller and Tables! \nType 
            'dice' to roll dice, 
            'dice set' for premade dice sets, 
            'create table' to create a roll table, or 
            'view tables' to view already made tables.
"""
        ))
    
        if choice in choice_dict:
            choice_dict[choice]()
            break

        else:
            print("Please provide a valid response.")
        

# Dice creator / roller; imported is for dice sets functionality
def dice(imported=None):
    
    dice_list = []

    def create_dice():

        while True: 
            
            while True:

                # Dice Format:
                # [faces on dice], [number of rolls]
                d_choice = str(input(
                    "Enter how many faces are on your die, "
                    "followed by a comma, "
                    "then the number of times you want the die to roll.\n"
                ))

                d_choice = d_choice.replace(" ", "")
                d = tuple(filter(None, d_choice.split(",")))

                # Check for valid dice results, else repeat function
                correct_count = 0
                for num in d:
                    if num.isnumeric() is False:
                        print("Please give a number value for your choices.")
                        continue
                    else:
                        correct_count += 1
                
                if correct_count == 2:
                    break
                    

            dice_list.append(d)

            # Check to add more dice or break loop and roll dice
            yn_choice = str(input(
                "Would you like to add more dice? [Y / N] "
            ))

            if yn_choice.upper() == "Y":
                create_dice()
                break

            elif yn_choice.upper() == "N":
                roll_dice(dice_list)
                break

            else:
                print("Please provide a valid response.")
    

    def roll_dice(d_list):

        dice_total = 0
        
        # The tuple in d_list is currently strings
        for face, num in d_list:

            print("Rolling " + num + " d" + face + "-sided dice.")
            
            for rolls in range(int(num)):
                
                dice_result = randint(1, int(face))

                if dice_result == int(face):
                    print(face + "!!")
                else:
                    print(dice_result)

                dice_total += dice_result
        
        print(f"The total rolled is {str(dice_total)}.")

    if imported:
        roll_dice(imported)
    else:
        create_dice()
        
        # Ask to either go back to menu or quit. With every menu
        # option leading to this it should be its own function:
        # "endplate"
        endplate("dice")



def dice_set(saved=None):
    
    # Start with being able to save a local CSV file, then
    # add cookie functionality when called from the website
    # Use `if __name__ is __main__` to check if the file
    # is being run locally or from Flask

    # File Structure:
    # [faces on dice],[number of rolls]; extra...$
    # Where $ is the delimiter

    # CSV and Web cookie Setup

    # Read Only function
    def ds_fetch():

        # Retrieve dice sets and separate into choices
        options = []
        with open("dice_sets.csv", 'r') as file:
            csvreader = csv.reader(file, delimiter="$")
            for option in csvreader:
                for content in option:
                    options.append(content)

        print(options)    
        for index, option in enumerate(options):
            print(str(index + 1) + ". " + option)

        # Query Option
        while True:
            
            select = int(input("Which dice set would you like to roll?\n"))

            # Check options list index
            if select <= (len(options) + 1):
                # Multiple dice roll(s) in a single query
                ds_roll_list = []
                try:
                    ds_roll = options[select - 1].split(";")
                    for roll in ds_roll:
                        ds_roll_list.append(tuple(filter(None, roll.split(","))))
                        dice(imported=ds_roll_list)
                    break
                # Single dice roll(s) in a single query
                except ValueError:
                    ds_roll_list.append(tuple(filter(None, options[select - 1].split(","))))
                    dice(imported=ds_roll_list)
            else:
                print("Please provide a valid response.")
            

    # Write To function
    def ds_make():

        with open("dice_sets.csv", 'a') as file:
            csvwriter = csv.writer(file, delimiter="$")
            new_ds = ""

            adding_dice = True
            while adding_dice:
                
                ds_input = str(input("Enter how many faces are on your die, "
                    "followed by a comma, "
                    "then the number of times you want the die to roll.\n"))

                new_ds = new_ds + ds_input

                while True:
                    ds_input_choice = str(input("Would you like to add another dice set? [Y / N] "))

                    if ds_input_choice.upper() == "Y":
                        new_ds = new_ds + ";"
                        break
                    
                    elif ds_input_choice.upper() == "N":
                        adding_dice = False
                        break

                    else:
                        print("Please provide a valid response.")
            
            csvwriter.writerow([new_ds.replace(' ', '')])


    
    # Query Handler
    print("Welcome to the Dice Set Maker!")
    
    # Embedded while loop break variable
    ds_stop = False
    while ds_stop == False:

    # Check if file exists yet
        try:
            ds_file = open('dice_sets.csv')
            ds_file.close
        except FileNotFoundError:
            while True:
                ds_create = input(str("You currently do not have a Dice Set file.\n"
                    "Would you like to create one? [Y / N] "))
                
                if ds_create.upper() == "Y":
                    open('dice_sets.csv', 'x')
                
                elif ds_create.upper() == "N":
                    print("A dice set file is required to use this function.")
                    ds_stop = True # Main while loop break 

                else:
                    print("Please provide a valid response.")
                    continue
                
                break
        
        if ds_stop is True:
            break

        # Main query menu
        ds_choice = str(input("Type 'fetch' to look at currently saved dice sets or\n"
            "'make' to save a new dice set.\n"))
        
        if ds_choice == 'fetch':
            ds_fetch()
            break

        elif ds_choice == 'make':
            ds_make()
            break

        else:
            print("Please provide a valid response.")

    endplate("dice set")

def view_table(saved):
    pass


def endplate(current):
    
    # Choice to function dictionary for retry option
    choice_dict = {
        'dice': dice, 
        'dice set': dice_set, 
        'view tables': view_table
    }

    while True:

        ep_choice = str(input(
            "Type 'menu' to return to the main menu, "
            "'retry' to redo the last command, "
            "or 'exit' to exit the program.\n"
        ))

        if ep_choice == "menu":
            main()
            break

        elif ep_choice == "retry":
            choice_dict[current]()
            break

        elif ep_choice == "exit":
            exit()
        
        else:
            print("Please provide a valid response.")


main()