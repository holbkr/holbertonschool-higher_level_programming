#!/usr/bin/node

/* Script that prints x time a sentence */

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  parseInt(x);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
