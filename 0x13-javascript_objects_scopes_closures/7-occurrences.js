#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;

  for (let i = 0; i < list.length; i++) {
    total = (list[i] === searchElement ? total + 1 : total);
  }

  return total;
}; 
