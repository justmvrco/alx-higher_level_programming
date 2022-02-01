#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (parseInt(movieId) < 8) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

  request(url, function (err, response, body) {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
