#include <iostream>
#include <string>

int average_calc(int arr[], int size);

int main()
{
    int arr[5] = {80, 50, 70, 85, 120};

    int result = average_calc(arr, 5);
    std::cout << result << std::endl;

    return 0;
}

int average_calc(int arr[], int size)
{
    int sum = 0, avg;
    std::string user_name = "Aman";

    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }

    avg = sum / size;

    std::string greet_result = "Hello " + user_name + ", your average is: " + std::to_string(avg) + ".";

    std::cout << greet_result << std::endl;

    return avg;
}
