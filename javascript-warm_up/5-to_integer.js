#!/usr/bin/node

/* Convert if possible a element to a number type */

const convertedNumber = parseInt(process.argv[2]);

if (isNaN(convertedNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertedNumber}`);
}
