#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let line = '';
      for (let b = 0; b < this.width; b++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}

module.exports = Rectangle;
