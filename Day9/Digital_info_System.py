# Project: Global ID Search System
# Objective: Search user info by ID and handle errors

info = {
    "101": {
        "name": "Alex Johnson", 
        "address": "New York, USA", 
        "age": 25, 
        "dob": "2001-03-12"
    },
    "102": {
        "name": "Yuki Tanaka", 
        "address": "Tokyo, Japan", 
        "age": 22, 
        "dob": "2004-07-21"
    },
    "103": {
        "name": "Liam Smith", 
        "address": "London, UK", 
        "age": 28, 
        "dob": "1998-11-05"
    },
    "104": {
        "name": "Sofia Rossi", 
        "address": "Rome, Italy", 
        "age": 23, 
        "dob": "2003-05-18"
    },
    "105": {
        "name": "Zhang Wei", 
        "address": "Beijing, China", 
        "age": 30, 
        "dob": "1996-09-30"
    },
    "106": {
        "name": "Hans Müller", 
        "address": "Berlin, Germany", 
        "age": 27, 
        "dob": "1999-01-25"
    },
    "107": {
        "name": "Amélie Dubois", 
        "address": "Paris, France", 
        "age": 21, 
        "dob": "2005-12-14"
    },
    "108": {
        "name": "Mateo Garcia", 
        "address": "Madrid, Spain", 
        "age": 24, 
        "dob": "2002-08-02"
    },
    "109": {
        "name": "Sarah Connor", 
        "address": "Sydney, Australia", 
        "age": 26, 
        "dob": "2000-04-10"
    },
    "110": {
        "name": "Fatima Ahmed", 
        "address": "Dubai, UAE", 
        "age": 29, 
        "dob": "1997-10-22"
    }
}

id_number = input("Enter Your ID Number: ").strip()

if id_number in info:
    user_data = info[id_number]
    print(f"\n--- Data Found for ID {id_number} ---")
    print(f"Name: {user_data['name']}")
    print(f"Address: {user_data['address']}")
    print(f"Age: {user_data['age']}")
else:
    print("\nError: ID not found in the Database! ")