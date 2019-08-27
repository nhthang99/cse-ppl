grammar MC;

@lexer::header {
// 1713239
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

mctype: INTTYPE | VOIDTYPE | FLOATTYPE | BOOLTYPE | ;

body: funcall SEMI COMMA;

exp: funcall | INTLIT | FLOATLIT | BOOLLIT | VOIDLIT;

funcall: ID LB exp? RB ;

/*========================= COMMENTS ============================*/



/*====================== PRIMITIVE TYPES  =======================*/

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

FLOATTYPE: 'float' ;

BOOLTYPE: 'boolean';

/*========================= IDENTIFIER ==========================*/

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

/*========================= LIMIT VALUE =========================*/

INTLIT: [+-]?[0-9]+;

FLOATLIT: ([0-9]*\.?[0-9]+[eE][+-]?[0-9]+)|([+-]?([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+));

BOOLLIT: true|false;

VOIDLIT: '';

/*========================== SEPARATORS =========================*/

LB: '(';

RB: ')';

LP: '{';

RP: '}';

LSB: '[';

RSB: ']';

SEMI: ';';

COMMA: ',';

/*====================== ESCAPE SEQUENCES ======================*/

/* Skip following characters:
   - backspace
   - formfeed
   - double quote
   - backslash
   - spaces
   - tabs
   - newlines
*/

WS : [ \b\f\"\\\t\r\n]+ -> skip; 

/*======================== OPERATORS =========================*/

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
ASSIGN: '=';
EQUAL: '==';
NOTEQUAL: '!=';
NOT: '!';
OR: '||';
AND: '&&';

/*======================== ERROR ===============================*/

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
