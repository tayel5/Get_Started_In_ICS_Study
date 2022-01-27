# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# the *args is pointless, instead we can do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_five(arg1, arg2, arg3, arg4, arg5):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}, arg5: {arg5}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I for nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
print_five("Alpha","Bravo", "Charlie", "Delta", "Echo")

