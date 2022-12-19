#!/usr/bin/node
const x = process.argv.slice(2)
if (Number.isInteger(parseInt(x[0])))
  for (let index = 0; index < x[0]; index++) {
    console.log('C is fun');
  }
else
  console.log('Missing number of occurrences');
