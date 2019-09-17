import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple(self):
        """A simple program"""
        input = """ int main () {} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_function_declare(self):
        """A program with a function declaration"""
        input = """int main () { pow(2,3); }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_funcs(self):
        """A program with 2 functions"""
        input = """void main () {}
int foo() {}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_function_nested(self):
        """2 functions nested"""
        input = """void foo() {
            int child(){}
}
"""
        expect = "Error on line 2 col 21: ("
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_vardecl(self):
        """Function with a variable declaration"""
        input = """void main(){
         int x;
         }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_complete(self):
        """A complete function"""
        input = """int double(int x){
    int a;
    a = a * a;
    return a ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_main_func(self):
        """Main function cannot have any parameter"""
        input = """void main (int a) {}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))
    # TODO: Main function cannot have any parameter

    def test_without_func(self):
        """Program without function"""
        input = """int a;
int x;
x = a + 9;
"""
        expect = "Error on line 3 col 0: x"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_parameters(self):
        """Function has many parameters"""
        input = """int foo(int a, int b) {}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_return(self):
        """Function return nothing with void type in return"""
        input = """void main ( ) {return ;}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))



    def test_return_void(self):
        """Function return nothing without void type return - compile-time error"""
        input = """int main ( ) {return ;}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))
    # TODO: Function return nothing

    def test_no_block(self):
        """Function has no block statement"""
        input = """void main ()
"""
        expect = "Error on line 2 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_no_func_name(self):
        """Function has no function name"""
        input = """int () {}
"""
        expect = "Error on line 1 col 4: ("
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_no_param(self):
        """Function has no parameter list"""
        input = """int void {}
"""
        expect = "Error on line 1 col 4: void"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_no_return_type(self):
        """Function has no function return type"""
        input = """main(){}
"""
        expect = "Error on line 1 col 0: main"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_vardecl_semi(self):
        """Variable declarations without semicolon"""
        input = """int a;
         int b
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_block_stmt(self):
        """A lonely block statement"""
        input = """{
    boolean alone;
    alone = true;
}
"""
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
    # TODO: can a block statement alone?

    def test_variables(self):
        """Variable declaration - many variable"""
        input = """int a, b, c;
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_array(self):
        """Variable declaration - an array with the size"""
        input = """int arr[3];
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_wrong_type(self):
        """Variable declaration - wrong primitive type"""
        input = """void a, b, c;
"""
        expect = "Error on line 1 col 6: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_array_without_size(self):
        """Variable declaration - an array without the size"""
        input = """float arr[];
"""
        expect = "Error on line 1 col 10: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_string_init(self):
        """Variable declaration with variable initialization"""
        input = """string str = "hello world";
"""
        expect = "Error on line 1 col 11: ="
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_global(self):
        """Global scope"""
        input = """int str;
void main() {
        str = "hello world";
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_2_dim_array(self):
        """Variable declaration - an 2-dimension array"""
        input = """int arr[1][2];
"""
        expect = "Error on line 1 col 10: ["
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_stmt_block(self):
        """Statement outside of a block - does not recognize"""
        input = """int str;
void main() {
    str = "hello word";
}
    str = str + 1;
