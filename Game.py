from Scene import Scenes, Begin, Death, DonutAlien, GummyBearAlien, WatermelonAlien, BossAlien, Win

# Text bases adventure game
# 1. Write the problem out
# 2. Extract key concepts from 1 and research them
# 3. Create a class heirarchy and object map for concept
# 4. Code the classes and a test to run them
# 5. Repeat and refine.

# 1. Write the problem out

# "You fell into a trap floor on your hike in the woods and this was not an ordinary hole.
#  The hole led you to the alien world called Zarn! However, the environment of the forest
#  looks exactly the same as on Earth. You have to beat these aliens to get out of the forest
#  and find a telephone booth to be able to teleport back to Earth."
# "There will be many alien you will encounter and at times even be teleported to another place to
#  fight. Many scenes are going to be needed. Then tell the engine where to go next"

# 2. Extract key concepts from 1 and research them
# Engine
# -start
# Map
# - current scene
# - next scene
# -move
# Player
# Scene
# -begin
# -Death
# -Donut Alien
# -Watermelon Alien
# -GummyWorm Alien
# -Boss Alien
# -Win


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # calls the opening_scene function but in that opening_scene function
        # next_scene is called which converts the '' to the actual class
        # so now we have the actual class name not a string
        current_scene = self.scene_map.opening_scene()
        # this is the last scene of the game. So the current_scene will keep changing
        # until it gets to the finial scene which is whaterver last_scene is set to
        last_scene = self.scene_map.next_scene('win')
        # while loop so the scenes keep on changing until current and last scene are true
        # current_scene and last_scene are both class's technically not the strings
        while current_scene != last_scene:
            # setting next_scene_name as whatever class current_scene is and going into
            # the enter funcion of that class so running through it
            next_scene_name = current_scene.enter()
            # after running through that classes enter function you run into
            # a string rather than another class so you have to 
            # convert the string again with next_scene and 
            # run through the top of the while loop all over again
            current_scene = self.scene_map.next_scene(next_scene_name)

        # after getting out of the while loop the current_scene will be the 
        # last last scene the computer has to go through and if you
        # don't call it then the program will never run through it.
        current_scene.enter()

# What does a map have?
# Scene, code to direct where to go
# function init to start scene
# function to get to next scene
# you don't have to have 'object' as a perameter
# it is technically an empty perameter
class Map(object):
    Scenes = {
        'donut_alien': DonutAlien(),
        'watermelon_alien': WatermelonAlien(),
        'gummy_bear_alien': GummyBearAlien(),
        'boss_alien': BossAlien(),
        'win': Win(),
        'begin': Begin(),
        'death': Death()
    }

    def __init__(self, start_scene):
        # makes whatever is passed through the Map class special with self.
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        # so this line converts the '' into the actual class name
        val = Map.Scenes.get(scene_name)
        # sets the value in val
        return val
    
    def opening_scene(self):
        # uses what is passed in the initialize function and 
        # makes the passed value unique for the next_scene
        return self.next_scene(self.start_scene)

a_map = Map('begin')
a_game = Engine(a_map)
a_game.play()

    






# get the game working first
# class Player():
    # pass

