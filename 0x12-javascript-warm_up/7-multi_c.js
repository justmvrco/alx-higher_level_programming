#!/usr/bin/node

// Script to print ints passed as arguments to the script.

const myArg = process.argv[2];

if (isNaN(Number(myArg))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < myArg; i++) {
    console.log('C is fun');
  }
}
