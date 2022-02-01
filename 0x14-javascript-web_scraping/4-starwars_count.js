#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  let count = 0;
  const pBody = JSON.parse(body).results;

  for (let i = 0; i < pBody.length; i++) {
    const a = pBody[i].characters.find((c) => {
      return c.match(/18/);
    });
    if (a !== undefined) {
      count++;
    }
  }

  console.log(count);
});
