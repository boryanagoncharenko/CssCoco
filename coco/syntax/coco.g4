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

type_expression : '(' parenthesis=type_expression ')'
                | operator='not' operand=type_expression
                | left=type_expression operator='and' right=type_expression
                | left=type_expression operator='or' right=type_expression
                | primary=Identifier
                ;

attr_expression : '(' attr_expression ')'
                | operator=('not'|'-'|'+') operand=attr_expression
                | left=attr_expression operator=('<'|'>'|'<='|'>='|'=='|'!=') right=attr_expression
                | left=attr_expression operator=('in'|'match'|'is') right=attr_expression
                | left=attr_expression operator='and' right=attr_expression
                | left=attr_expression operator='or' right=attr_expression
                | primary_call=api_call
                | primary_lit=list_
                | primary_str=String
                | primary_int=Integer
                | primary_id=Identifier
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