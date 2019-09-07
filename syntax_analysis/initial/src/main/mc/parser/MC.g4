grammar MC;

options{
	language=Java;
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

stmt: assign SM | call SM | return_t SM;

assign: ID EQ exp;

call: ID LP explist RP;

explist: (exp exptail)?;

exptail: (CM exp exptail)?;

return_t: RETURN exp;

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

fragment NonDigit: [a-zA-Z_];
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment Sign: '-';
fragment Dot: '.';
fragment Quote: '\'';

ID: NonDigit(NonDigit|Digit)*;

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
