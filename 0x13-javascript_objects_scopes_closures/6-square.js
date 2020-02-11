#!/usr/bin/node
const fiver = require('./5-square');

class Square extends fiver {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let a = 0; a < this.height; a++) {
        let line = '';
        for (let b = 0; b < this.width; b++) {
          line += c;
        }
        console.log(line);
      }
    }
  }
}

module.exports = Square;
