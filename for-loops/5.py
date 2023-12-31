# first two numbers
num1, num2 = 0, 1
n=int(input("Enter the length: "))

print("Fibonacci sequence:")
# run loop n times
for i in range(n):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res