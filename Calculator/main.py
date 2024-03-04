def plus(number_1, number_2):
    print(number_1 + number_2)
    return


def minus(number_1, number_2):
    print(number_1 - number_2)
    return


def multiply(number_1, number_2):
    print(number_1 * number_2)
    return


def divide(number_1, number_2):
    print(number_1 / number_2)
    return


choice = input(
    """Select your function:
1. Add
2. Subtract
3. Multiply
4. Divide
""")
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
if choice == "1":
    print("The answer is: ", end='')
    plus(number1, number2)
elif choice == "2":
    print("The answer is: ", end='')
    minus(number1, number2)
elif choice == "3":
    print("The answer is: ", end='')
    multiply(number1, number2)
elif choice == "4":
    print("The answer is: ", end='')
    divide(number1, number2)
