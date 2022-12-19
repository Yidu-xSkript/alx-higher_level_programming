#!/usr/bin/node
const x = process.argv.slice(2);
if (x.length > 1) {
  console.log(Math.max(...x));
} else {
  console.log(0);
}
