from sys import exit
from time import sleep
from textwrap import dedent

# Scenes for Game.py

# -begin
# -Death
# -Donut Alien
# -Watermelon Alien
# -GummyWorm Alien
# -Boss Alien
# -Win 

# this value is empty until the user inputs their name below in the Being class
name = ''

class Scenes():
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Begin(Scenes):
    # prob begin_speech =

    # begin_speech = {
    #     # why doesn't the dedent work here?
    #     print(dedent("""Hello Hiker! It is a beautiful day out today with it being a cool 55 
    #     and some clouds over your head! You have now been walking for over a hour
    #     you are sort of tired so you get clumsy and end up walking not on the trail!""")),
    #     sleep(3),
    #     for i in range(8):
    #         print(".", end='', flush=True)
    #         sleep(1),
    #     print(dedent("""Oof you fell into a trap hole on your hike and this is not an ordinary hole.
    #     The hole led you to the alien world called Zarn! 
    #     However, the environment of the forest looks exactly the same as on Earth. 
    #     You have to beat these aliens to get out of the forest
    #     and find a telephone booth to be able to teleport back to Earth."""))
    # }

    begin_speech = """
    Hello Hiker! It is a beautiful day out today with it being a cool 55 
    and some clouds over your head! You have now been walking for over a hour
    you are sort of tired so you get clumsy and end up walking not on the trail!
    UH OH!??!!
    Oof you fell into a trap hole on your hike and this is not an ordinary hole.
    The hole led you to the alien world called Zarn! 
    However, the environment of the forest looks exactly the same as on Earth. 
    You have to beat these aliens to get out of the forest
    and find a telephone booth to be able to teleport back to Earth.
    """

    def enter(self):
        print(Begin.begin_speech)
        sleep(8)
        print("Hello Hiker! What is your name?")
        # why do I make this global?
        global name
        name = input("> ")
        print(f"{name}, Would you like to walk left or right?")
        walk = input("> ")

        if walk == 'left':
            return 'donut_alien'
        elif walk == 'right':
            return 'gummy_bear_alien'
        else:
            # later change it so you just have to try to put in the 
            # input again
            exit(1)


class Death(Scenes):
    death_speech = "You are very weak you died already!\nWell maybe better luck next time!"

    def enter(self):
        print(Death.death_speech)
        # slows down when printed on screen
        sleep(2.5)
        print(f"BYE {name}:>")
        # exits the code but maybe change it to the beginning on the game later
        exit(1)

class DonutAlien(Scenes):

    def enter(self):
        print(dedent("""
        As you walk a little bit left you see this weird donut
        looking thing. You walk closer to it and the donut turns 
        towared you!!! IT IS A DONUT ALIEN and it seems HUNGRYYYY!"""))
        sleep(3)
        # repeats 6 times through for loop
        for i in range(6):
            # flush=True makes the '.' a sequence of single characters
            # so it prints out the '.' one at a time
            print(".", end='', flush=True)
            # puts a single second between printing out '.'
            sleep(1)
        print(f"\nWhat are you going to do {name}?! dance or fight???")
        # ask user for input
        action = input("> ")
        if action == 'dance':
            print(dedent("""
            The donut alien is impressed with you! The donute alien
            can actually speak english?!?!?! Donut alien says
            'Hello traveler! I am impressed and am willing to join
            you on your journy! May I accompany you?'
            yes or no?"""))
            answer = input("> ")
            if answer == 'yes':
                print("Now you have donut alien on your side!")
                sleep(3)
                return 'watermelon_alien'
            elif answer == 'no':
                print(dedent("""
                Donut Alien is mad!!!!! 
                You die from one of his sprinkles"""))
                return 'death'
            else:
                print(f"WHY YOU NOT TRYING TO ANSWER {name}???")
                return 'donut_alien'
        elif action == 'fight':
            print(dedent("""
            Wrong choice!!! Donut alien calls his friends over
            and they all jump you and you die!!!"""))
            return 'death'
        else:
            print("You can't run away hahaha")
            return 'donut_alien'
            
