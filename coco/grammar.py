from plyplus import Grammar


def parse(text):
    return __g.parse(text)


__g = Grammar("""
            start: context* ;
            context : WORD '{' (rule)* '}' ;

            rule: 'require' expr+
                | 'forbid' expr+
                | 'allow' expr+
                ;

            expr: '\(' expr '\)'
                | '\(' marker+ '\)'
                | expr OR_ expr
                | marker
                ;

            marker: name (repetition)? ;

            name: WORD
                | STRING
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