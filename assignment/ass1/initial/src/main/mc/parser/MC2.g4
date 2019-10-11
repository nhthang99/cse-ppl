grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : declaration+;
declaration: var_decla | func_decla;
var_decla: primi_type var_list SM;
var_list: variable var_tail;
var_tail: (CM variable var_tail)?;
variable: ID | identifier;
identifier: ID LSB INTLIT RSB;
primi_type: INTTYPE | FLOATTYPE | STRINGTYPE | BOOLEANTYPE;

func_decla: mctype ID LB para_list RB block_statement;
mctype: primi_type | VOIDTYPE | arr_point_type;
arr_point_type: primi_type LSB RSB;
para_list: (parameter para_tail)?;
para_tail: (CM parameter para_tail)?;
parameter: primi_type ID | primi_type ID LSB RSB;

block_statement: LP body_list RP;
body_list: (body body_list)?;
body: var_decla | statement;
statement: if_statement
    | do_while_statement SM
    | for_statement 
    | break_statement SM
    | countinue_statement SM
    | return_statement SM
    | expression SM
    | block_statement
    ; 
if_statement: IF LB expression RB statement (ELSE statement)?;
do_while_statement: DO statement* WHILE expression ;
for_statement: FOR LB expression SM expression SM expression RB statement;
break_statement: BREAK;
countinue_statement: COUNTINUE;
return_statement: RETURN expression?;

expression: expr | index_expr | invol_expr;
index_expr: (ID | invol_expr) LSB expression RSB ;
invol_expr: ID LB expr_list RB;
expr_list: (expression expr_tail)?;
expr_tail: (CM expression expr_tail)?;
expr: exp1 ASSIGN expr | exp1;
exp1: exp1 OR exp2 | exp2;
exp2: exp2 AND exp3 | exp3;
exp3: exp4 EQUAL exp4 | exp4 N_EQUAL exp4 | exp4;
exp4: exp5 LESS exp5 | exp5 LESS_EQUAL exp5 | exp5 GREAT exp5 | exp5 GREAT_EQUAL exp5 | exp5;
exp5: exp5 ADD exp6 | exp5 SUB exp6 | exp6;
exp6: exp6 DIV exp7 | exp6 MUL exp7 | exp6 MOD exp7 | exp7;
exp7: SUB (exp7 | exp8) | NOT (exp7 | exp8) | exp8;
exp8: (ID | invol_expr)LSB RSB | exp9;
exp9: LB expr RB | INTLIT | bool_lit | STRING | FLOATLIT | ID | index_expr | invol_expr;
 

INTTYPE: 'int' ;
VOIDTYPE: 'void' ;
BOOLEANTYPE: 'boolean';
STRINGTYPE: 'string';
FLOATTYPE: 'float';
BREAK: 'break';
COUNTINUE : 'countinue';
RETURN : 'return';
IF: 'if';
ELSE: 'else' ;
DO: 'do';
WHILE: 'while';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';

BLOCKCOMMENT: '/*' .* '*/' -> skip;
ALINECOMMENT: '//' ~[\n]* -> skip;

ID: [a-zA-Z_][a-z0-9A-Z_]*;

fragment ILLEGAL: '\\'[btrnf"\\];
fragment NILLEGAL: '\\'~[btnrf"\\];
STRING: '"' (~["\\]|ILLEGAL)* '"' {self.text = self.text[1:len(self.text)-1]};

INTLIT: [0-9]+;

bool_lit: TRUE | FALSE;

fragment NUMBER: [0-9];
fragment EXPONENT: [eE] '-'? [0-9]+;
FLOATLIT: NUMBER* '.' NUMBER+ EXPONENT | NUMBER+ EXPONENT | NUMBER+ '.' NUMBER* | NUMBER* '.' NUMBER+;

LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
OR: '||';
AND: '&&';
N_EQUAL: '!=';
EQUAL: '==';
ASSIGN: '=';
LESS: '<' ;
LESS_EQUAL: '<=';
GREAT: '>';
GREAT_EQUAL: '>=';

SM: ';';
CM : ',';
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: '"' (~["\\]|ILLEGAL)* ;
ILLEGAL_ESCAPE: '"' (~["\\]|ILLEGAL)*NILLEGAL ;