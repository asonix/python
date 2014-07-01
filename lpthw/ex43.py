#!/usr/bin/env python3

from sys import exit
from random import randint

# Mechanics

class Scene(object):

    def enter(self):
        print("")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print("scene_map",scene_map)
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print("current_scene",current_scene)

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            print("next scene",next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("map returns new scene",current_scene)


# Scenes

class Death(Scene):

    quips = {
        "dead",
        "dead",
        "dead",
        "dead",
        "dead"
    }

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

        action = input("> ")

        if action == "shoot":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            return(death)
        
        elif action == "dodge":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            return(death)


        elif action == "tell a joke":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            return("laser_weapons_armory")

        else:
            print("")
            return("central_corridor")


class LaserWeaponArmory(Scene):
    
    def enter(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print(code)
        guesses = 0
        guess = "adf"

        while guess != code and guesses < 10:
            if guesses != 0:
                print("BZZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("")
            print("")
            print("")
            print("")
            print("")
            return("the_bridge")
        else:
            print("")
            print("")
            print("")
            print("")
            return("death")


class TheBridge(Scene):

    def enter(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

        action = input("> ")

        if action == "throw the bomb":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            return("death")
        
        elif action == "slowly place the bomb":
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            return("escape_pod")

        else:
            print("")
            return("the_bridge")


class EscapePod(Scene):

    def enter(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("")
            print("")
            print("")
            print("")
            return(death)
        else:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("you won")
            return("finished")


class Map(object):
    
    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapons_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": Death()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene
        print("start_scene in __init__", self.start_scene)

    def next_scene(self,scene_name):
        print("scene_name",scene_name)
        print("start_scene in next_scene")
        val = Map.scenes.get(scene_name)
        print("next_scene returns", val)
        return(val)

    def opening_scene(self):
        return(self.next_scene(self.start_scene))


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
