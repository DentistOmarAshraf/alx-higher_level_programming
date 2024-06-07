#!/usr/bin/node
/**
 * Reading from file using fs module
 */

const fs = require('fs');
const args = process.argv.slice(2);

try {
  const text = fs.readFileSync(args[0], 'utf-8');
  console.log(text);
} catch (err) {
  console.error(err);
}
