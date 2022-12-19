#!/usr/bin/node

const process = require('process');
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  output = 'My number: ' + num;
  console.log(output);
}
