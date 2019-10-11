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
    def test_right_arr(self):
        
        input = """int test_case() {
            A[B[5+x]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_true_arr_and_func(self):
        
        input = """int arrayment8() {
            foo(x+2)[x+A[y]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_wrong_di_arr(self):
   
        input = """int ____main() {
            a[2][5];
        }"""
        expect = "Error on line 2 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_return_stament(self):
       
        input = """int ____main___() {
            return foo();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_return_and_recursion(self):
       
        input = """int foo(int a, float b) {
            if (b == 0) return 0;
            return a*foo(a, b-1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_wrong_di_arr1(self):
       
        input = """int _main() {
            float a = 4.9;
        }"""
        expect = "Error on line 2 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_two_func(self):
       
        input = """int[] decla() {
            int a[2];
            a[0] = 1;
            a[1] = 2;
            return a;
        }
        void main(int arg[]){
            int b[2];
            b = decla();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_mul_func(self):
           
        input = """int ____main() {
            a[2] = b[5]*i + func(5);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_if_els_stament(self):
        input = """int _main() {
            if(a == 5){
                print("D");
            }
            else{
                if(b != 9){
                    print("K");
                }
                else{
                    b = 70;
                }
                b = 12;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_wrong_funcall(self):
           
        input = """int _main() {
            func(int a, int b);
        }"""
        expect = "Error on line 2 col 17: int"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_wrong_funcall_sepera(self):
           
        input = """int _main_14() {
            funcall(a; b; c);
        }"""
        expect = "Error on line 2 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_do_while(self):
           
        input = """int main() {
            int a[3];
            do{
                boolean b;
                a[0] = foo(2);
                a[1] = put(2,7);
                a[2] = push(37);
            }
            while( b >= 0);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_countinue(self):
           
        input = """int _main() {
            int a;
            a = 1;
            if(a != 0) countinue;
            else{
                a = 0;
            }
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_for_statement(self):
           
        input = """int _main() {
            int i;
            int count;
            count =10;
            for(i = 0; i < count; i = i + 1){
                int a;
                a = i + 3;
                print(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_for_if_statement(self):
           
        input = """int ____main() {
            int i;
            int count;
            count =10;
            for(i = 0; i < count; i = i + 1){
                if( i == 5) break;
                else{
                    print(i);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_for_if_countinue(self):
        input = """int main() {
            int i;
            int count;
            count =10;
            for(i = 0; i < count; i = i + 1){
                if( i == 8) break;
                if(( i % 2) == 0) countinue;
                else{
                    print(i);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_while_if(self):
        input = """int main() {
            int x;
            x = 9;
            do{
                int a;
                a = 0;
                a = a + x;
                if((a%3) == 0) x= x+1;
                else{
                    x = x -1;
                }
            }
            while((x >=0) && (a < 100));
            return 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_expression(self):
        input = """int _main() {
            int a;
            a = 1.0987e4;
            int b;
            b = 8.97e-10;
            int c;
            c = (((a*a+a)*b-a*b)*a*b-34/a)/a -5*b;
            print(c);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_add_string(self):
        input = """int _main() {
            int a;
            a = 1;
            string s;
            s = "a normal string";
            s = s + ", and special string";
            print(s);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_wrong_initial(self):
        input = """void foo(){}
        int main() {
            int a;
            a = 1;
            float d = 5.6; 
            return 0;
        }"""
        expect = "Error on line 5 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_func_in_func(self):
        input = """int _main() {
            int a;
            a = 1;
            boolean b,g,h,g;
            int goo(){}
            return 0;
        }"""
        expect = "Error on line 5 col 19: ("
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_urnary_exp(self):
        input = """int _main(){
            int a;
            a = 1;
            a = -(((b[1+3]*2)*9-5+6)*7-100);
            a = -13.4;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_double_LSB_RSB(self):
        input = """int _main() {
            int a;
            a = 1;
            a = --a[b[2+4]+1];
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_for_countinue(self):
        input = """int _main() {
            int a;
            a = 1;
            for(i=0;i<6;i=i+1) countinue;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_argument_arraytype(self):
        input = """int _main(int arg[]) {
            int a;
            a = 1;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_null_stament(self):
        input = """string _main() {
            int a;
            a = 1;
            string s;
            for(;;){}
            return s;
        }"""
        expect = "Error on line 5 col 16: ;"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_assign_true_false(self):
        input = """int _main() {
            boolean a,b;
            a = true;
            b = false; 
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_for_in_while(self):
        input = """string _main() {
            int b;
            string s;
            s = "Hi";
            b = 1;
            do{
                int i;
                for(i = 10;i>0;i=i-1){}
                b=b-1;
            }
            while(b>0);
            return s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_miss_a_semi(self):
        input = """int _main() {
            do{}
            while(b>0)
            return 0;
        }"""
        expect = "Error on line 4 col 12: return"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_miss_semi_more_comma(self):
        input = """int _main(float b[], string arg) {
            do i=(6-x+t[z]+i)*7;
            while(i<100),
            return 0;
        }"""
        expect = "Error on line 3 col 24: ,"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_wrong_array_output(self):
        input = """int _func(int[], float b) {
            return 0;
        }"""
        expect = "Error on line 1 col 13: ["
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_invol_expr_in_index_expr(self):
           
        input = """int _main() {
            a[foo()] = foo1(1,2);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_invol_expr_has_array(self):
        input = """int _main() {
            b = foo(x+1,a[i]);
            break;
            return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_wrong_parameter(self):
        input = """int _(int self, 1) {
            return 0;
        }"""
        expect = "Error on line 1 col 16: 1"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_no_para(self):
        input = """void __(int ,float ) {
            return ;
        }"""
        expect = "Error on line 1 col 12: ,"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_serie_mul_and_div(self):
        input = """int _main() {
            int abc;
            abc = 5*6/7*2/5*8-9+2%1;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_wrong_para_array(self):
        input = """void _main(int a[10], string s) {
            return ;
        }"""
        expect = "Error on line 1 col 17: 10"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_decla_expect_function(self):
        input = """int a,b,c;
        int _main() {
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_no_function_no_decla(self):
        input = """a[i]=5+6-7*8/9;"""
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_expression_expect_func(self):
        input = """int a;
        a = a*b+8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_wrong_pointer(self):
        input = """void ___(float f) {
            int p[8];
            *p = 1;
            return 0;
        }"""
        expect = "Error on line 3 col 12: *"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_array_string(self):
        input = """int _(string a[]) {
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_array_string_type(self):  
        input = """string[] _main() {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_boolean_array(self):
        input = """boolean[] _main() {
            boolean b[3];
            b[0] = true;
            b[1] = false;
            b[2] = flase;
            return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_wrong_function_name_if(self):
        input = """int if() {
            return 0;
        }"""
        expect = "Error on line 1 col 4: if"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_wrong_type_decla(self):  
        input = """int[] _main() {
            int[] a[10];
            return 0;
        }"""
        expect = "Error on line 2 col 15: ["
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_array_void(self):
        input = """void[] _main() {
            return;
        }"""
        expect = "Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_wrong_identify_return(self):
        input = """int _main() {
            return = 12-4;
            return 0;
        }"""
        expect = "Error on line 2 col 19: ="
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_not_expr_and_mul(self):
        input = """int _main() {
            float f;
            int _main;
            _main = 2;
            f = !(a*b)*3+1/4%main;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_if_statement_except_function(self):
        input = """int a;
        if(a ==0) a=1;
        void _main() {
            return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_wrong_function_name_float(self):
        input = """float float() {
            return 1.0;
        }"""
        expect = "Error on line 1 col 6: float"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_return_floating_point(self):
        input = """float _() {
            return 1.0e38;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_wrong_type(self):
        input = """itn _main() {
            return 0;
        }"""
        expect = "Error on line 1 col 0: itn"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_block_statement_and_return(self):
        input = """int b;
        {
            int a;
            a = 1;
            if(a!=0) a++;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_nested_block(self):
        input = """void def(){
            {{{{int a;}}}}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_wrong_no_started_by_declaration(self):
        input = """
        if(a>0) a=a-1;
        int _main() {
            return 0;
        }"""
        expect = "Error on line 2 col 8: if"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_wrong_if_or_expr(self):
        input = """int _main() {
            int a;
            if(a==0) b=b+2 else a= 9+i||0;
            return 0;
        }"""
        expect = "Error on line 3 col 27: else"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_if_stament_or_expr(self):
        input = """int _main() {
            if(a==0) b=b*8%2; else a= 9+i||0;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_funcall_in_if(self):
        input = """int _main() {
            if(isFalse(b)) b=b+5;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_else_statement_no_if(self):
        input = """int _main() {
            int a;
            else b-1;
            return 0;
        }"""
        expect = "Error on line 3 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_do_statement_no_while(self):
        input = """int _main() {
            do{a=2;}
            return 0;
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_while_statement_no_do(self):
        input = """void _main() {
            while(!a){
                b=b*2;
            };
            return ;
        }"""
        expect = "Error on line 2 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_for_no_statement(self):
        input = """int _main() {
            int a;
            a = 1;
            for(a = 2; a >= -9;a=a-1) ;
            return 0;
        }"""
        expect = "Error on line 4 col 38: ;"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_countinue_in_break_statement(self):
        input = """int _main() {
            break countinue;
            return 0;
        }"""
        expect = "Error on line 2 col 18: countinue"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_countinue_in_reuturn_statement(self):
        input = """int _main() {
            return countinue;
        }"""
        expect = "Error on line 2 col 19: countinue"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_break_in_return(self):
        input = """int _main() {
            return break;
        }"""
        expect = "Error on line 2 col 19: break"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_not_expr_in_if_statement(self):
        input = """void _main() {
            if(----a) return 0;
            return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_double_add_in_if(self):
        input = """int _main() {
            if(a++) a=b+1;
            return 0;
        }"""
        expect = "Error on line 2 col 17: +"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_recursive_and_index_expr(self):
        input = """int _goo() {
            int a;
            a = 1;
            return _goo()[b[i]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_postfix_double_sub(self):
        input = """void _main() {
            int a;
            b--a;
            a--;
            return ;
        }"""
        expect = "Error on line 4 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_return_not_expr(self):
        input = """int _main() {
            string a;
            a = "a string \\n\\t\\b";
            int i;
            i=9;
            return ----i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_sub_and_add_series(self):
        input = """float _main() {
            int a;
            a = 1;
            float b;
            b=b+---2--a;
            return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_wrong_decla_in_reutrn_statement(self):
        input = """float main() {
            int a;
            return float b;
        }"""
        expect = "Error on line 3 col 19: float"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_wrong_return_type(self):
        input = """int _main() {
            return int;
        }"""
        expect = "Error on line 2 col 19: int"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_worng_return_array_type(self):
        input = """float[] _main() {
            int a;
            a = 1;
            return float[];
        }"""
        expect = "Error on line 4 col 19: float"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_worng_return_array(self):
        input = """float[] _main() {
            float a[10];
            return a[];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_wrong_if_in_for(self):
        input = """int _main() {
            int a;
            a = 1;
            for(if(!a) a=a+2;a<10;a=a+3){}
            return 0;
        }"""
        expect = "Error on line 4 col 16: if"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_funcall_and_index_exp_series(self):
        input = """int _main() {
            return goo(a[b-f(a[i])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_array_point_assign(self):
        input = """void _main() {
            int b;
            b=5;
            a[][]=b;
            return ;
        }"""
        expect = "Error on line 4 col 15: ["
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_series_less(self):
        input = """int _main() {
            if(a<b<c<d) b=1;
            return 0;
        }"""
        expect = "Error on line 2 col 18: <"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_nested_func(self):
        input = """int _main() {
            b=foo(func(a,goo(a[i]),a[f(a[b+i(1)||foo()])],x()));
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_nested_func_assign(self):
        input = """int _main() {
            int a;
            a = 1;
            fun1(fun2(fun3(a[2])))[1] = fun1(i || b[fun(t)]);
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_double_sub_and_not_in_if(self):
        input = """int _main() {
            int a;
            a = 1;
            if(i--2==76!a) return 0;
            return 0;
        }"""
        expect = "Error on line 4 col 23: !"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_lelf_expr_assigned(self):
        input = """int _main() {
            int a;
            a = 1;
            a+b=c;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_not_func_name(self):
        input = """() {
            
        }"""
        expect = "Error on line 1 col 0: ("
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_wrong_decla_function1(self):
        input = """
        float al(int a,float b);
        int _main() {
            return 0;
        }"""
        expect = "Error on line 2 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_space_string(self):
        input = """void main() {
            int a;
            a = 1;
            s = " " + " ";
            s1= " " " ";
        }"""
        expect = "Error on line 5 col 20:  "
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_a_line_comment(self):
        input = """int _main() {
            a=a+1;// a line comment;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_double_less(self):
        input = """int _main() {
            int a;
            a = 1;
            a<<9;
            return 0;
        }"""
        expect = "Error on line 4 col 14: <"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_decla_in_for(self):
        input = """int _main() {
            for(int i=0;i<4;i=i--1){}
            return 0;
        }"""
        expect = "Error on line 2 col 16: int"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_for_in_return_statement(self):
        input = """int _main() {
            return for(i=0;i<9;i=i+1){a=a+2;};
        }"""
        expect = "Error on line 2 col 19: for"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_string_and_bool(self):
        input = """void _main() {
            string a;
            a = "";
            a= a+" " - false;
            return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_add_boolean(self):
        input = """int _main() {
            int b;
            b= true + false;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_boolean_in_expr(self):
        input = """int _main() {
            a = 1;
            b = true/false+true*false;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_many_line_comment(self):
        input = """int _main() {
            int a;
            a = 1;
            /* comment 
            //////////*/
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_add_floating_point(self):
        input = """float _main() {
            float a;
            a = 12.7e34+5;
            return a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_empty_parameter(self):
        input = """int _main(,) {
            return 0;
        }"""
        expect = "Error on line 1 col 10: ,"
        self.assertTrue(TestParser.checkParser(input,expect,300))
        