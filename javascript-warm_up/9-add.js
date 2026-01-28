#!/usr/bin/node

/* script that prints the addition of 2 integers */

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  return (num1 + num2);
}

const a = process.argv[2];
const b = process.argv[3];
const result = add(a, b);
console.log(result);
