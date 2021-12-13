#!/usr/bin/node

// Script that prints "JavaScript is amazing".

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
