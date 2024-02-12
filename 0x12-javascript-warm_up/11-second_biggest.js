#!/usr/bin/node

/*
 * Find seconed biggest number
 */

const args = process.argv;

const arr = [];
args.forEach((value, index) => {
  if (index > 1) {
    arr.push(parseInt(value));
  }
});

if (arr.length <= 1) {
  console.log(0);
} else {
  arr.sort();
  console.log(arr[arr.length - 2]);
}
