from plyplus import Grammar


class Parser(object):

    _grammar = """

        start: statement* ;

        statement: convention
                 | convention_group
                 | repeater
                 ;

        convention: find_clause (REQUIRE|FORBID) constraint except_clause?
                  | (REQUIRE|FORBID) pattern except_clause?
                  ;

        convention_group: L_CURLY convention+ R_CURLY except_clause;

        repeater: FOR ;

        find_clause: FIND pattern;

        pattern: assignment? node (IN assignment? node)* ;

        node: type_expr attr_expr? ;

        type_expr: L_PAREN type_expr R_PAREN
                 | NOT type_expr
                 | type_expr AND type_expr
                 | type_expr OR type_expr
                 | WORD
                 ;

        constraint: attr_expr
                  ;

        except_clause: EXCEPT convention ;

        assignment: WORD '\=' ;

        attr_expr: '\(' attr_expr '\)'
                 | NOT attr_expr
                 | attr_expr AND attr_expr
                 | attr_expr OR attr_expr
                 | attr_expr ('<'|'<='|'>'|'>='|'!='|'==') attr_expr
                 | attr_expr IS node
                 | attr_expr MATCH STRING
                 | attr_expr '\.' WORD ('\(' node? '\)')?
                 | WORD
                 | NUMBER
                 ;

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
        L_CURLY: '{' ;
        R_CURLY: '}' ;
        WORD: '[a-zA-Z\-]+' (%unless
            ALLOW: '(?i)allow' ;
            AND: '(?i)and' ;
            EXCEPT: '(?i)except' ;
            FIND: '(?i)find' ;
            FOR: '(?i)for' ;
            FORBID: '(?i)forbid' ;
            IF: '(?i)if' ;
            IGNORE: '(?i)ignore' ;
            IN: '(?i)in';
            IS: '(?i)is';
            LOWERCASE: '(?i)lowercase' ;
            MATCH: '(?i)match' ;
            MESSAGE: '(?i)message' ;
            NOT: '(?i)not' ;
            OR: '(?i)or' ;
            REQUIRE: '(?i)require' ;
            TARGET: '(?i)target' ;
            UPPERCASE: '(?i)uppercase' ;
            WHERE: '(?i)where' ;
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
