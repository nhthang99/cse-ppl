import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redecl_with_param_1(self):
        input = '''
            int a;
            int main(int a, int b){
                int a;
            }
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_redecl_with_param_2(self):
        input = '''
            int a;
            int main(int a, int b){
                int b;
            }
        '''
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_redecl_array_and_var(self):
        input = '''
            int a;
            int main(int a, int b){
                int c[5];
                int c;
            }
        '''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_redecl_var_in_function(self):
        input = '''
            int a;
            int main(int a, int b){
                int c;
                int d;
                int c;
            }
        '''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_redecl_in_stmt_ifelse(self):
        input = '''
            int a;
            int main(int a, int b){
                if (a == b){
                    int a;
                }
                else {
                    int b;
                    int b;
                    int a;
                }
            }
        '''
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_redecl_func_global(self):
        input = '''
            int foo(){return 1;}
            int foo(){}
            int main(){}
            int main(int a, int b){
                int c;
            }
            int a;
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_redecl_func_overload(self):
        input = '''
            int main(){return 1;}
            int foo(int a, int b){
                return 1;
            }
            int foo1(int a, int b){return 1;}
            int foo(){}
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redecl_func_simple(self):
        input = '''
            void main(){return;}
            int foo(int a, int b){
                return 1;
            }
            int foo(int a, int b){}
            int foo(){}
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_redecl_func_overload_2(self):
        input = '''
            void main(){return;}
            int foo(int a, int b){
                int foo;
                int foo1;
                return a;
            }
            int foo(int a, int b){}
            int foo(){}
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redecl_in_subblock_1(self):
        input = '''
            void main(){return;}
            int foo(int a, int b){
                {
                    int a;
                    int b;
                    int c;
                    int c;
                }
            }
        '''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redecl_in_many_block(self):
        input = '''
            void main(){return;}  
            int foo(int a, int b){
                {
                    int a;
                    int b;
                    int c;
                }
                {
                    int c;
                }
                {
                    int c;
                }
                {
                    int d;
                    int d;
                }
            }
        '''
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redecl_in_param(self):
        input = '''
            void main(){return;}
            int foo(int a, int b, int a){
            }
        '''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redecl_overload_param(self):
        input = '''
            void main(){return;}
            int foo(int a, int b, float b){
            }
        '''
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_redecl_in_param_2(self):
        input = '''
            void main(int e, int e){}
            int foo(int a, int b, int e){
                return 1;
            }
        '''
        expect = "Redeclared Parameter: e"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_redecl_overloadparam(self):
        input = '''
            void main(int e){return;}
            int foo(int a, int b, int e, int e){
                return 1;
            }
        '''
        expect = "Redeclared Parameter: e"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_redecl_func_and_var(self):
        input = '''
            void main(int e){return;}
            int foo(int a, int b, int e){
                int main;
                int x;
                int x;
                return 1;
            }
        '''
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_redecl_global_var_and_func(self):
        input = '''
            int foo;
            void main(){return;}
            int foo(int a, int b, int e){
                return 1;
            }
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undecl_simple_ident(self):
        input = '''
            int main(int b){
                a;
                return 1;
            }
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_undecl_ident_in_block(self):
        input = '''
            int main(int b){
                return 1;
            }
            int f(){
                {
                    int a;
                    a = 1;
                    a = a * a;
                }
                {
                    a * a;
                }
                int c;
                return 1;
            }
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undecl_indent_in_nested_block(self):
        input = '''
            int a;
            void main(){return;}
            int f(){
                a = 1;
                {
                    int a;
                    a = 1;
                    {
                        a + a;
                    }
                    a = a * a;
                }
                {
                    {
                        int b;
                        b = 1;
                        a = 1;
                        {b*b;}
                    }
                    a * a;
                    b*b;
                }
                int c;
                return 1;
            }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undecl_in_nested_block_2(self):
        input = '''
            int a;
            void main(){return;}
            int f(){
                int b;
                b = 1;a = 1;
               {a *a; b*b;
               {b*b;
               {}
               b*b;
               }
               }
               {a *a ;
                    {b*b;}
                    d*d;
               }
               return 1;
            }
        '''
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,421))


    def test_undecl_simple_func(self):
        input = '''
            int main(int b){
                return 1;
            }
            int f(){
                int a;
                a = 1;
                foo(a);
                return 1;
            }
        '''
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undecl_func_when_declared_after_use(self):
        input = '''
            int main(int b){
                return 1;
            }
            int f(){
                int a;
                foo();
                foo1();
                return 1;
            }
            int foo(){
                return 1;
            }
        '''
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undecl_simple_param(self):
        input = '''
            int main(int b){
                return 1;
            }
            int f(){
                int a;
                main(x);
                return 1;
            }
        '''
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undecl_param_when_declare_after_use(self):
        input = '''
            int main(int b){
                return 1;
            }
            int f(){
                int a;
                a = 1;
                main(a);
                foo(x);
                foo(i);
                return 1;
            }
            int x;
            int foo(int m){return 1;}
        '''
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_expr_return_not_suitable(self):
        input = '''
            float f(int a, int b){return 1;}
            int main(int b){
                return f(b, b);
            }
        '''
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(f),[Id(b),Id(b)]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_expr_return_not_suitable_arraypointer(self):
        input = '''
            void main(){return;}
            float[] f(int a, int b){ return a;}
        '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_expr_return_coerce(self):
        input = '''
            void main(){return;}
            int m(int a){return 1;}
            float f(){
                int a;
                a = 1;
                {
                    float a;
                    a = 1/4;
                    return m(a);
                }
            }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(m),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_expr_param_is_function(self):
        input = '''
            void main(){return;}
            int x(float a){return 1;}
            int [] m(int a){
                int c;
                c = 1;
                x(f());
                return c;
            }
            float f(){
                return 1.0;
            }
        '''
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_stmt_non_return_with_nonvoid_func(self):
        input = '''
            void main(){m(1);return;}
            int [] m(int a){
                int c[5];
                return;
            }
            float f(){
                return 1.0;
            }
        '''
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_stmt_return_wrong_type(self):
        input = '''
            void main(){return;}
            int [] m(int a){
                int c[5];
                return a;
            }
            float f(){
                return 1;
            }
        '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_stmt_coerce(self):
        input = '''
            void main(){return;}
            int [] m(int a){
                int c[5];
                return c;
            }
            float [] f(){
                int a;
                a = 1;
                return a;
            }
        '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_expr_return_right_type_and_undeclare_mistake(self):
        input = '''
            void main(){return;}
            int [] m(int a){
                f();
                int c[5];
                return c;
            }
            int [] f(){
                f;
                int a;
                a = 1;
                return m(a);
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_expr_return_nested_func(self):
        input = '''
            void main(){return;}
            float f(){return 1;}
            int a(int b){return 1;}
            int x(){
                return a(f());
            }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(a),[CallExpr(Id(f),[])])"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_undecl_in_dowhile(self):
        input = '''
            void main(){return;}
            float f(){return 1.0;}
            int a(int b){return 1;}
            int x(){
                do b*b; while(a(1)==1);
                return 1;
            }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_wrong_type_in_if(self):
        input = '''
            void main(){return;}
            //float f(){return 1.0;}
            //int a(int b){return 1;}
            int x(){
                int a;
                a = 1;
                do 1; while(a+1);
                if (a == 1){return 1;}
                return 1;
            }
            
        '''
        expect = "Type Mismatch In Statement: Dowhile([IntLiteral(1)],BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_wrong_type_in_assign(self):
        input = '''
            int main(){
                int a,b;
                a = 1;b= 1;
                boolean x;
                a = a*b;
                x = a;
            }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_lhs_in_callexpr_array(self):
        input = '''
            int []f(){
                int c[5];
                return c;
            }
            int main(){
                int a;
                a = 1;
                float b;
                b = 1.5;
                f()[a] = a;
                f()[a] = b; 
            }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(CallExpr(Id(f),[]),Id(a)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_lhs_in_assign_stringtype(self):
        input = '''
            string []f(){
                string c[5];
                return c;
            }
            int main(){
                string c[5];
                c[1] = "abcd";
                f()[0] = c[1];
                c[1] = 1;
                return 1;
            }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(c),IntLiteral(1)),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_return_string(self):
        input = '''
            void main(){return;}
            string f(){
                string c[5];
                return "abcd";
            }
            string f1(){
                return 1;
            }
        '''
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_wrongtype_boolean(self):
        input = '''
            void main(){return;}
            string f(int x){
                int a;
                a = 1;
                if (x + 1 == a){}
                if (x + 1 != a){}
                if (x+ 1 + a){}
                return "abcd";
            }
        '''
        expect = "Type Mismatch In Statement: If(BinaryOp(+,BinaryOp(+,Id(x),IntLiteral(1)),Id(a)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_undecl_function_in_param(self):
        input = '''
            int f(int x){return 1;}
            int main(){
                f(u(3));
            }
        '''
        expect = "Undeclared Function: u"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_stmt_forstmt(self):
        input = '''
            int f(int x){return 1;}
            int main(){
                int a;
                a = 1;
                for (a; a > 1; a = a + 1) a + 1;
                f(1);
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_stmt_forstmt_1(self):
        input = '''
            int f(int x){return 1;}
            int main(){
                int a;
                a = 1;
                for (a; a > 1; a == a) f(2);
            }
        '''
        expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(>,Id(a),IntLiteral(1));BinaryOp(==,Id(a),Id(a));CallExpr(Id(f),[IntLiteral(2)]))"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_not_return_simple(self):
        input = '''
            void main(){return;}
            int f(){
                f();
            }
        '''
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_not_return_simple_with_ifelse(self):
        input = '''
            void main(){return;}
            int f(){
                if (1 == 1){
                    return 1;
                }
                else{}
            }
        '''
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_not_return_simple_with_many_blocks(self):
        input = '''
            void main(){f();return;}
            int f(){
                {
                    int a;
                }
                {int b; {}}
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_not_return_simple_with_many_stmt(self):
        input = '''
            void main(){
                f();
                return;
            }
            int f(){
                int a, b;
                a = 1;b = 1;
                if (a == 1){}
                else{}
                do a; b; return a; while(a==b);
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_not_return_simple_with_many_stmt_ifelse(self):
        input = '''
            void main(){f();return;}
            int f(){
                int a;
                a = 1;
                if (a == 1){
                    if (a == 2){
                        return 3;
                    }
                    else{
                        if (a == 4){return 3;}
                    }
                }
            }
        '''
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_not_return_simple_with_many_stmt_ifelse_2(self):
        input = '''
            void main(){f();return;}
            int f(){
                int a;
                a = 1;
                if (a == 1){
                    if (a == 2){
                        return 3;
                    }
                    else{
                        if (a == 4){return 3;}
                    }
                }
                return a;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_not_return_simple_with_many_for_stmt_and_ifelse(self):
        input = '''
            void main(){f();return;}
            int f(){
                int a;
                a = 1;
                if (a == 1){
                    if (a == 2){
                        return 3;
                    }
                    else{
                        if (a == 4){return 3;}
                    }
                    return 3;
                }
                else{
                    for (a; a > 1; a = a + 1){
                        int b;
                        return 1;
                    }
                }
            }
        '''
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_break_in_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                if (a == 1){break;}
                else{a;}
                return 1;
            }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_break_simple(self):
        input = '''
            int main(){
                break;
                return 1;
            }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_continue_in_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                if (a == 1){continue;}
                else{a;}
                return 1;
            }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_continue_simple(self):
        input = '''
            int main(){
                continue;
                return 1;
            }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_continue_in_for_with_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                for (a; a >1; a=a+1){
                    if (a == 1){
                        continue;
                    }
                    else {}
                }
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_break_in_for_with_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                for (a; a >1; a=a+1){
                    if (a == 1){
                        continue;
                    }
                    else {break;}
                }
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_continue_in_dowhile_with_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                do{
                    if (a == 1){
                        continue;
                    }
                    else {}
                }while(a == 1);
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_continue_and_break_in_dowhile_with_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                do{
                    if (a == 1){
                        continue;
                    }
                    else {break;}
                }while(a == 1);
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_no_entry_point_exist_main_var(self):
        input = '''
            int main;
            int f(){return 1;}
        '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_no_entry_point_no_main(self):
        input = '''
            int f(){return 1;}
        '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_no_entry_point_with_main(self):
        input = '''
            int main(int a){f();return a;}
            int f(){return 1;}
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_unary_op_with_boolean(self):
        input = '''
            int main(boolean a){
                if (a == a) return 1;
                else {
                    if (!a) return 3;
                    else return -3;
                }            
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_unreach_func_with_one_main(self):
        input = '''
            int main(boolean a){
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_unreach_func_with_one_main_and_some_func(self):
        input = '''
            int main(boolean a){
                return f();   
            }
            int foo(){
                return f();
            }
            int f(){
                return foo();
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_unreach_func_with_mistake(self):
        input = '''
            int main(boolean a){
                return f();   
            }
            int foo(){
                return 1;
            }
            int f(){
                return f();
            }
        '''
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_arraycell_operation(self):
        input = '''
            int main(boolean a){
                int b, c,d;
                b = c=d= 1;
                foo()[1] == b*c + d%2;
                return foo()[0];
            }
            int[] foo(){
                int a[5];
                return a;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_not_left_value_wrong(self):
        input = '''
            int main(boolean a){
                int b, c,d;
                b = 1;c = 1;d=1;
                b + c = c + d;
                return 1;
            }
        '''
        expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_not_left_value_with_id_right(self):
        input = '''
            int main(boolean a){
                int b, c,d;
                b = c=d=1;
                b = c + d;
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_not_left_value_with_arraycell_right(self):
        input = '''
            int [] foo(){
                int c[5];
                return c;
            }
            int main(boolean a){
                int b, c,d;
                b = c= d= 1;
                foo()[foo()[2]] = c + d * b;
                return 1;
            }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_not_left_value_with_arraycell_wrong(self):
        input = '''
            int [] foo(){
                int c[5];
                return c;
            }
            int main(boolean a){
                int b, c,d;
                c = 1;b=1;d=1;
                -foo()[foo()[2]]= c + d * b;
                return 1;
            }
        '''
        expect = "Not Left Value: UnaryOp(-,ArrayCell(CallExpr(Id(foo),[]),ArrayCell(CallExpr(Id(foo),[]),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_index_out_range_constant_in_not_constant(self):
        input = '''
            int main(boolean a){
                float d[5];
                d[d[d[5]]] = 2;
                return 1;
            }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(d),ArrayCell(Id(d),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_index_out_range_constant_negative_idx(self):
        input = '''
            int main(boolean a){
                float d[5];
                d[1.0] = 2;
                return 1;
            }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(d),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_arrypointer_with_normal_func(self):
        input = '''
            int f(){return 1;}
            int main(boolean a){
                f()[1] == 1;
                return 1;
            }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_index_out_range_constant_in_not_constant_negative_idx(self):
        input = '''
            int main(boolean a){
                float d[5];
                d[d[d[-5]]] = 2;
                return 1;
            }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(d),ArrayCell(Id(d),UnaryOp(-,IntLiteral(5))))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_unreachstmt_simple(self):
        input = '''
            int main(boolean a){
                float d[5];
                return 1;
                d[d[d[-5]]] = 2;
            }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(d),ArrayCell(Id(d),UnaryOp(-,IntLiteral(5))))"
        self.assertTrue(TestChecker.test(input,expect,476))
