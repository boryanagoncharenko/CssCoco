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


def get_css_parse_tree():
    file = open(sys.argv[1], encoding='utf-8')
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


def get_coco_ast():
    input_stream = antlr4.FileStream(sys.argv[2])
    lexer = cocoLexer.cocoLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = cocoParser.cocoParser(stream)
    tree = parser.stylesheet()
    visitor = ast.CocoCustomVisitor()
    convention_set = visitor.visitStylesheet(tree)
    return convention_set


def main():
    css_tree, error = get_css_parse_tree()
    if error:
        return 'Please check the validity of your css.'

    coco_ast = get_coco_ast()
    errors = checker.TypeChecker.check(coco_ast)
    if errors.contain_errors():
        return errors.string()

    log = violations.ViolationsFinder.find(coco_ast, css_tree)
    return log.to_string()

if __name__ == "__main__":
    print(main())
    sys.exit(0)
