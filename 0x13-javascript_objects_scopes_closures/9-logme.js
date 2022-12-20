#!/usr/bin/node
let log = 0;
exports.logMe = function (item) {
  const output = `${log}: ${item}`;
  console.log(output);
  log++;
};
