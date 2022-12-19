#!/usr/bin/node

const process = require('process');
if (process.argv.length > 2) {
  let i = 0;
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
