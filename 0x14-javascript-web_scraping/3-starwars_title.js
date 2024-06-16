#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

const id = process.argv[2];

request(url + id, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
