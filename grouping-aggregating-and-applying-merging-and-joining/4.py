def calculate_sum_and_average(students):
    group_scores = {}
    
    for student in students:
        group = student['group']
        score = student['score']
        
        if group in group_scores:
            group_scores[group]['sum'] += score
            group_scores[group]['count'] += 1
        else:
            group_scores[group] = {'sum': score, 'count': 1}
    
    for group, data in group_scores.items():
        average = data['sum'] / data['count']
        data['average'] = average

    return group_scores

# Example student data as a list of dictionaries
students = [
    {'name': 'Alice', 'group': 'A', 'score': 85},
    {'name': 'Bob', 'group': 'B', 'score': 92},
    {'name': 'Charlie', 'group': 'A', 'score': 78},
    {'name': 'David', 'group': 'B', 'score': 88},
    {'name': 'Eve', 'group': 'A', 'score': 91}
]

group_scores = calculate_sum_and_average(students)

for group, data in group_scores.items():
    print(f"Group {group}:")
    print(f"Sum of scores: {data['sum']}")
    print(f"Average score: {data['average']:.2f}")
    print()
