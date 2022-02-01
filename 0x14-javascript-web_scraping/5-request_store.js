#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const requestURL = process.argv[2];
const fPath = process.argv[3];

request(requestURL, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(fPath, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
