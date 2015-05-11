import os
import json
import coco.grammar as grammar
import coco.ast as cocoast
import coco.analysis as analysis
import src.parser as parser
import src.parse_tree as ast
import src.tree_search as matching

filename = os.path.join('samples', 'tiny.css')
file = open(filename)
css = file.read()
result = parser.Parser.parse_css(css)
l = json.loads(result.decode('utf-8'))
tr = parser.SExprTransformer.transform(l)
a = ast.ParseTreeBuilder.build(tr)
print(a.pretty_print())


# pattern_descriptors = [matching.NodeDescriptor(value='{'),
#                        matching.NodeDescriptor(type_='declaration'),
#                        # matching.NodeDescriptor(type_='decldelim'),
#                        matching.NodeDescriptor(value='}')]
# # pattern_descriptors = [matching.NodeDescriptor(type_='comment')]
# white_descriptors = [matching.NodeDescriptor(type_='space'),
#                      matching.NodeDescriptor(type_='indent'),
#                      matching.NodeDescriptor(type_='tab'),
#                      matching.NodeDescriptor(type_='newline'),
#                      matching.NodeDescriptor(type_='decldelim')]
# pattern = matching.NodePattern(pattern_descriptors, white_descriptors)
#
# requirement = matching.Requirement(inner_patterns=[[matching.NodeDescriptor(type_='newline'),
#                                                     matching.NodeDescriptor(type_='indent')],
#                                                    matching.NodeDescriptor(type_='newline')],
#                                    # after=[matching.NodeDescriptor(type_='newline')],
#                                    ignore_list=[matching.NodeDescriptor(type_='decldelim')])
#
#
# walker = matching.Walker()
# for nodes in walker.find_pattern(a, pattern):
#     success = requirement.is_fulfilled(nodes)
#     print(success)

coco_filename = os.path.join('samples', 'one.coco')
coco_file = open(coco_filename)
cs = coco_file.read()

res = grammar.parse(cs)

tree = cocoast.AstBuilder.build(res)
# print(tree.pretty_print())

map = analysis.Evaluator.evaluate(tree)

for convention in map:
    walker = matching.Walker()
    for nodes in walker.find_pattern(a, convention.pattern):
        success = convention.requirement.is_fulfilled(nodes)
        print(success)

