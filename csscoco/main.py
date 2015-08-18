import json
import os
import sys

import antlr4

import csscoco.css.parser as css_parser
import csscoco.css.parse_tree as css
import csscoco.lang.syntax.ast_builder as ast
import csscoco.lang.syntax.cocoLexer as cocoLexer
import csscoco.lang.syntax.cocoParser as cocoParser
import csscoco.lang.syntax.error_listener as listener
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


def try_get_coco_ast():
    input_stream = antlr4.FileStream(sys.argv[2])
    lexer = cocoLexer.cocoLexer(input_stream)

    stream = antlr4.CommonTokenStream(lexer)
    parser = cocoParser.cocoParser(stream)
    parser.removeParseListeners()
    error_listener = listener.CocoErrorListener()
    parser.addErrorListener(error_listener)
    tree = parser.stylesheet()
    if error_listener.has_errors():
        return False, error_listener.print_errors()
    visitor = ast.CocoCustomVisitor()
    convention_set = visitor.visitStylesheet(tree)
    return True, convention_set


def check_files_exist():
    css_file = sys.argv[1]
    coco_file = sys.argv[2]
    message = ''
    if not os.path.isfile(css_file):
        message = ''.join(['Could not find css file ', css_file, '\n'])
    if not os.path.isfile(coco_file):
        message = ''.join([message, 'Could not find coco file ', coco_file])
    if message:
        print(message)
        exit()


def main():
    check_files_exist()
    css_tree, error = get_css_parse_tree()
    if error:
        print('Please check the validity of your css.')
        exit()

    successful, output = try_get_coco_ast()
    if not successful:
        print(output)
        exit()
    coco_ast = output
    errors = checker.TypeChecker.check(coco_ast)
    if errors.contain_errors():
        print(errors.string())
        exit()

    successful, output = violations.ViolationsFinder.find(coco_ast, css_tree)
    print(output.to_string())
    exit()

print(main())

