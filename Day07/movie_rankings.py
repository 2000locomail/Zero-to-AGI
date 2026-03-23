# Project: Sorted Movie Rankings
# Objective: Sort movies alphabetically and identify the first and last

mov1 = input("Enter Movie Name: ")
rating1 = int(input(f"How much rating do you give {mov1} movie: "))
mov2 = input("Enter Movie Name: ")
rating2 = int(input(f"How much rating do you give {mov2} movie: "))
mov3 = input("Enter Movie Name: ")
rating3 = int(input(f"How much rating do you give {mov3} movie: "))
movie_list = [mov1, mov2, mov3]
movie_list.sort()
print("\nSorted Movie List:",movie_list)
print(f"First Movie: {movie_list[0]}")
print(f"Last Movie: {movie_list[-1]}")