class GummyBearAlien(Scenes):

    def enter(self):
        print(dedent("""
        You have partially left the forest for now!
        It looks like you are in another would now with
        chocolate waterfalls and gummy bears for trees!
        As you walk you dump into this big squishy gummy
        bear feeling thing"""))
        sleep(3)
        for i in range(6):
            print(".", end='', flush=True)
            sleep(1)
        print(dedent(f"""\nUh oh this 'thing' turns toward you and you see its
skittle eyes! IT IS A BIG GUMMY BEAR ALIEN!!!
What are you going to do {name}? 
run or fight?"""))

        action = input("> ")

        if action == 'run':
            print(dedent("""
            You trip on a branch shaped like a gummy worm
            and hit your head hard on the chocolate pie floor!"""))
            sleep(3)
            return 'death'
        elif action == 'fight':
            print(dedent("""
            The gummy bear alien jumps on you!!! You are now
            in the stomatch of the huge gummy bear
            but lucky for you in this universe calories don't count
            and you like gummy bears! So you end up eating your way out
            while the gummy bear alien was taking a nap! Congrats
            you conquered the gummy bear alien and get to run
            to safety!!!"""))
            sleep(8)
            return 'watermelon_alien'
        else:
            print("You can't run away hahaha")
            return 'gummy_bear_alien'
class WatermelonAlien(Scenes):
    # it is prob text =
    # text = {

    #     print(dedent("""You are one step closer to returning to Earth!
    #     You are able to see the telephone booth a mile in front 
    #     of you! Your legs are going and are running like no 
    #     one elses business! But WAIT!"""))
    #     sleep(3)
    #     for i in range(8):
    #         print(".", end='', flush=True)
    #         sleep(1)
    #     print(dedent("""Infront of you an alien that has a watermelon for 
    #     its head jumps right infront of you! 
    #     You try to run around the alien but you can't get past
    #     him! What are you going to do?!?"""))
    # }

    text = """
    You are one step closer to returning to Earth!
    You are able to see the telephone booth a mile in front 
    of you! Your legs are going and are running like no 
    one elses business! But WAIT!
    UH OH?!?!
    Infront of you an alien that has a watermelon for 
    its head jumps right infront of you! 
    You try to run around the alien but you can't get past
    him! What are you going to do?!?
    """

    def enter(self):
        print(f"Did you beat the gummy bear alien or donut alien earlier?")
        print("gummy or donut?")
        beat = input("> ")

        if beat == 'gummy':
            print(WatermelonAlien.text)
            sleep(2)
            print("fight or peace?")
            choice = input("> ")
            if choice == 'fight':
                print(dedent("""
                Right when you were about to swing
                for this alien the watermelon alien
                ran away because he saw in the distance
                what happened to his friend the gummy bear alien! 
                """))
                return 'boss_alien'
            elif choice == 'peace':
                print(dedent("""
                The watermelon alien sees that you
                are not a threat and takes you out
                like it was nothing! YOU DIEEEEEE
                """))
                sleep(3)
                return 'death'
            else:
                print("You can't run away hahaha")
                return 'watermelon_alien'
        if beat == 'donut':
            print(WatermelonAlien.text)
            sleep(2)
            print(dedent("""
            Send in your friend the donut alien or
            fight the watermelon alien yourself?"""))
            print("donut_alien or fight_yourself")
            choice = input("> ")
            if choice == 'donut_alien':
                print(dedent("""
                The donut alien and the watermelon alien are actually 
                enemies and dislike each other very much!!
                The donut and watermelon alien both put their
                heart and soul into this fight!"""))
                sleep(3)
                for i in range(8):
                    print(".", end='', flush=True)
                    sleep(1)
                print(dedent("""
                \nYour friend the donut alien comes on top though!
YAY you are one step closer to going home!!!
BUT your donut alien friend found the rest of
the journy to be too dangerous and went back to
his part of the forest."""))
                sleep(10)
                return 'boss_alien'
            elif choice == 'fight_yourself':
                print(dedent("""You tell your donut alien friend that you have
                this on in the bag and take a crack at the 
                watermelon alien! You swing but the watermelon
                alien grabs you before you contact him and swing
                you around above his head like a lasso!
                You get thrown to your friend the donut alien
                and you both clash into each other.
                The donut alien gets scared and runs away leaving you
                to DIEEEEEEEE!"""))          
                return 'death'
            else:
                print("HA you are going to have to fight the alien\
 from the start again lol")
                sleep(4)
                return 'watermelon_alien'

