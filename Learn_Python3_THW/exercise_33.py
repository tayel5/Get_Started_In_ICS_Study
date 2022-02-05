i = 0
numbers = []

print("Original while loop")
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


def circles(n,i):
    num = []
    for n in range(n,i+1):
        num.append(n)
    return num

make_num = circles(4,20)
print(make_num)

