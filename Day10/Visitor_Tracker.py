# Project: Unique Visitor Tracker
# Objective: Convert list to set, count unique IDs, and verify entry

info = [101,102,103,104,105,106,107,108,109,110]
info = set(info)
Visitors_ID = int(input("Enter Your Unique Visitor ID: "))

print(f"Total Unique Visitors Today: {len(info)}")

if Visitors_ID in info:
    print("Access Granted")
else:
    print("Access Deny")