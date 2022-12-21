#!/usr/bin/node
'use strict';
let arg = 'No argument';
if (process.argv[2]) {
  arg = process.argv[2];
}
console.log(arg);
