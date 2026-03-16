# Task: Secure Username Portal
# Objective: Sanitize input and verify security requirements

username = input("Enter your Username: ").strip()
doller = username.count("$")
if (len(username) > 5 and doller):
    print("Secure")
else:
    print("Weak")
