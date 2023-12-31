import csv

max_score = -1  # Initialize max_score with a low value
highest_scorer = None  # Initialize the highest scorer name

with open('student_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    scores = []

    for row in reader:
        try:
            score = int(row['Score'])
            scores.append(score)
            if score > max_score:
                max_score = score
                highest_scorer = row['Name']
        except ValueError:
            print(f"Skipping invalid score for student {row['Name']}")

    if scores:
        average_score = sum(scores) / len(scores)
        print(f"Average Score: {average_score:.2f}")
        print(f"Maximum Score: {max_score}")
        print(f"Highest Scorer: {highest_scorer} with a score of {max_score}")
    else:
        print("No valid student scores found in the file.")
