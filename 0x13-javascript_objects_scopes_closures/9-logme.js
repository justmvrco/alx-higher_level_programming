#!/usr/bin/node

// script that prints the number of arguments already prnted and the new argument value

function * generator () {
  let idx = 0;
  while (true) {
    yield idx++;
  }
}

const gen = generator();

exports.logMe = function (item) {
  console.log(gen.next().value + ': ' + item);
};
