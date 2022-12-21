#!/usr/bin/node
'use strict';
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = ''; let x = 0; let y = 0;
    while (x < this.width) {
      s += 'X';
      x++;
    }
    while (y < this.height) {
      console.log(s);
      y++;
    }
  }

  rotate () {
    const w = this.width; const h = this.height;
    this.width = h;
    this.height = w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
