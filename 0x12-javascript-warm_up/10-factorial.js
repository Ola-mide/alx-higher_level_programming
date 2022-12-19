#!/usr/bin/node

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const process = require('process');
const num = parseInt(process.argv[2]);
console.log(factorial(num));
