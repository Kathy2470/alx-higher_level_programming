#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  const printCharacters = (index) => {
    if (index === charactersUrls.length) {
      return;
    }

    request(charactersUrls[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to retrieve character data. Status code: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      printCharacters(index + 1);
    });
  };

  printCharacters(0);
});
