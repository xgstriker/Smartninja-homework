x = int(input("Iveskite pirma skaiciu: "))
y = int(input("Iveskite antra skaiciu: "))
operation = input("Iveskite matematine operacija (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Nesupratau operacijos")