import os
import json
import coco.grammar as grammar
import coco.ast as cocoast
import coco.analysis as analysis
import src.parser as parser
import src.parse_tree as ast


def get_css_parse_tree():
    filename = os.path.join('samples', 'tiny.css')
    file = open(filename)
    css = file.read()
    result = parser.Parser.parse_css(css)
    try:
        l = json.loads(result.decode('utf-8'))
    except ValueError:
        return None, '-----\nPlease check the validity of the css block!\n-----'
    tr = parser.SExprTransformer.transform(l)
    a = ast.ParseTreeBuilder.build(tr)
    print(a.pretty_print())
    return a, ''


def get_coco_ast():
    coco_filename = os.path.join('samples', 'one.coco')
    coco_file = open(coco_filename)
    cs = coco_file.read()

    res = grammar.Parser.parse(cs)
    tree = cocoast.AstBuilder.build(res)
    return tree


css_tree, error = get_css_parse_tree()
print(error)
if not error:
    coco_ast = get_coco_ast()
    map = analysis.Evaluator.evaluate(coco_ast)

    for convention in map:
        error = convention.is_violated(css_tree)
        # print(error)

