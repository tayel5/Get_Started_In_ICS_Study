def cafeteria():
    if key == 0:
        print("You run, starving to the caferteria doors and attempt to open, oh no! Its locked by order of Emperor Chang!!!\n")
        courtyard()
    else:
        print("You use the key on the cafeteria door and librate the food, the chicken finger mafia has already cleared out the chicken, but there are lots of Army MRE taco meat, tacos for everyone!!! You Win!!!")
        print(""""...
        ...
        ...
        ...
        or did you?""")

def admin():
    print("You are at the administration building")
    global dean_beat
    if dean_beat == 0:
        print("The Dean spots you and intercepts you\n")
        dean_battle()
    else:
        print("Lets not linger too long here or the Dean may appear again\n\n")
        courtyard()

def dean_battle():
    print("The Dean comes at you with reckless Dean-bandon")
    print("It seems your options are limited to handle the dean without murder")
    print("What will you do?")
    global dean_beat



    while dean_beat == 0:
        choice = input("(oculus)(animalsuit)(flexmuscles)> ")
        if choice == "oculus":
            print("The dean is distracted thinking he is some 3D god, get out of here to the cafeteria quick!")
            dean_beat = 1
            cafeteria()
        elif choice == "animalsuit":
            print("You try to compliment the Dean's magnificent animal suit, but alas that has just made the dean more powerful")
        elif choice == "flexmuscles":
            print("You flex your rippling muscles only to find the Dean enjoys the show, you've accomplished nothing")
        else:
            confusion()



def vent():
    print("Stuck in the vent with the monkey, you should've chang'd your response\n")

def courtyard():
    print("You are at the courtyard")
    print("From here you can go to the admin building, the cafeteria, or back to the library")
    print("What do you do?")

    choice = input("(admin)(cafeteria)(library)> ")

    if choice == "admin":
        admin()
    elif choice == "cafeteria":
        if dean_beat == 0:
            print("On the way to the cafeteria you stray too close to the admin building and see the Dean!!!")
            dean_battle()
        else:
            cafeteria()
    elif choice == "library":
        library()
    else:
        confusion()





def key_encounter():
    print("You look through the shelves and find the spanish 101 book!")
    print("As you paw through the book you don't learn any more spanish but you find a key hidden inside!\n\n\n\n\n")
    global key
    key = 1
    library()

def library():
    print("You are now at the library")
    print("As with many libraries there are bookshelves everywhere")
    print("From here you can do stuff in the library, go back to the study room or go outside to the courtyard")
    print("What do you you do?")
    global attempt
    choice = input("(bookshelves)(courtyard)(studyroom)> ")

    if choice == "bookshelves":
        if key == 0:
            key_encounter()
        else:
            print("You continue to look around the library but find nothing but ladders 101 books and the remnants of the great civil pillow war")
            library()
    elif choice == "courtyard":
        courtyard()
    elif choice == "sleep":
        sleep()

def sleep():
    print("You go back to sleep and deal with it another day")
    exit(0)

def confusion():
    # When an unavailable choice is made, let them know they're confused
    global attempt
    if attempt == 0:
        attempt += 1
        print("Not sure what you're doing there...")
    elif attempt == 1:
        attempt += 1
        print("Did you hit your head or something?")
    elif attempt == 2:
        attempt += 1
        print("No, not like that.")
    elif attempt == 3:
        attempt += 1
        print("Please refrain from creating multiple timelines without adequate felt goatees")
    elif attempt == 4:
        attempt += 1
        print("You're wrinkling my brain.")
    else:
        attempt = 0
        print("Let me chang your mind.")
    start()

def start():
    print("You're in the studyroom")
    print("What do you you do?")
    global attempt
    choice = input("(library)(courtyard)> ")

    if choice == "library":
        library()
    elif choice == "courtyard":
        courtyard()
    elif choice == "vent":
        vent()
    elif choice == "sleep":
        sleep()
    else:
        confusion()



attempt = 0
key = 0
dean_beat = 0
print("Welcome to Greendale!")
print("""You wake up in the study room with an enormous hunger, like really really bad hunger
you need to go to the cafeteria and eat something
you get up from the couch and see two doors, 
left takes you to the library proper, 
the right takes you out to the courtyard""")
start()