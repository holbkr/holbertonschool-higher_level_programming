#!/usr/bin/node

/*  script that toggles the class of the header element when the user clicks on the tag id toggle_header */

function toggleClass () {
  const headerChanging = document.querySelector('header');
  if (headerChanging.className === 'red') {
    headerChanging.setAttribute('class', 'green');
  } else {
    headerChanging.setAttribute('class', 'red');
  }
}

const clickableText = document.getElementById('toggle_header');

clickableText.addEventListener('click', toggleClass);
