import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Test variable declaration
    def test_single_variable_declaration(self):
        input = """int a;"""
        expect = "Program([VarDecl(Id(a),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_single_array_declaration(self):
        input = """float a[5];"""
        expect = "Program([VarDecl(Id(a),ArrayType(FloatType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_multi_variable_declaration(self):
        input = """boolean a,b;"""
        expect = "Program([VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_multi_array_declaration(self):
        input = """boolean a[10],b[5];"""
        expect = "Program([VarDecl(Id(a),ArrayType(BoolType,IntLiteral(10))),VarDecl(Id(b),ArrayType(BoolType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_mix_variable_declaration(self):
        input = """boolean a,b[5];"""
        expect = "Program([VarDecl(Id(a),BoolType),VarDecl(Id(b),ArrayType(BoolType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # Test program with variable declaration
    def test_program_multi_variable_declaration(self):
        input = """int a; float b; boolean c;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_program_multi_array_declaration(self):
        input = """int a[5]; float b[6]; boolean c[7];"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(6))),VarDecl(Id(c),ArrayType(BoolType,IntLiteral(7)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_program_miss_semi_colon(self):
        input = """int a; float b"""
        expect = "Program([VarDecl(Id(a),IntType),None,None])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_program_wrong_variable_type(self):
        input = """intl a; float b"""
        expect = "Program([])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_program_empty(self):
        input = """"""
        expect = "Program([])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # # Test function parameter
    def test_function_para_empty(self):
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_function_single_para(self):
        input = """int main(int a) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_function_multi_para(self):
        input = """void main(boolean a, float b) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),BoolType),VarDecl(Id(b),FloatType)],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_function_single_array(self):
        input = """void main(boolean a[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),ArrayTypePointer(BoolType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_function_multi_array(self):
        input = """void main(boolean a[], float b[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a),ArrayTypePointer(BoolType)),VarDecl(Id(b),ArrayTypePointer(FloatType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # Test program with function parameter
    def test_function_type_array(self):
        input = """int[] main() {}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_function_void_type_array(self):
        input = """void main() {}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_program_multi_function(self):
        input = """int[] main() {} float[] pow() {}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_program_multi_function_variable(self):
        input = """int[] main() {} float[] pow() {} int a,b,c;"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_program_multi_function_array(self):
        input = """int[] main() {} float[] pow() {} int a[5],b[5],c[5];"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(pow),[],ArrayTypePointer(FloatType),Block([])),VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),ArrayType(IntType,IntLiteral(5)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # Test statement
    def test_if_stmt_base(self):
        input = """void main() {if(true) print("hello");}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_if__else_stmt_base(self):
        input = """void main() {if(true) print("hello"); else put(5)}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),CallExpr(Id(print),[StringLiteral(hello)]),CallExpr(Id(put),[IntLiteral(5)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    