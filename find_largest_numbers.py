def find_largest_number(numbers):
    maxNumber = 0
    for n in numbers:
        if n>maxNumber:
            maxNumber=n
    return maxNumber

largest_number = find_largest_number([-2,-3,-1])

print(largest_number)