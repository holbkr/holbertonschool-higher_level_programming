#!/usr/bin/node

/* script that updates the text color of the headerelement to red (#FF0000)
when the user clicks on the tag with id red_header */

function changingColor () {
  const headerChanging = document.querySelector('header');
  headerChanging.style.color = '#FF0000';
}

const redText = document.getElementById('red_header');

redText.addEventListener('click', changingColor);
