grammar coco;

stylesheet : context* ;

context : name=Identifier '{' declaration* '}' ;

declaration : convention
            ;

convention : 'forbid' target=pattern 'message' message=String
           | 'require' requirement=logic_expr 'message' message=String
           | 'find' target=pattern 'require' requirement=logic_expr 'message' message=String
           ;

pattern : node_declaration (relation=('in'|'next-to') node_declaration)*
        ;

node_declaration : (variable=Identifier '=')? node=semantic_node ;

semantic_node : node_type=type_expression ('{' constraint=logic_expr '}')? ;

type_expression : '(' parenthesis=type_expression ')'
                | operator='not' operand=type_expression
                | left=type_expression operator='and' right=type_expression
                | left=type_expression operator='or' right=type_expression
                | primary=Identifier
                ;

whitespace_variation : whitespace_node ('or' whitespace_node)* ;

whitespace_node : node_type=Identifier ('{' quantifier=repeater '}')? ;

logic_expr : '(' parenthesis=logic_expr ')'
           | operand=calls_expr operator='is' node_type=Identifier/*(node)*/
           | operator='not' operand=logic_expr
           | left=logic_expr operator='and' right=logic_expr
           | left=logic_expr operator='or' right=logic_expr
           | primary_type=type_expr
           | primary_call=calls_expr
           ;

type_expr : variation=whitespace_variation operator='before' (variable=Identifier | operand=semantic_node)
          | variation=whitespace_variation operator='after' (variable=Identifier | operand=semantic_node)
          | variation=whitespace_variation operator='between' (variable=Identifier | operand=semantic_node)
            'and' (second_variable=Identifier | second_operand=semantic_node)
          ;

calls_expr : operator='-' operand=calls_expr
           | left=calls_expr operator=('<'|'>'|'<='|'>='|'=='|'!=') right=calls_expr
           | left=calls_expr operator=('in'|'not in'|'match'|'not match') right=calls_expr
           | primary_call=call_expression
           | primary_int=Integer
           | primary_str=String
           | primary_list=list_
           ;

call_expression : operand=call_expression '.' call=Identifier ('(' (argument=calls_expr|abstract=semantic_node ) ')')?
                | call=Identifier ('(' (argument=calls_expr|abstract=semantic_node ) ')')?
                ;

repeater : exact=Integer
         | lower=Integer ',' upper=Integer
         | ',' upper=Integer
         | lower=Integer ','
         ;

convention_group : '{' convention+ '}' ;

list_ : '[' list_element (',' list_element)* ']' ;

list_element : element_int=Integer
             | element_str=String
             | element_desc=semantic_node
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