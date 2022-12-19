#!/usr/bin/node
const x = process.argv.slice(2)
if (Number.isInteger(parseInt(x[0])))
    for (let i = 0; i < x[0]; i++) {
        for (let j = 0; j < x[0]; j++) {
            console.log('X');
        }       
    }
else
    console.log('Missing size');
