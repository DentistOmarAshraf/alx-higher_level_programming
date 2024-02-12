#!/usr/bin/node

/*
 * print (x)time from argv
 */

const args = process.argv;
const times = parseInt(args[2]);

if (times) {
  let str = '';
  for (let i = 0; i < times; i++) {
    for (let j = 0; j < times; j++) {
      str += 'X';
    }
    if (i !== times - 1) {
      str += '\n';
    }
  }
  console.log(str);
} else {
  console.log('Missing size');
}
