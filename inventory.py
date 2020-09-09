

from sys import exit

inventory = []

# remove item function
def rmv_item():

    print("What item would you like to remove? ")
    print(inventory)

    item = input("> ")

    print(f"You've removed {item} from inventory!")
    inventory.remove(item)
    print("Would you like to remove another item? Y/N")

    choice = input(">  ")
        
    if "Y" in choice or "y" in choice and len(inventory) != 0:
        rmv_item()

    
    elif "Y" in choice or "y" in choice and len(inventory) == 0:
        print("Inventory empty!")
        add_item()        

    else:
        print("Let's get back to the game!")
        exit()

# add item function

def add_item():
    print("Would you like to add an item? Y/N")

    choice = input(">  ")
    if "Y" in choice or "y" in choice and len(inventory) == 3:
        print("You can't do that! Inventory full!")
        print("Would you like to remove an item from inventory? Y/N")

        choice = input("> ")
        if "Y" in choice or "y" in choice:
            rmv_item()

        else:
            print("Let's get back to the game!")
            exit()
            
    elif "Y" in choice or "y" in choice and len(inventory) != 3:
        print("What item would you like to add? ")
    
        item = input("> ")

        inventory.append(item)
        print(f"You've added {item} to inventory!")
        add_item()
                    
    else:
        print("Let's get back to the game!")
        exit()

add_item()
