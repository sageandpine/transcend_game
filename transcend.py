

# from os import inventory.py as




# inventory = []

class Player(object):
    # create two empty bags that each player must use in the two worlds
    # Make it so every new game this is default
    spirit_pack = Inventory()
    flesh_pack = Inventory()

    def __init__(self):
        pass

    def check_invenory():
        pass
    # could entire inventory system go here instead? Why it's own class?



class Inventory(object):

    def __init__(self):
        inventory = []

    def add_item(self):
    if len(inventory) == 3:
        print("Inventory Full!")
        print("Would you like to remove an item?")
        choice = input("Y/N ")
        if choice is "Y" or "y":
            print(inventory)
            dump = input("What item would you like to remove? ")
            inventory.remove(dump)
            print(f"It works! {inventory}")

        else:
            pass

    else:
        item = input("What item will you add? ")
        inventory.append(item)
        print(inventory)
        add_item()

    def remove_item(self):
        pass


class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Dissolve(Scene):

    def enter(self):
        pass

class Resolve(Scene):

    def enter(self):
        pass

class Start_Room(Scene):

    def enter(self):
        pass



class WakeOne(Scene):

    def enter(self):
        pass

class WakeTwo(Scene):

    def enter(self):
        pass

class WakeThree(Scene):

    def enter(self):
        pass

class DreamOne(Scene):

    def enter(self):
        pass

class DreamTwo(Scene):

    def enter(self):
        pass

class DreamThree(Scene):

    def enter(self):
        pass

class Reincarnate(Scene):

    def enter(self):
        pass


class Map(object):


    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('start_room')
a_game = Engine(a_map)
a_game.play()
