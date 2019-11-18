grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}



/*********************PARSER**********************/

program: decl+ EOF;
decl: var_decl | func_decl;
var_decl: primitive_type idlist SM;
primitive_type
    : INTTYPE
    | FLOATTYPE
    | STRTYPE
    | BOOLTYPE
    ;
idlist: id_or_arr (CM id_or_arr)*;
id_or_arr
    : ID
    | ID LSB INTLIT RSB
    ;
func_decl: func_type ID LP paralist RP block_stmt;
func_type
    : primitive_type
    | VOIDTYPE
    | primitive_type LSB RSB;
paralist: (para (CM para)*)?;
para
    : primitive_type ID
    | primitive_type ID LSB RSB
    ;
stmt
    : if_stmt
    | do_while_stmt
    | for_stmt
    | return_stmt
    | block_stmt
    | break_stmt
    | continue_stmt
    | exp SM
    ;
block_stmt: LCB (stmt | var_decl)* RCB;
if_stmt
    : IF LP exp RP
        stmt
    (ELSE
        stmt)?
    ;
do_while_stmt
    : DO stmt+
    WHILE exp SM
    ;

for_stmt
    : FOR LP exp SM exp SM exp RP
        stmt
    ;
break_stmt: BREAK SM;
continue_stmt: CONTINUE SM;
return_stmt
    : RETURN SM
    | RETURN exp SM
    ;
exp: exp1 ASSIGN exp | exp1;
exp1: exp1 OR exp2 | exp2;
exp2: exp2 AND exp3 | exp3;
exp3: exp4 (EQUAL | NOT_EQUAL) exp4 | exp4;
exp4: exp5 (LT | LE | GT | GE) exp5 | exp5;
exp5: exp5 (ADD | SUB) exp6 | exp6;
exp6: exp6 (DIV | MUL | MOD) exp7 | exp7;
exp7: (SUB | NOT) exp7 | exp8;
exp8: exp9 LSB exp RSB | exp9;
exp9: LP exp RP | operand;
operand
    : INTLIT
    | FLOATLIT
    | STRLIT
    | BOOLLIT
    | ID
    | call
    ;
call: ID LP (exp (CM exp)*)? RP;
/********************* FRAGMENTS **********************/

fragment Digit: [0-9];
fragment NonDigit: [a-zA-Z_];
fragment NonZeroDigit: [1-9];
fragment LowerCase: [a-z];
fragment UpperCase: [A-Z];
fragment Dot: '.';
fragment DoubleQuote: '"';
fragment IllegalString
    : '\\' ~[bfrnt"\\]
    | '\\'
    ;
fragment StringChar
    : ~[\b\t\f\r\n"\\]
    | EscapeSequence
    ;
fragment EscapeSequence: '\\' [bfrnt"\\];
fragment ExponentPart: [eE] '-'? Digit+;
fragment FractionalPart
    : Digit+ '.' Digit*
    | Digit* '.' Digit+
    ;

/********************* LITERALS ***********************/

INTLIT: Digit+;

FLOATLIT
    : FractionalPart ExponentPart?
    | Digit+ ExponentPart
    ;

BOOLLIT: TRUE | FALSE;

STRLIT
    : DoubleQuote ( StringChar*) DoubleQuote
    {
        result = str(self.text)
        self.text = result[1:-1]
    }
    ;
/********************** TYPES  ************************/

INTTYPE: 'int' ;
FLOATTYPE: 'float';
STRTYPE: 'string';
BOOLTYPE: 'boolean';
VOIDTYPE: 'void' ;

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

/********************** COMMENT ***********************/

LINE_CMT
    : '//' ~[\r\n]*
    -> skip
    ;

BLOCK_CMT
    : '/*' .*? '*/'
    -> skip
    ;

/******************** IDENTIFIERS *********************/

ID
    : NonDigit (NonDigit | Digit)*
    ;

/******************** SEPARATORS **********************/

LP: '(' ;
RP: ')' ;

LCB: '{';
RCB: '}';

LSB: '[';
RSB: ']';

SM: ';' ;
CM: ',';

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

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING
    : DoubleQuote StringChar* ([\b\t\f\n\r"\\] | EOF)
    {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    }
    ;

ILLEGAL_ESCAPE
    : DoubleQuote StringChar* IllegalString
    {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    }
    ;

ERROR_CHAR
    : .
    {
        raise ErrorToken(self.text)
    }
;