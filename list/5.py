def find_intersection(list1, list2):
    # Use a set to store unique elements from list1
    set1 = set(list1)

    # Use a set comprehension to find common elements in list2
    common_elements = [x for x in list2 if x in set1]

    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = find_intersection(list1, list2)
print("Intersection of list1 and list2:", intersection)
