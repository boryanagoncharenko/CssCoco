from plyplus import Grammar


def parse(text):
    return __g.parse(text)


__g = Grammar("""
            start: context* ;
            context : WORD '{' (rule)* '}' ;

            rule: 'require' (css_marker | ws_marker) ((css_marker)? (ws_marker)?)*
                | 'allow' (css_marker | ws_marker) ((css_marker)? (ws_marker)?)*
                ;

            css_marker: css_keyword ;

            ws_marker: ws_keyword (repetition)? ;

            css_keyword: 'rule'
                | 'declaration'
                | 'selector'
                | 'block'
                | 'property'
                | 'value'
                | 'eof_'
                | STRING
                ;

            ws_keyword: 'whitespace_'
                | 'newline'
                | 'tab_'
                | 'space'
                ;

            repetition: '{' NUMBER '}'
                | '{' '\*' '}'
                ;

            WORD: '\w+' ;
            STRING: '"' '[^"]*' '"' ;
            NUMBER: '[1-9][0-9]*' ;
            COMMENT: '\/\*[.\s]*\*\/' (%ignore) ;
            SPACES: '[ \t\n]+' (%ignore) ;
            """, auto_filter_tokens=False)