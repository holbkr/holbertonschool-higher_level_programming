#!/usr/bin/node

/* Script that searches the second biggest integer in the list of arguments. */

const argumentsList = process.argv.slice(2).map(Number);

if (argumentsList.length < 2) {
  console.log('0');
} else {
  const numberSorted = argumentsList.sort((a, b) => b - a);
  console.log(numberSorted[1]);
}
