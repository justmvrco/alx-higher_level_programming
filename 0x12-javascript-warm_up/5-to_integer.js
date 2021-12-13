#!/usr/bin/node

// Script to print ints passed as arguments to the script.

const myArg = process.argv[2];

if (isNaN(Number(myArg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
