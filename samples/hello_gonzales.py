import os
import json
from src.parser import ParseWrapper
import src.ast as ast

json = ['root', ['ch1', ['ch2', ['ch3', ['s', ' '], ['p', 'p']]]]]
# json = ['root', ['ch0', ['ch1', ['stop', ''], ['s', '\n'], ['ch2', ['s', ' '], ['p', 'p'], ['s', '\t']]]]]
print(json)
transformer = ast.AstTransformer(json)
transformer._traverse_for_whitespace(json)
print(json)

# filename = os.path.join('samples', 'tiny.css')
# file = open(filename, 'r')
# css = file.read()
# result = ParseWrapper.parse_css(css)
# l = json.loads(result.decode('utf-8'))
# print(l)
# tr = ast.AstTransformer.transform(l)
# print(tr)
# a = ast.AstBuilder.build(tr)
# print(a.pretty_print())