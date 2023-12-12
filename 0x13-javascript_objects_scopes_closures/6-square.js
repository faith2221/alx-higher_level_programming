#!/usr/bin/node
/**
 * The square class that inherits from  previous square class
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
  for (let i = 0; i < this.height; i++) {
    let myVar = '';
    let y = 0;
    while (y < this.width) {
      myVar += myChar;
      y++;
    }

    console.log(myVar);
  }
 }
}

module.exports = Square;
