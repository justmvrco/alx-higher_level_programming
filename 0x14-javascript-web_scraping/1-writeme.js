#!/usr/bin/node

const fs = require('fs');

const data = process.argv[3];

fs.writeFile(process.argv[2], data, 'utf8', (err) => {
  if (err) {
    return console.log(err);
  }
});
