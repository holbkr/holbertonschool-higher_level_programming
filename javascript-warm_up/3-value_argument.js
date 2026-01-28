#!/usr/bin/node

/* script that prints the first argument passed to it */

const argumentsPassed = process.argv;
let i = -1;

for (let j = 0; argumentsPassed[j] !== undefined; j++) {
  i++;
}

if (i < 2) {
  console.log('No argument');
} else {
  console.log(argumentsPassed[2]);
}
