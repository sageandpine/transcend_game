class Player(object):

    def __init__(self, name):

        inventory = []

        map_counter = 0
        player_counter = 0
        inventory_counter = 0

        self.name = name
        self.map_counter = map_counter
        self.player_counter = player_counter
        self.inventory_counter = inventory_counter
        self.inventory = inventory
        
    def open_mind(self):
        print(self.name + " has opened their mind and is in the GAME!")

    def status(self):
        print("Current Status is--- ")
        print("Map = " + str(self.map_counter))
        print("Inventory = " + str(self.inventory_counter))
        print("Self Worth = " + str(self.player_counter))

    def show_inventory(self):
        print(f"Inventory - {self.inventory}")

    def add_inv_num(self, num):
        self.inventory_counter += num
        print("cha-ching!")
        
    def rm_inv_num(self, num):
        self.inventory_counter -= num
        print("depleted!")

    #def add_map_num(self, num):
     #   self.map_counter += num
      #  print("cha-ching!")
        
    #def rm_map_num(self, num):
     #   self.map_counter -= num
      #  print("depleted!")


    def rmv_item(self):
        print("What item would you like to remove? ")
        print(self.inventory)

        item = input("> ")

        print(f"You've removed {item} from inventory!")
        self.inventory.remove(item)
        self.rm_inv_num(1)
        
        print("Would you like to remove another item? Y/N")

        choice = input(">  ")
        
        if "Y" in choice and len(self.inventory) != 0 or "y" in choice and len(self.inventory) != 0:
            self.rmv_item()

    
        elif "Y" in choice and len(self.inventory) == 0 or "y" in choice and len(self.inventory) == 0:
            print("Inventory empty!")
            self.add_item()        

        else:
            print("Let's get back to the game!")
            #exit()
        
    def add_item(self):
        print("Would you like to add (A), remove (R) an item or return to the game (any other key)? ")

        choice = input(">  ")

        if "A" in choice and len(self.inventory) != 3 or "a" in choice and len(self.inventory) != 3:
            print("What item would you like to add? ")
            item = input("> ")

            self.inventory.append(item)
            self.add_inv_num(1)
            
            print(f"You've added {item} to inventory!")
            self.add_item()

            print("Return to game (G) or Edit (E) inventory?")
            choice = input("> ")
            if "G" in choice or "g" in choice:
                print("pronto toronto!")

            elif "E" in choice or "e" in choice:
                self.add_item()

            else:
                print("does not compute, but i make my own decisions sometimes....")
                self.add_item()

        elif "A" in choice and len(self.inventory) == 3 or "a" in choice and len(self.inventory) == 3:
            print("You can't do that! Inventory full!")
            self.add_item()

        elif "R" in choice or "r" in choice:
            self.rmv_item()
            

        else:
            print("Let's get back to the game!")
            #exit()    
        
ted = Player("Ted")
ted.open_mind()
ted.status()
ted.show_inventory()
ted.add_item()
ted.status()
