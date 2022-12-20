#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line = line + 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const newH = this.width;
    const newW = this.height;
    this.width = newW;
    this.height = newH;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
