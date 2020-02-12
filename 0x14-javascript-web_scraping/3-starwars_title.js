#!/usr/bin/node
const request = require('request');
request.get(`http://swapi.co/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    throw error;
  }
  const derulo = JSON.parse(body);
  console.log(derulo.title);
});
