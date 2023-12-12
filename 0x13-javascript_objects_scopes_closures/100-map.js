#!/usr/bin/node
const list = require('./100-data.js').list;

const newLIST = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
