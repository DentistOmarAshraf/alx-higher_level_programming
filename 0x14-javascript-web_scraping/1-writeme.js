#!/usr/bin/node
/**
 * Writing on file using fs module
 */

const fs = require('fs');
const args = process.argv.slice(2);

try {
  fs.writeFileSync(args[0], args[1], 'utf-8');
} catch (err) {
  console.error(err);
}
