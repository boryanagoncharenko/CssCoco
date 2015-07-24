grammar coco;

stylesheet : context* ;

context : name=Identifier (ignore=ignore_clause)? '{' convention* '}' ;

convention : action='forbid' target=pattern 'message' message=String
           | action='require' requirement=logic_expr 'message' message=String
           | find='find' target=pattern
             ('where' where=logic_expr)?
             action=('require'|'forbid') requirement=logic_expr
             'message' message=String
           ;

pattern : simple=node_declaration (relation=('in'|'next-to') node_declaration)*
        | fork=fork_pattern (relation='in' node_declaration)*
        ;

fork_pattern : '(' node_declaration (',' node_declaration)+ ')' ;

node_declaration : (variable=Identifier '=')? node=semantic_node ;

semantic_node : type_=node_type ('{' constraint=logic_expr '}')? ;

node_type : '(' parenthesis=node_type ')'
          | operator='not' operand=node_type
          | left=node_type operator='and' right=node_type
          | left=node_type operator='or' right=node_type
          | primary=Identifier
          ;

whitespace_variation : whitespace_node ('or' whitespace_node)* ;

whitespace_node : type_=Identifier ('{' quantifier=repeater '}')? ;

logic_expr : '(' parenthesis=logic_expr ')'
           | operator='not' operand=logic_expr
           | left=logic_expr operator='and' right=logic_expr
           | left=logic_expr operator='or' right=logic_expr
           | type_=type_expr
           | call=arithmetic_expr
           ;

type_expr : operand=arithmetic_expr operator='is' type_=Identifier/*(node)*/
          | variation=whitespace_variation operator=('before'|'after') operand=call_expr
          | variation=whitespace_variation operator='between' operand=call_expr 'and' second_operand=call_expr
          ;

arithmetic_expr : operator='-' operand=arithmetic_expr
                | left=arithmetic_expr operator=('<'|'>'|'<='|'>='|'=='|'!=') right=arithmetic_expr
                | left=arithmetic_expr operator=('in'|'not in'|'match'|'not match') right=arithmetic_expr
                | call=call_expr
                | primary=element
                ;

basic_expr : operator='-' operand=arithmetic_expr
           | primary=element
           ;

element : primary_bool=Boolean
        | primary_int=Integer
        | primary_str=String
        | primary_list=list_
        ;

call_expr : operand=call_expr '.' call=Identifier ('(' (argument=basic_expr | abstract=semantic_node ) ')')?
          | call=Identifier ('(' (argument=basic_expr | abstract=semantic_node ) ')')?
          ;

repeater : exact=Integer
         | lower=Integer ',' upper=Integer
         | ',' upper=Integer
         | lower=Integer ','
         ;

ignore_clause : 'ignore' (whitespace_node)+ (',' (whitespace_node)+)* ;

list_ : '[' list_element (',' list_element)* ']' ;

list_element : element_int=Integer
             | element_str=String
             | element_desc=semantic_node
             ;

fragment EscapeSequence : '\\' ['] ;

fragment Letter : [a-zA-Z] ;

fragment Digit : ZeroDigit | NonZeroDigit ;

fragment NonZeroDigit : [1-9] ;

fragment ZeroDigit : [0] ;

Boolean : 'true' | 'True' | 'false' | 'False' ;

Identifier : (Letter)(Letter|Digit|'_'|'-')* ;

Integer : (ZeroDigit | NonZeroDigit Digit*) ;

String : ['] ( EscapeSequence | ~['] )*? ['] ;

Comment : '/*' .*? '*/' -> skip ;

LineComment : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;