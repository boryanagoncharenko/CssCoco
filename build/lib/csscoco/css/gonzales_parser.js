/**
 * Created by boryana on 05/05/15.
 */

var str = '';

process.stdin.resume();

process.stdin.setEncoding('utf8');

process.stdin.on('data', function (data) {
    str += data;
});

process.stdin.on('end', function () {
    var gonzo = require('gonzales');
    var css = process.argv[2];
    var ast = gonzo.srcToCSSP(css);
    var res = JSON.stringify(ast);

    process.stdout.write(res);
});
