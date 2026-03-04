# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
   

    filtered_students = [student for student in student_list if student[2].lower() == major.lower()]
    
    return filtered_students


# Test code to verify the function works
if __name__ == "__main__":
    # Sample student data (ID, Name, Major)
    students = [
        (101, "Alice Johnson", "Computer Science"),
        (102, "Bob Smith", "Mathematics"),
        (103, "Charlie Davis", "Physics"),
        (104, "David Wilson", "Computer Science"),
        (105, "Eve Lewis", "Mathematics")
    ]
    
    # Test filtering (case insensitive)
    print("Testing filter_students_by_major:")
    print("-" * 40)
    
    # Test 1: Filter Computer Science students
    cs_students = filter_students_by_major(students, "Computer Science")
    print(f"Computer Science students: {cs_students}")
    
    # Test 2: Filter Mathematics students (using lowercase)
    math_students = filter_students_by_major(students, "mathematics")
    print(f"Mathematics students: {math_students}")
    
    # Test 3: Filter Physics students (using uppercase)
    physics_students = filter_students_by_major(students, "PHYSICS")
    print(f"Physics students: {physics_students}")
    
    # Test 4: Major with no matches
    chem_students = filter_students_by_major(students, "Chemistry")
    print(f"Chemistry students: {chem_students}")