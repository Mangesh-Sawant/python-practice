def print_number_till_n(n):
  first_number = 1
  while True:
      print(first_number)
      first_number +=1
      if first_number == n:
          return

n = int(input("Enter the number : "))

print_number_till_n(n)

