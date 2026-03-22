names = ["Amitabh", "Amit", "Sumit", "Amitya", "Satyam", "Satyajeet", "Tech"]
query = input("Enter your Query: ").strip().capitalize()
print(f"\n--- Search Results for '{query}' ---")
found = False
i = 0
while i < len(names):
    name = names[i]
    if query in name:
        print(f"Result Found: {name} (Index: {i})")
        found = True
    i += 1
if not found:
    print("No matching name found.")