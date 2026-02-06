#!/usr/bin/node

/* script that fetches and lists the title for all movies */

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const listMovies = document.querySelector('ul#list_movies');
    data.results.forEach(movie => {
      const newElement = document.createElement('li');
      newElement.textContent = movie.title;
      listMovies.appendChild(newElement);
    })
      .catch(error => {
        console.error('error', error);
      });
  });
