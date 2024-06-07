#!/usr/bin/node
/**
 * Using request lib to fetch API
 */

const args = process.argv.slice(2);
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
request(url, (err, resp, body) => {
  const data = JSON.parse(body);
  console.log(data.title);
  if (err) {
    console.error(err);
  }
});
