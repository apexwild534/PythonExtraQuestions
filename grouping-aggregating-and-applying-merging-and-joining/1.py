def calculate_average_score(student_data):
    total_score = 0
    num_students = len(student_data)
    
    for student in student_data:
        total_score += student['score']
    
    if num_students > 0:
        average_score = total_score / num_students
        return average_score
    else:
        return 0

# Example student data as a list of dictionaries
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 88},
    {'name': 'Eve', 'score': 91}
]

average = calculate_average_score(students)
print("Average score for all students:", average)
