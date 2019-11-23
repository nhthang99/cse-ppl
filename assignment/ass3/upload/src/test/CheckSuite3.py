import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    def test_redeclare_simple(self):
        """Simple redeclare: int a; int a; """
        input = '''int a;
        int a;
        int main(){
            return 1;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_redeclare_different_type(self):
        """Simple redeclare: int a; float a; """
        input = '''int a;
        float a;
        int main(){
            return 1;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_redeclare_array_type(self):
        """Simple redeclare: int a; string a[6]; """
        input = '''int a;
        string a[6];
        int main(){
            return 1;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_redeclare_para(self):
        """Simple redeclare: void main(int a, int a){
        } """
        input = '''void main(int a, int a){
            return;
        }'''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_redeclare_block(self):
        input = '''void main(int a, int b){
            int c;
            float c;
            return;
        }'''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_redeclare_block1(self):
        input = '''void main(int a, int b){
            int c;
            float b;
            return;
        }'''
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_redeclare_block2(self):
        input = '''void main(int a, int b){
            int c;
            float d;
            {
                int e;
                string e[8];
            }
            return;
        }'''
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_redeclare_func(self):
        input = '''
            int main1;
            void main1(int a, int b){
                int c;
                float d;
                {
                    int e;
                    string f[8];
                }
                return;
            }
            int main(){
                main1(1,2);
            return 1;
        }   '''
        expect = "Redeclared Function: main1"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_redeclare_func1(self):
        input = '''
            int a;
            float b;
            void main(){
                return;
            }
            string c[6];
            float main(int a, int b){
                int c;
                return 1.6;
            }'''
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_redeclare_block3(self):
        input = '''void main(int a, int b){
            int c;
            float d;
            {
                int c;
                string e[8];
            }
            return;
        }'''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_redeclare_block4(self):
        input = '''void main(int a, int b){
            int c;
            float d;
            {
                int f;
                string e[8];
            }
            float c;
            return;
        }'''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_redeclare_block5(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            {
                int g;
                int h;
                {
                    int i;
                    float i;
                }
            }
            return;
        }'''
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_redeclare_block6(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            {
                int g;
                int h;
                {
                    int i;
                    float j;
                }
                string g;
            }
            return;
        }'''
        expect = "Redeclared Variable: g"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_redeclare_para1(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            {
                int g;
                int h;
                {
                    int i;
                    float j;
                }
            }
            boolean d;
            return;
        }'''
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_redeclare_if(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            if (a>0){
                int e;
                string c;
                float e;
            }
            return;
        }'''
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_redeclare_if1(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            if (a>0){
                int e;
                string c;
                float a;
            }
            else{
                string m;
                float m;
            }
            return;
        }'''
        expect = "Redeclared Variable: m"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_redeclare_for(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            for(f=0;f<5;f=f+1){
                int f;
                float x;
                string x;
            }
            return;
        }'''
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_redeclare_dowhile(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            do
            {
                int a;
                float a;
            }
            a=1;
            while(false);
            return;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_redeclare_dowhile1(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            do
            {
                int e;
                float f;
            }
            {
                string c;
                boolean c;
            }
            a=9;
            while(true);
            return;
        }'''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_undeclare_func(self):
        input = '''
        int a;
        void main(){
            foo(3);
            return;
        }
        '''
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_undeclare_func1(self):
        input = '''
        int a;
        void main(){
            int m;
            {
                foo(a);
            }
            return;
        }
        '''
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_undeclare_func2(self):
        input = '''
        int foo(){
            return 1;
        }
        int a;
        void main(){
            int m;
            {
                foo();
            }
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_undeclare_func_last(self):
        input = '''
        int a;
        void main(){
            int m;
            {
                foo(a);
            }
            return;
        }
        int foo(int para){
            return 1;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_undeclare_func3(self):
        input = '''
        int a;
        void main(){
            int m;
            {
                main(foo(3));
            }
            return;
        }
        '''
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_undeclare_func4(self):
        input = '''
        int foo;
        void main(){
            int m;
            {
                main(foo(3));
            }
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_undeclare_func5(self):
        input = '''
        void main(){
            int m;
            {
                int foo;
                main(foo(3));
            }
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_undeclare_iden(self):
        input = '''
        int a;
        void main(){
            int m;
            {
                b=4;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_undeclare_iden1(self):
        input = '''
        void b(int a, string c){
            a=1;
            return;
        }
        int a;
        void main(){
            b(1,"s");
            int m;
            {
                b=4;
            }
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_undeclare_iden2(self):
        input = '''
        void b(int a, string c){
            int b;
            a=1;
            return;
        }
        void main(){
            int m;
            b(1,"s");
            {
                b=4;
            }
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),IntLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_undeclare_iden_bina(self):
        input = '''
        int a;
        void main(){
            int m;
            m=9;
            {
                a=b+m;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_undeclare_iden_una(self):
        input = '''
        int a;
        void main(){
            int m;
            {
                a=-b;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_undeclare_cell(self):
        input = '''
        int a[6];
        void main(){
            int m;
            {
                a[c*2+1]=1;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_undeclare_cell1(self):
        input = '''
        int a[6];
        void main(){
            int m;
            m=9;
            {
                b[m*2+1]=1;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_undeclare_if(self):
        input = '''
        int a[6];
        void main(){
            int m;
            m=-1;
            if(k<m){
                m=6;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_undeclare_if1(self):
        input = '''
        int a[6];
        void main(){
            int m;
            m=5;
            if(k<m){
                m=6;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_undeclare_for(self):
        input = '''
        int a[6];
        void main(){
            int m;
            m=9;
            for(x=0;m<6;m+1){
                a[1]=m;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_undeclare_for1(self):
        input = '''
        int a[6];
        void main(){
            int m;
            for(m=1;m<d;m+1){
                a[1]=m;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_undeclare_for2(self):
        input = '''
        int a[6];
        void main(){
            int m;
            for(m=1;m<10;m=m+t){
                a[1]=m;
            }
            return;
        }
        '''
        expect = "Undeclared Identifier: t"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_undeclare_return(self):
        input = '''
        int a[6];
        int main(){
            int m;
            for(m=1;m<10;m=m+1){
                a[1]=m;
            }
            g=1;
            return 1;
        }
        '''
        expect = "Undeclared Identifier: g"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_undeclare_do(self):
        input = '''
        int a[6];
        int main(){
            string m;
            do b=a[0]+1;
            m="7";
            while(a[3]==6);
            return 1;
        }
        '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_undeclare_do1(self):
        input = '''
        int a[6];
        int main(){
            string m;
            do a[1]=a[0]+1;
            m="7";
            while(x==6);
            return 1;
        }
        '''
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_type_mis_state_if(self):
        input = '''
        int a;
        int main(){
            string m;
            if(a){
                a=6;
            }
            return 1;
        }
        '''
        expect = "Type Mismatch In Statement: If(Id(a),Block([BinaryOp(=,Id(a),IntLiteral(6))]))"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_type_mis_state_if1(self):
        input = '''
        boolean a;
        int main(){
            string m;
            if(a){
                a=true;
            }
            return 1;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_type_mis_state_return(self):
        input = '''
        boolean a;
        int main(){
            string m;
            if(a){
                a=false;
            }
            return true;
        }
        '''
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_type_mis_state_return1(self):
        input = '''
        boolean a;
        int main(){
            string m;
            {
                a=true;
                return 1.6;
            }
        }
        '''
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.6))"
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_type_mis_state_return2(self):
        input = '''
        boolean a;
        int b;
        int main(){
            string m;
            {
                a=true;
                for(b=0;b<1;b=b+1){
                    if(b>0) return 3;
                }
                do return "a";
                while(true);
            }
        }
        '''
        expect = "Type Mismatch In Statement: Return(StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_type_mis_state_return_pointer(self):
        input = '''
        int b;
        int a[5];
        int[] main1(){
            return a;
        }
        int[] main(){
            string m;
            return main1();
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_type_mis_state_return_pointer1(self):
        input = '''
        int b;
        int a[5];
        float[] main1(){
            return a;
        }
        float main(){
            main1();
            return 1;
        }
        '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_type_mis_state_return_pointer2(self):
        input = '''
        int b;
        int a;
        int[] main1(){
            return a;
        }
        int main(){
            main1();
            return 1;
        }
        '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_type_mis_state_return_pointer3(self):
        input = '''
        int b;
        boolean c[6];
        boolean[] a(){
            return c;
        }
        int[] main1(){
            return a();
        }
        void main(){
            main1();
            return;
        }
        '''
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(a),[]))"
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_type_mis_state_return_void(self):
        input = '''
        int a;
        void main(){
            return 1;
        }
        '''
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_type_mis_expr_array_cell(self):
        input = '''
        int a;
        int b[4];
        void main(){
            b[true];
        }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_type_mis_expr_array_cell1(self):
        input = '''
        int a;
        int b[4];
        void main(){
            b[a+4];
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_type_mis_expr_array_cell2(self):
        input = '''
        int a;
        int b[4];
        void main(){
            a[2];
        }
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_type_mis_expr_array_cell3(self):
        input = '''
        int a;
        int b[4];
        int[] foo(){
            return b;
        }
        void main(){
            foo()[1];
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_type_mis_expr_array_bool(self):
        input = '''
        boolean a;
        int b;
        void main(){
            a=b;
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_type_mis_expr_array_bool1(self):
        input = '''
        boolean a;
        float f;
        void main(){
            f&&a;
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(f),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_type_mis_expr_int_float(self):
        input = '''
        int a;
        float f;
        void main(){
            f=a+1;
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_type_mis_expr_int_float1(self):
        input = '''
        int a;
        float f;
        void main(){
            a=f*1;
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(*,Id(f),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_type_mis_expr_int_float2(self):
        input = '''
        int a[10];
        float f;
        void main(){
            a[4]=f*1;
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(4)),BinaryOp(*,Id(f),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_type_mis_expr_int_float3(self):
        input = '''
        float a[10];
        float f;
        void main(){
            a[4]=11;
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_type_mis_expr_func(self):
        input = '''
        float a[10];
        int c(){
            return 6;
        }
        void main(){
            a[5]=c()+4.5;
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_type_mis_expr_func1(self):
        input = '''
        int a[10];
        float c(){
            return 4;
        }
        void main(){
            a[5]=c()*2;
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(5)),BinaryOp(*,CallExpr(Id(c),[]),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_type_mis_expr_func2(self):
        input = '''
        int a[10];
        int b[3];
        float c(){
            return 4;
        }
        void main(){
            a[5]=a+b;
            c();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_type_mis_expr_una(self):
        input = '''
        boolean a;
        boolean b;
        float c(){
            return 4;
        }
        void main(){
            a=!b;
            a=-b;
            c();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_type_mis_expr_una1(self):
        input = '''
        int a;
        int b;
        float c(){
            return 4;
        }
        void main(){
            a=-b;
            a=!b;
            c();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_type_mis_expr_una2(self):
        input = '''
        float a;
        float b;
        float c(){
            return 4;
        }
        void main(){
            a=-b;
            a=!b;
            c();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_type_mis_expr_ass(self):
        input = '''
        float a;
        float b;
        int d[4];
        int c(){
            return 1;
        }
        void main(){
            d[1] = 2;
            d=5;
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_type_mis_expr_ass1(self):
        input = '''
        float a;
        float b[9];
        float c(){
            return 1.1;
        }
        float d(){
            return 1;
        }
        void main(){
            a=d();
            b=c();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),CallExpr(Id(c),[]))"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_type_mis_expr_ass2(self):
        input = '''
        int a[2];
        int[] c(){
            return a;
        }
        int[] d(){
            return a;
        }
        void main(){
            a=d();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(d),[]))"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_type_mis_expr_func_call(self):
        input = '''
        int a[2];
        void c(int a, int b[], string c,float d){
            return;
        }
        int[] d(int e){
            return a;
        }
        int m(){
            return 69;
        }
        void main(){
            c(1, d(1), "m", 1);
            c(1, a, "m", 1.e5);
            c(m(),d(a[0]),"cc",2.2);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_type_mis_expr_func_call1(self):
        input = '''
        float a[2];
        void c(int a, int b[], string c){
            return;
        }
        float[] d(){
            return a;
        }
        void main(){
            c(1, d(), "m");
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(c),[IntLiteral(1),CallExpr(Id(d),[]),StringLiteral(m)])"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_type_mis_expr_func_call2(self):
        input = '''
        float a[2];
        void c(int a, int b[], string c){
            return;
        }
        float[] d(){
            return a;
        }
        void main(){
            c(1, 2.2, "m");
            d();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(c),[IntLiteral(1),FloatLiteral(2.2),StringLiteral(m)])"
        self.assertTrue(TestChecker.test(input,expect,475))
    def test_type_mis_expr_func_call3(self):
        input = '''
        float a[2];
        void c(int a, int b[], string c){
            return;
        }
        float[] d(){
            return a;
        }
        void main(){
            c(1, a, "m");
            d();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(c),[IntLiteral(1),Id(a),StringLiteral(m)])"
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_type_mis_expr_func_call4(self):
        input = '''
        float a[2];
        void c(int a, int b[], string c){
            return;
        }
        float[] d(){
            return a;
        }
        void main(){
            c(1, a, true);
            d();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(c),[IntLiteral(1),Id(a),BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_type_mis_expr_func_call5(self):
        input = '''
        float a[2];
        void c(int a, int b[], string c){
            return;
        }
        float[] d(){
            return a;
        }
        void main(){
            c(1, a, "vv",true);
            d();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(c),[IntLiteral(1),Id(a),StringLiteral(vv),BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_func_not_ret(self):
        input = '''
        int a(int b){
            if (b<0){
                return 1;
            }
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_func_not_ret1(self):
        input = '''
        int a(int b){
            for(b=0;b<1;b=b+1){
                if (b<0){
                    return 1;
                }
            }
            do{
                return 1;
            }
            while(true);
        }
        void main(){
            int b,c;
            c=2*(b=3);
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_func_not_ret2(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
            }
            else b=2;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_func_not_ret3(self):
        input = '''
        int a(int b){
            if(b>0){
                if(b<0){
                    return 1;
                }
            }
            else return 2;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_func_not_ret4(self):
        input = '''
        int a(int b){
            if(b>0){
                for(b=0;b<1;b=b+1){
                    if(b>0) return 1;
                    else return 2;
                }
            }
            else return 2;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,483))
    def test_func_not_ret5(self):
        input = '''
        int a(int b){
            if(b>0){
                b=b+1;
            }
            else return 2;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_func_not_ret6(self):
        input = '''
        int a(int b){
            do{
                if(b>0) return 1;
                return 2;
            }
            while(false);
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_func_not_ret7(self):
        input = '''
        int a(int b){
            if(b>0){
                if(b>0) return 1;
            }
            else{
                if(b>0) return 1;
                else return 1;
            }
            if(b>0){
                if(b>0) return 1;
                else return 1;
            }
            else{
                if(b>0) return 1;
                else return 1;
            }
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_func_not_ret8(self):
        input = '''
        int a(int b){
            if(b>0){
                if (b>0) return 1;
                else return 1;
            }
            if(b<=0){
                if (b>0) return 1;
                else return 1;
            }
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_func_not_ret9(self):
        input = '''
        int a(int b){
            for(b=0;b<1;b=b+1){
                if(b>0) return 1;
                else return 1;
            }
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_func_not_ret10(self):
        input = '''
        int a(int b){
            do{
                if(b>0) return 1;
                if(b<=0) return 1;
            }
            while(false);
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_func_not_ret11(self):
        input = '''
        int a(int b){
            {
                if (b>0) return 1;
                if(b<0) return 1;
                if (b==0) return 1;
            }
            for(b=0;b<1;b=b*2){
                return 1;
            }
            do{
                if (b>0) return 1;
                if(b<0) return 1;
                if (b==0) return 1;
            }
            while(true);
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Function a Not Return "
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_break_loop(self):
        input = '''
        int a(int b){
            for (b=0;b<1;b=b/2){
                if(b>0) break;
                else break;
            }
            do{
                break;
            }
            while(true);
            do break;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_break_loop1(self):
        input = '''
        int a(int b){
            break;
            do break;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_break_loop2(self):
        input = '''
        int a(int b){
            {
                b=1;
                break;
            }
            do break;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_break_loop3(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
                break;
            }
            do break;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_break_loop4(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
            }
            else break;
            do break;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_continue_loop(self):
        input = '''
        int a(int b){
            for (b=0;b<1;b=b/2){
                if(b>0) continue;
                else continue;
            }
            do{
                continue;
            }
            while(true);
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_continue_loop1(self):
        input = '''
        int a(int b){
            continue;
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_continue_loop2(self):
        input = '''
        int a(int b){
            {
                b=1;
                continue;
            }
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_continue_loop3(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
                continue;
            }
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_continue_loop4(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
            }
            else continue;
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,500))
    def test_continue_break_loop(self):
        input = '''
        int a(int b){
            for(b=0;b<1;b=b+1){
                if(b>0) break;
                else continue;
            }
            do{
                continue;
            }
            while(true);
            break;
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_no_entry(self):
        input = '''
        int a;
        int b;
        '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,502))
    def test_no_entry1(self):
        input = '''
        int a;
        int b;
        int main;
        '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,503))
    def test_no_entry2(self):
        input = '''
        int a;
        int b;
        int main;
        int c(){
            e();
            return 2;
        }
        int e(){
            c();
            return 1;
        }
        '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,504))
    def test_unreach_func(self):
        input = '''
        int a;
        int b;
        int c(){
            return 1;
        }
        int main(){
            return 1;
        }
        '''
        expect = "Unreachable Function: c"
        self.assertTrue(TestChecker.test(input,expect,505))
    def test_unreach_func1(self):
        input = '''
        int a;
        int b;
        int c(){
            c();
            return 1;
        }
        int main(){
            return 1;
        }
        '''
        expect = "Unreachable Function: c"
        self.assertTrue(TestChecker.test(input,expect,506))
    def test_unreach_func2(self):
        input = '''
        int a;
        int b;
        int c(){
            return 1;
        }
        int main(){
            if(2>1) c();
            return 1;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,507))
    def test_unreach_func3(self):
        input = '''
        int a;
        int b;
        int c(){
            c();
            return 1;
        }
        float d(int a){
            return a;
        }
        int main(){
            d(1);
            return 1;
        }
        '''
        expect = "Unreachable Function: c"
        self.assertTrue(TestChecker.test(input,expect,508))
    def test_unreach_func4(self):
        input = '''
        int a;
        int b;
        int c(){
            e();
            return 1;
        }
        float d(int a){
            d(22);
            return a;
        }
        int e(){
            d(3);
            return 1;
        }
        int main(){
            d(1);
            return 1;
        }
        '''
        expect = "Unreachable Function: c"
        self.assertTrue(TestChecker.test(input,expect,509))
    def test_type_mis_expr_LHSVoid(self):
        input = '''
        void a(){
            return;
        }
        void b(){
            return;
        }
        void main(){
            int a;
            a = b();
            return;
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(b),[]))"
        self.assertTrue(TestChecker.test(input,expect,510))
    def test_not_left(self):
        input = '''
        int b(){
            return 1;
        }
        void main(){
            int a;
            a=69;
            a+2 = b();
            return;
        }
        '''
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,511))
    def test_not_left1(self):
        input = '''
        int b(){
            return 1;
        }
        void main(){
            float a;
            a=0;
            a+2 = b();
            return;
        }
        '''
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,512))
    def test_not_left2(self):
        input = '''
        int b(){
            return 1;
        }
        void main(){
            float a;
            b() = 1*2;
            return;
        }
        '''
        expect = "Not Left Value: CallExpr(Id(b),[])"
        self.assertTrue(TestChecker.test(input,expect,513))
    def test_unreach_state(self):
        input = '''
        int a(int b){
            for(b=1;b<1;b=b+1){
                if(b>0) return 1;
                else break;
            }
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,514))
    # def test_unreach_state1(self):
    #     input = '''
    #     int a(int b){
    #         if(b>0) return 1;
    #         else return 2;
    #         return 3;
    #     }
    #     void main(){
    #         a(1);
    #         return;
    #     }
    #     '''
    #     expect = "Unreachable Statement: Return(IntLiteral(3))"
    #     self.assertTrue(TestChecker.test(input,expect,515))
    # def test_unreach_state2(self):
    #     input = '''
    #     int a(int b){
    #         if(b==1) return 1;
    #         return 0;
    #         return 2;
    #     }
    #     void main(){
    #         a(1);
    #         return;
    #     }
    #     '''
    #     expect = "Unreachable Statement: Return(IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,516))
    # def test_unreach_state3(self):
    #     input = '''
    #     int a(int b){
    #         do{
    #             b=1;
    #             break;
    #             b=2;
    #         }
    #         while(true);
    #         return 1;
    #     }
    #     void main(){
    #         a(1);
    #         return;
    #     }
    #     '''
    #     expect = "Unreachable Statement: BinaryOp(=,Id(b),IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,517))
    # def test_unreach_state4(self):
    #     input = '''
    #     int a(int b){
    #         if(b>0){
    #             if(b<0){
    #                 return 1;
    #             }
    #             else{
    #                 return 1;
    #                 }
    #         }
    #         else return 2;
    #         return 1;
    #     }
    #     void main(){
    #         a(1);
    #         return;
    #     }
    #     '''
    #     expect = "Unreachable Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,518))
    def test_unreach_state5(self):
        input = '''
        int a(int b){
            do{
                break;
            }
            while(true);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,519))
    # def test_unreach_state6(self):
    #     input = '''
    #         int main(){
    #         float a;
    #         a = 7.5;
    #         float b;
    #         b = 10.0;
    #         int c;
    #         c = 8;
    #         for (c; true; c + 1){
    #             do
    #                 c = c + 1;
    #                 for (4; true; 5){
    #                     if (a > b)
    #                        break;
    #                     c = c - 1;
    #                 }
    #                 a = a + 1; 
    #             while(true);

    #             if (true){
    #                 continue;
    #             }
    #             else
    #                 break;
    #             break;
    #         }
    #         return 0;
    #     }
    #     '''
    #     expect = "Unreachable Statement: Break()"
    #     self.assertTrue(TestChecker.test(input,expect,520))
    # def test_index_out_range(self):
    #     input = '''
    #         int main(){
    #             int a[4];
    #             a[5] = 1;
    #             return 1;
    #         }
    #     '''
    #     expect = "Index Out Of Range: ArrayCell(Id(a),IntLiteral(5))"
    #     self.assertTrue(TestChecker.test(input,expect,521))
    # def test_index_out_range1(self):
    #     input = '''
    #         int main(){
    #             int a[4];
    #             a[-4] = 1;
    #             return 1;
    #         }
    #     '''
    #     expect = "Index Out Of Range: ArrayCell(Id(a),UnaryOp(-,IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,522))
    # def test_index_out_range2(self):
    #     input = '''
    #         int main(){
    #             int a[4];
    #             a[-1*-2] = 1;
    #             a[-((1*2+1)/3+2)+3]=9;
    #             a[6*9] = 1;
    #             return 1;
    #         }
    #     '''
    #     expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(*,IntLiteral(6),IntLiteral(9)))"
    #     self.assertTrue(TestChecker.test(input,expect,523))
    # def test_index_out_range3(self):
    #     input = '''
    #         int main(){
    #             int a[4];
    #             a[0] = 1;
    #             a[-69*2]=3;
    #         }
    #     '''
    #     expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(*,UnaryOp(-,IntLiteral(69)),IntLiteral(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,524))
    # def test_uni_var(self):
    #     input = '''
    #         int a;
    #         int main(){
    #             int a;
    #             int b;
    #             b=a;
    #             return 1;
    #         }
    #     '''
    #     expect = "Uninitialized Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,525))
    # def test_uni_var1(self):
    #     input = '''
    #         int a;
    #         int main(){
    #             int a;
    #             {a=1;}
    #             for(a;a<1;a=a+1){
    #                 a=2;
    #             }
    #             int b;
    #             a=b;
    #             return 1;
    #         }
    #     '''
    #     expect = "Uninitialized Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,526))
    # def test_uni_var2(self):
    #     input = '''
    #         int a;
    #         int main(){
    #             int a;
    #             int b;
    #             int c;
    #             int d;
    #             a=1;
    #             if(a>0){
    #                 b=1;
    #             }
    #             d=c;
    #             return 1;
    #         }
    #     '''
    #     expect = "Uninitialized Variable: c"
    #     self.assertTrue(TestChecker.test(input,expect,527))
    # def test_uni_var3(self):
    #     input = '''
    #         int a;
    #         int main(){
    #             int a;
    #             int b;
    #             int c;
    #             int d;
    #             a=1;
    #             if(a>0){
    #                 b=1;
    #             }
    #             else c=1;
    #             c=d;
    #             return 1;
    #         }
    #     '''
    #     expect = "Uninitialized Variable: d"
    #     self.assertTrue(TestChecker.test(input,expect,528))
    # def test_uni_var4(self):
    #     input = '''
    #         int a;
    #         int main(){
    #             int b;
    #             do{
    #                 b=1;
    #             }
    #             while(true);
    #             int c;
    #             c=b;
    #             int d;
    #             float e;
    #             e=d;
    #             return 1;
    #         }
    #     '''
    #     expect = "Uninitialized Variable: d"
    #     self.assertTrue(TestChecker.test(input,expect,529))
    def test_forum(self):
        input = '''
        int foo() {
            return 3;
        }
        void main() {
            foo[3];
            return; 
        }'''
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,530))
    def test_forum1(self):
        input = '''
        int pow(int a, int n) {
            return a * pow(a, n-1);
        }
        void main() {
            int pow;
            pow = 2;
            pow(pow, 4);
        }
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(pow),[Id(pow),IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,531))