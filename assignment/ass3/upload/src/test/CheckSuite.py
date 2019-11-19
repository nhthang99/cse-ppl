import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_main_func_defined(self):
        """ Main Function Defined """
        input = Program([
                FuncDecl(Id("main"), [], VoidType(), Block([]))
                ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_main_func_undefined(self):
        """ Main Function Undefined """
        input = Program([
            FuncDecl(Id("main1"), [], VoidType(), Block([])),
            ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_var_redeclare1(self):
        """ Variable Declare"""
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            VarDecl("a", IntType()),
            VarDecl("a", IntType())
            ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_var_redeclare2(self):
        """ Variable Declare"""
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            VarDecl("a", IntType()),
            VarDecl("a", VoidType())
            ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_func_redeclare1(self):
        """ Function Declare"""
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            ])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_param_redeclare1(self):
        """ Parameter Declare"""
        input = Program([
            FuncDecl(Id("main"), [VarDecl("a", IntType()), VarDecl("a", IntType())], VoidType(), Block([])),
            ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_1(self):
        input = """int main(){
            a; 
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    # def test_mismatch_ifstmt1(self):
    #     """ Mismatch If Statement"""
    #     input = """
    #     int main(){
    #         if (1){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_mismatch_dowhilestmt1(self):
    #     """ Mismatch Dowhile Statement"""
    #     input = """
    #     int main(){
    #         do {} while(1);
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_mismatch_forstmt1(self):
    #     """ Mismatch For Statement"""
    #     input = """
    #     int main(){
    #         for (1;2;2){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(2);Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_mismatch_forstmt2(self):
    #     """ Mismatch For Statement"""
    #     input = """
    #     int main(){
    #         for (true;true;2){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);IntLiteral(2);Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_mismatch_forstmt3(self):
    #     """ Mismatch For Statement"""
    #     input = """
    #     int main(){
    #         for (true;1;false){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(BooleanLiteral(true);IntLiteral(1);BooleanLiteral(false);Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_mismatch_return_stmt1(self):
    #     """ Mismatch Return Statement"""
    #     input = """
    #     int main(){
    #         return;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return()"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_mismatch_return_stmt2(self):
    #     """ Mismatch Return Statement"""
    #     input = """
    #     void main(){
    #         return;
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,412))

    def test_id_undeclare1(self):
        input = """void main(){
            a = a + 1;
            a = a - 2;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_id_undeclare2(self):
        input = """
        int a;
        void main(){
            a = a + 1;
            a = a - b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_id_undeclare3(self):
        input = """
        float main(){
            int a;
            a = a + 1;
            a = a - b;
            a = a + a * c;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_mismatch_unary1(self):
        input = """
        void main(){
            boolean a;
            a = !4.5e10000;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,FloatLiteral(inf))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_mismatch_unary2(self):
        input = """
        void main(){
            boolean a;
            a = -1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_not_left_value(self):
        input = """
        int main(){
            5 = 5;
        }
        """
        expect = "Not Left Value: BinaryOp(=,IntLiteral(5),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,418))

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
            else
                a = a + 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_func_not_return_in_ifstmt2(self):
        input = """
        int main(){
            if (true)
                a = a + 1;
            else
                return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,432))
