# Basic student information

student_name = "Ufot David"
matric_number = "22/30GD083"
age = 20
cgpa = 4.55
is_active = True

# Courses registered
courses_registered = ["Engineering Mathematics III", "Mechanics of Deformable Bodies", "Engineering Drawing"]

# Grades in dictionary format
grades = {
    "Engineering Mathematics III": "A",
    "Mechanics of Deformable Bodies": "A",
    "Engineering Drawing": "A"
}

# List of student names
student_names = [
    "Ufot David",
    "OkeOwo Olamikun",
    "Aremu Abdulsalam",
    "Rotimi Oluwaseun",
    "Adigun Stephen",
]

# Dictionary storing each student's profile
students_profiles = {
    "Ufot David": {
        "matric": "22/30GD083",
        "age": 20,
        "cgpa": 4.55,
        "is_active": True,
        "courses": ["Engineering Mathematics III", "Mechanics of Deformable Bodies", "Engineering Drawing"],
        "grades": {"Engineering Mathematics III": "A", "Mechanics of Deformable Bodies": "A", "Engineering Drawing": "A"}
    },

    "OkeOwo Olamikun": {
        "matric": "22/30GD061",
        "age": 19,
        "cgpa": 4.12,
        "is_active": True,
        "courses": ["Dynamics", "Machine Design", "Mechanical Behaviour of Materials"],
        "grades": {"Dynamics": "A", "Machine Design": "B", "Mechanical Behaviour of Materials": "B"}
    },

    "Aremu Abdulsalam": {
        "matric": "22/30GD015",
        "age": 21,
        "cgpa": 4.24,
        "is_active": True,
        "courses": ["Engineering Drawing", "Fluid Mechanics", "Thermodynamics and Heat Transfer"],
        "grades": {"Engineering Drawing": "B", "Fluid Mechanics": "A", "Thermodynamics and Heat Transfer": "A"}
    },

    "Adigun Stephen": {
        "matric": "22/30GD024",
        "age": 20,
        "cgpa": 4.45,
        "is_active": True,
        "courses": ["Engineering Drawing", "Fluid Mechanics"],
        "grades": {"Engineering Drawing": "A", "Fluid Mechanics": "A"}
    },

    "Rotimi Oluwaseun": {
        "matric": "22/30GD077",
        "age": 21,
        "cgpa": 4.04,
        "is_active": True,
        "courses": ["Machine Drawing", "Engineering Economics"],
        "grades": {"Machine Drawing": "B", "Engineering Economics": "B"}
    }
}

# A set of unique courses offered in the department
unique_courses = set()
for profile in students_profiles.values():
    unique_courses.update(profile["courses"])
    
# Tuple for fixed department information
department_info = (
    "Mechanical Engineering Department",
    "Faculty of Engineering & Technology",
    2025
)

# analysis_and_reporting.py
# Part 3: Analysis and Reporting
# Task 3.1: List of Operations and Slicing

# list of 10 assignment scores

assignment_scores = [78, 85, 92, 88, 76, 90, 81, 95, 84, 89]
top_3_scores = assignment_scores[:3]
last_5_scores = assignment_scores[-5:]
every_other_score = assignment_scores[::2]

# print("Assignment Scores:", assignment_scores)
# print("Top 3 Scores:", top_3_scores)
# print("Last 5 Scores:", last_5_scores)
# print("Every Other Score:", every_other_score)

# Task 3.2: Set Operations

# Students who passed Fluid Mechanics
set_pass = {
    "Aremu Abdulsalam",
    "Adigun Stephen",
}

# students with CGPA above 4.0
set_merit = {
    "Adigun Stephen",
    "Rotimi Oluwaseun",
    "Ufot David",
    "OkeOwo Olamikun",
    "Aremu Abdulsalam",
}

# 1. Students who passed and have merit (intersection)
passed_and_merit = set_pass & set_merit


# 2. All distinct students in both sets (union)
all_distinct_students = set_pass | set_merit


# 3. Students who passed but do not have merit (difference)
passed_but_no_merit = set_pass - set_merit


# Display results
# print("Students who passed and have merit:", passed_and_merit),
# print("All distinct students:", all_distinct_students),
# print("Students who passed but do not have merit:", passed_but_no_merit)


# menu_system.py
# Part 4: Interactive Menu System

students = {
    "Ufot David": {"cgpa": 4.55},
    "OkeOwo Olamikun": {"cgpa": 4.12},
    "Aremu Abdulasalam": {"cgpa": 4.24},
    "Adigun Stephen": {"cgpa": 4.45},
    "Rotimi Oluwaseun": {"cgpa": 4.04}
}

def view_all_students():
    print("\nList of Students:")
    for name in students:
        print("-", name)

def add_new_student():
    name = input("Stephen Duke")
    cgpa = float(input("3.95"))
    students[name] = {"cgpa": cgpa}
    print("Student added successfully.")
#
def check_graduation_eligibility():
    name = input("Stephen Duke")
    if name in students:
        if students[name]["cgpa"] >= 2.0:
            print(f"{name} is eligible for graduation.")
        else:
            print(f"{name} is NOT eligible for graduation.")
    else:
        print("Student not found.")

def find_top_performer():
    top_student = max(students, key=lambda x: students[x]["cgpa"])
    print(f"Top performer: {top_student} with CGPA {students[top_student]['cgpa']}")

# Main menu loop
def main_menu():
    while True:
        print("\n=== Student Management Menu ===")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        match choice:
            case "1":
                view_all_students()
            case "2":
                add_new_student()
            case "3":
                check_graduation_eligibility()
            case "4":
                find_top_performer()
            case "5":
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

        print("4. Find top performer")

# Nested dictionary of students and their courses scores
students_scores = {
    "Ufot David": {
        "Machine Design": 85,
        "Machine Drawing": 78,
        "Fluid Mechanics": 90
    },
    "OkeOwo Olamikun": {
        "Machine Design": 72,
        "Machine Drawing": 69,
        "Fluid Mechanics": 75,
    },
    "Aremu Abdulsalam": {
        "Machine Design": 80,
        "Machine Drawing": 88,
        "Fluid Mechanics": 82
    },
    "Adigun Stephen": {
        "Machine Design": 74,
        "Machine Drawing": 71,
        "Fluid Mechanics": 73
    },
    "Rotimi Oluwaseun": {
        "Machine Design": 92,
        "Machine Drawing": 89,
        "Fluid Mechanics": 94
    },
}

# Calculate the average score for each student
print("Average score for each student:")
for student, scores in students_scores.items():
    average_score = sum(scores.values()) / len(scores)
    print(f"Student {student}: {average_score:.2f}")

# Identify students who scored above 70 in all registered courses
print("\nStudents who scored above 70 in all courses:")
for student, scores in students_scores.items():
    if all(score > 70 for score in scores.values()):
        print(student)


# Pattern Matching with match-case


def identify_data_type(value):
    match value:
        case int():
            return f"Input is an INTEGER with value: {value}"
        case float():
            return f"Input is a FLOAT with value: {value}"
        case list():
            return f"Input is a LIST with {len(value)} elements: {value}"
        case dict():
            return f"Input is a DICTIONARY with {len(value)} key-value pairs: {value}"
        case str():
            return f"Input is a STRING with length {len(value)}: '{value}'"
        case _:
            return "Input type is not supported."















