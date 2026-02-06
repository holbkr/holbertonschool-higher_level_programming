#!/usr/bin/node

/* script that adds a li element to a list when the user clicks on the element with id add_item */

function AddLi () {
  const listToChange = document.querySelector('ul.my_list');
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  listToChange.appendChild(newElement);
}

const clickableElem = document.getElementById('add_item');
clickableElem.addEventListener('click', AddLi);