class BossAlien(Scenes):

    def enter(self):
        print(dedent("""
        After beating the watermelon alien you run for that telephone booth
        with all your energy. You are running so fast that your eyes can't keep
        up! You reach the telephone booth with a sigh of relief and try to open
        the door. You keep on trying to open it but it just won't open?!
        You look up and see a giant hand that looks like 5 biceps for fingers
        holding the door shut. You then notice the shadow ontop of you and
        turn around."""))
        sleep(10)
        for i in range(8):
            print(".", end='', flush=True)
            sleep(1)
        print(dedent("""
        \nITS ANOTHER ALIEN!!!! BUT THIS ALIEN IS 10X THE SIZE OF THE REST
OF THE ALIENS!!!!
IT SEEMS LIKE IT IS THE BOSS ALIEN THAT IS THE GATEKEEPER TO THE 
TELEPHONE BOOTH!""")) 
        sleep(3)
        for i in range(8):
            print(".", end='', flush=True)
            sleep(1)
        print(dedent("""\nThe only way to take this alien down is to fight it!!!"""))
        sleep(2)
        print("Are you going to through a punch or kick?")
        choice = input("> ")
        if choice == 'punch':
            print(dedent("""
            Oof that might have been the wrong choice because 
he is 100x your size and the punch did nothing to him.
You broke your hand and did not hurt him at all. As a 
counter attack from the alien he grabs you and eats you.
You fall to his stomach.""")) 
            sleep(3)
            for i in range(8):
                print(".", end='', flush=True)
                sleep(1)
            print(dedent("""
            \nOut of no where an angel shows up
telling you that you can rewind 5 seconds!!!
Do you take it? yes or no?"""))
            choice = input("> ")
            if choice == 'yes':
                return 'boss_alien'
            elif choice == 'no':
                return 'death'
            else:
                print("""
                Why are you trying to not anwer?
                Well now you have to fight him all
                over again!!!
                """)
                sleep(2.5)
                return 'boss_alien'

        elif choice == 'kick':
            print(dedent("""
You kick the alien right in its pressure on his leg
and he gets annoyed with you! He picks you up and
throws you across the forest!!!!"""))
            sleep(3)
            for i in range(8):
                print(".", end='', flush=True)
                sleep(1)
            print(dedent("""
OUCH you take a hit but is still okay enough to fight!
You look to your right and see an old rustic sword
right next to you!!!!!! You pick it up and feel this
rush of energy that you would get from like a red bull.
Now you run full speed right toward the alien but what 
are you going to do? Go for its leg again or eyes???
leg or eyes?"""))
            choice = input("> ")
            if choice == 'leg':
                print(dedent("""
You slice his leg but to the big alien it is just like 
a normal cut. It did not do much but annoy the alien again!
He picks you up and swings you around like you are his doll
and hits you on the ground until you go unconsious"""))
                sleep(3)
                for i in range(8):
                    print(".", end='', flush=True)
                    sleep(1)
                print("YOU DIED!!!!!!!")
                return 'death'
            elif choice == 'eyes':
                print(dedent("""
You have the power to jump really high now and jump high
enough to reach the aliens eyes! You stab his right eyes and on the way down
stab his chest ripping him wide open!!!
You have done it!!!! The alien is dead!!!!"""))
                sleep(3)
                for i in range(8):
                    print(".", end='', flush=True)
                    sleep(1)
                print(dedent("""
Now you can go into the telephone booth with nothing in your way
good job!!!"""))
                return 'win'
            else:
                print("""
                Why are you trying to not anwer?
                Well now you have to fight him all
                over again!!!
                """)
                sleep(2.5)
                return 'boss_alien'
        else:
            print("You can't run away hahaha")
            return 'boss_alien'

        


class Win(Scenes):

    def enter(self):
        print("""
        You return to Earth with minimul injuries!
        Your feet are dragging across the trail from 
        exhaustion but you make it to your car!
        You drive home in a hurry becuase you are hungry and 
        tired!
        YAY!
        You make it home and decide to watch Netflix
        while having some instant ramen. Good job you lived!!!
        """)



