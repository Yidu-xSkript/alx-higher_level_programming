#!/usr/bin/node
'use strict';
let arg = 'No argument';
if (process.argv[2]) {
  arg = 'Argument found';
}
if (process.argv[3]) {
  arg = 'Arguments found';
}
console.log(arg);
