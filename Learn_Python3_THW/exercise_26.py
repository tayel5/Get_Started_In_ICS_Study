from sys import argv  # needed to import argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()  # not originally defined
print("How much do you weigh?", end=' ')  # needed closing bracket
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.") # Height was not defined

script, filename = argv   # argv needed import

txt = open(filename)  # mispelled variable

print(f"Here's your file {filename}:") # needed f"" statement for {filename} to work
print(txt.read()) # misspelled txt as tx

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # used a _ rather than a .


print('Let\'s practice everything.') # needed escape function for "Let's"
print('''You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.''') # needed ''' for multiline string

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # needed closing "
print(poem)
print("--------------") # needed opening "


five = 10 - 2 + 3 - 6 # in order to equal 5, last subtraction needs to be against 6
print(f"This should be five: {five}") # needed closing bracket

def secret_formula(started): # needed colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # needed / to reflect number of crates needed if each crate holds 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # added crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # misspelled variable
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 #misspelled variable
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # python3 requires ()

if people >= cats: # changed from < to >=
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # needed :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # needed :
    print("People are less than or equal to dogs.") # needed closing "


if people == dogs: # needed == not =
    print("People are dogs.")
