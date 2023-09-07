#include <iostream>

// Function declaration
int factorial(int num);

int main() {
    int num;
    int main_result;

    while (true) {
        std::cout << "Enter a non-negative integer (or -1 to exit): ";
        std::cin >> num;

        if (num == -1) {
            break;
        }

        if (num < 0) {
            std::cout << "Please enter a non-negative integer." << std::endl;
        } else {
            main_result = factorial(num);

            std::cout << "Factorial of"<< num << "is :" << main_result << std::endl;
        }
    }
    return 0;
}

// Function definition
int factorial(int num) {
    int result = 1;
    for (int i = num; i >= 1; i--) {
        result *= i;
    }
    return result;
}
