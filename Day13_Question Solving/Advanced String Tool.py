text = input("Entey your Name: ")
print("1. Reverse Text")
print("2. Count Vowels")
print("3. Exit")
choice = input("\nSelect an Option(1-3): ")
if choice == "1":
    reversed_text = text[::-1]
    print(f"Reversed String: {reversed_text}")
elif choice == "2":
    t_text = text.lower()
    vowels = t_text.count("a") + t_text.count("e") + t_text.count("i") + t_text.count("o") + t_text.count("u")
    print(f"Total Vowels found: {vowels}")

elif choice == "3":
    print("Exiting Engine...")
else:
    print(f"Invalid Choice,  {text}!")