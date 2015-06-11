import os
import json

import antlr4

import coco.syntax.listener as customListener
import coco.syntax.cocoLexer as cocoLexer
import coco.syntax.cocoParser as cocoParser
import coco.ast.ast as ast
import css.parser as parser
import css.parse_tree as css
import coco.analysis.violations as violations


def get_css_parse_tree():
    filename = os.path.join('samples', 'tiny.css')
    file = open(filename)
    css_source = file.read()
    result = parser.Parser.parse_css(css_source)
    try:
        l = json.loads(result.decode('utf-8'))
    except ValueError:
        return None, '-----\nPlease check the validity of the css block!\n-----'
    tr = parser.SExprTransformer.transform(l)
    a = css.ParseTreeBuilder.build(tr)
    print(a.pretty_print())
    return a, ''


def get_coco_ast():
    coco_filename = os.path.join('samples', 'one.coco')
    coco_file = open(coco_filename)
    cs = coco_file.read()

    # res = grammar.Parser.parse(cs)

    input = antlr4.FileStream(coco_filename)
    lexer = cocoLexer.cocoLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = cocoParser.cocoParser(stream)
    walker = antlr4.ParseTreeWalker()

    tree = parser.stylesheet()
    # listener = customListener.CocoCustomListener()
    # walker.walk(listener, tree)

    visitor = customListener.CocoCustomVisitor()
    visitor.visitStylesheet(tree)

    return None


css_tree, error = get_css_parse_tree()
print(error)
if not error:
    coco_ast = get_coco_ast()


is_stylesheet = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string='stylesheet'))
is_rule = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string='ruleset'))
is_declaration = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string='declaration'))
# is_next_rule = cocoast.IsExpr(cocoast.ImplicitVariableExpr.DEFAULT, cocoast.NodeTypeExpr(type_string='ruleset'))
# is_tag = cocoast.IsExpr(cocoast.ImplicitVariableExpr.DEFAULT, cocoast.NodeTypeExpr(type_string='ident'))
# is_child = cocoast.IsExpr(cocoast.ImplicitVariableExpr.DEFAULT,
#                           cocoast.NodeTypeExpr(type_string='combinator', value_string='>'))
# contains_tag = cocoast.ContainsExpr(cocoast.ImplicitVariableExpr.DEFAULT, is_tag)

stylesheet = ast.NodeExprWrapper(is_stylesheet)
rule = ast.NodeExprWrapper(is_rule)
declaration1 = ast.NodeExprWrapper(is_declaration, identifier='a')
declaration2 = ast.NodeExprWrapper(is_declaration, identifier='b')
declaration3 = ast.NodeExprWrapper(is_declaration, identifier='c')

is_newline = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string='newline'))
is_space = ast.IsExpr(ast.ImplicitVariableExpr.DEFAULT, ast.NodeTypeExpr(type_string='space'))
# requirement = cocoast.BetweenExpr(cocoast.VariableExpr('r1'),
#                                   cocoast.WhitespaceVariation([
#                                       cocoast.SequencePatternExpr([cocoast.NodeSequenceExprWrapper(is_newline, cocoast.Repeater(2, 3))]),
#                                       # cocoast.SequencePatternExpr([cocoast.NodeSequenceExprWrapper(is_space, cocoast.Repeater(lower=1, upper=10))])
#                                       ]),
#                                   cocoast.VariableExpr('r2')
#                                   )

# requirement = cocoast.BeforeExpr(cocoast.VariableExpr('d1'), cocoast.WhitespaceVariation([
#     cocoast.SequencePatternExpr([cocoast.NodeExprWrapper(is_newline)])
# ]))

relations = ast.Relations()
relations.register_relation(stylesheet, ast.IsAncestorOfRelation(rule))
relations.register_relation(rule, ast.IsAncestorOfRelation(declaration1))
relations.register_relation(rule, ast.IsAncestorOfRelation(declaration2))
relations.register_relation(rule, ast.IsAncestorOfRelation(declaration3))
pattern = ast.PatternExpr(stylesheet, [stylesheet, rule, declaration1, declaration2, declaration3], relations)

convention = ast.ForbidConvention(pattern, "Forbid pattern found")
context = ast.SemanticContext([convention], None)
sheet = ast.ConventionSet([context])

violations.ViolationsFinder.find(sheet, css_tree)
