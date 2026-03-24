def find_sum_of_n_number(n):
    sum_of_n_number = 0
    for i in range(1,n+1):
        sum_of_n_number += i
    return sum_of_n_number


total = find_sum_of_n_number(3)

print(total)



