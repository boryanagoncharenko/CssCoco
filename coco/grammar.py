from plyplus import Grammar


def parse(text):
    return __g.parse(text)


__g = Grammar("""
            start: context* ;
            context : WORD '{' (rule)* '}' ;

            rule: 'require' (css_marker | ws_expr) (css_marker? ws_expr?)*
                | 'allow' (css_marker | ws_expr) (css_marker? ws_expr?)*
                ;

            ws_expr: ws_marker OR_ ws_marker
                | ws_marker
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
                | 'comment'
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

            OR_: 'orrr';
            L_PAREN: '\(' ;
            R_PAREN: '\)' ;
            WORD: '\w+' ;
            STRING: '"' '[^"]*' '"' ;
            NUMBER: '[1-9][0-9]*' ;
            COMMENT: '\/\*[\S\s]*\*\/' (%ignore) ;
            SPACES: '[ \t\n]+' (%ignore) ;
            """, auto_filter_tokens=False)



            # ws_expr: L_PAREN ws_expr R_PAREN
            #     | L_PAREN ws_marker+ R_PAREN
            #     | ws_expr OR_ ws_expr
            #     | ws_marker
            #     ;