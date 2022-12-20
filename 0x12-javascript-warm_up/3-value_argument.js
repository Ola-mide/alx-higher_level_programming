#!/usr/bin/node

const process = require('process');
if (process.argv.slice(2) === []) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
