import os
import json
import time
import sys

import antlr4

import csscoco.css.parser as parser
import csscoco.css.parse_tree as css
import csscoco.lang.syntax.ast_builder as ast
import csscoco.lang.syntax.cocoLexer as cocoLexer
import csscoco.lang.syntax.cocoParser as cocoParser
import csscoco.lang.analysis.violations as violations
import csscoco.lang.analysis.type_checker as checker


def get_css_parse_tree():
    filename = sys.argv[1]

    file = open(filename, encoding='utf-8')
    css_source = file.read()
    result = parser.Parser.parse_css(css_source)
    try:
        l = json.loads(result.decode('utf-8'))
    except ValueError:
        return None, '-----\nPlease check the validity of the css block!\n-----'
    tr = parser.SExprTransformer.transform(l)
    a = css.ParseTreeBuilder.build(tr)
    # print(a.pretty_print())
    return a, ''


def get_coco_ast():
    coco_filename = sys.argv[2]
    input_stream = antlr4.FileStream(coco_filename)
    lexer = cocoLexer.cocoLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = cocoParser.cocoParser(stream)
    tree = parser.stylesheet()
    visitor = ast.CocoCustomVisitor()
    convention_set = visitor.visitStylesheet(tree)

    return convention_set


def main():
    print('--- Parsing CSS ---')
    # start_time = time.time()

    # get_css_parse_tree()
    css_tree, error = get_css_parse_tree()
    if error:
        print(error)
        exit()

    coco_ast = get_coco_ast()
    errors = checker.TypeChecker.check(coco_ast)
    if errors.contain_errors():
        print(errors.string())
        exit()

    # print('--- Parsed CSS for sec:', (time.time() - start_time))
    print('--- Detecting violations ---')
    # start_time = time.time()

    # set = temp.ToGo.get_google_set()
    # violations.ViolationsFinder.find(set, css_tree)
    violations.ViolationsFinder.find(coco_ast, css_tree)
    print('--- Done ---')
    # print('--- Detected violations for secs:', (time.time() - start_time))

main()
# cProfile.run('main()')
