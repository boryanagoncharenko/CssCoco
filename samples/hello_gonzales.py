import os
import json
import coco.grammar as grammar
import coco.ast as cocoast
import coco.analysis as analysis
import src.parser as parser
import src.parse_tree as ast

filename = os.path.join('samples', 'tiny.css')
file = open(filename)
css = file.read()
result = parser.Parser.parse_css(css)
l = json.loads(result.decode('utf-8'))
tr = parser.SExprTransformer.transform(l)
a = ast.ParseTreeBuilder.build(tr)
# print(a.pretty_print())


coco_filename = os.path.join('samples', 'one.coco')
coco_file = open(coco_filename)
cs = coco_file.read()

res = grammar.parse(cs)
tree = cocoast.AstBuilder.build(res)

print(tree.pretty_print())
# for t in analysis.ExpressionEvaluator().test(tree.contexts[0].statements[0].markers_list, []):
#     print(t)
map = analysis.Evaluator.evaluate(tree)

for convention in map:
    print(convention.is_violated(a))

