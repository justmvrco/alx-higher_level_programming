#!/usr/bin/node

// script that implements the class square from 5-square

const Sq1 = require('./5-square');

module.exports = class Square extends Sq1 {
  charPrint (c) {
    let rows;
    if (c === undefined) {
      rows = 'X';
      for (let i = 0; i < this.width - 1; i++) {
        rows += 'X';
      }
    } else {
      rows = c;
      for (let i = 0; i < this.width - 1; i++) {
        rows += c;
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rows);
    }
  }
};	
