import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Test VarDecl: 6 cases
    def test_1(self):
        input = """int a;"""
        expect = str(Program([VarDecl("a", IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_2(self):
        input = """float b[5];"""
        expect = str(Program([VarDecl("b", ArrayType(5, FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_3(self):
        input = """boolean c,d[10];"""
        expect = str(Program([VarDecl("c", BoolType()), VarDecl("d", ArrayType(10, BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_4(self):
        input = """boolean e,f;"""
        expect = str(Program([VarDecl("e", BoolType()), VarDecl("f", BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_5(self):
        input = """int a;
                    float b;"""
        expect = str(Program([VarDecl("a", IntType()), VarDecl("b", FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_6(self):
        input = """int a;
                    float b;
                    boolean c,d[50];"""
        expect = str(Program([VarDecl("a", IntType()), VarDecl("b", FloatType()),
                            VarDecl("c", BoolType()), VarDecl("d", ArrayType(50, BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    #Test FuncDecl without body: 10 cases
    def test_funcdecl_no_body_1(self):
        input = """void main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_funcdecl_no_body_2(self):
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_funcdecl_no_body_3(self):
        input = """boolean[] main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], ArrayPointerType(BoolType()), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_funcdecl_no_body_4(self):
        input = """void func(int a) {}"""
        expect = str(Program([FuncDecl(Id("func"), [VarDecl("a", IntType())], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_funcdecl_no_body_5(self):
        input = """boolean foo(int a, float b) {}"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl("a", IntType()), VarDecl("b", FloatType())], BoolType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcdecl_no_body_6(self):
        input = """string[] foo(int a, float b, string c) {}"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl("a", IntType()),
                        VarDecl("b", FloatType()), VarDecl("c", StringType())], ArrayPointerType(StringType()), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_funcdecl_no_body_7(self):
        input = """ int a;
                    void main(int a) {}"""
        expect = str(Program([VarDecl("a",IntType()), FuncDecl(Id("main"), [VarDecl("a", IntType())], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_funcdecl_no_body_8(self):
        input = """int foo(boolean x) {}
                    string b;"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl("x", BoolType())], IntType(), Block([])), VarDecl("b", StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_funcdecl_no_body_9(self):
        input = """void func(int a[]) {}"""
        expect = str(Program([FuncDecl(Id("func"), [VarDecl("a", ArrayPointerType(IntType()))], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_funcdecl_no_body_10(self):
        input = """string[] func(int a[]) {}"""
        expect = str(Program([FuncDecl(Id("func"), [VarDecl("a", ArrayPointerType(IntType()))], ArrayPointerType(StringType()), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))


    #Test statement: 15 test cases
    def test_statement_1(self):
        input = """
                void main() {
                    int a;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    VarDecl("a", IntType())
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_statement_2(self):
        input = """
                void main() {
                    int a, b;
                    float c[10];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    VarDecl("a", IntType()), VarDecl("b", IntType()), VarDecl("c", ArrayType(10, FloatType()))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_statement_3(self):
        input = """
                void main() {
                    if (1 > 2) return;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    If(BinaryOp(">", IntLiteral(1), IntLiteral(2)), Return())
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_statement_4(self):
        input = """
                int main() {
                    if (1 > 2) return 0;
                    else return 1;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([
                    If(BinaryOp(">", IntLiteral(1), IntLiteral(2)), Return(IntLiteral(0)), Return(IntLiteral(1)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_statement_5(self):
        input = """
                void main() {
                    do
                        x + 1;
                    while 1 > 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    Dowhile([BinaryOp("+", Id("x"), IntLiteral(1))], BinaryOp(">", IntLiteral(1), IntLiteral(2)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_statement_6(self):
        input = """
                void main() {
                    do
                        x + 1;
                        a = x * 2;
                    while 1 > 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    Dowhile([BinaryOp("+", Id("x"), IntLiteral(1)),
                            BinaryOp("=", Id("a"), BinaryOp("*", Id("x"), IntLiteral(2)))],
                            BinaryOp(">", IntLiteral(1), IntLiteral(2)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_statement_7(self):
        input = """
                void main() {
                    for (i = 0; i < 10; i = i + 1)
                        print(i);
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    For(BinaryOp("=", Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        CallExpr(Id("print"), [Id("i")]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_statement_8(self):
        input = """
                void main() {
                    for (i = 0; i < 10; i = i + 1)
                        if (i == 5) break;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    For(BinaryOp("=", Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        If(BinaryOp("==", Id("i"), IntLiteral(5)), Break()))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_statement_9(self):
        input = """
                void main() {
                    for (i = 0; i < 10; i = i + 1)
                        if (i == 5) continue;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    For(BinaryOp("=", Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        If(BinaryOp("==", Id("i"), IntLiteral(5)), Continue()))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_statement_10(self):
        input = """
                int main() {
                    if (1 > 2) if (3 < 4) return 1; else return 0;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([
                    #If(BinaryOp(">", IntLiteral(1), IntLiteral(2)), If(BinaryOp("<", IntLiteral(3), IntLiteral(4)), Return(IntLiteral(1)), Return(IntLiteral(0))))
                    If(BinaryOp(">", IntLiteral(1), IntLiteral(2)), If(BinaryOp("<", IntLiteral(3), IntLiteral(4)), Return(IntLiteral(1)), Return(IntLiteral(0))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_statement_11(self):
        input = """
                void main() {
                    for (i = 0; i < 10; i = i + 1)
                        for (j = 0; j < 10; j = j + 1)
                            if (j == 5) break;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    For(BinaryOp("=", Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(10)),
                        BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        For(BinaryOp("=", Id("j"), IntLiteral(0)),
                            BinaryOp("<", Id("j"), IntLiteral(10)),
                            BinaryOp("=", Id("j"), BinaryOp("+", Id("j"), IntLiteral(1))),
                            If(BinaryOp("==", Id("j"), IntLiteral(5)), Break()))
                    )
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_statement_12(self):
        input = """
                void main() {
                    do
                        do
                            x + 1;
                        while 3 < 4;
                    while 1 > 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    Dowhile([Dowhile([BinaryOp("+", Id("x"), IntLiteral(1))], BinaryOp("<", IntLiteral(3), IntLiteral(4)))], BinaryOp(">", IntLiteral(1), IntLiteral(2)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_statement_13(self):
        input = """
                void main() {
                    break; break; break;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    Break(), Break(), Break()
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_statement_14(self):
        input = """
                void main() {
                    break; break; break;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    Break(), Break(), Break()
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_statement_15(self):
        input = """
                void main() {
                    for(i = 0; i < 5; i = i + 1)
                        if (i == 2)
                            do
                                return;
                            while i < 5;
                        else continue;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    For(BinaryOp("=", Id("i"), IntLiteral(0)),
                        BinaryOp("<", Id("i"), IntLiteral(5)),
                        BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        If(BinaryOp("==", Id("i"), IntLiteral(2)), Dowhile([Return()], BinaryOp("<", Id("i"), IntLiteral(5))), Continue())
                    )
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))


    #Test expression: 69 test cases
    def test_exp_1(self):
        input = """
                void main() {
                    1;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    IntLiteral(1)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_exp_2(self):
        input = """
                void main() {
                    1.2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    FloatLiteral(1.2)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_exp_3(self):
        input = """
                void main() {
                    1.e3;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    FloatLiteral(1.e3)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_exp_4(self):
        input = """
                void main() {
                    true; false;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BooleanLiteral(True), BooleanLiteral(False)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_exp_5(self):
        input = """
                void main() {
                    "string";
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    StringLiteral("string")
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_exp_6(self):
        input = """
                void main() {
                    id;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    Id("id")
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_exp_7(self):
        input = """
                void main() {
                    id[0];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("id"), IntLiteral(0))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_exp_8(self):
        input = """
                void main() {
                    random();
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("random"),[])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_exp_9(self):
        input = """
                void main() {
                    random(10);
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("random"),[IntLiteral(10)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_exp_10(self):
        input = """
                void main() {
                    random(0, 10);
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("random"),[IntLiteral(0), IntLiteral(10)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_exp_11(self):
        input = """
                void main() {
                    (1);
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    IntLiteral(1)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_exp_12(self):
        input = """
                void main() {
                    ((((((1))))));
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    IntLiteral(1)
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_exp_13(self):
        input = """
                void main() {
                    1 = 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("=", IntLiteral(1), IntLiteral(2))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_exp_14(self):
        input = """
                void main() {
                    1 || 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("||", IntLiteral(1), IntLiteral(2))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_exp_15(self):
        input = """
                void main() {
                    1 && 2;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("&&", IntLiteral(1), IntLiteral(2))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_exp_16(self):
        input = """
                void main() {
                    1 == 2; a != b;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("==", IntLiteral(1), IntLiteral(2)),
                    BinaryOp("!=", Id("a"), Id("b"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_exp_17(self):
        input = """
                void main() {
                    1 < 2; a <= b; 3 > 4; c >= d;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("<", IntLiteral(1), IntLiteral(2)),
                    BinaryOp("<=", Id("a"), Id("b")),
                    BinaryOp(">", IntLiteral(3), IntLiteral(4)),
                    BinaryOp(">=", Id("c"), Id("d"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_exp_18(self):
        input = """
                void main() {
                    1 - 2; a + b;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("-", IntLiteral(1), IntLiteral(2)),
                    BinaryOp("+", Id("a"), Id("b"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_exp_19(self):
        input = """
                void main() {
                    1 * 2; a / b; 3 % 4;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("*", IntLiteral(1), IntLiteral(2)),
                    BinaryOp("/", Id("a"), Id("b")),
                    BinaryOp("%", IntLiteral(3), IntLiteral(4))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_exp_20(self):
        input = """
                void main() {
                    -a; !b;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    UnaryOp("-", Id("a")), UnaryOp("!", Id("b"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_exp_21(self):
        input = """
                void main() {
                    1[2];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(IntLiteral(1), IntLiteral(2))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_exp_22(self):
        input = """
                void main() {
                    a[b+c];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), BinaryOp("+", Id("b"), Id("c")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_exp_23(self):
        input = """
                void main() {
                    a[func()];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), CallExpr(Id("func"), []))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_exp_23(self):
        input = """
                void main() {
                    a[func(1)];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), CallExpr(Id("func"), [IntLiteral(1)]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_exp_24(self):
        input = """
                void main() {
                    a[(((func(1))))];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), CallExpr(Id("func"), [IntLiteral(1)]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_exp_25(self):
        input = """
                void main() {
                    a[func(1, b)];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), CallExpr(Id("func"), [IntLiteral(1), Id("b")]))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_exp_26(self):
        input = """
                void main() {
                    a[b[10]];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), ArrayCell(Id("b"), IntLiteral(10)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_exp_27(self):
        input = """
                void main() {
                    a[b[foo()]];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), ArrayCell(Id("b"), CallExpr(Id("foo"), [])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_exp_28(self):
        input = """
                void main() {
                    ((((a))))[b[foo()]];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), ArrayCell(Id("b"), CallExpr(Id("foo"), [])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_exp_29(self):
        input = """
                void main() {
                    func()[b[foo()]];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(CallExpr(Id("func"), []), ArrayCell(Id("b"), CallExpr(Id("foo"), [])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_exp_30(self):
        input = """
                void main() {
                    func(1, a[0])[b[foo((true))]];
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(CallExpr(Id("func"), [IntLiteral(1), ArrayCell(Id("a"), IntLiteral(0))]),
                    ArrayCell(Id("b"), CallExpr(Id("foo"), [BooleanLiteral(True)])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_exp_31(self):
        input = """
                void main() {
                    {}
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_exp_32(self):
        input = """
                void main() {
                    {int a;}
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([Block([VarDecl("a", IntType())])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_exp_33(self):
        input = """
                void main() {
                    {foo();}
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([Block([CallExpr(Id("foo"), [])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_exp_34(self):
        input = """
                void main() {
                    {}{}{}{}{}{}{}{}
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                Block([]), Block([]), Block([]), Block([]), Block([]), Block([]), Block([]), Block([])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_exp_35(self):
        input = """
                void main() {
                    {{{{{{{}}}}}}}
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                Block([Block([Block([Block([Block([Block([Block([])])])])])])])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_exp_36(self):
        input = """
                void main() {
                    foo(foo(foo(foo(foo()))));
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])])])])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_exp_37(self):
        input = """
                void main() {
                    if (a)
                        if (b) 1;
                        else 2;
                    else 3;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                If(Id("a"), If(Id("b"), IntLiteral(1), IntLiteral(2)), IntLiteral(3))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_exp_38(self):
        input = """
                void main() {
                    1 = 2 = 3 = 4;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("=", IntLiteral(1), BinaryOp("=", IntLiteral(2), BinaryOp("=", IntLiteral(3), IntLiteral(4))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_exp_39(self):
        input = """
                void main() {
                    1 || 2 || a || b;
                    3 && 4 && c && d;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("||", BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), Id("a")), Id("b")),
                    BinaryOp("&&", BinaryOp("&&", BinaryOp("&&", IntLiteral(3), IntLiteral(4)), Id("c")), Id("d"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_exp_40(self):
        input = """
                void main() {
                    a == b;  c != d;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("==", Id("a"), Id("b")), BinaryOp("!=", Id("c"), Id("d"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_exp_41(self):
        input = """
                void main() {
                    a + b - c + d;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("+", BinaryOp("-", BinaryOp("+", Id("a"), Id("b")), Id("c")), Id("d"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_exp_42(self):
        input = """
                void main() {
                    a * b / c % d;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("%", BinaryOp("/", BinaryOp("*", Id("a"), Id("b")), Id("c")), Id("d"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_exp_43(self):
        input = """
                void main() {
                    -!-!a;
                }"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    UnaryOp("-", UnaryOp("!", UnaryOp("-", UnaryOp("!", Id("a")))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_exp_44(self):
        input = """
                void main(){
                    a = b && c || d == e;
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([
                    BinaryOp("=", Id("a"),BinaryOp("||",BinaryOp("&&",Id("b"),Id("c")),
                    BinaryOp("==",Id("d"),Id("e"))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_exp_45(self):
        input = """
                void main(){
                    1 >= -!a;
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([
                    BinaryOp(">=", IntLiteral(1), UnaryOp("-", UnaryOp("!", Id("a"))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_exp_46(self):
        input = """
                void main(){
                    a - b * c / f + d = e[0];
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([
                    BinaryOp("=", BinaryOp("+", BinaryOp("-", Id("a"),
                    BinaryOp("/", BinaryOp("*", Id("b"), Id("c")), Id("f"))), Id("d")),
                    ArrayCell(Id("e"), IntLiteral(0)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_exp_47(self):
        input = """
                void main(){
                    a < b * c * f = -d = !e[0];
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([
                    BinaryOp("=", BinaryOp("<", Id("a"), BinaryOp("*", BinaryOp("*", Id("b"), Id("c")), Id("f"))),
                    BinaryOp("=", UnaryOp("-", Id("d")), UnaryOp("!", ArrayCell(Id("e"), IntLiteral(0)))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_exp_48(self):
        input = """
                void main(){
                    a + (b + (c + d));
                }
        """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([
                    BinaryOp("+", Id("a"), BinaryOp("+", Id("b"), BinaryOp("+", Id("c"), Id("d"))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_exp_49(self):
        input = """
                void main(){
                    ((a = b) = c) = d;
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("=", BinaryOp("=", BinaryOp("=", Id("a"), Id("b")), Id("c")), Id("d"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_exp_50(self):
        input = """
                void main(){
                    (a + b) * c;
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), Id("c"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_exp_51(self):
        input = """
                void main(){
                    ((((a + b)))) * c;
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("*", BinaryOp("+", Id("a"), Id("b")), Id("c"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_exp_52(self):
        input = """
                void main(){
                    (a <= b) + (c >= d);
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("+", BinaryOp("<=", Id("a"), Id("b")), BinaryOp(">=", Id("c"), Id("d")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_exp_53(self):
        input = """
                void main(){
                    (a() <= b()) + (c() >= d());
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("+", BinaryOp("<=", CallExpr(Id("a"), []), CallExpr(Id("b"), [])),
                    BinaryOp(">=", CallExpr(Id("c"), []), CallExpr(Id("d"), [])))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_exp_54(self):
        input = """
                void main(){
                    a[b < c + d];
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    ArrayCell(Id("a"), BinaryOp("<", Id("b"), BinaryOp("+", Id("c"), Id("d"))))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_exp_55(self):
        input = """
                void main(){
                    a = b > c + !d == e * f && g;
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    BinaryOp("=", Id("a"), BinaryOp("&&", BinaryOp("==", BinaryOp(">", Id("b"), BinaryOp("+", Id("c"), UnaryOp("!", Id("d")))), BinaryOp("*", Id("e"), Id("f"))), Id("g")))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_exp_56(self):
        input = """
                void main(){
                    foo("");
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("foo"), [StringLiteral("")])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_exp_57(self):
        input = """
                void main(){
                    foo("", "");
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("foo"), [StringLiteral(""), StringLiteral("")])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_exp_58(self):
        input = """
                void main(){
                    foo(1.234E5678);
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("foo"), [FloatLiteral(1.234E5678)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_exp_59(self):
        input = """
                void main(){
                    foo(1234e-5678, 8765E4321);
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("foo"), [FloatLiteral(1234e-5678), FloatLiteral(8765E4321)])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_exp_60(self):
        input = """
                void main(){
                    //
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_exp_61(self):
        input = """
                void main(){
                    foo("\\n", "\\b");
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
                    CallExpr(Id("foo"), [StringLiteral("\\n"), StringLiteral("\\b")])
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_exp_62(self):
        input = """
                void main(){
                    /* */
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_exp_63(self):
        input = """
                void main(){
                    // /**/
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_exp_64(self):
        input = """
                void main(){
                    /*
                        This is a block comment
                    */
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_exp_65(self):
        input = """
                void main(/* */){
                    /*
                        Is this a block comment ?????
                    */
                }
        """
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_exp_66(self):
        input = """
                int a;
                void main(){

                }
        """
        expect = str(Program([VarDecl("a", IntType()), FuncDecl(Id("main"), [], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_exp_67(self):
        input = """
                int a;
                void main(float b){

                }
        """
        expect = str(Program([VarDecl("a", IntType()), FuncDecl(Id("main"), [VarDecl("b", FloatType())], VoidType(), Block([
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_exp_68(self):
        input = """
                int a;
                void main(float b){
                    return c;
                }
        """
        expect = str(Program([VarDecl("a", IntType()), FuncDecl(Id("main"), [VarDecl("b", FloatType())], VoidType(), Block([
                    Return(Id("c"))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_exp_69(self):
        input = """
                int a[10];
                void main(float b[]){
                    return c[0];
                }
        """
        expect = str(Program([VarDecl("a", ArrayType(10, IntType())), FuncDecl(Id("main"), [VarDecl("b", ArrayPointerType(FloatType()))], VoidType(), Block([
                    Return(ArrayCell(Id("c"), IntLiteral(0)))
        ]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
