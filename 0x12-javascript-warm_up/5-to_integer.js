#!/usr/bin/node
/*
 * printing args
 */

const args = process.argv;

if (parseInt(args[2])) {
  console.log('My number: ' + parseInt(Number(args[2])));
} else {
  console.log('Not a number');
}
