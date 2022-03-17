# Python Build Process
# 1. Write or draw about the problem
# 2. Extract  key concepts from 1 and research them
# 3. Create a class hierarchy and ibject map for the concepts
# 4. Code the classes and a test to run them
# 5. Repeat and refine

# 1:
#   "Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map."
# Scenes:
#       Death
#       Central Corridor
#       Laser Weapon Armory
#       The Bridge
#       Escape Pod

# 2:
#   pull out nouns and analyze class hierarchy:
#       Alien
#       Player
#       Ship
#       Maze
#       Room
#       Scene
#       Gothon
#       Escape Pod
#       Planet
#       Map
#       Engine
#       Death
#       Central Corridor
#       Laser Weapon Armory
#       The Bridge

# 3: Hierarchy
    # Map
    # Engine
    # Scene
    #   Death
    #   Central Corridor
    #   Laser Weapon Armory
    #   The Bridge
    #   Escape Pod

# actions needed:
# Map:
#   - next_scene
#   - opening_scene
# Engine:
#   - play
# Scene:
#   -enter
#   Death
#   Central Corridor
#   Laser Weapon Armory
#   The Bridge
#   Escape Pod

# 4: Code classes

# class Scene(object):
#     def enter(self):
#         pass
#
# class Engine(object):
#     def __init__(self, scene_map):
#         pass
#
#     def play(self):
#         pass
#
# class Death(Scene):
#     def enter(self):
#         pass
#
# class CentralCorridor(Scene):
#     def enter(self):
#         pass
#
# class LaserWeaponArmory(Scene):
#     def enter(self):
#         pass
#
# class TheBridge(Scene):
#     def enter(self):
#         pass
#
# class EscapePod(Scene):
#     def enter(self):
#         pass
#
# class Map(object):
#     def __init__(self, start_scene):
#         pass
#
#     def next_scene(self, scene_name):
#         pass
#
#     def opening_scene(self):
#         pass
#
# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()

# 5: Repeat and refine
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("Configure this scene")
        print("Subclass it and implement enter()")

        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    u_ded = [
        "You died",
        "You died hard",
        "Its the end of your world",
        "Typical dying person",
        "Your life flashed before your eyes, it was short"

    ]
    def enter(self):
        print(Death.u_ded[randint(0, len(self.u_ded)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and killed the crew!
        You must get to the armory and ge the neutron destruct bomb and install it on the bridge, and
        escape
        
        You're running down the corridor, A gothon jumps out, oh my goodness, it is Shia Lebouf, he is a Gothon!!
        So much makes more sense to you now you think as he pulls his weapon to blast you with."""))

        action = input("(shoot)(dodge)(joke)> ")

        if action == "shoot":
            print(dedent("""
            Quickly you draw and shoot super star Shia Lebouf...
            but you missed!
            In a craze he attacks and eats you like the cannibal gothon he is"""))

            return 'death'

        if action == "dodge":
            print(dedent("""
            You dodge, unfortunately you step on a banana mid-dodge, and slip
            Actual Cannibal Shia Labouf eats you"""))

            return 'death'

        elif action == "joke":
            print(dedent("""
            With all your might you tell the greatest joke in the world.
            By human standards it was really bad but Shia Labouf thought it was hilarious
            His laughter exceeds his body's capacity and explodes.
            You decide to write a tribute to the joke as you jump into the Weapon Armory door"""))
            return 'laser_weapon_armory'
        else:
            print("Try again, not a valid action")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):

        print(dedent("""You enter the Weapon Armory and run to the neutron bomb container, 
                     it has a keypad on it which locks after 10 failed attempts. The code is 3 digits"""))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        # print(code) # testing
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZ")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code or guess == '999':
            print(dedent("""
            The container opens and you grab the bomb and start heading to the bridge"""))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes the final time and the box is sealed forever. You wait for your ineviatable demise
            """))
            return 'death'



class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You enter the bridge and find yourself surrounded by Shia Laboufs!!! 
        All Gothons are Shia Labouf!!!!????
        """))

        action = input("(throw)(place)> ")

        if action == "throw":
            print(dedent("""
            You throw the bomb at the Gothons, as it lands they open fire on you to death.
            Did the bomb go off? You don't know, you're dead"""))
            return 'death'

        elif action == "place":
            print(dedent("""
            You slowly place the bomb on the deck, pointing your blaster as it as a threat to the gothons
            once placed you back up slowly while still threatening to shoot the bomb 
            once out the door sprint to the escape pods"""))
            return 'escape_pod'

        else:
            print("Invalid option, everything stays frozen in time")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You run as fast as possible to the escape pods
        you make it to the escape pods and find five available escape pods, which one do you take?"""))

        good_pod = randint(1,5)
        # print(good_pod) # testing
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
            You jump into pod #{guess} and hit the eject button
            It appears you picked a malfunctioning pod
            The hull is crushed in an instant and the pod implodes with you in it"""))
            return 'death'
        else:
            print(dedent(f"""
            You jump into pod #{guess} and hit the eject button
            It flies towards a safe planet
            You look back to take one last look as the ship explodes
            along with hopefully all that remains of Shia Labouf"""))
            return 'finished'


class Finished():
    def enter(self):
        print("Congrats! You won and saved the universe from Shia Labouf!!!")

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()