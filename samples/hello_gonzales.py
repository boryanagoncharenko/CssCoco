import os
import json
import src.parser as parser
import src.ast as ast
import src.matching as matching

filename = os.path.join('samples', 'tiny.css')
file = open(filename, 'r')
css = file.read()
result = parser.ParseWrapper.parse_css(css)
l = json.loads(result.decode('utf-8'))
tr = parser.SExprTransformer.transform(l)
a = ast.AstBuilder.build(tr)
print(a.pretty_print())


pattern_descriptors = [matching.NodeDescriptor(value='{'),
                       matching.NodeDescriptor(type_='declaration'),
                       # matching.NodeDescriptor(type_='decldelim'),
                       matching.NodeDescriptor(value='}')]
# pattern_descriptors = [matching.NodeDescriptor(type_='comment')]
white_descriptors = [matching.NodeDescriptor(type_='space'),
                    matching.NodeDescriptor(type_='indent'),
                    matching.NodeDescriptor(type_='tab'),
                    matching.NodeDescriptor(type_='newline'),
                    matching.NodeDescriptor(type_='decldelim')]
pattern = matching.Pattern(pattern_descriptors, white_descriptors)

requirement = matching.Requirement(inner=[matching.NodeDescriptor(type_='space'), matching.NodeDescriptor(type_='space')],
                                   # after=[matching.NodeDescriptor(type_='newline')],
                                   ignores=[matching.NodeDescriptor(type_='indent'),
                                            matching.NodeDescriptor(type_='decldelim')])


walker = matching.Walker()
for nodes in walker.find_pattern(a, pattern):
    success = requirement.is_fulfilled(nodes)
    print(success)
# for i in walker.find_start_node(a, descriptor):
#     print(i.type_, i.parent.type_, str(i.index))

# print(walker.find_start_node(a, descriptor))
