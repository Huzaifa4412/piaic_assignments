def main():
    print("============== Python Calculator ==============")
    print("============== By: Huzaifa Mukhtar ============\n")

    while True:
        print("\n")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print(" 1) +  (Addition)")
        print(" 2) -  (Subtraction)")
        print(" 3) *  (Multiplication)")
        print(" 4) /  (Division)")
        print(" 5) %  (Modulus)")
        print(" 6) ** (Power)")
        print(" 7) // (Floor Division)")
        print(" OR type 'all' to perform all operations")
        print(" OR type 'exit' to quit the calculator")

        operator = input("Enter your choice: ").strip()

        if operator.lower() == "exit":
            print("\nExiting the calculator...")
            print("Thank you for using my calculator")
            break

        elif operator == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")

        elif operator == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")

        elif operator == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")

        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")

        elif operator == "%":
            print(f"Result: {num1} % {num2} = {num1 % num2}")

        elif operator == "**":
            print(f"Result: {num1} ** {num2} = {num1**num2}")

        elif operator == "//":
            if num2 == 0:
                print("Error: Cannot perform floor division by zero!")
            else:
                print(f"Result: {num1} // {num2} = {num1 // num2}")

        elif operator.lower() == "all":
            print("\nPerforming all operations:")
            print(f"Addition:           {num1} + {num2}  = {(num1 + num2):.2f}")
            print(f"Subtraction:        {num1} - {num2}  = {(num1 - num2):.2f}")
            print(f"Multiplication:     {num1} * {num2}  = {(num1 * num2):.2f}")
            if num2 != 0:
                print(f"Division:           {num1} / {num2}  = {(num1 / num2):.2f}")
                print(f"Modulus:            {num1} % {num2}  = {(num1 % num2):.2f}")
                print(f"Floor Division:     {num1} // {num2} = {(num1 // num2):.2f}")
                print(f"Power:              {num1} ** {num2} = {(num1**num2):.2f}")
            else:
                print(
                    "Division, Modulus, and Floor Division cannot be performed (division by zero)."
                )

        else:
            print("Invalid operator! Please choose a valid option.\n")


if __name__ == "__main__":
    main()
