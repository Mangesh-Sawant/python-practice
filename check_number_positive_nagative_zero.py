def check_number_is_zero_positive_negative(number):
    if number > 0:
        return print("number is positive")
    elif number < 0:
        return print("number is negative")
    else:
        return print("number is zero")

number = -2

check_number_is_zero_positive_negative(number)