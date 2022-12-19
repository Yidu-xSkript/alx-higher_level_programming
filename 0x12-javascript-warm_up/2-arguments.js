#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg.length == 1) {
  console.log('Argument Found');
} else if (arg.length > 1) {
  console.log('Arguments Found');
} else {
  console.log('No Argument');
}
