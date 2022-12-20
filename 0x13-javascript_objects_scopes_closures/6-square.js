#!/usr/bin/node
const Square5 = require('./5-square');
class Square extends Square5 {
  super (size) {}

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line = line + c;
      }
      console.log(line);
    }
  }
}
module.exports = Square;
