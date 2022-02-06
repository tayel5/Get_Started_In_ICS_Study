def cafeteria():
    print("You are at the Cafeteria, you win!!!")

def admin():
    print("You are at the administration building")

def gym():
    print("You are at the gym")

def vent():
    print("Stuck in the vent with the monkey, you should've chang'd your response")

def courtyard(num):
    print("You are at the courtyard")

def library(num):
    print("You are now at the library")

def sleep(why):
    print(why)
    exit(0)

def confusion(why,num):
    print(why)
    start(num)

def start(attempt):
    print("What do you you do?")

    choice = input("(left)(right)> ")

    if choice == "left":
        library(attempt)
    elif choice == "right":
        courtyard(attempt)
    elif choice == "vent":
        vent()
    elif choice == "sleep":
        sleep("You go back to sleep and deal with it another day")
    elif attempt == 0:
        attempt += 1
        confusion("Not sure what you're doing there...", attempt)
    elif attempt == 1:
        attempt += 1
        confusion("Did you hit your head or something?", attempt)
    elif attempt == 2:
        attempt += 1
        confusion("No, not like that.", attempt)
    elif attempt == 3:
        attempt += 1
        confusion("Please refrain from creating multiple timelines without adequate felt goatees", attempt)
    elif attempt == 4:
        attempt += 1
        confusion("You're wrinkling my brain.", attempt)
    else:
        confusion("Clear your mind.", attempt)


num = 0
print("Welcome to Greendale!")
print("""You wake up in the study room and see two doors, 
one takes you to the library proper, 
the other takes you out to the courtyard""")
start(num)