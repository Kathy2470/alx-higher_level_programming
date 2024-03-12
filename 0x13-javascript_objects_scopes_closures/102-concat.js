#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) throw err;

    const concatenatedData = data1.trim() + '\n' + data2.trim();

    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) throw err;
      console.log('Files have been concatenated successfully!');
    });
  });
});
