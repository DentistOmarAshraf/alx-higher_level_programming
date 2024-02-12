#!/usr/bin/node

/*
 * print (x)time from argv
 */

const args = process.argv;
const times = parseInt(args[2]);

if (times) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
