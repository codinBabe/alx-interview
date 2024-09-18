#!/usr/bin/node
// This script displays the names of characters from a Star Wars movie
// based on the movie number given in the command line argument
const request = require('request');

function getStarWarsCharacters () {
  const arg = process.argv[2];
  if (arg && arg > 0 && arg <= 7) {
    const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
    request(url, async function (error, response, body) {
      if (error) {
        console.error(error);
      } else {
        const characters = JSON.parse(body).characters;
        for (const character of characters) {
          const name = await new Promise((resolve, reject) => {
            request(character, function (error, response, body) {
              if (error) {
                reject(error);
              } else {
                resolve(JSON.parse(body).name);
              }
            });
          });
          console.log(name);
        }
      }
    });
  } else {
    console.log('Enter a valid movie number between 1 and 7');
  }
}

getStarWarsCharacters();
