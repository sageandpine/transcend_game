from sys import exit

def inventory_full(full_fleshpack, full_soulpack):
    """
gt: function where each pack has its own list and also a variable that holds
the value of True if the pack is full by default. 
    """
    if full_fleshpack and full_soulpack:
        print("Inventory is full")
    elif full_fleshpack and not full_soulpack:
        print("fleshpack is full, would you like to access soulpack?")
        #could go to soulpack directly or ask if you want to as prompted
        soulpack()
    elif not full_fleshpack and full_soulpack:
        print("soulpack is full, would you like to access fleshpack?")
        #could go to fleshpack directly or ask if you want to as prompted
        fleshpack()
    elif not full_fleshpack and not full_soulpack:
        display_inventory()
        #calls the function that user can interact with.

def display_inventory():
    """
a compact menu that forces the user to pick a pack to access before adding
or removing items. 
    """
    print("INVENTORY MENU")
    print("#########################")
    print("f = fleshpack")
    print("s = soulpack")
    print("c = close inventory")
    print("#########################")
    inventory_input = input("please select one: ")
    open_packs(inventory_input)

def open_packs(inventory_input):
    if inventory_input=="c":
        print("Let's get back to the game!")
    elif inventory_input=="f":
        print("Accessing fleshpack")
        fleshpack()
    elif inventory_input=="s":
        print("Accessing soulpack")
        soulpack()
    else:
        print("Input not valid, try again")
        display_inventory()



def fleshpack():
    print("FLESHPACK ACTIVATE")
    """
gt: for both fleshpack and soulpack, I'm thinking list and strings to be able
to slice and pull parts as needed. Using split. to know the position of the
items. 
    """
    exit

def soulpack():
    print("SOULPACK ACTIVATE")
    """
gt: see above
    """
    exit





#    """
#gt: the idea here is that a player function could theoretically return a call
#to inventory() with the correct set of conditions. You can test them by
#changing the value of the Booleans. 
#    """
inventory_full(False, False)







