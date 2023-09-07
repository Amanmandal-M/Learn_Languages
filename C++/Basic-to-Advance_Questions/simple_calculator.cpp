#include <iostream>

int main() {
    int choice;
    
    double num1, num2;

    while (true) {

        //Display the menu 
        std::cout << "Simple Calculator Menu:" << std::endl;
        std::cout << "1. Addition" << std::endl;
        std::cout << "2. Subtraction" << std::endl;
        std::cout << "3. Multiplication" << std::endl;
        std::cout << "4. Division" << std::endl;
        std::cout << "5. Exit" << std::endl;
        std::cout << "Enter your choice: " << std::endl;
        std::cin >> choice;

        if (choice == 5) {
            // Exit the program if the user chooses option 5
            break;
        }

        // Prompt the user for two numbers
        std::cout << "Enter the first number: ";
        std::cin >> num1;
        std::cout << "Enter the second number: ";
        std::cin >> num2;

        // Perform the selected operation and display the results

        switch (choice)
        {
        case 1:
            std::cout << "Result is: " << (num1+num2) << std::endl;
            break;
        case 2:
            std::cout << "Result is: " << (num1-num2) << std::endl;
            break;
        case 3:
            std::cout << "Result is: " << (num1*num2) << std::endl;
            break;
        case 4:
            if(num2 != 0){
                std::cout << "Result is: " << (num1/num2) << std::endl;
            }else{
                std::cout << "Cannot divide by zero!" << std::endl;
            }
            break;
        default:
        std::cout << "Invalid choice. Please try again." << std::endl;
            break;
        }
    }
    return 0;
}