"""
        expect = "Error on line 5 col 4: str"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_block_decl(self):
        """Block statement only has declarations"""
        input = """int main(){
  int x, y;
  string str;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_block_stmt_only(self):
        """Block statement only has statements"""
        input = """int main(){
    str = "hello world";
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

        # 228

    def test_multi_param(self):
        """Parameter list has 2 type of parameter declarations"""
        input = """void main(float a,int x[]) {}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_comments(self):
        """Function with comments"""
        input = """// Begin
    int main() {
    /* code here */
    int x;
    // end
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_parenthesis(self):
        """Function missed parenthesis"""
        input = """void main() {

"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_literal_list(self):
        """List of literal"""
        input = """void main() {
    //declaration
    int a;
    float b;
    string c;
    boolean d;
    //statements
    a = 69;
    b = - 6.9e96;
    c = "this is a";
    d = false;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_exp_assign(self):
        """Expression list - assign"""
        input = """void main () {
    int a, b;
    a = b;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_exp_add(self):
        """Expression list - add sub"""
        input = """void main () {
    int a, b;
    float c;
    c = a - b;
    c = c + a;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_exp_mul(self):
        """Expression list - mul div mod"""
        input = """void main () {
    int a, b, c;
    a = b * c;
    c = a / b;
    b = c % a;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_exp_negative(self):
        """Expression list - negative literal"""
        input = """void main () {
    int a;
    boolean x;
    a = -69;
    x = !true;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_exp_precedence(self):
        """Expression list - precedence"""
        input = """void main () {
    int a;
    a = 6 + (4 - 2 * (3 + 7) / 4);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_exp_bracket(self):
        """Expression list - precedence without bracket"""
        input = """void main () {
    int a;
    a = 5 + 3 * 2 - 8 / 4 % 2;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_wrong(self):
        """Wrong program"""
        input = """} int main {
"""
        expect = "Error on line 1 col 0: }"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_var_decl_semi(self):
        """Variable declaration without semicolon in the end of the declaration"""
        input = """void main(){
    int x
}
"""
        expect = "Error on line 3 col 0: }"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_array_pointer(self):
        """Array pointer return function"""
        input = """int[] foo(int a[]) {
    return a;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_var_decl_array_pointer(self):
        """Variable declaration cannot take array pointer type"""
        input = """int[] foo() {
    int a[];
}
"""
        expect = "Error on line 2 col 10: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_var_decl_array(self):
        """Variable declaration with array type"""
        input = """void main() {
    int a[3];
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_func_array_pointer(self):
        """Function has an array pointer type as parameter"""
        input = """int[] foo( int b[] ) {}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_stmt_if_full(self):
        """If statement formal"""
        input = """void main() {
    if ( a == true ) return b; else return c;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_stmt_if(self):
        """If statement without else"""
        input = """void main() {
    if ( a == true && b == false ) return b;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_stmt_if_exp(self):
        """If statement has wrong expression"""
        input = """void main() {
    if ( a = true ) return b; else return c;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))
    # TODO: still true in ParserSuite

    def test_stmt_if_nested(self):
        """If statement nested"""
        input = """void main() {
    if ( a == true )
        if ( b == true ) return b;
        else return c;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_stmt_if_nested_parenthesis(self):
        """If statement nested with parenthesis"""
        input = """void main() {
    if ( a == true )
        {
          if ( b == true ) return b;
          else return c;
        }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_stmt_if_semi(self):
        """Missing semicolon inside if else statement"""
        input = """void main() {
    if ( a == true ) return b else return c;
}
"""
        expect = "Error on line 2 col 30: else"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_stmt_if_block(self):
        """If else statement with block statement"""
        input = """void main() {
    if ( a == true ) { return b; } else { return c; }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_block_semi(self):
        """Block statements end with semicolon"""
        input = """void main() {
    if ( a == true ) { return b; } else { return c }
}
"""
        expect = "Error on line 2 col 51: }"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_stmt_if_else_nested(self):
        """If else nested inside else statement"""
        input = """void main() {
    if ( a == true )
        return b;
    else {
        if ( b == true )
            return x;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_if_else_nested(self):
        """If else nested inside if & else statement"""
        input = """void main() {
    if ( a == true ) {
        if ( b == false )
            return b;
    } else {
        if ( b == true )
            return a;
        else
            return b;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_do_while_single(self):
        """Do while with 1 statement"""
        input = """void main(int a) {
    do a = a + 1; while a < 10 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_do_while_many(self):
        """Do while with many statement"""
        input = """void main(int a) {
    do a = a + 1; b = b + 1; while a < 10 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_do_while_block(self):
        """Do while with block statement"""
        input = """void main(int a) {
    do { a = a + 1; b = b + 1; } while a < 10 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_do_while_exp(self):
        """Do while with many expression"""
        input = """void main(int a) {
    do a = a + 1; while a < 10; b > 2 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_do_while_exp_block(self):
        """Do while with many expression in block"""
        input = """void main(int a) {
    do a = a + 1; while { a < 10; b > 2; }
}
"""
        expect = "Error on line 2 col 24: {"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_do_while_stmt(self):
        """Do while with no statement"""
        input = """void main(int a) {
    do while a < 10 ;
}
"""
        expect = "Error on line 2 col 7: while"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_do_while_empty_block(self):
        """Do while with empty block statement"""
        input = """void main() {
    do { } while a < 10 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
    # TODO: Do while with empty block statement

    def test_do_while_block_nested(self):
        """Do while nested inside block statement"""
        input = """void main(int a) {
    do {
        do x = x + 1;
        while true ;
    }
    while x < 10 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_do_while_infinity(self):
        """Do while overflow"""
        input = """void main(int a) {
    do {
        x = x + 1;
    }
    while true ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_for_stmt(self):
        """For statement standard"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) a = a + 2 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_for_block(self):
        """For statement with block statement"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        b = b + 1;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_for_no_stmt(self):
        """For statement with no statement"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) ;
}
"""
        expect = "Error on line 2 col 38: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_for_exp(self):
        """For statement with wrong first expression"""
        input = """void foo() {
    for ( x + 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))
    # TODO: For statement with wrong first expression

    def test_for_structure(self):
        """For expression with wrong structures"""
        input = """void foo() {
    for ( x = 1 , x < 3 , x = x + 1 ) {
        a = a + 2 ;
    }
}
"""
        expect = "Error on line 2 col 16: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_for_nested(self):
        """For statement nested"""
        input = """void foo() {
    for ( x = 1 ; x < 5 ; x = x + 1 ) {
        for ( a = 1 ; a < 3 ; a = a + 1 ) b = b * b ;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_for_missing(self):
        """For statement missing expression 2"""
        input = """void foo() {
    for ( x = 1 ; ; x = x + 1 ) {
        a = a + 2 ;
        b = b + 1;
    }
}
"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_for_missing_another(self):
        """For statement missing expression 3"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; ) {
        a = a + 2 ;
    }
}
"""
        expect = "Error on line 2 col 26: )"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_for_missing_first(self):
        """For statement missing expression 1"""
        input = """void foo() {
    for ( ; x < 3 ; x = x + 1 ) {
        b = b + 1;
    }
}
"""
        expect = "Error on line 2 col 10: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_break(self):
        """Break statement"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        break ;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_break_loop(self):
        """Break statement appear outside loop"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
    }
    break ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_break_arg(self):
        """Break statement with argument"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        break(1);
    }
}
"""
        expect = "Error on line 4 col 13: ("
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_continue(self):
        """Continue statement"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        continue ;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_continue_loop(self):
        """Continue statement appear outside of a loop"""
        input = """void foo() {
    continue ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_continue_nested(self):
        """Continue statements are nested"""
        input = """void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        continue(continue;);
    }
}
"""
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_continue_semi(self):
        """Continue statement missed semicolon"""
        input = """void foo() {
    continue
}
"""
        expect = "Error on line 3 col 0: }"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_return_void_func(self):
        """Return statement with void type"""
        input = """void main() {
    return ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_return_value_to_void(self):
        """Return statement with value to void"""
        input = """void main(int x) {
    return x;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_return_array_pointer(self):
        """Return statement with array pointer type"""
        input = """int[] main() {
    int a[2];
    return a[];
}
"""
        expect = "Error on line 3 col 13: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_param_with_array(self):
        """Array length in a parameter declaration"""
        input = """void f(int a[5]) {}
"""
        expect = "Error on line 1 col 13: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_array_pointer_as_param(self):
        """Array pointer in a parameter declaration"""
        input = """void f(int a[]) {}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_block_stmt_exp(self):
        """Block statement with expressions"""
        input = """void foo(){
    i = 2;
    a = "true";
    69;
    foo(i, a);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_block_block(self):
        """Block of block statement"""
        input = """void foo(){
    i = 2; {
        a = "true"; {
            69;
        }
    }
    foo(i, a);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_intlit(self):
        """Wrong value to integer"""
        input = """void main() {
    int a;
    a = 3.14159;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_local_scope(self):
        """Local scope"""
        input = """void main() {
    putInt(a);
}
    int foo(){
        int a;
        a = 1;
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_global_scope(self):
        """Global scope"""
        input = """int a;
void main() {
    a = 0;
    putInt(a);
}
int foo(){
    a = 1;
    return a;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_if_stmt_for(self):
        """If statement and for statement are nested"""
        input = """void main() {
    if ( a == 0 ) {
        for ( x = 0 ; x < 3 ; x = x + 1 ) a = a - 1;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_infinity_loop(self):
        """Infinity loop"""
        input = """void main(int x) {
    int a;
    a = 0;
    for ( x = 0 ; a < 3 ; x = x + 1 ) x = x - 1 ;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_stmt_after_return(self):
        """Statement after return statement will be ignore"""
        input = """void main() {
    int a;
    a = 2;
    return a;
    a = a + 1;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_block_stmt_semi(self):
        """Block statement has not end with semicolon"""
        input = """void main() {
    int a;
    int b
}
"""
        expect = "Error on line 4 col 0: }"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_func_block_stmt(self):
        """Function declaration with many block statement"""
        input = """void main(){
    // first block
    {
        // second block
        {
            // third block
            {
                // fourth block
            }
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_func_nothing(self):
        """Function does not do anything"""
        input = """int f() {
    return 69;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_myth(self):
        """Myth program"""
        input = """void main () { int a, b;}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
