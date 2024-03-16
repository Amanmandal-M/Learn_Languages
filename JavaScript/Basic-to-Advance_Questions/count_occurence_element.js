//  Problem Statement:
//  Write a javascript function that takes a array of integers and a target integer as input and returns the count of occurrences of the target integer in the list.

//  Input:
//  A list of integers nums.
//  An integer target to count occurrences of.

//  Output:
//  Return the count of occurrences of target in the list nums.

//  For example:
//  If the input array is [1, 2, 3, 4, 2, 2, 5] and the target integer is 2, the output should be 3 because 2 occurs three times in the list.

function targetedNumber(numbers, n) {
    let count = 0;
    for( let i=0; i < numbers.length; i++ ) {
        if (numbers[i] == n) count+=1;
    }
    return count;
}

const arrayInt = [1, 2, 3, 4, 2, 2, 5];
const target = 2;
const printedTargetNumber =  targetedNumber(arrayInt , target);
console.log(printedTargetNumber);  // Output: 3 