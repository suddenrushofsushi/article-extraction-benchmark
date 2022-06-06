const Mercury = require('@postlight/mercury-parser');

var args = process.argv.slice(2);
console.log(args);
var url = args[0];
Mercury.parse(url, {
  html:
    '<html><body><article><h1>Thunder (mascot)</h1><p>Thunder is the stage name for the horse who is the official live animal mascot for the Denver Broncos</p></article></body></html>',
}).then(result => console.log(result));

