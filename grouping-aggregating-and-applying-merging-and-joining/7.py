import statistics

def calculate_median_and_std_deviation(students):
    group_scores = {}
    
    for student in students:
        group = student['group']
        score = student['score']
        
        if group in group_scores:
            group_scores[group].append(score)
        else:
            group_scores[group] = [score]
    
    result = {}
    
    for group, scores in group_scores.items():
        median = statistics.median(scores)
        std_deviation = statistics.stdev(scores)
        result[group] = {'median': median, 'std_deviation': std_deviation}
    
    return result

# Example student data as a list of dictionaries
students = [
    {'name': 'Alice', 'group': 'A', 'score': 85},
    {'name': 'Bob', 'group': 'B', 'score': 92},
    {'name': 'Charlie', 'group': 'A', 'score': 78},
    {'name': 'David', 'group': 'B', 'score': 88},
    {'name': 'Eve', 'group': 'A', 'score': 91}
]

result = calculate_median_and_std_deviation(students)

for group, data in result.items():
    print(f"Group {group}:")
    print(f"Median Score: {data['median']:.2f}")
    print(f"Standard Deviation: {data['std_deviation']:.2f}")
    print()
