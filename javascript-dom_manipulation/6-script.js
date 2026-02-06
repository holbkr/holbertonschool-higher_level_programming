#!/usr/bin/node

/* Write a JavaScript script that fetches the character name
from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag with id character. */

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
  .then(response => response.json())
  .then(data => {
    const nameToAdd = data.name;
    const elementModify = document.getElementById('character');
    elementModify.innerHTML = nameToAdd;
  })
  .catch(error => {
    console.error('error', error);
  });
