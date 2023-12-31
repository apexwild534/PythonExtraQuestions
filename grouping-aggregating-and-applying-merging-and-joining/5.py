# Define two lists of dictionaries
list1 = [
    {'id': 1, 'name': 'Alice', 'age': 25},
    {'id': 2, 'name': 'Bob', 'age': 30},
    {'id': 3, 'name': 'Charlie', 'age': 28}
]

list2 = [
    {'id': 2, 'city': 'New York'},
    {'id': 3, 'city': 'Los Angeles'},
    {'id': 4, 'city': 'Chicago'}
]

# Perform an inner join based on the 'id' key
inner_join_result = [
    {**item1, **item2}
    for item1 in list1
    for item2 in list2
    if item1['id'] == item2['id']
]

# Print the result of the inner join
for item in inner_join_result:
    print(item)
