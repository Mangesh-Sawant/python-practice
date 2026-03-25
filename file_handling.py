with open("example.txt", "w+") as file:
    file.write("write plus, ")

with open("example.txt", "a+") as file:
    file.write("My name is Khan and i am Not Good, ")

with open("example.txt", "r") as file:
    print(file.read())