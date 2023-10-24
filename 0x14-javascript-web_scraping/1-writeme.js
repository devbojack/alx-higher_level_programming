#!/usr/bin/node

const fs = require('fs').promises;

(async () => {
  try {
    const filePath = process.argv[2];
    const content = process.argv[3];

    if (!filePath || !content) {
      console.error('Usage: ./script.js <file-path> <content>');
      return;
    }

    await fs.writeFile(filePath, content, 'utf8');
    console.log('File written successfully.');
  } catch (err) {
    console.error(err);
  }
})();
