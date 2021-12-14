#!/usr/bin/node

// script that converts a number to a certain base

exports.converter = function (base) {
  function newBase (number) {
    return number.toString(base);
  }

  return newBase;
};
