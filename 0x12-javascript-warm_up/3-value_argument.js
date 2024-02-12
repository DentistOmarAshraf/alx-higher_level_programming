#!/usr/bin/node

/*
 * Printing Args
 */

const args = process.argv;
const hasarg = args.some((value, index) => index > 1);

if (!hasarg) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
