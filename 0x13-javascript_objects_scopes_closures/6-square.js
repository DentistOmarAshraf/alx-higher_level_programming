#!/usr/bin/node

const Square = require('./5-square');

module.exports = class extends Square {
  charPrint (c) {
    let i = c;
    if (!i) {
      i = 'X';
    }
    let str = '';
    for (let j = 0; j < this.width; j++) {
      for (let k = 0; k < this.height; k++) {
        str += i;
      }
      if (j !== this.width - 1) {
        str += '\n';
      }
    }
    console.log(str);
  }
};
