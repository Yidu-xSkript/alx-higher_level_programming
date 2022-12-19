#!/usr/bin/node
function add(a, b) {
    return a + b;
}
const arg = process.argv.slice(2);
console.log(add(parseInt(arg[0]), parseInt(arg[1])));
