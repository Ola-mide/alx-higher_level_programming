#!/usr/bin/node

const process = require('process');
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    let j = 0;
    while (j < size) {
      line = line + 'X';
      j++;
    }
    console.log(line);
  }
}
