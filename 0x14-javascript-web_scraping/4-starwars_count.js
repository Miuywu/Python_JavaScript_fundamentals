#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    throw error;
  }
});
request.get('https://swapi.co/api/people/18/', (error, response, body) => {
  if (error) {
    throw error;
  }
  let c = 0;
  for (const film of JSON.parse(body).films) {
    if (typeof film === 'string') {
      c++;
    }
  }
  return console.log(c);
});
