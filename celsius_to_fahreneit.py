# F = (9/5 × 25) + 32 = 77°F

def get_fahrenheit_from_celsius(celsius):
    return (9/5 * celsius) + 32

celsius = int(input("Enter the celsius : "))

print(get_fahrenheit_from_celsius(celsius))