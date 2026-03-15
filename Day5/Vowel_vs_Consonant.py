# Task: Professional Vowel vs Consonant Checker
# Objective: Accurate detection using logical 'or' and case normalization

vowel = input("Enter one English Character : ").lower()
if (vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u"):
    print("This is a Vowel")
else:
    print("This is a Consonant")
