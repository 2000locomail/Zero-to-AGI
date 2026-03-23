names = ["Satya", "Ace", "King", "Queen", "Jack", "Sumit", "Tech", "Ace","Ace", "King", "Queen", "Jack", "King", "Queen", "Jack", "Sumit"]
names_set = set(names)
duplicates = len(names) - len(names_set)
duplicates_names = []
seen = set()
for name in names:
    if name in seen:
        if name not in duplicates_names:
            duplicates_names.append(name)
    else:
        seen.add(name)

print(f"The number of total duplicates: {duplicates} ")
print(f"Names that were repeated: {duplicates_names}")