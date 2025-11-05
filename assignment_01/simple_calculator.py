num1 = int(input("Enter a Num1 "))
num2 = int(input("Enter a Num2 "))
select_operator = input("Enter a Operator ")


def calculator(num1, num2, select_operator):
    if select_operator == "+":
        print(num1 + num2)
    elif select_operator == "-":
        print(num1 - num2)
    elif select_operator == "*":
        print(num1 * num2)
    elif select_operator == "/":
        print(num1 / num2)
    else:
        print("invalid_operator")


calculator(num1, num2, select_operator)
