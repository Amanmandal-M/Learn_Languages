const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.question('Enter positive integer Number: ', (num) => {
    num = +num;

    if (isNaN(num) || num <= 0 || !Number.isInteger(num)) {
        console.log(`Invalid input. Please enter a positive integer.`);
        rl.close();
        return;
    }

    let factor = 1;
    for (let i = 1; i <= num; i++) {
        factor *= i;
    }

    console.log(`Factorial of ${num} is ${factor}`);

    rl.close();
});
