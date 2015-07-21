var gonzo = require('gonzales-ast');
var ast = gonzo.parse('a {margin: 0}'); // formerly 
var css_string = gonzo.toCSS(ast); // formerly 
 
 console.log(ast)