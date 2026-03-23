secret_number = 7
guess = int(input("Enter a number for Guess secret number: "))
if guess == secret_number:
    print(f"Right it is {secret_number}.")
# High Checks
elif guess >= secret_number+100:
    print("Too High almost 100 unit or more.")
elif guess == secret_number+10:
    print("High almost 10 unit.")
# Small Checks
elif guess <= secret_number-100:
    print("Small almost 100 unit.")
elif guess <= secret_number-10:
    print("Too Small almost 10 unit or more.")
else:
    print("🤏 Very close, but not quite!")