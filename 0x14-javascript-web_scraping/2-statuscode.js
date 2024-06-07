#!/usr/bin/node
/**
 * Using Request Module function
 */

const request = require('request');
const args = process.argv.slice(2);

request(args[0], (err, response, body) => {
  console.log('code: ' + response.statusCode);

  if (err) {
    console.error(err);
  }
});
