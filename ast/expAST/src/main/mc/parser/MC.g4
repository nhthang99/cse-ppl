grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
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

exp: term COMPARE term | term ; // COMPARE is none-association

term: factor EXPONENT term | factor ; 

factor: operand (ANDOR operand)* ; // ANDOR is left-association

operand: INTLIT | BOOLIT | LB exp RB ;

BOOLIT: 'true' | 'false' ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

COMPARE: '<' | '>' | '>=' | '<=' | '==' | '!=' ;

EXPONENT: '^';

ANDOR: '&&' | '||' ;

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;