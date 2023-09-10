#include <iostream>

int find_second_largest(int arr[], int size);

int main(){
    int arr[7] = {5, 2, 8, 1, 3, 9, 4};
    
    int result = find_second_largest(arr, 7);
    std::cout << "The second largest element is: " << result << std::endl;
    
    return 0;
}


int find_second_largest(int arr[], int size) {
    
    int max = 0;         
    int second_max = 0;
    
    for(int i=0; i<size; i++){
        if(arr[i] > max){
            second_max = max; 
            max = arr[i]; 
        }
        else if(arr[i] > second_max && arr[i] != max){
            second_max = arr[i];
        }
    }
    
    return second_max;
}
