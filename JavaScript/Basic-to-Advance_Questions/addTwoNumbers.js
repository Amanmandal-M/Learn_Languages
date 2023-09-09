const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

(()=>{
    rl.question('Enter First Number: ', (num1) => {
        rl.question('Enter Second Number: ', (num2) => {
            num1 = parseInt(num1);
            num2 = parseInt(num2);

            if (isNaN(num1) || isNaN(num2)) {
                console.log('Invalid input. Please enter valid numbers.');
            } else {
                console.log(`Result is : ${num1 + num2}`);
            }

            rl.close();
        });
    });
})();
