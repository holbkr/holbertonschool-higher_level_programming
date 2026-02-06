#!/usr/bin/node

/* script that updates the text of the header element to New Header!!!
when the user clicks on the element with id update_header */

function updateText () {
  const headerSelect = document.querySelector('header');
  headerSelect.textContent = 'New Header!!!';
}

const clickableElement = document.getElementById('update_header');
clickableElement.addEventListener('click', updateText);
