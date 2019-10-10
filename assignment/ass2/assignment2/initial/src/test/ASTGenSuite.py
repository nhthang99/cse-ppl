import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl1(self):
        """ Test Variable Declare """
        input = """int a,b,c[3];"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),ArrayType(IntType,IntLiteral(3)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_decl2(self):
        """ Test Variable Declare """
        input = """int a,b,c,d, e, t,h;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(e),IntType),VarDecl(Id(t),IntType),VarDecl(Id(h),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_var_decl3(self):
        """ Test Variable Declare """
        input = """int a[1], b[5], c[0], d[100];"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(1))),VarDecl(Id(b),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),ArrayType(IntType,IntLiteral(0))),VarDecl(Id(d),ArrayType(IntType,IntLiteral(100)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_decl4(self):
        """ Test Variable Declare """
        input = """
        int a[1], b[5], c, d;
        float c, d, e[10];
        boolean e , a[1];
        """
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(1))),VarDecl(Id(b),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),ArrayType(FloatType,IntLiteral(10))),VarDecl(Id(e),BoolType),VarDecl(Id(a),ArrayType(BoolType,IntLiteral(1)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_decl5(self):
        """ Test Variable Declare """
        input = """int a[1], b[5], c, d;
        float c, d; int e[10];
        boolean e , a[1];
        string a, d[5]; int a; int f4;"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(1))),VarDecl(Id(b),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),ArrayType(IntType,IntLiteral(10))),VarDecl(Id(e),BoolType),VarDecl(Id(a),ArrayType(BoolType,IntLiteral(1))),VarDecl(Id(a),StringType),VarDecl(Id(d),ArrayType(StringType,IntLiteral(5))),VarDecl(Id(a),IntType),VarDecl(Id(f4),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_var_decl6(self):
        """ Test Variable Declare """
        input = """int a[1], b[5], c, d; float c, d; int e[10];
        string a, b, c, d[5], o[0];
        boolean n,                   m,            t, abc;
        boolean abc; boolean abc_____xyz;
        """
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(1))),VarDecl(Id(b),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),ArrayType(IntType,IntLiteral(10))),VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType),VarDecl(Id(d),ArrayType(StringType,IntLiteral(5))),VarDecl(Id(o),ArrayType(StringType,IntLiteral(0))),VarDecl(Id(n),BoolType),VarDecl(Id(m),BoolType),VarDecl(Id(t),BoolType),VarDecl(Id(abc),BoolType),VarDecl(Id(abc),BoolType),VarDecl(Id(abc_____xyz),BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_var_decl7(self):
        """ Test Variable Declare """
        input = """int a; float b; string c; boolean a;
        int a[1]; float b[1]; string d[5]; boolean e[6];"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType),VarDecl(Id(a),BoolType),VarDecl(Id(a),ArrayType(IntType,IntLiteral(1))),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(1))),VarDecl(Id(d),ArrayType(StringType,IntLiteral(5))),VarDecl(Id(e),ArrayType(BoolType,IntLiteral(6)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_var_decl8(self):
        """ Test Variable Declare """
        input = """int a;
        
        string d[5]; boolean e[6]           ;
        
        float b; string cbc, ___abc; boolean abc, xyz; string a[1];

        int a[1]; float b[1];           int a;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(d),ArrayType(StringType,IntLiteral(5))),VarDecl(Id(e),ArrayType(BoolType,IntLiteral(6))),VarDecl(Id(b),FloatType),VarDecl(Id(cbc),StringType),VarDecl(Id(___abc),StringType),VarDecl(Id(abc),BoolType),VarDecl(Id(xyz),BoolType),VarDecl(Id(a),ArrayType(StringType,IntLiteral(1))),VarDecl(Id(a),ArrayType(IntType,IntLiteral(1))),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(1))),VarDecl(Id(a),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_var_decl9(self):
        """ Test Variable Declare """
        input = """int a;
        string a; float __a[1]; boolean m[0];
        string abc[2]; string abc; string ac;
        float a,b, c[10], c[10000000000], d[999999999];
        boolean abc[1000], a; int abc, m[199999999];
        """
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(a),StringType),VarDecl(Id(__a),ArrayType(FloatType,IntLiteral(1))),VarDecl(Id(m),ArrayType(BoolType,IntLiteral(0))),VarDecl(Id(abc),ArrayType(StringType,IntLiteral(2))),VarDecl(Id(abc),StringType),VarDecl(Id(ac),StringType),VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),ArrayType(FloatType,IntLiteral(10))),VarDecl(Id(c),ArrayType(FloatType,IntLiteral(10000000000))),VarDecl(Id(d),ArrayType(FloatType,IntLiteral(999999999))),VarDecl(Id(abc),ArrayType(BoolType,IntLiteral(1000))),VarDecl(Id(a),BoolType),VarDecl(Id(abc),IntType),VarDecl(Id(m),ArrayType(IntType,IntLiteral(199999999)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_var_decl10(self):
        """ Test Variable Declare """
        input = """int a[5],b; float b[5]; string b[1]; boolean m[100];
        float a,b,c,d,f,g,h;                    float f1,f2,f3[10], f[14];
        string m[10]; float b[10];"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),IntType),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(5))),VarDecl(Id(b),ArrayType(StringType,IntLiteral(1))),VarDecl(Id(m),ArrayType(BoolType,IntLiteral(100))),VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(f),FloatType),VarDecl(Id(g),FloatType),VarDecl(Id(h),FloatType),VarDecl(Id(f1),FloatType),VarDecl(Id(f2),FloatType),VarDecl(Id(f3),ArrayType(FloatType,IntLiteral(10))),VarDecl(Id(f),ArrayType(FloatType,IntLiteral(14))),VarDecl(Id(m),ArrayType(StringType,IntLiteral(10))),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(10)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_non_body_func_decl1(self):
        """ Test Non Body Function Declare """
        input = r"""int abc(){}"""
        expect = "Program([FuncDecl(Id(abc),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))


    def test_non_body_simple_func_decl2(self):
        """ Test Non Body Function Declare """
        input = r"""int abc(int a){}"""
        expect = "Program([FuncDecl(Id(abc),[VarDecl(a,IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_non_body_func_decl3(self):
        """ Test Non Body Function Declare """
        input = r"""int main(){}
        int main(int a[]){}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_non_body_func_decl4(self):
        """ Test Non Body Function Declare """
        input = r"""int[] main(){}
        float[] main(){}
        string[] main(){}
        boolean[] main(){}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(main),[],ArrayTypePointer(FloatType),Block([])),FuncDecl(Id(main),[],ArrayTypePointer(StringType),Block([])),FuncDecl(Id(main),[],ArrayTypePointer(BoolType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_non_body_func_decl5(self):
        """ Test Non Body Function Declare """
        input = r"""int main(){}
        float main(){}
        string main(){}
        boolean main(){}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(main),[],FloatType,Block([])),FuncDecl(Id(main),[],StringType,Block([])),FuncDecl(Id(main),[],BoolType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_non_body_func_decl6(self):
        """ Test Non Body Function Declare """
        input = r"""int a(){}
        int[] a(){}
        float b(){}
        float[] b(){}
        string c(){}
        string[] c(){}
        boolean d(){}
        boolean[] d(){}"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([])),FuncDecl(Id(a),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(b),[],FloatType,Block([])),FuncDecl(Id(b),[],ArrayTypePointer(FloatType),Block([])),FuncDecl(Id(c),[],StringType,Block([])),FuncDecl(Id(c),[],ArrayTypePointer(StringType),Block([])),FuncDecl(Id(d),[],BoolType,Block([])),FuncDecl(Id(d),[],ArrayTypePointer(BoolType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_non_body_func_decl7(self):
        """ Test Non Body Function Declare """
        input = r"""int main(int a, float b, string str[]){}
        int main(int a[], float b[], boolean c[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(str,ArrayTypePointer(StringType))],IntType,Block([])),FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(c,ArrayTypePointer(BoolType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_non_body_func_decl8(self):
        """ Test Non Body Function Declare """
        input = r"""int main(int a, float b[], string c[], boolean d){}
        float main(){}
        boolean[] main(int a[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(c,ArrayTypePointer(StringType)),VarDecl(d,BoolType)],IntType,Block([])),FuncDecl(Id(main),[],FloatType,Block([])),FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType))],ArrayTypePointer(BoolType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    
    def test_non_body_func_decl9(self):
        """ Test Non Body Function Declare """
        input = r"""int foo(int a, int b){}
        int[] main(){}
        float[] main(string args[]){}
        string[] int2str(int a){}
        boolean isTrue(boolean a){}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType)],IntType,Block([])),FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],ArrayTypePointer(FloatType),Block([])),FuncDecl(Id(int2str),[VarDecl(a,IntType)],ArrayTypePointer(StringType),Block([])),FuncDecl(Id(isTrue),[VarDecl(a,BoolType)],BoolType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_non_body_func_decl10(self):
        """ Test Non Body Function Declare """
        input = r"""int main(string args[]){}
        int[] __str__(string a, string exception, boolean b[], float a){}
        boolean[] __abc(boolean isTrue){}
        float pi(float pi){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],IntType,Block([])),FuncDecl(Id(__str__),[VarDecl(a,StringType),VarDecl(exception,StringType),VarDecl(b,ArrayTypePointer(BoolType)),VarDecl(a,FloatType)],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(__abc),[VarDecl(isTrue,BoolType)],ArrayTypePointer(BoolType),Block([])),FuncDecl(Id(pi),[VarDecl(pi,FloatType)],FloatType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_func_decl_body_vardecl1(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int main(){
        int a;
        float c;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType),VarDecl(Id(c),FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_func_decl_body_vardecl2(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int[] main(float b[], string a){
        int a[10];
        string c;
        boolean a[1000];
        float a;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(a,StringType)],ArrayTypePointer(IntType),Block([VarDecl(Id(a),ArrayType(IntType,IntLiteral(10))),VarDecl(Id(c),StringType),VarDecl(Id(a),ArrayType(BoolType,IntLiteral(1000))),VarDecl(Id(a),FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_func_decl_body_vardecl3(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int main(){
            float a;
            string a;
            boolean b;
            int b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),FloatType),VarDecl(Id(a),StringType),VarDecl(Id(b),BoolType),VarDecl(Id(b),IntType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_func_decl_body_vardecl4(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int[] main(float b[], string a){
            int a[5];
            float b[10];
            string c[15];
            boolean d[20];
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(a,StringType)],ArrayTypePointer(IntType),Block([VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(b),ArrayType(FloatType,IntLiteral(10))),VarDecl(Id(c),ArrayType(StringType,IntLiteral(15))),VarDecl(Id(d),ArrayType(BoolType,IntLiteral(20)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_func_decl_body_vardecl5(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int[] main(float b[], string a){
            int a, a[5];
            float c, d, e[10], f[15]; int a,b,c;
            string a,b,c; string a[20];
            boolean a; float b; boolean a;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(a,StringType)],ArrayTypePointer(IntType),Block([VarDecl(Id(a),IntType),VarDecl(Id(a),ArrayType(IntType,IntLiteral(5))),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),ArrayType(FloatType,IntLiteral(10))),VarDecl(Id(f),ArrayType(FloatType,IntLiteral(15))),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(c),StringType),VarDecl(Id(a),ArrayType(StringType,IntLiteral(20))),VarDecl(Id(a),BoolType),VarDecl(Id(b),FloatType),VarDecl(Id(a),BoolType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_if_stmt1(self):
        """ Test If Statement """
        input = r"""void main(){
            if (true)
                a = a + 1;
            else
                a = b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_if_stmt2(self):
        """ Test If Statement """
        input = r"""void main(){
            if (true)
                a = a + 1;
                b = b - 2;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(=,Id(b),BinaryOp(-,Id(b),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_if_stmt3(self):
        """ Test If Statement """
        input = r"""void main(){
            if (true) 
                a = 1;
                if (false)
                    a = 1;
                else
                    a = 2;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),BinaryOp(=,Id(a),IntLiteral(1))),If(BooleanLiteral(false),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_if_stmt4(self):
        """ Test If Statement """
        input = r"""void main(){
            if (a == 1) 
                if (b != true)
                    a = 1;
                else
                    a = 2;
            else
                a = 4;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),If(BinaryOp(!=,Id(b),BooleanLiteral(true)),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),IntLiteral(2))),BinaryOp(=,Id(a),IntLiteral(4)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_if_stmt5(self):
        """ Test If Statement """
        input = r"""void main(){
            if (true)
                if (a == true)
                    if (b == false)
                        if (1)
                            a = 2;
                        else
                            b = 5;
                    else
                        a = 5;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),If(BinaryOp(==,Id(a),BooleanLiteral(true)),If(BinaryOp(==,Id(b),BooleanLiteral(false)),If(IntLiteral(1),BinaryOp(=,Id(a),IntLiteral(2)),BinaryOp(=,Id(b),IntLiteral(5))),BinaryOp(=,Id(a),IntLiteral(5)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))