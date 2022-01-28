def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")



age = int(input("What is your age?"))
height = int(input("What is your height?"))
weight = float(input("What is your weight?"))
iq = float(input("what is your iq?"))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it anyway, ok will do!

print("Here is a puzzle.")

print("first divide iq/2:", divide(iq,2), "\nmultiply result by weight: ", multiply(weight, divide(iq,2)), "\nSubtract that result by height: ",subtract(height, multiply(weight, divide(iq, 2))), "\nThe Last step, add that result to age: ",add(age, subtract(height, multiply(weight, divide(iq, 2)))))

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Who the heck knows what that even means anymore?")