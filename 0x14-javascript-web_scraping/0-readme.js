#!/usr/bin/node

const fs = require('fs').promises;

(async () => {
  try {
    const filePath = process.argv[2];

    if (!filePath) {
      console.error('Usage: ./script.js <file-path>');
      return;
    }

    const data = await fs.readFile(filePath, 'utf8');
    process.stdout.write(data);
  } catch (err) {
    console.error(err);
  }
})();
