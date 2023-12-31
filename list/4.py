def reverse_list_in_place(my_list):
    left = 0
    right = len(my_list) - 1

    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1

# Example usage:
my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print("Reversed list:", my_list)
