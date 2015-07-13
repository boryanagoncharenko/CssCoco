grammar coco;

stylesheet : context* ;

context : name=Identifier '{' declaration* '}' ;

declaration : convention
            ;

convention : 'forbid' target=pattern msg=message
           | 'find' target=pattern 'require' requirement=attr_expression msg=message
           ;

pattern : node ('in' node)*
        ;

node : (Identifier '=')? type_expression (constraint)?;

node_descriptor : type_expression (constraint)? ;

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
                | left=attr_expression operator=('in'|'match') right=attr_expression
                | left=attr_expression operator='is' right=type_expression
                | call=call_expression
                | left=attr_expression operator='and' right=attr_expression
                | left=attr_expression operator='or' right=attr_expression
                | primary_list=list_
                | primary_str=String
                | primary_int=Integer
                ;

call_expression : operand=call_expression '.' call=Identifier ('(' (argument=attr_expression|argument2=node_descriptor ) ')')?
                | call=Identifier ('(' (argument=attr_expression|argument2=node_descriptor ) ')')?
                ;

message : 'message' String ;

convention_group : '{' convention+ '}' ;

api_call : Identifier ('.' api_call)* ;

method_call : method_name=Identifier ('(' (attr_expression)? ')')? ;

list_ : '[' list_element (',' list_element)* ']' ;

list_element : element_int=Integer
             | element_str=String
             | element_desc=type_expression (constraint)?
             | element_id=Identifier
             ;

fragment EscapeSequence : '\\' ['] ;

fragment Letter : [a-zA-Z] ;

fragment Digit : ZeroDigit | NonZeroDigit ;

fragment NonZeroDigit : [1-9] ;

fragment ZeroDigit : [0] ;

Identifier : (Letter)(Letter|Digit|'_'|'-')* ;

Integer : (ZeroDigit | NonZeroDigit Digit*) ;

String : ['] ( EscapeSequence | ~['] )*? ['] ;

Comment : '/*' .*? '*/' -> skip ;

LineComment : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;