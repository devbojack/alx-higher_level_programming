#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }  
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
};
