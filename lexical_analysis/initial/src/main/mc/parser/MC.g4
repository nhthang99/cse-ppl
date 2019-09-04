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

program  : mctype 'main' LB RB LP body? RP EOF ;

mctype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

fragment Letter: [a-z];
fragment Digit: [0-9];
fragment Sign: '-';
fragment Dot: '.';
fragment Quote: '\'';

ID: Letter(Letter|Digit)*;

INTLIT: [0-9]+;

Float: (Digit* Dot Digit+) | (Digit+ Dot Digit*);

FloatEx: Digit+ Dot Digit+;

FLOATLIT: Float|(Digit+|FloatEx)'e'Sign?Digit+;

STRLIT: Quote ('\'\'' | ~'\'')* Quote;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
