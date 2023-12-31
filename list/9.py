def sort_list_of_dicts(list_of_dicts, key_to_sort):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key_to_sort])
    return sorted_list

# Example usage:
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 28},
    {'name': 'David', 'age': 22}
]

sorted_students = sort_list_of_dicts(students, key_to_sort='age')
print("Sorted list of students based on age:")
for student in sorted_students:
    print(student)
