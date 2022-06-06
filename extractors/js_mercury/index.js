const Mercury = require('@postlight/mercury-parser');
const fs = require('fs');

var args = process.argv.slice(2);
var url = args[0];
var html = fs.readFileSync(args[1], 'utf8');

Mercury.parse(url, {
  html: html,
  contentType: 'text',
}).then(result => console.log(result['content']));

