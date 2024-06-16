#!/usr/bin/node
const x = Number(process.argv[2]);
const s = 'X';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log(s.repeat(x));
  }
}
