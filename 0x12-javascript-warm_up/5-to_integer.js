#!/usr/bin/node
const arg = process.argv.slice(2);
if (Number.isInteger(parseInt(arg[0]))) {
  console.log(`My Number: ${parseInt(arg[0])}`);
} else {
  console.log('Not a number');
}
