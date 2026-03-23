while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Calculator closed.")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", num1 / num2)

        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter valid numbers only!")

    except Exception as e:
        print("Something went wrong:", e)
        