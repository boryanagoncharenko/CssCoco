grammar coco;

start_rule : Word+ ;

Word : [a-z]+ ;

Comment : '/*' .*? '*/' -> skip ;

LineComment : '//' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;