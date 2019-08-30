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

/********************* FRAGMENTS **********************/

fragment Digit: [0-9];

fragment NonZeroDigit: [1-9];

fragment LowerCase: [a-z];

fragment UpperCase: [A-Z];

fragment Dash: '_';

fragment Dot: '.';

fragment ExponentPart: [eE] '-'? Digit+;

fragment
FractionalPart
    : Digit+ '.' Digit*
    | Digit* '.' Digit+
    ;

/********************** TYPES  ************************/

INTTYPE: 'int' ;

FLOATTYPE: 'float';

STRTYPE: 'string';

BOOLTYPE: 'boolean';

VOIDTYPE: 'void' ;

/********************* KEY WORDS **********************/

/******************** IDENTIFIERS *********************/

ID
    : 
    (LowerCase | UpperCase | Dash)
    (LowerCase | UpperCase | Digit | Dash)*
    ;

/********************* LITERALS ***********************/

INTLIT
    : '0' 
    | NonZeroDigit Digit*
    ;

FLOATLIT
    : FractionalPart ExponentPart?
    | Digit+ ExponentPart
    ;


/******************** SEPARATORS **********************/

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

LSB: '[';

RSB: ']';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
