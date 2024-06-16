#!/usr/bin/node
const list = require('./100-data').list;
const newlist = list.map((i, index) => (i * index));
console.log(list);
console.log(newlist);
