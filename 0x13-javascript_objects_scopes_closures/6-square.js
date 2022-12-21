#!/usr/bin/node
'use strict';
const SquareMain = require('./5-square');

module.exports = class Square extends SquareMain {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}
