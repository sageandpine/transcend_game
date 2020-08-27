

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

        def remove_item(self):
            dump = input("What item would you like to remove? ")
            inventory.remove(dump)
            print(f"Item removed {inventory}")
            if len(inventory) != 3:
                choice = input("Would you like to remove another item? Y/N ")
                if choice == "Y" or "y":
                    remove_item()
                else:
                    pass

        def add_item(self):
            if len(inventory) == 3:
                print("Inventory Full!")
                print("Would you like to remove an item?")
                choice = input("Y/N ")
                if choice == "Y" or "y":
                    print(inventory)
                    remove_item()
                else:
                    pass

            else:
                item = input("What item will you add? ")
                inventory.append(item)
                print(inventory)
                if len(inventory) != 3:
                    choice = input("Would you like to add another item? Y/N ")
                    if choice == "Y" or "y":
                        add_item()
                    else:
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
        print(dedent("""
              This is the opening scene. You have been asleep and you wake
              to the sun rising....the sunlight through the window has a
              dreamlike quality. It makes you want to go back to
              sleep.
              """))

        choice = input("/nWhat do you do? /nStay Awake/Back to Bed")
        if choice == "Stay Awake" or "stay awake":
              next_scene(WakeOne)

        elif choice == "Back to Bed" or "back to bed":
              next_scene(DreamOne)

        else:
              print("""
                    I'm sorry, I am a simple input device. Please
                    choose from given options""")
              opening_scene()



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
    scenes = {
        'start_room': StartRoom(),
        'wake_one': WakeOne(),
        'wake_two': WakeTwo(),
        'wake_three': WakeThree(),
        'dream_one': DreamOne(),
        'dream_two': DreamTwo(),
        'dream_three': DreamThree(),
        'reincarnate': Reincarnate(),
        'resolve': Resolve(),
        'dissolve': Dissolve()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene    

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
              

a_map = Map('start_room')
a_game = Engine(a_map)
a_game.play()
