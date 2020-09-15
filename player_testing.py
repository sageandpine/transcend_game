from sys import exit

class Player(object):

    def __init__(self, name):

        flesh_pack = []
        soul_pack = []
        while len(flesh_pack) == 0:
            full_flesh_pack = False

        while len(soul_pack) == 0:
            full_soul_pack = False

        self.full_soul_pack = full_soul_pack
        self.full_flesh_pack = full_flesh_pack
        self.name = name
        self.flesh_pack = flesh_pack
        self.soul_pack = soul_pack
        
    def inventory_full(self):
        """
        gt: function where each pack has its own list and also a variable that holds
        the value of True if the pack is full by default. 
        """

        if full_fleshpack == True and full_soul_pack == True:
            print("Inventory is full")

        elif full_fleshpack == True and full_soulpack== False:
            print("fleshpack is full")
            #could go to soulpack directly or ask if you want to as prompted
            self.display_inventory()

        elif full_fleshpack == False and full_soulpack == True:
            print("soulpack is full")
            #could go to fleshpack directly or ask if you want to as prompted
            self.display_inventory()

        else:
            print("zzzzzz")
            self.display_inventory()
            #calls the function that user can interact with.



    def rmv_flesh(self):
        if self.flesh_pack == 0:
            print("you can't squeeze blood from a stone...")
            print("inventory empty")
            display_inventory()
        else:
            print("What item would you like to remove? ")
            print(self.flesh_pack)

            item = input("> ")

            print(f"You've removed {item} from inventory!")
            self.flesh_pack.remove(item)
            self.display_inventory()

    def rmv_soul(self):
        if self.soul == 0:
            print("your soul is empty...")
            display_inventory()
            
        else:
            print("What item would you like to remove? ")
            print(self.soul_pack)

            item = input("> ")

            print(f"You've removed {item} from inventory!")
            self.soul_pack.remove(item)
            self.display_inventory()
            
#while len*(inventory) != 3 return True etc. 

    def display_inventory(self):
        """
        a compact menu that forces the user to pick
        a pack to access before adding
        or removing items. 
        """
        
    print("INVENTORY MENU")
    print("#########################")
    print("f = fleshpack")
    print("s = soulpack")
    print("c = close inventory")
    print("#########################")
    choice = input("please select one: ")

    if "c" in choice:
        print("returning to game")

    elif "f" in choice and len(self.flesh_pack) != 3:
        print(f"Fleshpack-- {self.flesh_pack}")
        print(
        self.add_item()

    elif "f" in choice and len(self.flesh_pack) == 3:
        self.inventory_full()

    elif "s" in choice and len(self.soul_pack) != 3:
        print(f"Soulpack-- {self.soul_pack}")
        self.add_item()

    else:
        print("not sure what is going on!")
        
   # open_packs(choice)
    def add_soul(self):
        if len(self.soul_pack) == 3:
            self.inventory_full()
        
        else:
            print("What item would you like to add? ")
            item = input("> ")
       
            self.soul_pack.append(item)
            
            print(f"You've added {item} to inventory!")

            if len(self.soul_pack) == 3:
                self.inventory_full()
                
            else:
                self.display_inventory()
                
    def add_flesh(self):
        if len(self.flesh_pack) == 3:
            self.inventory_full()
        
        else:
            print("What item would you like to add? ")
            item = input("> ")
       
            self.flesh_pack.append(item)
            
            print(f"You've added {item} to flesh pack!")

            if len(self.flesh_pack) == 3:
                self.inventory_full()
                
            else:
                self.display_inventory()
                
        
        
ted = Player("Ted")
ted.display_inventory()

