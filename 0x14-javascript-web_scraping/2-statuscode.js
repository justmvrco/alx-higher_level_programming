#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');

request(requestURL, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log('code: ' + response.statusCode);
});
