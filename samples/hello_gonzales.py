import os
import json
from src.parser import ParseWrapper

filename = os.path.join('samples', 'small.css')
file = open(filename, 'r')
css = file.read()
result = ParseWrapper.parse_css(css)
print(json.loads(result.decode('utf-8')))
# print(result)