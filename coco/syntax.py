from plyplus import Grammar


class Parser(object):

    _grammar = """
        start: rule* ;

        rule: if_rule
            | whitespace_rule
            ;

        if_rule: IF selector (WHERE req_expr)? (REQUIRE | FORBID | ALLOW) req_expr ;

        selector: marker '>' selector
                | marker
                ;

        req_expr: '\(' req_expr '\)'
                | req_expr MATCH (STRING | UPPERCASE | LOWERCASE)
                | req_expr '=' req_expr
                | req_expr IN list
                | req_expr NOT IN list
                | NOT req_expr
                | req_expr AND req_expr
                | req_atom
                ;

        list: '\[' STRING (',' STRING)* '\]' ;

        req_atom: marker ('\.' WORD)+ ;

        whitespace_rule: (REQUIRE | FORBID | ALLOW) sequence+ ;

        sequence: '\(' sequence '\)'
                | '\(' marker+ '\)'
                | sequence OR sequence
                | marker
                ;

        marker: name (repetition)? ;

        name: WORD
            | STRING
            ;

        repetition: '{' NUMBER '}'
            | '{' '\*' '}'
            ;

        L_PAREN: '\(' ;
        R_PAREN: '\)' ;
        WORD: '[a-zA-Z\-]+' (%unless
            IN: 'in';
            IF: 'if' ;
            OR: 'or' ;
            NOT: 'not' ;
            AND: 'and' ;
            TARGET: 'target' ;
            IGNORE: 'ignore' ;
            WHERE: 'where' ;
            REQUIRE: 'require' ;
            FORBID: 'forbid' ;
            ALLOW: 'allow' ;
            MESSAGE: 'message' ;
            MATCH: 'match' ;
            UPPERCASE: 'uppercase' ;
            LOWERCASE: 'lowercase' ;
        );
        STRING: '"' '[^"]*' '"' ;
        NUMBER: '[1-9][0-9]*' ;
        COMMENT: '\/\*[\S\s]*\*\/' (%ignore) ;
        SPACES: '[ \t\n]+' (%ignore) ;
        """

    _parser = Grammar(_grammar, auto_filter_tokens = False)

    @staticmethod
    def parse(text):
        return Parser._parser.parse(text)
