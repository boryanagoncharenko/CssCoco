import os
import json
import src.parser as parser
import src.ast as ast

filename = os.path.join('samples', 'tiny.css')
file = open(filename, 'r')
css = file.read()
result = parser.ParseWrapper.parse_css(css)
l = json.loads(result.decode('utf-8'))
print(l)
tr = parser.SExprTransformer.transform(l)
print(tr)
a = ast.AstBuilder.build(tr)
print(a.pretty_print())