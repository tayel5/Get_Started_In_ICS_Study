def stuff_and_juice(good_stuff, box_of_juice):
    print(f"You have {good_stuff} stuff!")
    print(f"You have {box_of_juice} boxes of juice!")
    print("Man that's enough for a party!")
    print("Get a napkin.\n")

print("We can just give the function numbers directly:")
stuff_and_juice(20, 30)

print("OR, we can use variables from our script")
amount_of_stuff = 10
amount_of_juice = 50

stuff_and_juice(amount_of_stuff,amount_of_juice)

print("And we can combine the two, variables and math:")
stuff_and_juice(amount_of_stuff + 100, amount_of_juice + 1000)