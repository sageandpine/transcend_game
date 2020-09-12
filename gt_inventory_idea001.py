

def inventory(fleshpack, full_fleshpack, soulpack, full_soulpack):
    """
gt: inventory is composed of a function where each pack has its own list and
also a variable that holds the value of True if the pack is full by default.
This allows a better flow for the program. 
    """
    if full_fleshpack and full_soulpack:
        print("Inventory is full")
    elif full_fleshpack and not full_soulpack:
        print("fleshpack is full, would you like to access soulpack?")
        #insert module to get input
    elif not full_fleshpack and full_soulpack:
        print("soupack is full, would you like to access fleshpack?")
        #insert module to get input 
    elif not full_fleshpack and not full_soulpack:
        open_inventory()
        #calls the function that user can interact with. 

def open_inventory():
    """
gt: open inventory I haven't figured out yet, but it would take the input
from user and maybe print the inventory. 
    """
    print("INVENTORY MENU")
    print("#########################")
    print("f = fleshpack")
    print("s = soulpack")
    print("c = close inventory")
    print("#########################")

##    if inventory_input="c":
##        print("Exiting inventory")
##    elif inventory_input="f":
##        print("Accessing fleshpack")
##        fleshpack()
##    elif inventory_input="s":
##        print("Accessing soulpack")
##        soulpack()
##    else:
##        print("Input not valid, try again")

    

def fleshpack():
    print("FLESHPACK ACTIVATE")
    """
gt: for both fleshpack and soulpack, I'm thinking list and strings to be able
to slice and pull parts as needed. Using split. could help locate variables in
a string that call the correct print out from a list.
    """
    

def soulpack():
    print("SOULPACK ACTIVATE")
    """
gt: see above
    """
fitem1="fitem1"
fitem2="fitem2"
fitem3="fitem3"
sitem1="sitem1"
sitem2="sitem2"
sitem3="sitem3"
fleshpack=[fitem1, fitem2, fitem3]
soulpack=[sitem1, sitem2, sitem3]

#    """
#gt: the idea here is that a player function could theoretically return a call
#to inventory() with the correct set of conditions. You can test them by
#changing the value of the Booleans. 
#    """
inventory(fleshpack, False, soulpack, False)







