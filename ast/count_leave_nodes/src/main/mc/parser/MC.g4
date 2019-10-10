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

program: vardecls EOF;

vardecls: vardecl vardecls | vardecl ;

vardecl: mctype ids SEMI ;

mctype: INTTYPE | FLOATTYPE | ARRAY LB INTLIT RB OF mctype ;

ids: ID (COMMA ID)* ;

ARRAY: 'array';

OF: 'of';

INTTYPE: 'int' ;

FLOATTYPE: 'float' ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '[' ;

RB: ']' ;

COMMA: ',';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;