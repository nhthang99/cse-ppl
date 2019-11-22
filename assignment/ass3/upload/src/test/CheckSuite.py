import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_no_entry_point1(self):
        """ No Entry Point """
        input = """
        int main1(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_no_entry_point2(self):
        """ No Entry Point """
        input = """
        int main1(){}
        int main2(){}
        int main3(){}
        int main4(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclare_global_var1(self):
        """ Global Variable Redeclared """
        input = """
        int a;
        boolean a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclare_global_var2(self):
        """ Global Variable Redeclared """
        input = """
        int a;
        boolean b;
        string c;
        float d;
        float a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_func1(self):
        """ Function Redeclared """
        input = """
        int main(){return 1;}
        void main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare_func2(self):
        """ Function Redeclared """
        input = """
        void main1(){}
        void main2(){}
        int main3(){return 1;}
        int main(){return 0;}
        boolean main1(){return true;}
        """
        expect = "Redeclared Function: main1"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare_param1(self):
        """ Parameter Redeclared """
        input = """
        void main(int a, boolean a){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_param2(self):
        """ Parameter Redeclared """
        input = """
        void main(int a, boolean b){}
        int main2(int a, string b, float a){
            return a;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_id_undeclared1(self):
        input = """void main(){
            a = a + 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_id_undeclared2(self):
        """ Undeclared Identifier """
        input = """
        int a;
        void main(){
            a = a + 1;
            a = a - b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_id_undeclared3(self):
        """ Undeclared Identifier """
        input = """
        void main(){
            float a;
            int b;
            a = a + 1;
            a = a - b;
            a = a / c;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_func_undeclared1(self):
        """ Undeclared Function """
        input = """
        void main(){
            print("Hello");
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_func_undeclared2(self):
        """ Undeclared Function """
        input = """
        void main(){
            int num;
            putInt(num);
            print(getInt());
        }
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_func_undeclared3(self):
        """ Undeclared Function """
        input = """
        int main(){
            int a;
            int b;
            a = sum(a, b);
            a = sub(a, b);
            return a;
        }
        int sum(int a, int b){
            return a + b;
        }
        """
        expect = "Undeclared Function: sub"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_mismatch_condition_ifstmt1(self):
        """ Mismatch Condition(Void) If Statement """
        input = """
        void main(){
            if (print()){}
        }
        void print(){}
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(print),[]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_mismatch_condition_ifstmt2(self):
        """ Mismatch Condition(Int) If Statement """
        input = """
        void main(){
            int a;
            if (getNum(a)){}
        }
        int getNum(int num){
            return num;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getNum),[Id(a)]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_mismatch_condition_ifstmt3(self):
        """ Mismatch Condition(String) If Statement """
        input = """
        void main(){
            string a;
            a = "Hello";
            if (getString(a)){}
            else {}
        }
        string getString(string a){
            return a;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getString),[Id(a)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_mismatch_condition_ifstmt4(self):
        """ Mismatch Condition(Float) If Statement """
        input = """
        void main(){
            int a;
            a = 1;
            int b;
            b = 5;
            if (div(a, b)){}
            else {}
        }
        float div(int a, int b){
            float rlt;
            rlt = a / b;
            return rlt;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(div),[Id(a),Id(b)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,417))

    # TODO: error
    def test_mismatch_condition_ifstmt5(self):
        """ Mismatch Condition(Array) If Statement """
        input = """
        void main(){
            float a[25];
            if (div(a)){}
            else{}
        }
        float[] div(float a[]){
            int i;
            for (i = 0; i < 5; i = i+1){
                a[i] = 1;
            }
            return a;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(div),[Id(a)]),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_mismatch_condition_dowhilestmt1(self):
        """ Mismatch Condition(Int) Dowhile Statement """
        input = """
        void main(){
            do {} while(1);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_mismatch_condition_dowhilestmt2(self):
        """ Mismatch Condition(Float) Dowhile Statement """
        input = """
        void main(){
            int a;
            do {} while(getFloatingPoint(a));
        }
        float getFloatingPoint(int a){
            return a * 1.0;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(getFloatingPoint),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_mismatch_condition_dowhilestmt3(self):
        """ Mismatch Condition(String) Dowhile Statement """
        input = """
        void main(){
            string str;
            do {} while(getStr(str));
        }
        string getStr(string str){
            return str;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(getStr),[Id(str)]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_mismatch_condition_dowhilestmt4(self):
        """ Mismatch Condition(Void) Dowhile Statement """
        input = """
        void main(){
            int a;
            do {} while(putInt(a));
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(putInt),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_mismatch_forstmt1(self):
        """ Mismatch For Statement"""
        input = """
        int main(){
            for (1;2;2){}
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(2);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_mismatch_forstmt2(self):
        """ Mismatch For Statement"""
        input = """
        int main(){
            for (true;true;2){}
        }
        """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);IntLiteral(2);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_mismatch_forstmt3(self):
        """ Mismatch For Statement"""
        input = """
        int main(){
            for (true;1;false){}
        }
        """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);IntLiteral(1);BooleanLiteral(false);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_mismatch_return_stmt1(self):
        """ Mismatch Return Statement"""
        input = """
        int main(){
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_mismatch_return_stmt2(self):
        """ Mismatch Return Statement"""
        input = """
        void main(){
            return;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_mismatch_unary1(self):
        input = """
        void main(){
            boolean a;
            a = !4.5e10000;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,FloatLiteral(inf))"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_mismatch_unary2(self):
        input = """
        void main(){
            boolean a;
            a = -1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_not_left_value(self):
        input = """
        int main(){
            5 = 5;
        }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_mismatch_binary1(self):
        input = """
        int main(){
            float a;
            int b;
            a = 1;
            b = 1.000;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_mismatch_binary2(self):
        input = """
        int main(){
            float a;
            int b;
            a = 1;
            b = a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_mismatch_binary3(self):
        input = """
        int main(){
            float a;
            boolean b;
            a + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_mismatch_binary4(self):
        input = """
        int main(){
            float a;
            a % 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_mismatch_binary5(self):
        input = """
        int main(){
            boolean a;
            int b;
            b % a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_mismatch_binary6(self):
        input = """
        int main(){
            boolean is_true;
            is_true = 14 == 14.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLiteral(14),FloatLiteral(14.0))"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_mismatch_binary7(self):
        input = """
        int main(){
            boolean is_true;
            boolean a;
            is_true = a > 14.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),FloatLiteral(14.0))"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_mismatch_binary8(self):
        input = """
        int main(){
            int a;
            int b;
            a && b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_mismatch_binary9(self):
        input = """
        int main(){
            boolean a;
            boolean b;
            int c;
            c = a || b;
            
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(||,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_mismatch_binary10(self):
        input = """
        int main(){
            int a;
            int b;
            int c;
            a = 5;
            c = 1.0 + a + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(+,BinaryOp(+,FloatLiteral(1.0),Id(a)),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_func_not_return1(self):
        input = """
        int main(){
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_func_not_return2(self):
        input = """
        int main(){
            int a;
            int b;
            int c;
            a = 5;
            c = 1 + a + b;
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_func_not_return_in_ifstmt1(self):
        input = """
        int main(){
            if (true)
                return 1;
            else{
                int a;
                a = a + 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_func_not_return_in_ifstmt2(self):
        input = """
        int main(){
            if (true){
                int a;
                a = a + 1;
            }
            else
                return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_func_not_return_in_forstmt1(self):
        input = """
        int main(){
            int i;
            int a;
            for (i=1;i<10;i=i+1)
                a = a + 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_func_not_return_in_dowhile_stmt1(self):
        input = """
        int main(){
            int i;
            int a;
            do a = a + 1; while (true);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_break_not_in_loop(self):
        input = """
        int main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_continue_not_in_loop(self):
        input = """
        int main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))

    # def test_unreach_func(self):
    #     input = """
    #     void main(){
    #         int a;
    #     }
    #     int main1(){main(); return 1;}
    #     void main2(){main1();}
    #     """
    #     expect = "Unreachable Function: main2"
    #     self.assertTrue(TestChecker.test(input,expect,437))

    def test_2(self):
        input = """
        void main(){
            if (true){
                int a;
                a = 1;
            }
            else {
                a = a + 1;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,438))
        