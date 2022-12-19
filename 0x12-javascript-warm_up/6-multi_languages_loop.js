#!/usr/bin/node
const multiLStr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const key in multiLStr) {
    if (Object.hasOwnProperty.call(multiLStr, key)) {
        const element = multiLStr[key];
        console.log(element);
    }
}
