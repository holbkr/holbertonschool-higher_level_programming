#!/usr/bin/node

/* script that adds the class red to the header element when the user clicks on the tag with id red_header */

function addingClass () {
  const headerChanging = document.querySelector('header');
  headerChanging.classList.add('red');
}

const clickableText = document.getElementById('red_header');

clickableText.addEventListener('click', addingClass);
