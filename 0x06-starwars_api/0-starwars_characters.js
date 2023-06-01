#!/usr/bin/node
const request = require('request');

const film = process.argv[2];

if (film >= 1 && film <= 7) {
  request('https://swapi-api.alx-tools.com/api/films/' + film, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const reply = JSON.parse(body);
      reply.characters.forEach(element => {
        request(element, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const Creply = JSON.parse(body);
            console.log(Creply.name);
          }
        });
      });
    }
  });
}
