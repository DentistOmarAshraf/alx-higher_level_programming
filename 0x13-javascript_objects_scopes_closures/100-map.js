#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

const nlist = list.map((val, ind) => val * ind);

console.log(nlist);
