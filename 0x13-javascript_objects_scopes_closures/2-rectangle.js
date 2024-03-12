#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive interger or is equal to 0, create
      this.width = undefined;
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
