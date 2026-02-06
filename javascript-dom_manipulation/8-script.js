#!/usr/bin/node

/* script that displays the value of hello from that fetch in the HTML element with id hello. */

document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const helloData = data.hello;
      const elementToModify = document.getElementById('hello');
      elementToModify.textContent = helloData;
    })
    .catch(error => {
      console.error('error', error);
    });
});
