#!/usr/bin/node
/*
 * printing args
 */

const args = process.argv;

if (Number(args[2])) {
  console.log('My Number: ' + parseInt(Number(args[2])));
} else {
  console.log('Not a number');
}
