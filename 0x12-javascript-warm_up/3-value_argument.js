#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg.length === 0) {
  console.log('No Argument');
} else {
  console.log(`${arg}`);
}
