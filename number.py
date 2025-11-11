import random
counter=0
def generate_random_number():
    return random.randint(1, 100)

def increment_counter():
    global counter
    counter += 1

usernum=int(input("Enter a number between 1 to 100:"))
random_number=generate_random_number()
while usernum != random_number:
    increment_counter()
    while counter>10:
        print(f"Sorry, you've exceeded the maximum number of attempts. The correct number was {random_number}.")
        exit()
    if usernum < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    usernum=int(input("Enter a number between 1 to 100:"))
print(f"Congratulations! You've guessed the number {random_number} correctly in {counter} attempts.")
