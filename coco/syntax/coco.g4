grammar coco;

stylesheet : context* ;

context : name=Identifier '{' declaration* '}' ;

declaration : convention
            ;

convention : 'forbid' pattern
           ;

pattern : node
        ;

node : (Identifier '=')? type_expression (constraint)?;

constraint : '{' attr_expression '}' ;

type_expression : '(' type_expression ')'
                | 'not' type_expression
                | type_expression 'or' type_expression
                | Identifier
                ;

attr_expression : '(' attr_expression ')'
                | op=('not'|'-'|'+') operand=attr_expression
                | left=attr_expression op=('<'|'>'|'<='|'>='|'=='|'!=') right=attr_expression
                | left=attr_expression op=('in'|'match'|'is') right=attr_expression
                | left=attr_expression 'and' right=attr_expression
                | left=attr_expression 'or' right=attr_expression
                | primary_rule=node
                | primary_rule=api_call
                | primary_rule=list_
                | primary=String
                | primary=Integer
                | primary=Identifier
                ;

convention_group : '{' convention+ '}' ;

api_call : (Identifier '.')? method_call ('.' method_call)* ;

method_call : Identifier '(' (attr_expression)? ')' ;

list_ : '[' list_element (',' list_element)* ']' ;

list_element : Integer
             | String
             | Identifier
             ;

fragment StringCharacter : EscapeSequence | ~[\\] ;

fragment Quote : ['] ;

fragment EscapeSequence : '\\' Quote ;

fragment Letter : [a-zA-Z] ;

fragment Digit : ZeroDigit|NonZeroDigit ;

fragment NonZeroDigit : [1-9] ;

fragment ZeroDigit : [0] ;


Identifier : (Letter)(Letter|Digit|'_'|'-')* ;

Integer : (ZeroDigit | NonZeroDigit Digit*) ;

String : Quote StringCharacter*? Quote ;

Comment : '/*' .*? '*/' -> skip ;

LineComment : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;