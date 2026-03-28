# The "Digital Family Tree" (Hierarchy Explorer)

data_tree = [
    "Grandfather", [
        "Father", [
            "Son", 
            "Daughter"
        ],
        "Uncle", [
            "Cousin (Male)", 
            "Cousin (Female)"
        ]
    ]
]

def explore_tree(members):
    for member in members:
        if isinstance(member, list):
            explore_tree(member)
        else:
            print(f"Member: {member}")

explore_tree(data_tree)