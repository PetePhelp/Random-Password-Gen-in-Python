# Random Password Generator
import random
# If you have any advice on how I structure my code let me know always looking to improve B)

while True:
    try:
        x = int(input("Choose a Length for password: "))
        if x > 0:
            break

        elif x < 0:
            continue
    except ValueError:
        print(end="")
print("Here is your password: ")
for _ in range(x):
    _ = random.randint(1,2)
    if _ == 1:
        chrgen = random.randint(97,122)
        a = chr(chrgen)
        print(a, end="")
    if _ == 2:
        numgen = random.randint(1,9)
        print(numgen, end="")
print("\n")
