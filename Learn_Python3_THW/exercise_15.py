from sys import argv

script, filename = argv

# Variable to open the target file as part of the command
txt = open(filename)

# prints sentence with name of file
print(f"Here's yur file {filename}:")
# print the content of the file
print(txt.read())

# close the first txt file
txt.close()

print("Type the filename again:")
# file_again accepts the name of the file
file_again = input("> ")

# opens the (new?) file
txt_again = open(file_again)

# Prints content of the file
print(txt_again.read())

# closes the second txt file
txt_again.close()