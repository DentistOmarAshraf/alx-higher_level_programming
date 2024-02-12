#!/usr/bin/node

/*
 * Printing Args
 */

const args = process.argv;
const hasarg = args.some((value, index) => index > 1);

if (!hasarg) {
  console.log('No argument');
} else {
  args.forEach((val, ind) => {
    if (ind > 1) {
      console.log(val);
    }
  });
}
