def find_largest_element(list1):
  largest_element = list1[0]
  for element in list1:
    if element > largest_element:
      largest_element = element
  return largest_element


# Example usage:

list1 = [10, 20, 30, 40, 50, 30]
largest_element = find_largest_element(list1)

print("The largest element in the list is:", largest_element)
