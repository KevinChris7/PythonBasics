
number1 = float(input("Enter the first number : "))
op = input("Please Enter the operator : ")
number2 = float(input("Enter the second number : "))

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "*":
    print(number1 * number2)
elif op == "/":
    print(number1 / number2)
else:
    print("Entered operator is invalid")

