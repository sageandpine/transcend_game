ffrom sys import exit

# To do--- all functions are linked, now work on map and room classes
# also better documentation needed for everything
        
class Player(object):



    def __init__(self, name):

        flesh_pack = []
        soul_pack = []
        self.name = name
        
        full_flesh_pack = False
        full_soul_pack = False

        self.flesh_pack = flesh_pack
        self.soul_pack = soul_pack
        self.full_soul_pack = full_soul_pack
        self.full_flesh_pack = full_flesh_pack


    def inventory_full(self):
        """
        gt: function where each pack has its own list and also a variable that holds
        the value of True if the pack is full by default. 
        """
        while len(self.soul_pack) == 3:
            self.full_soul_pack = True
            print("soul pack full!")
            response = input("Remove item from soul pack? Y/N ")
            if "y" in response:
                self.rmv_soul()
            else:
                self.display_inventory()
                  
        while len(self.flesh_pack) == 3:
            self.full_flesh_pack = True
            print("flesh pack full!")
            response = input("Remove item from flesh pack? Y/N ")
            if "y" in response:
                self.rmv_flesh()
            else:
                self.display_inventory()

    def rmv_flesh(self):
        if len(self.flesh_pack) == 0:
            print("you can't squeeze blood from a stone...")
            print("inventory empty")
            self.display_inventory()
        else:
            print("What item would you like to remove? ")
            print(self.flesh_pack)

            item = input("> ")

            print(f"You've removed {item} from inventory!")
            self.flesh_pack.remove(item)
            response = input("Remove another item from flesh pack? Y/N")
            if "y" in response:
                self.rmv_flesh()

            else:
                self.display_inventory()

    def rmv_soul(self):
        if len(self.soul_pack) == 0:
            print("your soul is empty...")
            self.display_inventory()
            
        else:
            print("What item would you like to remove? ")
            print(self.soul_pack)

            item = input("> ")

            print(f"You've removed {item} from inventory!")
            self.soul_pack.remove(item)
            response = input("Remove another item from soul pack? Y/N")
            if "y" in response:
                self.rmv_soul()

            else:
                self.display_inventory()
            

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
            self.add_flesh()

        elif "f" in choice and len(self.flesh_pack) == 3:
            self.inventory_full()

        elif "s" in choice and len(self.soul_pack) != 3:
            print(f"Soulpack-- {self.soul_pack}")
            self.add_soul()

        else:
            print("not sure what is going on!")
        

                
        
        
ted = Player("Ted")
ted.display_inventory()


