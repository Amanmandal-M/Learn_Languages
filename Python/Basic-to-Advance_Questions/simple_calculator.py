while True:
    # Display the menu 
    print("Simple Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if not choice.isdigit():
        print('Please enter a valid choice (1-5).\n')
        continue
    
    choice = int(choice)

    if choice == 5:
        break
    elif choice > 5:
        print('Invalid choice. Please try again.\n')
        continue

    # Prompt the user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform the selected operation and display the results
    if choice == 1:
        print("Result is:", num1 + num2,"\n")
    elif choice == 2:
        print("Result is:", num1 - num2,"\n")
    elif choice == 3:
        print("Result is:", num1 * num2,"\n")
    elif choice == 4:
        if num2 != 0:
            print("Result is:", num1 / num2,"\n")
        else:
            print("Cannot divide by zero! \n")
    else:
        print("Invalid choice. Please try again.\n")
