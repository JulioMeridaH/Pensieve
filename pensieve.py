"""This program is to help the user to manage thoughts.
It's inspired in the Pensieve of Dumbledore (Harry Potter reference) where thoughts can be dumped in a pool for future review.
Coded by @JulioMeridaH || Updated: November, 23th of 2024"""
import json

def show_thoughts():
    """ Shows a numbered list of thoughts """

    #Opens the document
    thoughts = open_json_document('thoughts')
    #Measure the size
    thoughts_number = len(thoughts)
    #print the list of active thoughts
    for i in range(thoughts_number):
        print(f"{i+1} - {thoughts[i]}")

def main():
    """ Presents a welcome message and the main menu to select options """
    
    #Opening message
    print("\nHi! These were your last thoughts: \n")
    show_thoughts()
    print("\nWhat do you want to do now?: ")

    #Storing the options to show on menu
    options = ["Add a thought", "Clean a thought", "Exit"]

    #Making the user select a menu option
    while True:
        #Show the menu and call the corresponding functions
        select = show_menu(options)
        match select:
            case 1:
                add_thought()
                print("\nAdded. This is your list of thoughts updated:\n")
                show_thoughts()
            case 2:
                clean_thought()
                print("\nCleaned. This is your list of thoughts updated:\n")
                show_thoughts()
            case 3:
                print("\nGood bye!\n")
                break
            case _:
                print("\nOption no valid")

def show_menu(options):
    """ Print a menu with the options numerated starting from 1 and returns the corresponding number to the selected option """
    print("\nSelect an option: ")

    #Show the options
    for i in range(len(options)):
        print(f"{i+1} - {options[i]}")

    #Managing error if the user input a not valid option
    try:
        select = int(input("\nYour option: "))
        return select #If valid return the selected value
    except:
        return #If not valid, it'll return empty and caller line will call again

def add_thought():
    """Adds a new thought to the existing list or create a new one and add its first element."""
    
    #Opens the document
    thoughts = open_json_document('thoughts')
    #Ask the user for new thought
    current_thought = input("\nWhat is that thought?: ")
    #Adds it to the list
    thoughts.append(current_thought)
    #Saves the changes
    close_json_document('thoughts',thoughts)

def clean_thought():
    """Cleans one thought by selecting a number from the list of active thoughts."""

    #Opens the document
    thoughts = open_json_document('thoughts')
    #Show active thoughts
    print("\nThese are the active thoughts:\n")
    show_thoughts()
    #Makes user select an active thoight to clean
    while True:
        try: #If user makes a valid selection
            select = int(input("\nWhich one do you want to clean?: "))
            del thoughts[select - 1]
            #Saves the changes and break the infinite cycle
            close_json_document('thoughts',thoughts)
            break
        except: #If user makes an invalid selection
            print("\Option no valid.")

def open_json_document(name):
    """Opens a JSON document with *name* as name before the .json extension. If it doesn't exist return an empty list."""

    try:
        with open(f'{name}.json', 'r') as file:
            return json.load(file)
    except:
        return []

def close_json_document(name,variable):
    """Dumps the *variable* in a JSON file named *name*.json"""
    with open(f'{name}.json', 'w') as file:
        json.dump(variable, file)

if __name__ == '__main__':
    main()