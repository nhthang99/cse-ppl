import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # Super simple test
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4); 
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_null_prog(self):
        """ null program """
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    # Test simple erorr of function declaration
    def test_wrong_miss_close_1(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_miss_close_2(self):
        """Miss } int main() {"""
        input = """int main() {"""
        expect = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_miss_semi(self):
        """Miss ; int main() {print()}"""
        input = """int main() {print()}"""
        expect = "Error on line 1 col 19: }"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_wrong_miss_type_func(self):
        """Miss type of function in  main() {}"""
        input = """main() {}"""
        expect = "Error on line 1 col 0: main"
        self.assertTrue(TestParser.checkParser(input,expect,206))


    # Test variable declaration
    def test_var_dcls(self):
        """simple declaration"""
        input = """int a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_var_dcls_assign(self):
        """can not assign in variable declaration"""
        input = """float a  = 10;"""
        expect = "Error on line 1 col 9: ="
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_var_dcls_miss_semi(self):
        """Miss ; in string a"""
        input = """string a"""
        expect = "Error on line 1 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_var_dcls_array(self):
        """simple array variable declaration"""
        input = """boolean a[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_var_dcls_array_miss_size(self):
        """miss size of array"""
        input = """int a[];"""
        expect = "Error on line 1 col 6: ]"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_var_dcls_array_wrong_size(self):
        """size of array must be integer literal"""
        input = """float a[2+3];"""
        expect = "Error on line 1 col 9: +"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_mul_var_dcls_float(self):
        """size of array must be integer literal"""
        input = """float a, b, c[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_mul_var_dcls_string(self):
        """size of array must be integer literal"""
        input = """string a, b, c[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_mul_var_dcls_int(self):
        """size of array must be integer literal"""
        input = """int a, b, c[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
# Test if else
    def test_if(self):
        """simple if"""
        input = """int main() { if(a>2) print(2);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_if_else(self):
        """simple if else"""
        input = """int main() { if(a>2) print(2); else print(3); }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_if_else_block_stmt(self):
        """complex if else"""
        input = """int main() { if(a>2) {int b; print(b);} else {print("PPL");}}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_if_else_miss_close(self):
        """miss ( in if (a>2 """
        input = """int main() { if(a>2 print(2); else print(3); }"""
        expect = "Error on line 1 col 20: print"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    

    # Test do while stmt
    def test_do_while_1(self):
        """ simple do while"""
        input = """int main() { do continue; while 2>3;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_do_while(self):
        """ simple do while"""
        input = """int main() { do break; while 2>3;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_do_while_complex(self):
        """ complex do while"""
        input = """int main() { do {continue;}{foo();}{foo();} while 2>3;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_do_while_miss_stmt(self):
        """ miss statement"""
        input = """int main() { do while 2>3;}"""
        expect = "Error on line 1 col 16: while"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_do_while_miss_expr(self):
        """ miss expresstion"""
        input = """int main() { do print(); while;}"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    # Test for stmt
    def test_for(self):
        """ simple for"""
        input = """int main() {for(i = 0; i < n; i = i + 1) break;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_for_miss_expr(self):
        """ miss expression """
        input = """int main() {for(i = 0; i < n;) break;}"""
        expect = "Error on line 1 col 29: )"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_for_miss_stmt(self):
        """ miss stmt"""
        input = """int main() {for(i = 0; i < n; i = i + 1) }"""
        expect = "Error on line 1 col 41: }"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    # test break stmt
    def test_break(self):
        """ simple for"""
        input = """int main() {for(i = 0; i < n; i = i + 1) {if(a ==0) break;}}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_break_non_semi(self):
        """ simple for"""
        input = """int main() {for(i = 0; i < n; i = i + 1) {if(a ==0) break}}"""
        expect = "Error on line 1 col 57: }"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    # test continue stmt
    def test_continue(self):
        """ simple for"""
        input = """int main() {for(i = 0; i < n; i = i + 1) {if(a ==0) continue;}}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_continue_non_semi(self):
        """ simple for"""
        input = """int main() {for(i = 0; i < n; i = i + 1) {if(a ==0) continue}}"""
        expect = "Error on line 1 col 60: }"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    # Test expression
    def test_expr(self):
        """ simple expression"""
        input = """int main() {1 + 2 - 3 * 4 / 5;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_assign_1(self):
        """ simple assign expression"""
        input = """int main() {a = 1 + 2 - 3 * 4 / 5;}"""
        expect = "successful"
    def test_assign_2(self):
        """ simple assign expression"""
        input = """int main() {a + b = 5;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_bool_expr(self):
        """ simple boolean expression"""
        input = """int main() {a = true || true && false;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_compare_expr(self):
        """ simple compare expression"""
        input = """int main() {check = 1 + 2 - 3 * 4  == 5;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_continue_compare_expr(self):
        """ simple compare expression"""
        input = """int main() {check = 1 + 2 - 3 * 4  == 5 != 6;}"""
        expect = "Error on line 1 col 40: !="
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_index_expr_1(self):
        """ simple index expression"""
        input = """int main() {ele = arr[5];}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_index_expr_2(self):
        """ complex index expression"""
        input = """int main() {ele = arr[2*3 - 1];}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_index_expr_3(self):
        """ complex index expression"""
        input = """int main() {ele = arr[2*3 - 1 + a[2]];}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_index_expr_4(self):
        """ complex index expression"""
        input = """int main() {ele = foo(2)[2*3 - 1 + a[2]];}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_function_operand(self):
        """ operand is function """
        input = """int main() {a = c(2) + a(2) + b(3);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    # Test call function
    def test_calfunc_null_arg(self):
        """ null arg list"""
        input = """int main() {foo();}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_calfunc_one_arg(self):
        """ one arg """
        input = """int main() {foo(1+2);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_calfunc_miss_arg(self):
        """ mis arg """
        input = """int main() {foo(2,);}"""
        expect = "Error on line 1 col 18: )"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_calfunc_miss_close(self):
        """ mis arg """
        input = """int main() {foo(2,;}"""
        expect = "Error on line 1 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,248))
   
   # Test declare function
    def test_array_type_arg(self):
        """ mis arg """
        input = """int main(int a[]) {print();}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_array_type_func(self):
        """ mis arg """
        input = """int[] main(int a[]) {print();}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

# Test multi declaration
    def test_var_global(self):
        """ global variable """
        input = r"""
        int a;
        int main(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_tool_func(self):
        """ tool function """
        input = r"""
        int foo(){}
        int main(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_complex_prog(self):
        """ complex program """
        input = r"""
        int a;
        int foo(){}
        int main(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    # Test block statement
    def test_block_in_block(self):
        """ complex program """
        input = r"""int main(){
            {}{}{}{}{}{}{}{}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    # # # Test long code

    def test_if_stmt_for(self):
        """If statement and for statement are nested"""
        input = """void main() {
    if ( a == 0 ) {
        for ( x = 0 ; x < 3 ; x = x + 1 ) a = a - 1;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_global_scope(self):
        """Global scope"""
        input = """int a;
void main() {
a = 0; print(a);
}
int foo(){
a = 1; return a;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_local_scope(self):
        """Local scope"""
        input = """void main() {
    putInt(a);
} int foo(){
        int p;
        z = 10;
    }
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_block_block(self):
        """Block of block statement"""
        input = """void foo(){    k = 2; {
        a = "hello"; {
            69;  }
    }  foo(i, a);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_param_with_array(self):
        """Array length in a parameter declaration"""
        input = """void f(int a[5]) {} """
        expect = "Error on line 1 col 13: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_array_pointer_as_param(self):
        """Array pointer in a parameter declaration"""
        input = """void f(int a[]) {} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    # Hard test

    def test_hard_0(self):
        """Hard test"""
        input = """int main()
{
int a;
float b;
string c;
print(a + b + c);
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_hard_1(self):
        """Hard test"""
        input = """
        int main ()
{
    float a, b, c, x, y, z;
    a = 9;
           b = 12;
           c = 3;
           x = a - b / 3 + c * 2 - 1;
           y = a - b / (3 + c) * (2 - 1);
           z = a - ( b / (3 + c) * 2) - 1;
           printf ("x = %f",x);
           printf ("y = %f",y);
           printf ("z = %f",z);
    return 0;

}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_hard_2(self):
        """Hard test"""
        input = """
        void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        continue ;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_hard_3(self):
        """Hard test"""
        input = """
        void foo() {
    for ( x = 1 ; x < 5 ; x = x + 1 ) {
        for ( a = 1 ; a < 3 ; a = a + 1 ) b = b * b ;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_hard_4(self):
        """Hard test"""
        input = """
        void main(){
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
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_hard_5(self):
        """Hard test"""
        input = """int main ()
{
    a = !(a && b || c);
    e = a / b *c / (10 * c % d);
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_hard_6(self):
        """Hard test"""
        input = """int main() {int a[5]; int b[6]; a + b = 9;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_hard_7(self):
        """Hard test"""
        input = """string brth(string a) {for(i = 10; 1; i = i + 1) print(a[1]);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_hard_8(self):
        """Hard test"""
        input = """int[] arrot(int i) {print(0); return 1;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_hard_9(self):
        """Hard test"""
        input = """int a[10]; int b[10];
        int showa() {print(a);}
        int showb() {print(b);}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_for_block_stmt(self):
        """For statement and block statement"""
        input = r"""void foo() 
        {
            for ( x = 1 ; x < 3 ; x = x + 1 ) 
            {
                a = a + 100 ; b = b - 1;
            }
        }   
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_for_no_stmt(self):
        """For and no stmt"""
        input = r"""int main()  {
            for ( i = 1 ; i < 100000000000000 ; r = t + 1 ) ;
        }
        """
        expect = "Error on line 2 col 60: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_for_exp(self):
        """For statement simple """
        input = r"""void main() 
        {
            for ( i = 0 ; i<=10000000000000000 ; i = i * 1 ) 
            { n = n + 2 ; }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_for_wrong(self):
        """For with wrong """
        input = r"""void foo() 
        {
            for ( i = 1) {
                n = n + 2 ;
            }
        }
        """
        expect = "Error on line 3 col 23: )"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_func_nothing(self):
        """Function does not do anything"""
        input = """int f() {
    return 69;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_myth(self):
        """Myth program"""
        input = """void main () { int a, b;}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_hard_11(self):
        """Hard test"""
        input = """
        int main ()
{
    float a, b, c, x, y, z;
    a = 9;
           b = 12;
           c = 3;
           x = a - b / 3 + c * 2 - 1;
           for ( x = 1 ; x < 5 ; x = x + 1 ) {
        for ( a = 1 ; a < 3 ; a = a + 1 ) b = b * b ;
    }
           y = a - b / (3 + c) * (2 - 1);
           z = a - ( b / (3 + c) * 2) - 1;
    return 0;

}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_hard_12(self):
        """Hard test"""
        input = """
        void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a = a + 2 ;
        continue ; break;
        a[5] =10;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_hard_13(self):
        """Hard test"""
        input = """
        void foo() {
a[a[a[a[6]]]];
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_hard_14(self):
        """Hard test"""
        input = """
        void main(){
    // first block
    {
        // second block
        a = 5;
        {
            // third block
            c =10;
            {
                // fourth block
                d = 1;
            }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_hard_15(self):
        """Hard test"""
        input = """int main ()
{
    a = !(a && b || c);
    e = a / b *c / (9* c % d);
    z = !(a && b || c);
    v = r / b *l / (1 * c % d);
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_hard_16(self):
        """Hard test"""
        input = """int main() {int a[5]; int b[6]; a + b = 10;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_hard_17(self):
        """Hard test"""
        input = """string brth(string a) {for(i = 10; 1; i = i + 1) print(a[1], 2, 3);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_hard_18(self):
        """Hard test"""
        input = """int[] arrot(int i) {print(0, 1, "hi"); return true;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_invalid_callfunc_1(self):
        """Test Invalid Call Function"""
        input = '''int main(){
            bye("alo")
        }
        '''
        expect = 'Error on line 3 col 8: }'
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_invalid_call_func_2(self):
        """Test Invalid Call Function"""
        input = '''int main(){
            bye("alo";
        }
        '''
        expect = 'Error on line 2 col 21: ;'
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_invalid_call_func_3(self):
        """Test Invalid Call Function"""
        input = '''int main(){
            bye("alo"};
        }
        '''
        expect = 'Error on line 2 col 21: }'
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_call_multiple_func(self):
        """Test Call Multiple Function"""
        input = '''int main(){
            a = b() + c() + d();
            a = a / sum(a,b) + sub(a,b);
            print(a);
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_invalid_return_1(self):
        """Test Invalid Return Statement"""
        input = '''int main(){
            return boolean;
        }
        '''
        expect = 'Error on line 2 col 19: boolean'
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_invalid_return_2(self):
        """Test Invalid Return Statement"""
        input = '''int main(){
            RETURN true;
        }
        '''
        expect = 'Error on line 2 col 19: true'
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_complex_program(self):
        """Test Complex Program """
        input = '''
        int main()
{
    float a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
    printf("Enter coefficients a, b and c: ");
    scanf("%lf %lf %lf",a, b,c);
    discriminant = b*b-4*a*c;
    // condition for real and different roots
    if (discriminant > 0)
    {
    // sqrt() function returns square root
        root1 = (-b+sqrt(discriminant))/(2*a);
        root2 = (-b-sqrt(discriminant))/(2*a);
        printf("root1 = %.2lf and root2 = %.2lf",root1 , root2);
    }
    //condition for real and equal roots
    else if (discriminant == 0)
    {
        root1 = root2 = -b/(2*a);
        printf("root1 = root2 = %.2lf;", root1);
    }
    // if roots are not real 
    else
    {
        realPart = -b/(2*a);
        imaginaryPart = sqrt(-discriminant)/(2*a);
        printf("root1 = %.2lf+%.2lfi and root2 = %.2f-%.2fi", realPart, imaginaryPart, realPart, imaginaryPart);
    }
    return 0;
}   
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_pro_peo(self):
        """Hard test"""
        input = """
        void foo() {
    for ( x = 1 ; x < 3 ; x = x + 1 ) {
        a[5] =10;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    
    def test_complex_program3(self):
        """Test Complex Program """
        input = '''
        int main()
{
    int base, exponent;
    int result;
    result = 1;
    printf("Enter a base number: ");
    scanf("%d", base);
    printf("Enter an exponent: ");
    scanf("%d", exponent);
    do
    {
        result = result * base;
        exponent = exponent - 1;
    }while (exponent != 0);
    printf("Answer = %lld", result);
    return 0;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_complex_program_(self):
        """Test Complex Program """
        input = '''
        int evaluatePostfix(string exp)  
{  
    // Create a stack of capacity equal to expression size  
    int stack;
    stack = createStack(strlen(exp));  
    int i;  
  
    // See if stack was created successfully  
    if (!stack) return -1;  
  
    // Scan all characters one by one  
    for (i = 0; exp[i]; i = i + 1)  
    {  
        //if the character is blank space then continue  
        if(exp[i] == " ")continue;  
          
        // If the scanned character is an  
        // operand (number here),extract the full number  
        // Push it to the stack.  
        else if (isdigit(exp[i]))  
        {  
            int num;
            num=0;  
              
            //extract full number  
            while(isdigit(exp[i]))  
            {  
            num = num * 10 + (int)(exp[i] - '0');  
                i = i + 1;  
            }  
            i--;  
              
            //push the element in the stack  
            push(stack,num);  
        }  
          
        else
        {  
            int val1;
            val1 = pop(stack);  
            int val2;
            val2 = pop(stack);  
              
            switch (exp[i])  
            {  
            case '+': push(stack, val2 + val1); break;  
            case '-': push(stack, val2 - val1); break;  
            case '*': push(stack, val2 * val1); break;  
            case '/': push(stack, val2/val1); break;  
              
            }  
        }  
    }  
    return pop(stack);  
}  
        '''
        expect = 'Error on line 27 col 12: while'
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_complex_program_900(self):
        """Test Complex Program """
        input = '''
        int main()
 
{
 
  int year;
 
  printf("Please enter a year to check whether it is a leap year or not");
 
  scanf("%d", year);
 
 
 
  if ( year%400 == 0)
 
    printf("%d is a leap year", year);
 
  if ( year%100 == 0)
 
    printf("%d is not a leap year", year);
 
  if ( year%4 == 0 )
 
    printf("%d is a leap year", year);
 
  else
 
    printf("%d is not a leap year", year);  
 
  return 0;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_complex_program_600(self):
        """Test Complex Program """
        input = '''
    int main()
{
   int i,fact,num;
 
   printf("Please enter a number to find factorial : ");
   scanf("%d",num);
 
   for(i=1;i<=num;i = i+1)
   fact=fact*i;
   printf("");
   printf("Entered number is %d and it's factorial (%d!) is %d",num,num,fact);
   return 0;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_complex_program_700(self):
        """Test Complex Program """
        input = '''
    int main()
{
   int f1, f2, fib_ser, cnt, lmt;
 
   do
   {
      fib_ser=f1+f2;
      cnt = cnt + 1;
      printf("%d\\n",fib_ser);
      f1=f2;
      f2=fib_ser;
   }while (cnt < lmt);
   return 0;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_complex_program_800(self):
        """Test Complex Program """
        input = '''
    int main()
 
{
 
      float a, b, c;
 
      printf("\\nPlease enter 3 numbers: ");
 
      scanf("%f %f %f", a, b, c);
 
      if(c<=a && c<=b)
 
         printf("The smallest number is %.3f", c);
 
      return 0;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_complex_program_300(self):
        """Test Complex Program """
        input = '''
    int main()
{
   int A, B, temp;

   temp = A;
   A = B;
   B = temp;
 
   printf("\\nAfter swapping:\\n");
   printf("A - %d \\nB - %d", A, B);
 
   return 0;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_complex_program_100(self):
        """Test Complex Program """
        input = '''
    int main()
 
{
 
   int n, sum , d;
   scanf("%d",n);
   do
   {
      rem = n % 10;
      sum = sum + rem;
      n = n / 100;
   }while(n != 0);

   return 0;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_complex_program_200(self):
        """Test Complex Program """
        input = '''
    int main()
 
{
   if (fp1 = fopen("test1.c", "r"))
   {
      ch = getc(fp1);
      fp2 = fopen("test2.c", "w+");
      return 0;
   }
 
   return 1;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 300))

