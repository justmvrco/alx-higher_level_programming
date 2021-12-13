#!/usr/bin/node

// Script to find the factorial of a number

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
