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
        print(self.name + " has opened their mind!")

    def status(self):
        print("Current Status is--- ")
        print("Map = " + str(self.map_counter))
        print("Inventory = " + str(self.inventory_counter))
        print("Self Worth = " + str(self.player_counter))

    def show_inventory(self):
        print(f"Inventory - {self.inventory}")

    def rmv_item(self):
        print("What item would you like to remove? ")
        print(self.inventory)

        item = input("> ")

        print(f"You've removed {item} from inventory!")
        self.inventory.remove(item)
        print("Would you like to remove another item? Y/N")

        choice = input(">  ")
        
        if "Y" in choice and len(self.inventory) != 0 or "y" in choice and len(self.inventory) != 0:
            self.rmv_item()

    
        elif "Y" in choice and len(self.inventory) == 0 or "y" in choice and len(self.inventory) == 0:
            print("Inventory empty!")
            self.add_item()        

        else:
            print("Let's get back to the game!")
            exit()
        
    def add_item(self):
        print("Would you like to add an item? Y/N")

        choice = input(">  ")

        if "Y" in choice and len(self.inventory) != 3 or "y" in choice and len(self.inventory) != 3:
            print("What item would you like to add? ")
    
            item = input("> ")

            self.inventory.append(item)
            print(f"You've added {item} to inventory!")
            self.add_item()
            
        elif "Y" in choice and len(self.inventory) == 3 or "y" in choice and len(self.inventory) == 3:
            print("You can't do that! Inventory full!")
            print("Would you like to remove an item from inventory? Y/N")

            choice = input("> ")
            if "Y" in choice or "y" in choice:
                self.rmv_item()

            else:
                print("Let's get back to the game!")
                exit()
            

                    
        else:
            print("Let's get back to the game!")
            exit()    
        
ted = Player("Ted")
ted.open_mind()
ted.status()
ted.show_inventory()
ted.add_item()
