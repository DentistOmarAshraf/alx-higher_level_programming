#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const actor = 'Wedge Antilles';

const url = args[0];

request(url, (err, resp, body) => {
  const data = JSON.parse(body).results;

  let count = 0;
  for (let x = 0; x < data.length; x++) {
    const res = data[x];
    for (let y = 0; y < res.characters.length; y++) {
      request(res.characters[y], (err, resp, body) => {
        const name = JSON.parse(body).name;
        if (name === actor) { count++; }
        if (x === data.length - 1 && y === res.characters.length - 1) { console.log(count); }
        if (err) { console.error(err); }
      });
    }
  }
  if (err) { console.error(err); }
});
