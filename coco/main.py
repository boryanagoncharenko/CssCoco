import os
import json
import time
import threading
import queue
import cProfile

import antlr4
#
import coco.syntax.ast_builder as customListener
import coco.syntax.cocoLexer as cocoLexer
import coco.syntax.cocoParser as cocoParser
import css.parser as parser
import css.parse_tree as css
import coco.analysis.violations as violations
import coco.temp as temp


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
    # print(a.pretty_print())
    return a, ''
    # return tr


def get_coco_ast():
    coco_filename = os.path.join('samples', 'one.coco')
    coco_file = open(coco_filename)
    # cs = coco_file.read()

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
    convention_set = visitor.visitStylesheet(tree)

    return convention_set


def nodes_counter(node):

    if not node.has_children():
        return 1
    else:
        num_children = 0
        for child in node.value:
            num_children += nodes_counter(child)
        return 1 + num_children


def main():
    print('--- Parsing CSS ---')
    start_time = time.time()

    # get_css_parse_tree()
    css_tree, error = get_css_parse_tree()
    print(error)
    res = nodes_counter(css_tree)
    print('Number of nodes: ', res)
    # if not error:
    coco_ast = get_coco_ast()

    print('--- Parsed CSS for sec:', (time.time() - start_time))
    print('--- Detecting violations ---')
    start_time = time.time()

    # set = temp.ToGo.get_google_set()
    # violations.ViolationsFinder.find(set, css_tree)
    violations.ViolationsFinder.find(coco_ast, css_tree)

    print('--- Detected violations for secs:', (time.time() - start_time))

main()
# cProfile.run('main()')
