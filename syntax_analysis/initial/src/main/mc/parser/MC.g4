grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}

program: manydcls EOF ;

manydcls: dcls manydcls | dcls;

dcls: vardcls | funcdcls;

vardcls: type idlist SM;

type: INT | FLOAT;

idlist: ID CM idlist | ID;

funcdcls: type ID paradcls body;

paradcls: LP paralist RP;

paralist: (para paratail)?;

paratail: (SM para paratail)?;

para: type idlist;

body: LB vardcl_stmt_list RB;

vardcl_stmt_list: (vardcl_stmt vardcl_stmt_list)?;

vardcl_stmt: vardcls | stmt;

stmt: stmt_type SM;

stmt_type: assign | call | return;

assign: ID EQ exp;

call: ID LP explist RP;

explist: (exp exptail)?;

exptail: (CM exp exptail)?;

return: RETURN exp;

exp
    : 
    operand
    | <assoc=left> exp (MUL | DIV) exp
    | operand SUB operand
    | <assoc=right> exp ADD exp
    ; 

operand
    : 
    INTLIT
    | FLOATLIT
    | ID
    | call
    | subexp
    ;

subexp: LP exp RP;

fragment Letter: [a-z];
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment Sign: '-';
fragment Dot: '.';
fragment Quote: '\'';

ID: Letter(Letter|Digit)*;

INTLIT: '0' | NonZeroDigit Digit*;

Float: (Digit* Dot Digit+) | (Digit+ Dot Digit*);

FloatEx: Digit+ Dot Digit+;

FLOATLIT: Float|(Digit+|FloatEx)'e'Sign?Digit+;

INT: 'int';

FLOAT: 'float';

RETURN: 'return';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SM: ';' ;

CM: ',';

EQ: '=';

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
