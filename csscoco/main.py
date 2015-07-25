import json
import sys

import antlr4

import csscoco.css.parser as css_parser
import csscoco.css.parse_tree as css
import csscoco.lang.syntax.ast_builder as ast
import csscoco.lang.syntax.cocoLexer as cocoLexer
import csscoco.lang.syntax.cocoParser as cocoParser
import csscoco.lang.analysis.violations as violations
import csscoco.lang.analysis.type_checker as checker


def get_css_parse_tree(filename):
    file = open(filename, encoding='utf-8')
    css_source = file.read()
    result = css_parser.Parser.parse_css(css_source)
    try:
        l = json.loads(result.decode('utf-8'))
    except ValueError:
        return None, '-----\nPlease check the validity of the css block!\n-----'
    tr = css_parser.SExprTransformer.transform(l)
    a = css.ParseTreeBuilder.build(tr)
    # print(a.pretty_print())
    return a, ''


def get_coco_ast(filename):
    input_stream = antlr4.FileStream(filename)
    lexer = cocoLexer.cocoLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = cocoParser.cocoParser(stream)
    tree = parser.stylesheet()
    visitor = ast.CocoCustomVisitor()
    convention_set = visitor.visitStylesheet(tree)
    return convention_set


def main(args):
    css_tree, error = get_css_parse_tree(args[1])
    if error:
        print(error)
        exit()

    coco_ast = get_coco_ast(args[2])
    errors = checker.TypeChecker.check(coco_ast)
    if errors.contain_errors():
        print(errors.string())
        exit()

    log = violations.ViolationsFinder.find(coco_ast, css_tree)
    return log.to_string()

if __name__=='__main__':
    sys.exit(main(sys.argv))

# cProfile.run('main()')
