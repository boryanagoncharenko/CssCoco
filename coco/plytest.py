import coco.ast as ast
import coco.analysis as analysis
from plyplus import Grammar

list_parser = Grammar("""
        start: context* ;
        context : WORD '{' (rule)* '}' ;

        rule: 'require' (css_marker | space_marker) ((css_marker)? (space_marker)?)*
            | 'allow' (css_marker | space_marker) ((css_marker)? (space_marker)?)*
            ;

        css_marker: 'rule'
            | 'declaration'
            | 'selector'
            | 'block'
            | 'property'
            | 'value'
            | 'eof'
            | STRING
            ;

        space_marker: 'newline'
            | 'tab_'
            | 'space'
            ;

        WORD: '\w+' ;
        STRING: '"' '[^"]*' '"' ;
        SPACES: '[\s\t\n]+' (%ignore) ;
        """, auto_filter_tokens=False)

res = list_parser.parse("Whitespace { require tab_ tab_ rule space space rule tab_ newline rule newline newline}")

print(res.select('context'))

tree = ast.AstBuilder.build(res)
print(tree.pretty_print())

print(analysis.Evaluator.evaluate(tree))

