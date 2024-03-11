#!/usr/bin/node

function factorial(n) {
    if (isNaN(n) || parseInt(n) < 0) {
        return 1;
    } else if (parseInt(n) === 0) {
        return 1;
    } else {
        return parseInt(n) * factorial(parseInt(n) - 1);
    }
}

console.log(factorial(process.argv[2]));
