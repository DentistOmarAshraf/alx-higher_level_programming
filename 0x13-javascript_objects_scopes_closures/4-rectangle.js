#!/usr/bin/node
/**
 * class Rectangle
 */

module.exports = class Rectangle {
/* Constructor function that accept only positve argument */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      super.constructor();
    }
  }

  /* Print function that print rectangle using (X) */
  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      if (i !== this.height - 1) {
        str += '\n';
      }
    }
    console.log(str);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
