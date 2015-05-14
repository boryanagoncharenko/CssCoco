from plyplus import Grammar


class Parser(object):

    _grammar = """
        start: context* ;
        context : WORD '{' (rule)* '}' ;

        rule: (REQUIRE | FORBID | ALLOW) expr+ ;

        expr: '\(' expr '\)'
            | '\(' marker+ '\)'
            | expr OR expr
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
        WORD: '[a-zA-Z]+' (%unless
            OR: 'or' ;
            REQUIRE: 'require' ;
            FORBID: 'forbid' ;
            ALLOW: 'allow' ;
            MESSAGE: 'message' ;
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
