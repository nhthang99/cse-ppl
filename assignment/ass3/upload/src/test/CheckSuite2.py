import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_no_entry_point_with_name_func_not_main(self):
        input = """
        int foo() { return 1; }
        int main(){
            int foo;
            foo();
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point_with_name_func_not_main_many_param(self):
        input = """
        void man(int a, float b, string a){
            
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_no_entry_point_with_no_function_main(self):
        input = """
        int main;
        string foo(int a, string b[]){
            return "Tan Dai";
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclare_param(self):
        input = """
        int main(int a,float a){
            return 1;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_variable_with_two_variable(self):
        input = """
        int a; 
        void main(){}  
        float a;    
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare_variable_with_variable_and_function(self):
        input = """
        void a(){}
        int a; 
        void main(){}      
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare_function_with_variable_and_function(self):
        input = """
        int a; 
        void a(){} 
        void main(){}      
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_function_with_variable_and_function_and_variable(self):
        input = """
        int a; 
        void a(){} 
        int a;
        void main(){}      
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclare_in_block(self):
        input = """
        int a; 
        void main(int b){
            int a;
            int a;
        }     
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_correct_with_same_varDecl_diff_scope(self):
        input = """
        int a; 
        void main(int b,int bb){
            float a;
            int m;
            
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_correct_with_varDecl_diff_scope_in_many_block(self):
        input = """
        float a; 
        void main(int b,int bb){
            float a;
            int m;
            {
                float a;
                {
                    float a;
                }
            }
            
        }    
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_mismatch_stmt_condition_expr_in_if_is_Int(self):
        input = """
        int a; 
        void main(){
            a=1;
            if(a+1){}
        }   
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(1)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_mismatch_stmt_condition_expr_in_if_is_String(self):
        input = """
        int a; 
        void main(){
            if("My name is Dai"){
                a = 1;
            }
        }   
        """
        expect = "Type Mismatch In Statement: If(StringLiteral(My name is Dai),Block([BinaryOp(=,Id(a),IntLiteral(1))]))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_mismatch_stmt_condition_expr_in_if_is_Float(self):
        input = """
        string a; 
        void main(){
            if(1.5){
                a = "Dai";
            }
        }   
        """
        expect = "Type Mismatch In Statement: If(FloatLiteral(1.5),Block([BinaryOp(=,Id(a),StringLiteral(Dai))]))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_correct_stmt_condition_expr_in_if_is_bool(self):
        input = """ 
        void main(){
            if(true){

            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_mismatch_stmt_condition_expr_in_doWhile_is_Float(self):
        input = """
        void main(){
            do{

            }while(9.8);
        }   
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],FloatLiteral(9.8))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_mismatch_stmt_condition_expr_in_doWhile_is_Binary(self):
        input = """
        string a; 
        void main(){
            do{

            }while((1 + 3.5)/4);
        }   
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],BinaryOp(/,BinaryOp(+,IntLiteral(1),FloatLiteral(3.5)),IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input,expect,416))

    
    def test_correct_stmt_condition_expr_in_DoWhile_is_bool(self):
        input = """ 
        int a;
        void main(){
            do{
                a = 7;  
            }  
            while(true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417))

    
    def test_mismatch_stmt_condition_expr_in_for_exp1_string(self):
        input = """
        string a; 
        void main(){
            
            for("a";true;10){
                int a;
            }
        }   
        """
        expect = "Type Mismatch In Statement: For(StringLiteral(a);BooleanLiteral(true);IntLiteral(10);Block([VarDecl(a,IntType)]))"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_mismatch_stmt_condition_expr_in_for_exp2_not_bool(self):
        input = """
        string a; 
        void main(){
            
            for(5;"true";10){
                int a;
            }
        }   
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(5);StringLiteral(true);IntLiteral(10);Block([VarDecl(a,IntType)]))"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_mismatch_stmt_condition_expr_in_for_exp3_not_int(self):
        input = """
        string a; 
        void main(){
            
            for(5;false;10.1){
                int a;
            }
        }   
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(5);BooleanLiteral(false);FloatLiteral(10.1);Block([VarDecl(a,IntType)]))"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_mismatch_stmt_function_int_return_float(self):
        input = """
        int main(){
            return 1.1;
        } 
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_mismatch_stmt_function_float_return_not_float(self):
        input = """
        float main(){
            return "dai";
        } 
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(dai))"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_mismatch_stmt_function_string_return_not_string(self):
        input = """
        string main(){
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_mismatch_stmt_function_arrTypeString_return_not_arrString(self):
        input = """
        string[] main(){
            int a[5];
            return a;
        }  
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_mismatch_stmt_function_arrTypeint_return_not_arrint(self):
        input = """
        int[] main(){
            float a[5];
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_mismatch_stmt_function_void_return_exp(self):
        input = """
        
        void main(){
            int a;
            a = 10;
            {
                if(a==1){
                    a = a+1;
                }
            }
            return a + 1;
        }   
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,426))

        
    def test_correct_function_float_return_int(self):
        input = """
        
        float main(){
            int a;
            a = 10;
            {
                if(a==1){
                    a = a+1;
                }
            }
            return a + 1;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undecl_function_not_param(self):
        input = """
        
        void main(){
            foo();
        }   
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undecl_function_many_param(self):
        input = """
        
        void main(){
            foo(1,"dai",2.2);
        }   
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_correct_decl_function(self):
        input = """
        int foo(int a,string b,float c){
            return 1;
        }
        void main(){
            foo(1,"dai",10);
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))


    def test_undecl_identifier(self):
        input = """
        
        void main(){
            a = 10;
        }   
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undecl_identifier_beyond_scope(self):
        input = """
        
        void main(){
            {
                float a;
            }
            a = 10.1;
        }   
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undecl_identifier_beyond_many_scope(self):
        input = """
        
        void main(){
            {
                
                {
                    {
                        string b;
                    }
                    b = "dai";
                }
            }
            
        }   
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_correct_vardecl(self):
        input = """
        
        void main(){
            int a;
            {
                {
                    a = 1;
                }
            }
            
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_break_not_in_loop(self):
        input = """
        
        void main(){
            break;
        }   
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_break_not_in_loop_stmt_if(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                break;
            }
        }   
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_break_not_in_loop_stmt_if_else(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                a = a+2;
            }
            else 
                break;
        }   
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_continue_not_in_loop(self):
        input = """
        
        void main(){
            continue;
        }   
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_continue_not_in_loop_stmt_if(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                continue;
            }
        }   
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_continue_not_in_loop_stmt_if_else(self):
        input = """
        int a;
        void main(){
            a = 1;
            if(true){
                a = a+2;
            }
            else 
                continue;
        }   
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_unreachable_func(self):
        input = """
        
        void a(){
            
        }
        void foo(){
            a();
        }
        
        void main(){
            
        }   
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_unreachable_func_nested_block(self):
        input = """
        
        void a(){
            
        }
        void b(){}
        void foo(){
            { 
                a();
            }
        }
        
        void main(){
            {
                {
                    foo();
                }
            }
        }   
        """
        expect = "Unreachable Function: b"
        self.assertTrue(TestChecker.test(input,expect,442))


    def test_unreachable_func_with_recursion(self):
        input = """
        
        void a(){
            a();
        }
        void b(){
            b();
            b();
        }
        void foo(){
            foo();
        }
        
        void main(){
            a();
            {
                b();
            }
        }   
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_not_left_value_with_var(self):
        input = """
        int a ;
        void main(){
            a + 1 = 10 ;
        }   
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_not_left_value_with_exp_left_not_storage(self):
        input = """
        int a ;
        void main(){
            3 = a;
        }   
        """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_not_left_value_with_exp_left_not_storage_function(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            3 + 1 = foo();
        }   
        """
        expect = "Not Left Value: BinaryOp(+,IntLiteral(3),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_not_left_value_with_function(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            foo() = 10 ;
        }   
        """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_not_left_value_with_arraycell(self):
        input = """
        int a[6],b[7],c[8];
        void main(){
            b[1] + 1 = c[7] + 10;
        } 
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(b),IntLiteral(1)),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_correct_left_value_with_var(self):
        input = """
        int a,b,c;
        void main(){
            a = b = c = 10;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_correct_left_value_with_var2(self):
        input = """
        int a,b,c;
        void main(){
            a = b = c = (10+3)/4 + 5*9 - 2;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_correct_left_value_with_arraycell(self):
        input = """
        int a[6],b[7],c[8];
        void main(){
            a[1] = a[2] = a[4] + 10;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_correct_left_value_with_arraycell_2(self):
        input = """
        int a[6],b[7],c[8];
        void main(){
            a[1] = b[1] = c[7] + 10%5;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_TypeMismatchExpr_ArrayCell_with_type_idx_float(self):
        input = """
        void main(){
            int a[5];
            a[1.2] = 5;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_TypeMismatchExpr_ArrayCell_with_type_idx_string(self):
        input = """
        void main(){
            int a[5];
            a["1"] = 9;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_TypeMismatchExpr_ArrayCell_with_type_idx_bool(self):
        input = """
        void main(){
            int a[5];
            a[true] = 9;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_TypeMismatchExpr_ArrayCell_with_type_arr_int(self):
        input = """
        void main(){
            int a;
            a[5] = 10;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_TypeMismatchExpr_ArrayCell_with_type_arr_string(self):
        input = """
        void main(){
            string a;
            a[5] = 10;
        }   
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_correct_ArrayCell_with_type_arr_ArrayPointer(self):
        input = """
        void main(int a[], float b){
            a[1] = 9;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))


    def test_TypeMismatchInExpression_IntType_BoolType(self):
        input = """
        void main(){int a; a = true;}   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_TypeMismatchInExpression_Sum_IntType_StringType(self):
        input = """
        void main(){int a; string b; a = 1 + b;}   
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_TypeMismatchInExpression_Unary_with_BoolType(self):
        input = """
        void main(){boolean a,b; b=-a;}   
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_TypeMismatchInExpression_Unary_Minus_with_StringType(self):
        input = """
        void main(){string a,b; b=-a;}   
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,462))


    def test_TypeMismatchInExpression_IntType_FloatType(self):
        input = """
        void main(){
            int a;
            a = 1.1;
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_TypeMismatchInExpression_IntType_Equal_FloatType(self):
        input = """
        void main(){
            int a; 
            a = a+1.0*5;
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),BinaryOp(*,FloatLiteral(1.0),IntLiteral(5))))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_No_TypeMismatchInExpression_FloatType_Equal_FloatType(self):
        input = """
        void main(){
            int a; float b; 
            b = 1.0e1+5.0*a;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_No_TypeMismatchInExpression_FloatType_Equal_IntType(self):
        input = """
        void main(){
            float a; 
            a = 100;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_No_TypeMismatchInExpression_FloatType_Equal_IntType(self):
        input = """
        void main(){
            float a; 
            a = 100;
        }   
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_TypeMismatchInExpression_Operator_MOD_FloatType(self):
        input = """
        void main(){
            float a; 
            a = a % 1.1;
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_TypeMismatchInExpression_IntType_Equal_BoolType(self):
        input = """
        void main(){
            int a; 
            a = true&&(1==1);
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(&&,BooleanLiteral(true),BinaryOp(==,IntLiteral(1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_TypeMismatchInExpression_BoolType_Equal_FloatType(self):
        input = """
        void main(){
            boolean a; 
            a = 1.0 == 1.4;
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLiteral(1.0),FloatLiteral(1.4))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_TypeMismatchInExpression_IntType_Equal_Func_FloatType(self):
        input = """
        float foo(){
            return 9.8;
        }
        void main(){
            int a;
            a = foo();
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_TypeMismatchInExpression_IntType_Equal_ArrayIntType(self):
        input = """
        void main(int b[]){
            {
                int a; a=b;
            }
        }   
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_TypeMismatchInExpression_IntType_Equal_FunctionArrayIntType(self):
        input = """
        int[] foo(){int b[5]; return b;}
        void main(){
            int a; 
            a=foo();
        }  
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_No_TypeMismatchInExpression_IntType_Equal_ArrayElementIntType(self):
        input = """
        
        void main(){
            int a; 
            int b[5];
            a = b[1] + 5;
        }  
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_TypeMismatchInExpression_CallExpr(self):
        input = """
        void main(){
            int a,b; 
            a = b[1];
        }  
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_No_TypeMismatchInExpression_CallExpr(self):
        input = """
        int [] foo(int i)
        {
            int a[5];
            return a;
        }
        void main(){
            int a,c; 
            a=foo(1)[2]+10*4/2;
        } 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_TypeMismatchInExpression_CallExpr_not_ArrayType(self):
        input = """
        int foo(){int a; return a;}
        void main(){
            int a; 
            a=foo()[2];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_TypeMismatchInExpression_CallExpr_number_param_not_equal(self):
        input = """
        void foo(int a,int b,int c){}
        void main(){
            foo(1,2);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_TypeMismatchInExpression_CallExpr_param_not_same_type(self):
        input = """
        void foo(int a,int b){}
        void main(){
            foo(1,2.5);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),FloatLiteral(2.5)])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_No_TypeMismatchInExpression_CallExpr_param_same_element_type(self):
        input = """
        void foo(int a[],int b){}
        void main(){
            int m[5];
            foo(m,2);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_No_TypeMismatchInExpression_CallExpr_param_same__type(self):
        input = """
        void foo(int a[],int b, float c){}
        void main(){
            int m[5];
            int c;
            foo(m, 2 , c = 10);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_FunctionNotReturn_with_if_stmt_return(self):
        input = """
        int main(int a){
            if(a==1)
            {
                return 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_No_FunctionNotReturn_with_both_if_else_stmt_return(self):
        input = """
        int main(int a){
            if(a==1)
                return 1;
            else
                return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_No_FunctionNotReturn_with_return_in_block(self):
        input = """
        int main(int a){
            if(a==1)
                return 1;

            return 0;   
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_No_FunctionNotReturn_with_return(self):
        input = """
        int main(int a){
            do{}
            while(a==1);

            return 0;   
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_FunctionNotReturn_without_return_in_block(self):
        input = """
        int main(int a){
            int i;
            if(a==1)
                return 1;
            
            for(i=0;i<=5;i=i+2){
                return 1 ;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_FunctionNotReturn_with_empty_stm_in_block(self):
        input = """
        int main(int a){
            
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_No_FunctionNotReturn_with_has_return_in_block(self):
        input = """
        int main(int a){

            if(a==1){
                return 1;
            }

            {
                {
                    return 1;
                }
            }
            

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_FunctionNotReturn_with_doWhile(self):
        input = """
        int main(int a){

            if(a==1){
                return 1;
            }
            do{
                if(a==1){
                    return 1;
                }
            }while(false);
            

        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_No_FunctionNotReturn_with_doWhile(self):
        input = """
        int main(int a){

            if(a==1){
                return 1;
            }
            do{
                break;
                continue;
                return 1;
            }while(true);
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_No_FunctionNotReturn_with_if_else_stmt(self):
        input = """
        int main(int a){

            if(a==1){
                return 1;
            }
            else{
                return 1;
            }

            if(true){
                return 1;
            }
            else{
                
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_FunctionNotReturn_with_for_stmt(self):
        input = """
        int main(int a){
            for(a=0;a !=10;a=a+2){
                return 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_No_FunctionNotReturn_with_for_stmt_and_doWhile_has_return(self):
        input = """
        int main(int a){
            for(a=0;a !=10;a=a+2){
                return 1;
            }
            do{
                {
                    if(a==1){
                        return 1;
                    }
                    else{
                        return 0;
                    }
                }
            }while(a==1);

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_FunctionNotReturn_with_if_stmt_and_doWhile_has_return(self):
        input = """
        int main(int a){
            if( a == 1)
                return 1;
            else
                a = a+1;

            do{
                {
                    if(a==1)
                        return 1;
                }
            }while(a==1);

        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_FunctionNotReturn_with_doWhile_nested_For(self):
        input = """
        int main(int a){
            for(a = 0;a >= 10; a = a*5){
                do{
                    return 1;
                }while(a == 5);
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_FunctionNotReturn_with_For_nested_DoWhile(self):
        input = """
        float main(int a){
            do{
                for(a = 0;a >= 10; a = a*5){
                    int b;
                    float c;
                    c = (b + 5 - 10/50)/5;
                    return c;
                }
                
            }while(a == 5);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_No_FunctionNotReturn_with_For_nested_DoWhile(self):
        input = """
        float main(int a){
            do{
                for(a = 0;a >= 10; a = a*5){}
                int b;
                float c;
                c = (b + 5 - 10/50)/5;
                return c;
                
            }while(a == 5);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_No_BreakNotInLoop_with_DoWhile(self):
        input = """
        void main(int a){
            do{
                if(a == 1){
                    break;
                }
            }while(a == 5);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_No_BreakNotInLoop_with_For(self):
        input = """
        void main(int a){
            for(a=1;a>5;a=a-1){
                {
                    {
                        {
                            break;
                        }
                    }
                }
                continue;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_TypeMisMatchInExpr_with_build_in_function(self):
        input = """
        void main(int a){
            putInt(1);
            getInt();
            putStringLn("1");
            putFloat(1);
            putBool(1);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putBool),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,498))


    def test_redeclared_build_in_function(self):
        input = """
        int main(){
            int a;
            a = putInt();
            return 0;
        }
        int putInt(){
            return 1;
        }
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_TypeMismatchExpr_ArrayCell_with_function(self):
        input = """
        int foo() {
            return 1;
        }

        void main() {
            foo[3]; 
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_TypeMismatchExpr_ArrayCell_with_variable(self):
        input = """
        int foo;
        void main(){
            foo[3];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_TypeMismatchExpr_ArrayCell_with_va(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            foo();
            foo;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_simple__un_not_left_value_in_nested_assigmnet(self):
        input = """
        void main(){
            float a;
            a = (a = a-1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,503))
