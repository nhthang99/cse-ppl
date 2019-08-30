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

fragment NonDigit: [a-zA-Z_];

fragment NonZeroDigit: [1-9];

fragment LowerCase: [a-z];

fragment UpperCase: [A-Z];

fragment Dash: '_';

fragment Dot: '.';

fragment DoubleQuote: '"';

fragment ExponentPart: [eE] '-'? Digit+;

fragment FractionalPart
    : Digit+ '.' Digit*
    | Digit* '.' Digit+
    ;

/********************** TYPES  ************************/

INTTYPE: 'int' ;

FLOATTYPE: 'float';

STRTYPE: 'string';

BOOLTYPE: 'boolean';

VOIDTYPE: 'void' ;

fragment PrimitiveTypes
    : INTTYPE
    | FLOATTYPE
    | STRTYPE
    | BOOLTYPE
    | VOIDTYPE
    ;

/********************* KEY WORDS **********************/

BREAK: 'break';

CONTINUE: 'continue';

ELSE: 'else';

FOR: 'for';

IF: 'if';

RETURN: 'return';

DO: 'do';

WHILE: 'while';

TRUE: 'true';

FALSE: 'false';

/******************** IDENTIFIERS *********************/

ID
    : NonDigit (NonDigit | Digit)*
    ;

/********************** COMMENT ***********************/

LINE_CMT
    : '//' ~[\r\n]*
    -> skip
    ;

BLOCK_CMT
    : '/*' .*? '*/'
    -> skip
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

BOOLLIT
    : TRUE
    | FALSE
    ;

STRLIT
    : DoubleQuote ~'"' DoubleQuote
    ;

/******************** SEPARATORS **********************/

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

LSB: '[';

RSB: ']';

SEMI: ';' ;

COMMA: ',';

/********************* OPERATORS **********************/

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

MOD: '%';

NOT: '!';

OR: '||';

AND: '&&';

NOT_EQUAL: '!=';

EQUAL: '==';

LT: '<';

GT: '>';

LE: '<=';

GE: '>=';

ASSIGN: '=';

/*********************** SKIP *************************/

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
