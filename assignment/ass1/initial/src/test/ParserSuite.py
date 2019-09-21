import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_declare_variable(self):
        """Declare Variable"""
        input = """int a;
        float b;
        string a[12];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_declare_variable2(self):
        """Declare Variable"""
        input = """
        boolean a;
        boolean a[2];
        string a;
        boolean b[3];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_func_name(self):
        """Test Function Name"""
        input = '''boolean abc__bc-ab(int c){

        }'''
        expect = '''Error on line 1 col 15: -'''
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    def test_func_name2(self):
        """Test Function Name"""
        input = '''
        int abc(){}
        boolean abc(){}
        float[] abc(){}
        void print(){}
        int[] abc(){}
        string low2up(){}
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_declare_function(self):
        """Declare Function"""
        input = """void print(string a){
            printf("hello" + a);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_declare_function2(self):
        """Declare Function"""
        input = """int main(string arg[]){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_declare_function3(self):
        """Declare Function"""
        input = """
void goo ( float x [ ] ) {
    float y[ 10 ] ;
    int z[ 10 ] ;
    foo( x ) ;
    foo( y ) ;
    foo( z ) ;
    return;
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_declare_function4(self):
        """Declare Function"""
        input = """
float square ( float x )   // function definition
{
    float p ;
    p = x * x ;
    return ( p ) ;
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test_declare_function5(self):
        """Declare Function"""
        input = """
boolean swap(int a, int b)
{ 
    int tmp;
    tmp = a;
    a = b;
    b = tmp;
    printf(a, b);
    return true;
}
int main(){
    int a,b;
    boolean result;
    result = swap(a,b);
    print(result);
}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test_func_para(self):
        """Test Paralist In Function"""
        input = '''
        int a(int abc){}
        float a(int a[]){}
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test_func_para2(self):
        """Test Paralist In Function"""
        input = '''
        void a(){}
        string a(int a, int b, int c, float d[]){}
        float a(a, b, c){}
        '''
        expect = '''Error on line 4 col 16: a'''
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_func_para3(self):
        """Test Paralist In Function"""
        input = '''
        int float2int(float a){}
        int a(int a[], int b, float c[], string d){}
        float b(){}
        int c(string c[], int a, int b){}
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,215))
    
    def test_unclose_body_function(self):
        """Test Unclose Body Function"""
        input = '''
        int b(){}
        void c(int c){return ;}
        int d()
        '''
        expect = '''Error on line 5 col 8: <EOF>'''
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test_unclose_body_function2(self):
        """Test Unclose Body Function"""
        input = '''
        int main(){}
        int main()
        '''
        expect = '''Error on line 4 col 8: <EOF>'''
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    def test_insert_semi_function(self):
        """Test Insert Semicolon Function"""
        input = '''
        int main(){}
        int main(int a, int b[]){};
        '''
        expect = '''Error on line 3 col 34: ;'''
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test_without_semi_declare_var(self):
        """Test Without Semicolon Declare Variable"""
        input = '''
        int a;
        float b;
        boolean c;
        string d
        '''
        expect = '''Error on line 6 col 8: <EOF>'''
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_declare_voidtype_var(self):
        """Test Declare Void Type Variable"""
        input = '''
        int a;
        void b;
        '''
        expect = '''Error on line 3 col 14: ;'''
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_declare_array_not_numberof_eles(self):
        """Test Declare Array Not Number of Elements"""
        input = '''
        int a;
        float b;
        boolean c[];
        '''
        expect = '''Error on line 4 col 18: ]'''
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test_func_nested(self):
        """Test Function Nested"""
        input = '''void foo(int i){
            int child_foo(float f){}
        }'''
        expect = '''Error on line 2 col 25: ('''
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test_init_var(self):
        """Test Initial Variable"""
        input = '''int a = b;
        '''
        expect = '''Error on line 1 col 6: ='''
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_array(self):
        """Test Array"""
        input = '''void foo(int a, float b[]){
            int c[3];
            if(a>0) foo(a-1,b);
            return ;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test_declare_array(self):
        """Test Declare Array """
        input = '''
        int a[1];
        string a[8];
        bool a[];
        '''
        expect = '''Error on line 4 col 8: bool'''
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_expr(self):
        """Test Expression """
        input = '''string c(){
            s = a +b + c * d;
            d = a && b;
            e = !a;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,226))
    
    def test_expr2(self):
        """Test Expression """
        input = '''int[] foo(int b[]){
            int a[1];
            if (true) return a;
            else return b;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test_expr3(self):
        """Test Expression """
        input = '''void foo(){
            if(false) return;
            else return 2;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_if(self):
        """Test If Statement """
        input = '''int main(){
            if (a==b) a=c;
            else c=d;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_if2(self):
        input = '''int main(){
            if(a>c)
                if (!c) c+x;
                else d+s;
            else true;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,230))
    
    def test_if3(self):
        input = '''int cc(int c){
            if(c==d) s(a[3+c],a==b,false);
            else a;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_if4(self):
        input = '''int foo(int  c[]){
            if (a==c)
                if (d=f)
                    if(lv=2) c=d;
                    else c = a[cc+9];
                else "disdsi/"/4;
            else sdji=7/3;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,232))
    
    def test_unclose_if(self):
        """Test Unclose If Statement """
        input = '''int main(){
            if abc a=c;
            else c=d;
        }'''
        expect = '''Error on line 2 col 15: abc'''
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_index_expression(self):
        """Test Index Expression"""
        input = """int main(){
            foo(2)[3+x] = a[b[2]] + 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_exp4(self):
        input = '''string c(){
            3[3+x] = true[b[2]] +3;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_do_while(self):
        """Test Do While"""
        input = '''int main(){
            do a=c; d=5; do i=i+3;c+d; while c!=9; while a;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,236))
    
    def test_do_while2(self):
        """Test Do While"""
        input = '''
        int main(){
            do a=c;c=d;d=e;c=23.e4+3;
            while c+d=6;
        }
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,237))
    
    def test_do_while3(self):
        """Test Do While"""
        input = '''int main(){
            do{
                a=c;
                d=b;
            }
            {
                a=a+4;
                b>4;
            }
            while a!=b;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_do_while_non_semi(self):
        """Test Do While Non Semicolon"""
        input = '''int main(){
            do{
                a=c;
                d=b;
            }
            {
            }
            while a!=b
        }'''
        expect = '''Error on line 9 col 8: }'''
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_do_while_block_condition(self):
        """Test Do While Block Condition"""
        input = '''int main(){
            do{
                a=c;
                d=b;
            }
            {
            }
            while (a!=b);
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_for(self):
        """Test For Statement"""
        input = '''int main(){
            for(i=0;i<3;i=i+1) if (a=b) c=d; else d;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_for2(self):
        """Test For Statement""" 
        input = '''int main(){
            for (true;(a);1) do {a=c;b=d;}{} while a;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,242))
    
    def test_for_non_block_condition(self):
        """Test For Statement Non Block Condition""" 
        input = '''int main(){
            for true;(a);1 do {a=c;b=d;}{} while a;
        }'''
        expect = '''Error on line 2 col 16: true'''
        self.assertTrue(TestParser.checkParser(input,expect,243))
    
    def test_for_semi(self):
        """Test For Statement With Semicolon""" 
        input = '''int main(){
            for (true;(a);1) ;
        }'''
        expect = '''Error on line 2 col 29: ;'''
        self.assertTrue(TestParser.checkParser(input,expect,244))
    
    def test_break(self):
        """Test Break"""
        input = '''int main(){
            break;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_continue(self):
        """ Test Continue"""
        input = '''int main(){
            continue;
        }'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,246))
    
    def test_return(self):
        """ Test Continue"""
        input = '''int main(){ (foo(2))[3+x] ; return 1;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_return2(self):
        """ Test Continue"""
        input = '''void main(){ (foo(2))[3+x] ; return;}'''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,248))
    
    def test_null_block_stmt(self):
        """ Test Null Block"""
        input = '''
        int main(){}
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,249))
    
    def test_block_stmt(self):
        """ Test Block"""
        input = '''
        int main(){
            int ab;
            {
                {
                    {
                        {
                            break;
                        }
                        break;
                    }
                    break;
                }
                break;
            }
        }
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_while_stmt(self):
        """ Test While Statement"""
        input = '''
        int main()
        {
            int i;
            i = 0;
            while(i==1)
            {
            printf("while vs do-while");
            }
            printf("Out of loop");
        }
        '''
        expect = '''Error on line 6 col 12: while'''
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_invalid_func(self):
        """ Test Invalid Function"""
        input = '''
        private boolean check(TokenType type) {
            if (isAtEnd()) return false;         
            return peek().type == type;          
        }     
        '''
        expect = '''Error on line 2 col 8: private'''
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_invalid_func2(self):
        """ Test Invalid Function"""
        input = '''
        public boolean check(TokenType type) {
            if (isAtEnd()) return false;         
            return peek().type == type;          
        }     
        '''
        expect = '''Error on line 2 col 8: public'''
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_mix(self):
        """ Test Mix"""
        input = '''
        void main()
{
	clrscr();
	int no_star, no_row, i, j;
	for(i=0; i<no_row; i++)
	{
		for(j=0; j<p; j++)
		{
			printf("* ");
		}
		printf("");
	}
	getch();
}     
        '''
        expect = '''Error on line 6 col 22: +'''
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_mix2(self):
        """ Test Mix"""
        input = '''
        int main(){
            int i;
            i = 1;
            for (i;i;i)
        }
        '''
        expect = '''Error on line 6 col 8: }'''
        self.assertTrue(TestParser.checkParser(input,expect,255))
    
    def test_mix3(self):
        """ Test Mix"""
        input = '''
        void main( ){ if (a) if (b) if (c) for(i=0;i<9;i=i+1) foo(2,4); else a; else for(i=0;i<9;i=i+1) foo(2,4);}
        '''
        expect = '''successful'''
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_invalid_if(self):
        """Test Invalid If Statement"""
        input = '''
        void main() {
            if (a == b)
                if (c == d)
                    foo();
                else
                    foo();
            else
                foo();
            else {
                //comment
            }
        }
        '''
        expect = 'Error on line 10 col 12: else'
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_invalid_if2(self):
        """Test Invalid If Statement"""
        input = '''
        void main() {
            else {
                //comment
            }
        }
        '''
        expect = 'Error on line 3 col 12: else'
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_invalid_if3(self):
        """Test Invalid If Statement"""
        input = '''
        void main() {
            if {a == b}{
                //comment
            }
            else {
                //comment
            }
        }
        '''
        expect = 'Error on line 3 col 15: {'
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_invalid_do_while(self):
        """Test Invalid Do While Statement"""
        input = '''
        int main(string arg[])
        {
            do 
            
            while (a!=b);
        }
        '''
        expect = 'Error on line 6 col 12: while'
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_invalid_do_while2(self):
        """Test Invalid Do While Statement"""
        input = '''
        int main(string arg[])
        {
            do {}
        }
        '''
        expect = 'Error on line 5 col 8: }'
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_invalid_for(self):
        """Test Invalid For Statement"""
        input = '''
        int main(string arg[])
        {
            for [i=1;i>1;i+1]{}
        }
        '''
        expect = 'Error on line 4 col 16: ['
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_invalid_for2(self):
        """Test Invalid For Statement"""
        input = '''
        int main(string arg[])
        {
            for {i=1;i>1;i+1}{}
        }
        '''
        expect = 'Error on line 4 col 16: {'
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_invalid_for3(self):
        """Test Invalid For Statement"""
        input = '''
        int main(string arg[])
        {
            for (i=1;i>1;i+1 {}
        }
        '''
        expect = 'Error on line 4 col 29: {'
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_break_non_semi(self):
        """Test Break Non Semicolon Statement"""
        input = '''
        int main(string arg[])
        {
            for (i=1;i>1;i+1) {
                break
            }
        }
        '''
        expect = 'Error on line 6 col 12: }'
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_continue_non_semi(self):
        """Test Continue Non Semicolon Statement"""
        input = '''
        int main(string arg[])
        {
            for (i=1;i>1;i+1) {
                continue
            }
        }
        '''
        expect = 'Error on line 6 col 12: }'
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_return_non_semi(self):
        """Test Return Non Semicolon Statement"""
        input = '''
        int main(string arg[])
        {
            for (i=1;i>1;i+1) {
                return
            }
        }
        '''
        expect = 'Error on line 6 col 12: }'
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_declare_func_noname(self):
        """Test Declare Function Noname"""
        input = '''
        int (){}
        '''
        expect = 'Error on line 2 col 12: ('
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_declare_func_end_with_semi(self):
        """Test Declare Function End With Semicolon"""
        input = '''
        int main(){};
        '''
        expect = 'Error on line 2 col 20: ;'
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_expression_with_keyword(self):
        """Test Expression With Keyword"""
        input = '''
        int main(){
            int a;
            a = continue + 1;
        };
        '''
        expect = 'Error on line 4 col 16: continue'
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_expression_with_keyword2(self):
        """Test Expression With Keyword"""
        input = '''
        int main(){
            int a;
            a = int + 1;
        };
        '''
        expect = 'Error on line 4 col 16: int'
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_expression_with_keyword3(self):
        """Test Expression With Keyword"""
        input = '''
        int main(){
            int a;
            a = void + 1;
        };
        '''
        expect = 'Error on line 4 col 16: void'
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    # def test_invalid_expression(self):
    #     """Test Invalid Expression"""
    #     input = '''
    #     int main(){
    #         a = a & 1;
    #     };
    #     '''
    #     expect = 'Error on line 4 col 16: void'
    #     self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_expression(self):
        """Test Expression"""
        input = '''
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
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 274))
    
    def test_expression2(self):
        """Test Expression"""
        input = '''
        int main ()
{
    int a;
    a = a + 1;
    print(a);
    a = a* 1;
    a = a / 1 && 1 || 1 % 1;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_expression3(self):
        """Test Expression"""
        input = '''
        int main ()
{
    a = !(a && b || c);
    e = a / b *c / (10 * c % d);
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_expression4(self):
        """Test Expression"""
        input = '''
        int main ()
{
    a = !(a && b || c);
    e = a / b *c / (10 * c % d) && !(1) || (1) / 2;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_expression5(self):
        """Test Expression"""
        input = '''
        int main ()
{
    a = !(a && b || c);
    e = a / b *c / (10 * c % d) && !(1) || (1) / 2;
    (b)[3] = a && b;
    !(b) = 3;
    b! = a || b;
}
        '''
        expect = 'Error on line 8 col 5: !'
        self.assertTrue(TestParser.checkParser(input, expect, 278))
    
    def test_invalid_expression2(self):
        """Test Invalid Expression"""
        input = '''
        int main ()
{
    int a;
    a = b[];
}
        '''
        expect = 'Error on line 5 col 10: ]'
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_invalid_expression3(self):
        """Test Invalid Expression"""
        input = '''
        int main ()
{
    int a;
    a = [2]b;
}
        '''
        expect = 'Error on line 5 col 8: ['
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_block_external_func(self):
        """Test External Function"""
        input = '''{}
        '''
        expect = 'Error on line 1 col 0: {'
        self.assertTrue(TestParser.checkParser(input, expect, 281))
    
    def test_declare_func_into_block(self):
        """Test Declare Function Into Block"""
        input = '''int main(){
            {
                void main(){
                    return;
                }
            }
        }
        '''
        expect = 'Error on line 3 col 16: void'
        self.assertTrue(TestParser.checkParser(input, expect, 282))
    
    def test_call_func(self):
        """Test Call Function"""
        input = '''int main(){
            call("alo");
            reply("hi. i am here");
            end_call("bye");
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_invalid_call_func(self):
        """Test Invalid Call Function"""
        input = '''int main(){
            call("alo")
        }
        '''
        expect = 'Error on line 3 col 8: }'
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_invalid_call_func2(self):
        """Test Invalid Call Function"""
        input = '''int main(){
            call("alo";
        }
        '''
        expect = 'Error on line 2 col 22: ;'
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_invalid_call_func3(self):
        """Test Invalid Call Function"""
        input = '''int main(){
            call("alo"};
        }
        '''
        expect = 'Error on line 2 col 22: }'
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_call_multiple_func(self):
        """Test Call Multiple Function"""
        input = '''int main(){
            a = b() + c() + d();
            print(a);
            a = a / sum(a,b) + sub(a,b);
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_invalid_return(self):
        """Test Invalid Return Statement"""
        input = '''int main(){
            return boolean;
        }
        '''
        expect = 'Error on line 2 col 19: boolean'
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_invalid_return2(self):
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

    def test_complex_program2(self):
        """Test Complex Program """
        input = '''
        int main()
{
    int i, num;
    float data;
    printf("Enter total number of elements(1 to 100): ");
    scanf("%d", num);
    // Allocates the memory for 'num' elements.
    if(data == NULL)
    {
        printf("Error!!! memory not allocated.");
        exit(0);
    }
    printf("\\n");
    // Stores the number entered by the user.
    for(i = 0; i < num; i = i + 1)
    {
       printf("Enter Number %d: ", i + 1);
       scanf("%f", data + i);
    }
    // Loop to store largest number at address data
    for(i = 1; i < num; i = i + 1)
    {
       // Change < to > if you want to find the smallest number
       if(data < (data + i))
           data = (data + i);
    }
    printf("Largest element = %.2f", data);
    return 0;
}
        '''
        expect = 'successful'
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

    def test_complex_program4(self):
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
          
        // If the scanned character is an operator, pop two  
        // elements from stack apply the operator  
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

    def test_complex_program5(self):
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

    def test_complex_program6(self):
        """Test Complex Program """
        input = '''
    int main()
{
   int i,fact,num;
 
   printf("Please enter a number to find factorial : ");
   scanf("%d",num);
 
   if (num<0)
   {
      printf("\\nPlease enter a positive number to");
      printf(" find factorial and try again. ");
      printf("\\nFactorial can't be found for negative");
      printf(" values. It can be only positive or 0 ");
      return 1;
   } 
 
   for(i=1;i<=num;i = i+1)
   fact=fact*i;
   printf("");
   printf("Entered number is %d and it's factorial (%d!) is %d",num,num,fact);
   return 0;
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_complex_program7(self):
        """Test Complex Program """
        input = '''
    int main()
{
   int f1, f2, fib_ser, cnt, lmt;
 
   printf("Please enter the limit of the Fibonacci series :");
   scanf("%d",lmt);
   printf("\\nFibonacci series is: \\n%d \\n%d \\n",f1,f2);
 
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

    def test_complex_program8(self):
        """Test Complex Program """
        input = '''
    int main()
 
{
 
      float a, b, c;
 
      printf("\\nPlease enter 3 numbers: ");
 
      scanf("%f %f %f", a, b, c);
 
      if(a<=b && a<=c)
 
         printf("The smallest number is %.3f", a);
 
      if(b<=a && b<=c)
 
         printf("The smallest number is %.3f", b);
 
      if(c<=a && c<=b)
 
         printf("The smallest number is %.3f", c);
 
      return 0;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_complex_program9(self):
        """Test Complex Program """
        input = '''
    int main()
{
   int A, B, temp;
 
   printf("Please enter the 1st number : ");
   scanf("%d",A);
   printf("\\nPlease enter the 2nd number : ");
   scanf("%d",B);
 
   printf("\\nBefore swapping:\\n");
   printf("A - %d \\nB - %d", A, B);
 
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

    def test_complex_program10(self):
        """Test Complex Program """
        input = '''
    int main()
 
{
 
   int n, sum , rem; 
 
   printf("Please enter an integer\\n");
 
   scanf("%d",n);
 
 
 
   do
 
   {
 
      rem = n % 10;
 
      sum = sum + rem;
 
      n = n / 10;
 
   }while(n != 0);
 
   printf("Sum of all individual digits of an entered number is %d\\n",sum);
 
   return 0;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_complex_program11(self):
        """Test Complex Program """
        input = '''
    int main()
 
{
 
   string ch;
 
   string fp1;
 
   string fp2;
 
   /* Assume this test1.c file has some data.
 
      For example "Hi, How are you?" */
 
   if (fp1 = fopen("test1.c", "r"))
 
   {
 
      ch = getc(fp1);
 
      // Assume this test2.c file is empty
 
      fp2 = fopen("test2.c", "w+");
 
      do
      {
 
         fputc(ch, fp2);
 
         ch = getc(fp1);
 
      }while (ch != EOF);
 
      fclose(fp1);
 
      fclose(fp2);
 
      return 0;
 
   }
 
   return 1;
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_complex_program12(self):
        """Test Complex Program """
        input = r'''
    int  main()
 
{
 
    int i;
    i = 8;
 
    printf("Factorial of the number %d is %d\n", i, factorial(i));
 
    return 0;
 
}
 
 
 
int factorial( int i)
 
{
 
   if(i < 2) 
 
   {
 
      return 1;
 
   }
 
   return i * factorial(i - 1);
 
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 301))