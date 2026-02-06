#!/usr/bin/node

/* Script that tell you if several arguments are passed */

let numberArgument = process.argv.length;
numberArgument -= 2;

if (numberArgument === 0) {
  console.log('No argument');
} else if (numberArgument === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
