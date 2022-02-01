#!/usr/bin/node
const request = require('request');

const requestURL = process.argv[2];
const users = {};

request(requestURL, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  const pBody = JSON.parse(body);

  for (let i = 0; i < pBody.length; i++) {
    const tmp = pBody[i].userId;
    if (pBody[i].completed) {
      users[tmp] = (users[tmp] || 0) + 1;
    }
  }

  console.log(users);
});
