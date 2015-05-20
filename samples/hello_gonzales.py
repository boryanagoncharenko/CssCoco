import os
import json
import coco.syntax as grammar
import coco.ast.ast as cocoast
import coco.analysis as analysis
import src.parser as parser
import src.parse_tree as ast
import src.conventions as matching


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

    print(map.find_violations(css_tree))


# a = matching.Sequence([matching.SimpleDescriptor(value='{'), matching.SimpleDescriptor(type_='decl')])
# b = matching.Sequence([matching.SimpleDescriptor(type_='decl'), matching.SimpleDescriptor(value='}')])
# c = matching.Sequence([matching.SimpleDescriptor(value='{'), matching.SimpleDescriptor(type_='decl'),
#                        matching.SimpleDescriptor(value='}')])
#
# av = matching.SequenceVariation([a], matching.NodeDescriptor.ANY)
# bv = matching.SequenceVariation([b], matching.NodeDescriptor.ANY)
# cv = matching.SequenceVariation([c], matching.NodeDescriptor.ANY)
#
# print(av.is_part_of_variation(cv))
# print(bv.is_part_of_variation(cv))


    # You can have two consecutive \n nodes because they could be separated by an indent which is ignored
    # There could be more symbols than in the sequence that are not checked for at all