#!/usr/bin/node

/*
 * factorial function
 */

const args = process.argv;

const factorial = (x) => {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
};

console.log(`${factorial(parseInt(args[2]))}`);
