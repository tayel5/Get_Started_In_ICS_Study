from sys import argv

script, user_name = argv
prompt = '++++ '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like burgers {user_name}?")
burgers = input(prompt)

print(f"What did you do last summer {user_name}?")
summer = input(prompt)

print("What is your favorite book?")
book = input(prompt)

print(f"""
Alright, so you said {burgers} about liking burgers, thats nice.
You did {summer} last summer, seems nice.
And your favorite book is {book}. 
However, there was a correct answer though and that is Way of Kings.
""")