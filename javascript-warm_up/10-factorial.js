#!/usr/bin/node

/* script that computes and prints a factorial */

function factorialFunction (n) {
  if (n === 1) {
    return (1);
  } else {
    return n * factorialFunction(n - 1);
  }
}

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('1');
} else {
  console.log(factorialFunction(number));
}
