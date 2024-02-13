#!/usr/bin/node

const dict = require('./101-data').dict;

let entry = Object.entries(dict);

entry = entry.sort(function (a, b) {
  return a[1] - b[1];
});

const obj = {};
for (let i = 0; i < entry.length; i++) {
  const key = entry[i][1].toString();
  if (!obj[key]) {
    obj[key] = [];
  }
  obj[key].push(entry[i][0]);
}
console.log(obj);
