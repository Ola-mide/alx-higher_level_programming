#!/usr/bin/node

const process = require('process');
if (process.argv.length > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
