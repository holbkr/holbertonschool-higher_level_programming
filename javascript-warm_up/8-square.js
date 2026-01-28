#!/usr/bin/node

/* Script that prints a square of x */

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing size');
} else {
  parseInt(x);
  for (let i = 0; i < x; i++) {
    for (let i = 0; i < x; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
