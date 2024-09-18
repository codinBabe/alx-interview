#!/usr/bin/node
// This script displays the names of characters from a Star Wars movie
// based on the movie number given in the command line argument
const request = require('request');

function getStarWarsCharacters () {
  const arg = process.argv[2];
  if (arg && arg > 0 && arg <= 7) {
    try {
      request
        .get(`https://swapi-api.alx-tools.com/api/films/${arg}`)
        .on('response', (response) => {
          const data = JSON.parse(response.body);
          data.characters.forEach((character) => {
            request.get(character).on('response', (response) => {
              const data = JSON.parse(response.body);
              console.log(data.name);
            });
          });
        });
    } catch (error) {
      console.log(error);
    }
  } else {
    console.log('Enter a valid number between 1 and 7');
  }
}

getStarWarsCharacters();
