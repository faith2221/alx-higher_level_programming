#!/usr/bin/node

let total = 0;

exports.logMe = function count (item) {
  console.log(`${total}: ${item}`);
  total += 1;
};
