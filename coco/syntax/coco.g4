grammar coco;

stylesheet : context* ;

context : name=Identifier '{' declaration* '}' ;

declaration : convention
            ;

convention : 'forbid' target=pattern msg=message
           | 'require' requirement=attr_expression msg=message
           | 'find' target=pattern 'require' requirement=attr_expression msg=message
           ;

pattern : semantic=node ((relation='in' node)* | (relation='next-to' node)*)
        ;

node : (decl=Identifier '=')? abstract=abstract_node
     | parse=parse_node
     ;



parse_node  : operand=parse_node ('or' right=parse_node)+
            | primary=Identifier quantifier=repeater
            | primary=Identifier
            ;

type_expression : '(' parenthesis=type_expression ')'
                | operator='not' operand=type_expression
                | left=type_expression operator='and' right=type_expression
                | left=type_expression operator='or' right=type_expression
                | primary=Identifier repeater
                | primary=Identifier
                ;

attr_expression : '(' parenthesis=attr_expression ')'
                | operator=('not'|'-'|'+') operand=attr_expression
                | left=attr_expression operator=('<'|'>'|'<='|'>='|'=='|'!=') right=attr_expression
                | left=attr_expression operator=('in'|'not in'|'match'|'not match'|'is') right=attr_expression
                | operand=attr_expression '.' call=Identifier ('(' (argument=attr_expression|abstract=abstract_node ) ')')?
                | query=query_expression
                | left=attr_expression operator='and' right=attr_expression
                | left=attr_expression operator='or' right=attr_expression
                | primary_list=list_
                | primary_str=String
                | primary_int=Integer
                | primary_call=Identifier '(' (argument=attr_expression|abstract=abstract_node ) ')'
                | primary_id=Identifier
                ;

logic_expr : '(' parenthesis=logic_expr ')'
           | left=CALL operator='is' right=(just leave it as Identifier)(abstract_node)
           | operator='not' operand=logic_expr
           | left=logic_expr operator='and' right=logic_expr
           | left=logic_expr operator='or' right=logic_expr
           | type_expr
           | calls_expr
           ;

type_expr : left=whitespace_node operator='before' right=VARIABLE or abstract_node
          | left=whitespace_node operator='after' right=VARIABLE or abstract_node
          | left=whitespace_node operator='between' first=VARIABLE or abstract_node 'and' second=VARIABLE or abstract_node
          ;

calls_expr : operator=('-'|'+') operand=attr_expression
           | left=attr_expression operator=('<'|'>'|'<='|'>='|'=='|'!=') right=attr_expression
           | left=attr_expression operator=('in'|'not in'|'match'|'not match') right=attr_expression
           | primary=call_expression
           | primary_int=Integer
           | primary_str=String
           | primary_list=list_
           ;

call_expression : operand=attr_expression '.' call=Identifier ('(' (argument=attr_expression|abstract=abstract_node ) ')')?
                | call=Identifier ('(' (argument=attr_expression|abstract=abstract_node ) ')')?
                ;

abstract_node : node_type=type_expression ('{' constraint=attr_expression '}')?;
whitespace_node : Identifier repeater (or)


query_expression : left=parse_node operator='before' right=whitespace_argument
                 | left=parse_node operator='after' right=whitespace_argument
                 | left=parse_node operator='between' first=whitespace_argument 'and' second=whitespace_argument
                 ;

whitespace_argument : abstract=abstract_node
                    | call=call_expression
                    ;

repeater : '{' (exact=Integer |(lower=Integer ',' upper=Integer) |(',' upper=Integer) |(lower=Integer ',')) '}' ;


message : 'message' String ;

convention_group : '{' convention+ '}' ;

api_call : Identifier ('.' api_call)* ;

method_call : method_name=Identifier ('(' (attr_expression)? ')')? ;

list_ : '[' list_element (',' list_element)* ']' ;

list_element : element_int=Integer
             | element_str=String
             | element_desc=abstract_node
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