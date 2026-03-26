# List of subjects with duplicates (Representing multiple students)

subject_list = [
    "English", "Math", "Chemistry", "Physics", "Hindi", 
    "Math", "English", "Physics", 
    "English", "Math", "Chemistry", "Physics", "Hindi", 
    "Math", "English", "Physics"
]
def show_unique_subjects(subject_list):
    subject_set = set(subject_list)
    for subject in subject_set: # Loop through the set directly
        print(f"Subject = {subject}")
    
# Function Call
show_unique_subjects(subject_list)
