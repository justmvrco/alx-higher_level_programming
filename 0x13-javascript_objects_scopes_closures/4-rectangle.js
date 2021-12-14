#!/usr/bin/node

// script that creates a class.

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rows = 'X';
    for (let i = 0; i < this.width - 1; i++) {
      rows += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rows);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
