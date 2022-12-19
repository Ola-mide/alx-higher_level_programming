#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (args.length === 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 2; i < args.length; i++) {
    nums.push(parseInt(args[i]));
  }
  nums.sort(function (a, b) { return b - a; });
  console.log(nums[1]);
}
