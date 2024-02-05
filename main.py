from random import randint

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
        'create': create,
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
            print("Please choose a valid option.")
        

def dice():
    
    dice_list = []


    def create_dice():

        while True: 
            
            d_choice = str(input(
                """Enter how many faces are on your die, 
                followed by a comma,
                then the number of times you want the die to roll. 
"""
            ))

            d = tuple(filter(None, d_choice.split(",")))

            # Check for valid dice results, else repeat function
            for num in d:
                if num.isnumeric() is False:
                    print("Please give a number value for your choices.")
                    create_dice()

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
                print("Please provide Y or N as an answer.")
    

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

    create_dice()

    # Ask to either go back to menu or quit. With every menu
    # option leading to this it should be its own function:
    # "endplate"
    endplate("dice")

def dice_set(saved):
    pass

def create():
    pass

def view_table(saved):
    pass

def file_create():
    pass

def endplate(current):
    
    # Choice to function dictionary for retry option
    choice_dict = {
        'dice': dice, 
        'dice set': dice_set, 
        'create': create,
        'view tables': view_table
    }

    while True:

        ep_choice = str(input("""
        Type 'menu' to return to the main menu,
        'retry' to redo the last command,
        or 'exit' to exit the program.
"""
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
            print("Please choose a valid option.")


main()