import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_more_simple_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_true_and_false(self):
           
        input = """void f(int a,float b, float c){
            true && false || (2 > 3/5);
        }"""
        expect = "Program([FuncDecl(Id(f),[VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType)],VoidType,Block([BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),BinaryOp(>,IntLiteral(2),BinaryOp(/,IntLiteral(3),IntLiteral(5))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_more_call_function(self):
        input = """int main () {
            putIntLn(4);
            ar[12];
            foo(a[10],r);
            break;continue;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)]),ArrayCell(Id(ar),IntLiteral(12)),CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(10)),Id(r)]),Break(),Continue()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_if_and_have_not_semiconlon(self):
        input = """int main () {
            if( (c > x) < d){
                int a,b;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,BinaryOp(>,Id(c),Id(x)),Id(d)),Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_if_in_if(self):
        input = """int foo () {
            if (a+1) {{{{if(b+a) foo();}}}} else {if (c+d) t+a; else func(a(b(c)))[f+6*d()];}
        }"""
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([If(BinaryOp(+,Id(a),IntLiteral(1)),Block([Block([Block([Block([If(BinaryOp(+,Id(b),Id(a)),CallExpr(Id(foo),[]))])])])]),Block([If(BinaryOp(+,Id(c),Id(d)),BinaryOp(+,Id(t),Id(a)),ArrayCell(CallExpr(Id(func),[CallExpr(Id(a),[CallExpr(Id(b),[Id(c)])])]),BinaryOp(+,Id(f),BinaryOp(*,IntLiteral(6),CallExpr(Id(d),[])))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_array_type_and_invol(self):
        input = """int[] ham(int a[], float b[]) {
            return;
        }"""
        expect = "Program([FuncDecl(Id(ham),[VarDecl(Id(a),ArrayTypePointer(IntType)),VarDecl(Id(b),ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_do_while(self):
        input = """void fo() {
            do{ f(foo(fr(aaa(e(r()))))); } while a>d;
        }"""
        expect = "Program([FuncDecl(Id(fo),[],VoidType,Block([Dowhile([Block([CallExpr(Id(f),[CallExpr(Id(foo),[CallExpr(Id(fr),[CallExpr(Id(aaa),[CallExpr(Id(e),[CallExpr(Id(r),[])])])])])])])],BinaryOp(>,Id(a),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_bool_in_do(self):
        input = """int main () {
           do{ true;} while d>a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([BooleanLiteral(true)])],BinaryOp(>,Id(d),Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_if_in_do_while(self):
        input = """float d () {
           do if (a==s) {if (t>a) if (d>=e) if (a<y) if (r<=o) {x+1;}} while foo();
        }"""
        expect = "Program([FuncDecl(Id(d),[],FloatType,Block([Dowhile([If(BinaryOp(==,Id(a),Id(s)),Block([If(BinaryOp(>,Id(t),Id(a)),If(BinaryOp(>=,Id(d),Id(e)),If(BinaryOp(<,Id(a),Id(y)),If(BinaryOp(<=,Id(r),Id(o)),Block([BinaryOp(+,Id(x),IntLiteral(1))])))))]))],CallExpr(Id(foo),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_invol_invol(self):
        input = """string m( string x, float b[]) {
            foo(f(t(e(call(f[3 + f[2*g[x]]])))));
        }"""
        expect = "Program([FuncDecl(Id(m),[VarDecl(Id(x),StringType),VarDecl(Id(b),ArrayTypePointer(FloatType))],StringType,Block([CallExpr(Id(foo),[CallExpr(Id(f),[CallExpr(Id(t),[CallExpr(Id(e),[CallExpr(Id(call),[ArrayCell(Id(f),BinaryOp(+,IntLiteral(3),ArrayCell(Id(f),BinaryOp(*,IntLiteral(2),ArrayCell(Id(g),Id(x))))))])])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_if_statement(self):
        input = """int a; float b;
        void h(){
            if(x>d) print("f");
        }"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),FuncDecl(Id(h),[],VoidType,Block([If(BinaryOp(>,Id(x),Id(d)),CallExpr(Id(print),[StringLiteral(f)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_bool_list(self):
        input = """boolean[] main () {
            boolean t[34];
            return ast;
        }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(BoolType),Block([VarDecl(Id(t),ArrayType(BoolType,IntLiteral(34))),Return(Id(ast))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_null_block(self):
        input = """string[] main () {
            {{{{{}}}}}
        }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(StringType),Block([Block([Block([Block([Block([Block([])])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_countinue_in_for(self):
        input = """int main (float y) {
            for(dd>e;t % r; t+1){
                if(a>3) if (b>c) if (f=i) continue;

            }
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(y),FloatType)],IntType,Block([For(BinaryOp(>,Id(dd),Id(e));BinaryOp(%,Id(t),Id(r));BinaryOp(+,Id(t),IntLiteral(1));Block([If(BinaryOp(>,Id(a),IntLiteral(3)),If(BinaryOp(>,Id(b),Id(c)),If(BinaryOp(=,Id(f),Id(i)),Continue())))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_for_in_for(self):
        input = """string foo() {
           for(d=y;d<g;d==r+2) {
                for(d=y;d<g;d=d/4) 
                {
                    for(d=y;d<g;d=e%r){
                        if (c>d) if (d>e) if (t>f) break;
                        continue;
                    }
                    continue;
                }
                continue;
           }
        }"""
        expect = "Program([FuncDecl(Id(foo),[],StringType,Block([For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(==,Id(d),BinaryOp(+,Id(r),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(=,Id(d),BinaryOp(/,Id(d),IntLiteral(4)));Block([For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(=,Id(d),BinaryOp(%,Id(e),Id(r)));Block([If(BinaryOp(>,Id(c),Id(d)),If(BinaryOp(>,Id(d),Id(e)),If(BinaryOp(>,Id(t),Id(f)),Break()))),Continue()])),Continue()])),Continue()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_do_while_in_do_while(self):
        input = """boolean fg() {
            do do do do do a = 1; while a>7;while b<8;while r%6; while d*9;while t>=0;
        }"""
        expect = "Program([FuncDecl(Id(fg),[],BoolType,Block([Dowhile([Dowhile([Dowhile([Dowhile([Dowhile([BinaryOp(=,Id(a),IntLiteral(1))],BinaryOp(>,Id(a),IntLiteral(7)))],BinaryOp(<,Id(b),IntLiteral(8)))],BinaryOp(%,Id(r),IntLiteral(6)))],BinaryOp(*,Id(d),IntLiteral(9)))],BinaryOp(>=,Id(t),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_if_in_do_while_do(self):
        input = """int m (int e[]) {
            do do do do do if (c%v) if (t>=5) if (6<=t) if (y%6) r+t; else f+4; else r-9; else 6%t; else r*6; while a>7;while b<8;while r%6; while d*9;while t>=0;
        }"""
        expect = "Program([FuncDecl(Id(m),[VarDecl(Id(e),ArrayTypePointer(IntType))],IntType,Block([Dowhile([Dowhile([Dowhile([Dowhile([Dowhile([If(BinaryOp(%,Id(c),Id(v)),If(BinaryOp(>=,Id(t),IntLiteral(5)),If(BinaryOp(<=,IntLiteral(6),Id(t)),If(BinaryOp(%,Id(y),IntLiteral(6)),BinaryOp(+,Id(r),Id(t)),BinaryOp(+,Id(f),IntLiteral(4))),BinaryOp(-,Id(r),IntLiteral(9))),BinaryOp(%,IntLiteral(6),Id(t))),BinaryOp(*,Id(r),IntLiteral(6)))],BinaryOp(>,Id(a),IntLiteral(7)))],BinaryOp(<,Id(b),IntLiteral(8)))],BinaryOp(%,Id(r),IntLiteral(6)))],BinaryOp(*,Id(d),IntLiteral(9)))],BinaryOp(>=,Id(t),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_for_in_if_if(self):
        input = """int main(int d) {
            if (c<v) if (t>=5) if (6>=t) if (!y) r+t; else for(d=y;d<g;d==d%s)  f+4; else for(d=y;d<g;d=e-3) r-9; else for(d=y;d<g;d==d/5) 6%t; else for(d=y;d<g;d=e*8) r*6;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(d),IntType)],IntType,Block([If(BinaryOp(<,Id(c),Id(v)),If(BinaryOp(>=,Id(t),IntLiteral(5)),If(BinaryOp(>=,IntLiteral(6),Id(t)),If(UnaryOp(!,Id(y)),BinaryOp(+,Id(r),Id(t)),For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(==,Id(d),BinaryOp(%,Id(d),Id(s)));BinaryOp(+,Id(f),IntLiteral(4)))),For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(=,Id(d),BinaryOp(-,Id(e),IntLiteral(3)));BinaryOp(-,Id(r),IntLiteral(9)))),For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(==,Id(d),BinaryOp(/,Id(d),IntLiteral(5)));BinaryOp(%,IntLiteral(6),Id(t)))),For(BinaryOp(=,Id(d),Id(y));BinaryOp(<,Id(d),Id(g));BinaryOp(=,Id(d),BinaryOp(*,Id(e),IntLiteral(8)));BinaryOp(*,Id(r),IntLiteral(6))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_not_and_not(self):
        input = """int foh() {
            in = !a;
            in = !!!!!!(foo());
        }"""
        expect = "Program([FuncDecl(Id(foh),[],IntType,Block([BinaryOp(=,Id(in),UnaryOp(!,Id(a))),BinaryOp(=,Id(in),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,CallExpr(Id(foo),[]))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_for_and_for(self):
        input = """int n() {
            for(a = 9; a>9; a = a+1) for(a = 9; a>9; a = a+1) for(a = 9; a>9; a = a+1) do do do a+2; while(!a) ; while(!b) ; while(!d) ;
        }"""
        expect = "Program([FuncDecl(Id(n),[],IntType,Block([For(BinaryOp(=,Id(a),IntLiteral(9));BinaryOp(>,Id(a),IntLiteral(9));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));For(BinaryOp(=,Id(a),IntLiteral(9));BinaryOp(>,Id(a),IntLiteral(9));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));For(BinaryOp(=,Id(a),IntLiteral(9));BinaryOp(>,Id(a),IntLiteral(9));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Dowhile([Dowhile([Dowhile([BinaryOp(+,Id(a),IntLiteral(2))],UnaryOp(!,Id(a)))],UnaryOp(!,Id(b)))],UnaryOp(!,Id(d))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_equal_equal(self):
        input = """int main () {
            if (!(b+t==b4*9)) a+s; else r+t;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(UnaryOp(!,BinaryOp(==,BinaryOp(+,Id(b),Id(t)),BinaryOp(*,Id(b4),IntLiteral(9)))),BinaryOp(+,Id(a),Id(s)),BinaryOp(+,Id(r),Id(t)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_for_while(self):
        input = """int f () {
            for(d=9;d<30;d=d+1) do if (--a) f=r-d+e; while g+8 ;
        }"""
        expect = "Program([FuncDecl(Id(f),[],IntType,Block([For(BinaryOp(=,Id(d),IntLiteral(9));BinaryOp(<,Id(d),IntLiteral(30));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Dowhile([If(UnaryOp(-,UnaryOp(-,Id(a))),BinaryOp(=,Id(f),BinaryOp(+,BinaryOp(-,Id(r),Id(d)),Id(e))))],BinaryOp(+,Id(g),IntLiteral(8))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_negative_and_for(self):
        input = """int mrt () {
            for(d=9;d<30;d=d-1){
                int b;
                continue;
                f= --------a + ------g;
                do{
                    a = ---b;
                    f =!!!!d;
                    a[10] = b[x + 3];
                }
                while false;if (a/3) f=5;else r;break;
            }
        }"""
        expect = "Program([FuncDecl(Id(mrt),[],IntType,Block([For(BinaryOp(=,Id(d),IntLiteral(9));BinaryOp(<,Id(d),IntLiteral(30));BinaryOp(=,Id(d),BinaryOp(-,Id(d),IntLiteral(1)));Block([VarDecl(Id(b),IntType),Continue(),BinaryOp(=,Id(f),BinaryOp(+,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a))))))))),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(g))))))))),Dowhile([Block([BinaryOp(=,Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(b))))),BinaryOp(=,Id(f),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(d)))))),BinaryOp(=,ArrayCell(Id(a),IntLiteral(10)),ArrayCell(Id(b),BinaryOp(+,Id(x),IntLiteral(3))))])],BooleanLiteral(false)),If(BinaryOp(/,Id(a),IntLiteral(3)),BinaryOp(=,Id(f),IntLiteral(5)),Id(r)),Break()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_while_invol_expr(self):
        input = """int main () {
            do break;do break;break;break; do break;i+5;break; while d<=d;while foo();while(a[10]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Break(),Dowhile([Break(),Break(),Break(),Dowhile([Break(),BinaryOp(+,Id(i),IntLiteral(5)),Break()],BinaryOp(<=,Id(d),Id(d)))],CallExpr(Id(foo),[]))],ArrayCell(Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_array_type(self):
        input = """int main () {
            //foo()[4];
            return s[f[g[j[h[t[56+foo()+q[5] / f(v)[9]]]]]]];
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(ArrayCell(Id(s),ArrayCell(Id(f),ArrayCell(Id(g),ArrayCell(Id(j),ArrayCell(Id(h),ArrayCell(Id(t),BinaryOp(+,BinaryOp(+,IntLiteral(56),CallExpr(Id(foo),[])),BinaryOp(/,ArrayCell(Id(q),IntLiteral(5)),ArrayCell(CallExpr(Id(f),[Id(v)]),IntLiteral(9)))))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_float_and_LB_RB(self):
        input = """int main () {
            foo()[4+9%t];
            t= (3.e54 + 7-(yu*9/t + a[h]*(s8-9/(y%r[t+h]))));
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(CallExpr(Id(foo),[]),BinaryOp(+,IntLiteral(4),BinaryOp(%,IntLiteral(9),Id(t)))),BinaryOp(=,Id(t),BinaryOp(-,BinaryOp(+,FloatLiteral(3e+54),IntLiteral(7)),BinaryOp(+,BinaryOp(/,BinaryOp(*,Id(yu),IntLiteral(9)),Id(t)),BinaryOp(*,ArrayCell(Id(a),Id(h)),BinaryOp(-,Id(s8),BinaryOp(/,IntLiteral(9),BinaryOp(%,Id(y),ArrayCell(Id(r),BinaryOp(+,Id(t),Id(h))))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_do_while_else_else(self):
        input = """int main () {
            //f()[][][];
            do{
                r+2=d;
                !(d+y=r);
                if (r-i==0){
                    e(t(y()))[gt];
                    break;
                    continue;
                }
                else{
                    if(ast==0) g+3%2;
                    else{
                        if(true) gr-0;
                        else break;
                        continue;
                        continue;
                    }
                }
            }
            while (foo()[8]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,Id(r),IntLiteral(2)),Id(d)),UnaryOp(!,BinaryOp(=,BinaryOp(+,Id(d),Id(y)),Id(r))),If(BinaryOp(==,BinaryOp(-,Id(r),Id(i)),IntLiteral(0)),Block([ArrayCell(CallExpr(Id(e),[CallExpr(Id(t),[CallExpr(Id(y),[])])]),Id(gt)),Break(),Continue()]),Block([If(BinaryOp(==,Id(ast),IntLiteral(0)),BinaryOp(+,Id(g),BinaryOp(%,IntLiteral(3),IntLiteral(2))),Block([If(BooleanLiteral(true),BinaryOp(-,Id(gr),IntLiteral(0)),Break()),Continue(),Continue()]))]))])],ArrayCell(CallExpr(Id(foo),[]),IntLiteral(8)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_bool_and_bool(self):
        input = """float[] main () {
            boolean k;
            k = true -false*true/true%true*false;
        }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(FloatType),Block([VarDecl(Id(k),BoolType),BinaryOp(=,Id(k),BinaryOp(-,BooleanLiteral(true),BinaryOp(*,BinaryOp(%,BinaryOp(/,BinaryOp(*,BooleanLiteral(false),BooleanLiteral(true)),BooleanLiteral(true)),BooleanLiteral(true)),BooleanLiteral(false))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_do_while_logic_expr(self):
        input = """int[] m () {
            do{ int a;float b; id;}while !(elr&&true||false||s>=0&&y<=9);
        }"""
        expect = "Program([FuncDecl(Id(m),[],ArrayTypePointer(IntType),Block([Dowhile([Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),Id(id)])],UnaryOp(!,BinaryOp(||,BinaryOp(||,BinaryOp(&&,Id(elr),BooleanLiteral(true)),BooleanLiteral(false)),BinaryOp(&&,BinaryOp(>=,Id(s),IntLiteral(0)),BinaryOp(<=,Id(y),IntLiteral(9))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_simple_program_logic_expr(self):
        """Simple program: int main() {} """
        input = """int a,b[10],c,d,k;
        float f(){
            true;false;hello||e;
        }"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),ArrayType(IntType,IntLiteral(10))),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),VarDecl(Id(k),IntType),FuncDecl(Id(f),[],FloatType,Block([BooleanLiteral(true),BooleanLiteral(false),BinaryOp(||,Id(hello),Id(e))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_many_program(self):
        input = """float fl(string f){
            return;
        }
        boolean bo(float l){
            f = true || false;
            return b;
        }
        string f(int a){
            if(9||t) re = t;
            else{
                f;
            }
            return re;
        }"""
        expect = "Program([FuncDecl(Id(fl),[VarDecl(Id(f),StringType)],FloatType,Block([Return()])),FuncDecl(Id(bo),[VarDecl(Id(l),FloatType)],BoolType,Block([BinaryOp(=,Id(f),BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false))),Return(Id(b))])),FuncDecl(Id(f),[VarDecl(Id(a),IntType)],StringType,Block([If(BinaryOp(||,IntLiteral(9),Id(t)),BinaryOp(=,Id(re),Id(t)),Block([Id(f)])),Return(Id(re))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_for_and_logic_expr(self):
        
        input = """float ty(int y){
            for(t = o;t-i;t || true&&false){
                if(foo()[y]){
                    g+9;
                }
                else{
                    t-u;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(ty),[VarDecl(Id(y),IntType)],FloatType,Block([For(BinaryOp(=,Id(t),Id(o));BinaryOp(-,Id(t),Id(i));BinaryOp(||,Id(t),BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)));Block([If(ArrayCell(CallExpr(Id(foo),[]),Id(y)),Block([BinaryOp(+,Id(g),IntLiteral(9))]),Block([BinaryOp(-,Id(t),Id(u))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_comment_many_line(self):
        
        input = """string h(string g[]){
            float ed[98];
            /* astgen%^&*, y([r]);
            id = 90;
            id[] =0;
            return gh;
            */
            return bool[789];
            break;
            if(e||r) continue;
        }"""
        expect = "Program([FuncDecl(Id(h),[VarDecl(Id(g),ArrayTypePointer(StringType))],StringType,Block([VarDecl(Id(ed),ArrayType(FloatType,IntLiteral(98))),Return(ArrayCell(Id(bool),IntLiteral(789))),Break(),If(BinaryOp(||,Id(e),Id(r)),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_return_do_while(self):
        
        input = """int f(int y){
            return foo(fr(a,r,h))[i];
            do {
                f=9;
                if(t+8) g+3;
                else{
                    r-9*u;
                }
                do{
                    ef;
                } while a||true;
            } while(b&&false);
        }"""
        expect = "Program([FuncDecl(Id(f),[VarDecl(Id(y),IntType)],IntType,Block([Return(ArrayCell(CallExpr(Id(foo),[CallExpr(Id(fr),[Id(a),Id(r),Id(h)])]),Id(i))),Dowhile([Block([BinaryOp(=,Id(f),IntLiteral(9)),If(BinaryOp(+,Id(t),IntLiteral(8)),BinaryOp(+,Id(g),IntLiteral(3)),Block([BinaryOp(-,Id(r),BinaryOp(*,IntLiteral(9),Id(u)))])),Dowhile([Block([Id(ef)])],BinaryOp(||,Id(a),BooleanLiteral(true)))])],BinaryOp(&&,Id(b),BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_complex_if_dowhile_for(self):
        
        input = """int a(float h){
            for(t=i;u-9;y&&t){
                if(!0){
                    do{
                        break;cotinue;
                    }while(false);
                }
                else{
                    for(true;false;true){
                        return;
                    }
                }
                !w;break;continue;id;
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[VarDecl(Id(h),FloatType)],IntType,Block([For(BinaryOp(=,Id(t),Id(i));BinaryOp(-,Id(u),IntLiteral(9));BinaryOp(&&,Id(y),Id(t));Block([If(UnaryOp(!,IntLiteral(0)),Block([Dowhile([Block([Break(),Id(cotinue)])],BooleanLiteral(false))]),Block([For(BooleanLiteral(true);BooleanLiteral(false);BooleanLiteral(true);Block([Return()]))])),UnaryOp(!,Id(w)),Break(),Continue(),Id(id)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_null_program(self):
       
        input = """void a(){

        }
        void b(int bc[]){

        }
        string c(float f){

        }"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,Block([])),FuncDecl(Id(b),[VarDecl(Id(bc),ArrayTypePointer(IntType))],VoidType,Block([])),FuncDecl(Id(c),[VarDecl(Id(f),FloatType)],StringType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_parameter_float(self):
       
        input = """int a,t[9],k[10];
        int pt(){
                add(t+3.89e-56);
        }"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(t),ArrayType(IntType,IntLiteral(9))),VarDecl(Id(k),ArrayType(IntType,IntLiteral(10))),FuncDecl(Id(pt),[],IntType,Block([CallExpr(Id(add),[BinaryOp(+,Id(t),FloatLiteral(3.89e-56))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_index_expr_and_float(self):
        
        input = """int a,b[10];
        int f(){
            foo(a,t,a[32])[3.45e-6];
            return;
        }"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),ArrayType(IntType,IntLiteral(10))),FuncDecl(Id(f),[],IntType,Block([ArrayCell(CallExpr(Id(foo),[Id(a),Id(t),ArrayCell(Id(a),IntLiteral(32))]),FloatLiteral(3.45e-06)),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_return_float(self):
       
        input = """int a(string t){
            return 4.56e3-9;
        }"""
        expect = "Program([FuncDecl(Id(a),[VarDecl(Id(t),StringType)],IntType,Block([Return(BinaryOp(-,FloatLiteral(4560.0),IntLiteral(9)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_return_string(self):
        
        input = """string[] a(){
            return "astgensuite123456";
        }"""
        expect = "Program([FuncDecl(Id(a),[],ArrayTypePointer(StringType),Block([Return(StringLiteral(astgensuite123456))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_if_string(self):
        
        input = """int a(){
            if("ast1") "statement1";
            else if("ast2"){ "statement2";break;continue;}
            else if("ast3"){"statement3";}
            return a[10];
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([If(StringLiteral(ast1),StringLiteral(statement1),If(StringLiteral(ast2),Block([StringLiteral(statement2),Break(),Continue()]),If(StringLiteral(ast3),Block([StringLiteral(statement3)])))),Return(ArrayCell(Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_string_in_while(self):
       
        input = """void a(){
            do{break;continue;id;continue;}while("astwhile");
            return;
        }"""
        expect = "Program([FuncDecl(Id(a),[],VoidType,Block([Dowhile([Block([Break(),Continue(),Id(id),Continue()])],StringLiteral(astwhile)),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_for_and_string(self):
        
        input = """int a(){
            for("ast1;";"ast2;";"ast3;"){
                do{a=1;b=2;c=3;}while "astwhile";
                break;
                continue;
                return a[10];
            }
            return;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([For(StringLiteral(ast1;);StringLiteral(ast2;);StringLiteral(ast3;);Block([Dowhile([Block([BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(b),IntLiteral(2)),BinaryOp(=,Id(c),IntLiteral(3))])],StringLiteral(astwhile)),Break(),Continue(),Return(ArrayCell(Id(a),IntLiteral(10)))])),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_many_return_in_dowhile(self):
        
        input = """int a(string a[]){
            do{
                return a[10]; return fo(a,t,y);return id()[10];return;
            }
            while "ast";
        }"""
        expect = "Program([FuncDecl(Id(a),[VarDecl(Id(a),ArrayTypePointer(StringType))],IntType,Block([Dowhile([Block([Return(ArrayCell(Id(a),IntLiteral(10))),Return(CallExpr(Id(fo),[Id(a),Id(t),Id(y)])),Return(ArrayCell(CallExpr(Id(id),[]),IntLiteral(10))),Return()])],StringLiteral(ast))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_nested_block_in_dowhile(self):
        
        input = """int a(float a){
            do{{{{{{{true;id;1;}2;3;4;5;}return;}break;continue;returna;}1;true;false;}int a,s,d,f,r,t;}}while true;
        }"""
        expect = "Program([FuncDecl(Id(a),[VarDecl(Id(a),FloatType)],IntType,Block([Dowhile([Block([Block([Block([Block([Block([Block([Block([BooleanLiteral(true),Id(id),IntLiteral(1)]),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),Return()]),Break(),Continue(),Id(returna)]),IntLiteral(1),BooleanLiteral(true),BooleanLiteral(false)]),VarDecl(Id(a),IntType),VarDecl(Id(s),IntType),VarDecl(Id(d),IntType),VarDecl(Id(f),IntType),VarDecl(Id(r),IntType),VarDecl(Id(t),IntType)])])],BooleanLiteral(true))]))])"
    #     self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_nested_block_in_for(self):
        
        input = """int fo(int f){
            for(true;false;true){{{{{1;2;3;true;}break;continue;return d();}if(true) a+1;}i;doo()[a+2];}dr;false;}
        }"""
        expect = "Program([FuncDecl(Id(fo),[VarDecl(Id(f),IntType)],IntType,Block([For(BooleanLiteral(true);BooleanLiteral(false);BooleanLiteral(true);Block([Block([Block([Block([Block([IntLiteral(1),IntLiteral(2),IntLiteral(3),BooleanLiteral(true)]),Break(),Continue(),Return(CallExpr(Id(d),[]))]),If(BooleanLiteral(true),BinaryOp(+,Id(a),IntLiteral(1)))]),Id(i),ArrayCell(CallExpr(Id(doo),[]),BinaryOp(+,Id(a),IntLiteral(2)))]),Id(dr),BooleanLiteral(false)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_else_nested_block(self):
        
        input = """int a(){
            if(false) return;
            else{{{{1;2;3;}1.2;3.4e-5;f;}true;false;return;}}
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([If(BooleanLiteral(false),Return(),Block([Block([Block([Block([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),FloatLiteral(1.2),FloatLiteral(3.4e-05),Id(f)]),BooleanLiteral(true),BooleanLiteral(false),Return()])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_block_and_block(self):
       
        input = """int a(){
            {{{int a,m,n,e[3],y;true;float b;string l;}}}{}{}{}{}{}
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Block([Block([Block([VarDecl(Id(a),IntType),VarDecl(Id(m),IntType),VarDecl(Id(n),IntType),VarDecl(Id(e),ArrayType(IntType,IntLiteral(3))),VarDecl(Id(y),IntType),BooleanLiteral(true),VarDecl(Id(b),FloatType),VarDecl(Id(l),StringType)])])]),Block([]),Block([]),Block([]),Block([]),Block([])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_null_if(self):
        
        input = """int a(){
            if (!(true&&false)){
                {}{}{}{}
            }
            else{}
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([If(UnaryOp(!,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false))),Block([Block([]),Block([]),Block([]),Block([])]),Block([]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_bool_array(self):
       
        input = """boolean[] _main() {
            boolean b[3];
            b[0] = true;
            b[1] = false;
            b[2] = flase;
            return b;
        }"""
        expect = "Program([FuncDecl(Id(_main),[],ArrayTypePointer(BoolType),Block([VarDecl(Id(b),ArrayType(BoolType,IntLiteral(3))),BinaryOp(=,ArrayCell(Id(b),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(b),IntLiteral(1)),BooleanLiteral(false)),BinaryOp(=,ArrayCell(Id(b),IntLiteral(2)),Id(flase)),Return(Id(b))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_mul_and_mod(self):
       
        input = """int _main() {
            float f;
            int _main;
            _main = 2;
            f = !(a*b)*3+1/4%main;
            
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(_main),[],IntType,Block([VarDecl(Id(f),FloatType),VarDecl(Id(_main),IntType),BinaryOp(=,Id(_main),IntLiteral(2)),BinaryOp(=,Id(f),BinaryOp(+,BinaryOp(*,UnaryOp(!,BinaryOp(*,Id(a),Id(b))),IntLiteral(3)),BinaryOp(%,BinaryOp(/,IntLiteral(1),IntLiteral(4)),Id(main)))),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_expr_func_call_func(self):
        
        input = """int a(){
            a[10]*b[t+9]-e[t+g[u]]/t[e+y]%foo(a,r,e)[t-foo()];
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([BinaryOp(-,BinaryOp(*,ArrayCell(Id(a),IntLiteral(10)),ArrayCell(Id(b),BinaryOp(+,Id(t),IntLiteral(9)))),BinaryOp(%,BinaryOp(/,ArrayCell(Id(e),BinaryOp(+,Id(t),ArrayCell(Id(g),Id(u)))),ArrayCell(Id(t),BinaryOp(+,Id(e),Id(y)))),ArrayCell(CallExpr(Id(foo),[Id(a),Id(r),Id(e)]),BinaryOp(-,Id(t),CallExpr(Id(foo),[])))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_index_in_invol(self):
        
        input = """int a(){
            b = foo(x+1,a[i]);
            break;
            return b;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([BinaryOp(=,Id(b),CallExpr(Id(foo),[BinaryOp(+,Id(x),IntLiteral(1)),ArrayCell(Id(a),Id(i))])),Break(),Return(Id(b))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_logic_in_call_func(self):
        
        input = """int a(){
            b=foo(func(a,goo(a[i]),a[f(a[b+i(1)||foo()])],x()));
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([BinaryOp(=,Id(b),CallExpr(Id(foo),[CallExpr(Id(func),[Id(a),CallExpr(Id(goo),[ArrayCell(Id(a),Id(i))]),ArrayCell(Id(a),CallExpr(Id(f),[ArrayCell(Id(a),BinaryOp(||,BinaryOp(+,Id(b),CallExpr(Id(i),[IntLiteral(1)])),CallExpr(Id(foo),[])))])),CallExpr(Id(x),[])])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_nested_assign(self):
        
        input = """int a(){
            a = b[10] = foo(a,d,f)= f(a,r,a[2])[t-8] = t%5 = r;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(=,ArrayCell(Id(b),IntLiteral(10)),BinaryOp(=,CallExpr(Id(foo),[Id(a),Id(d),Id(f)]),BinaryOp(=,ArrayCell(CallExpr(Id(f),[Id(a),Id(r),ArrayCell(Id(a),IntLiteral(2))]),BinaryOp(-,Id(t),IntLiteral(8))),BinaryOp(=,BinaryOp(%,Id(t),IntLiteral(5)),Id(r))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_assign_call_func(self):
        
        input = """int a(){
            int a;
            a = 1;
            fun1(fun2(fun3(a[2])))[1] = fun1(i || b[fun(t)]);
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,ArrayCell(CallExpr(Id(fun1),[CallExpr(Id(fun2),[CallExpr(Id(fun3),[ArrayCell(Id(a),IntLiteral(2))])])]),IntLiteral(1)),CallExpr(Id(fun1),[BinaryOp(||,Id(i),ArrayCell(Id(b),CallExpr(Id(fun),[Id(t)])))])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_null_string(self):
        
        input = """int a(){
            int a;
            a = 1;
            s = " " + " ";
            s1= " " - " ";
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(s),BinaryOp(+,StringLiteral( ),StringLiteral( ))),BinaryOp(=,Id(s1),BinaryOp(-,StringLiteral( ),StringLiteral( )))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_expression_and_comment(self):
        
        input = """int a(){
            a=a+1;// a line comment;
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_string_and_bool(self):
        
        input = """int a(){
            string a;
            a = "";
            a= a+" " - false;
            return ;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(a),StringType),BinaryOp(=,Id(a),StringLiteral()),BinaryOp(=,Id(a),BinaryOp(-,BinaryOp(+,Id(a),StringLiteral( )),BooleanLiteral(false))),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_return_comment(self):
        
        input = """int a(){
            return /*expr;*/;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_comment_in_comment(self):
        
        input = """int a(){
            int a;
            a = 1;
            /* comment 
            //////////*/
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_null_for(self):
        
        input = """int a(){
            for(true;!e;t){
                {}{}{
                    {}{}
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([For(BooleanLiteral(true);UnaryOp(!,Id(e));Id(t);Block([Block([]),Block([]),Block([Block([]),Block([])])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_complex_program(self):
        
        input = """int a(){
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
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(x),IntType),BinaryOp(=,Id(x),IntLiteral(9)),Dowhile([Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),IntLiteral(0)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(x))),If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(3)),IntLiteral(0)),BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1))),Block([BinaryOp(=,Id(x),BinaryOp(-,Id(x),IntLiteral(1)))]))])],BinaryOp(&&,BinaryOp(>=,Id(x),IntLiteral(0)),BinaryOp(<,Id(a),IntLiteral(100)))),Return(IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_complex_for(self):
        input = """int a(){
            int i;
            int count;
            count =10;
            for(i = 0; i < count; i = i + 1){
                if( i == 8) break;
                if(( i % 2) == 0) continue;
                else{
                    print(i);break;continue;return;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(i),IntType),VarDecl(Id(count),IntType),BinaryOp(=,Id(count),IntLiteral(10)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(count));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),IntLiteral(8)),Break()),If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),Continue(),Block([CallExpr(Id(print),[Id(i)]),Break(),Continue(),Return()]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_null_program(self):
        
        input = """int a(){
           
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_nested_LB_RB(self):
        
        input = """int a(){
            ((((foo()[t+9]))));
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([ArrayCell(CallExpr(Id(foo),[]),BinaryOp(+,Id(t),IntLiteral(9)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_return_nested_LB_RB(self):
        
        input = """int a(){
           return ((((!(true)))));
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Return(UnaryOp(!,BooleanLiteral(true)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_array_in_dowhile(self):
        
        input = """int a(){
            int a[3];
            do{
                boolean b;
                a[0] = foo(2);
                a[1] = put(2,7);
                a[2] = push(37);
            }
            while( b >= 0);
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(a),ArrayType(IntType,IntLiteral(3))),Dowhile([Block([VarDecl(Id(b),BoolType),BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),CallExpr(Id(foo),[IntLiteral(2)])),BinaryOp(=,ArrayCell(Id(a),IntLiteral(1)),CallExpr(Id(put),[IntLiteral(2),IntLiteral(7)])),BinaryOp(=,ArrayCell(Id(a),IntLiteral(2)),CallExpr(Id(push),[IntLiteral(37)]))])],BinaryOp(>=,Id(b),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_complex_if(self):
        
        input = """int a(){
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
                do{}while (true);
                {}{}
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([If(BinaryOp(==,Id(a),IntLiteral(5)),Block([CallExpr(Id(print),[StringLiteral(D)])]),Block([If(BinaryOp(!=,Id(b),IntLiteral(9)),Block([CallExpr(Id(print),[StringLiteral(K)])]),Block([BinaryOp(=,Id(b),IntLiteral(70))])),BinaryOp(=,Id(b),IntLiteral(12)),Dowhile([Block([])],BooleanLiteral(true)),Block([]),Block([])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_array_two_function(self):
        
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
        expect = "Program([FuncDecl(Id(decla),[],ArrayTypePointer(IntType),Block([VarDecl(Id(a),ArrayType(IntType,IntLiteral(2))),BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(a),IntLiteral(1)),IntLiteral(2)),Return(Id(a))])),FuncDecl(Id(main),[VarDecl(Id(arg),ArrayTypePointer(IntType))],VoidType,Block([VarDecl(Id(b),ArrayType(IntType,IntLiteral(2))),BinaryOp(=,Id(b),CallExpr(Id(decla),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_string_for_dowhile(self):
        
        input = """int a(){
            for(true;false;" "){
                do{
                    for("";true;false){
                        do{
                            for("";"";""){
                                if("") s+9;
                            }
                        }while !false;
                    }
                }while !true;
                return;
                break;
                continue;
                
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([For(BooleanLiteral(true);BooleanLiteral(false);StringLiteral( );Block([Dowhile([Block([For(StringLiteral();BooleanLiteral(true);BooleanLiteral(false);Block([Dowhile([Block([For(StringLiteral();StringLiteral();StringLiteral();Block([If(StringLiteral(),BinaryOp(+,Id(s),IntLiteral(9)))]))])],UnaryOp(!,BooleanLiteral(false)))]))])],UnaryOp(!,BooleanLiteral(true))),Return(),Break(),Continue()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_many_var_decla(self):
        
        input = """int a(){
            int a;
            a = 1.0987e4;
            int b;
            b = 8.97e-10;
            int c;
            c = (((a*a+a)*b-a*b)*a*b-34/a)/a -5*b;
            print(c);
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),FloatLiteral(10987.0)),VarDecl(Id(b),IntType),BinaryOp(=,Id(b),FloatLiteral(8.97e-10)),VarDecl(Id(c),IntType),BinaryOp(=,Id(c),BinaryOp(-,BinaryOp(/,BinaryOp(-,BinaryOp(*,BinaryOp(*,BinaryOp(-,BinaryOp(*,BinaryOp(+,BinaryOp(*,Id(a),Id(a)),Id(a)),Id(b)),BinaryOp(*,Id(a),Id(b))),Id(a)),Id(b)),BinaryOp(/,IntLiteral(34),Id(a))),Id(a)),BinaryOp(*,IntLiteral(5),Id(b)))),CallExpr(Id(print),[Id(c)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_neg_return_func(self):
        
        input = """int a(){
            return ---- fo(a,b,e[3+y])[rewq+67*t[56%r]-i[0]];
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Return(UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,ArrayCell(CallExpr(Id(fo),[Id(a),Id(b),ArrayCell(Id(e),BinaryOp(+,IntLiteral(3),Id(y)))]),BinaryOp(-,BinaryOp(+,Id(rewq),BinaryOp(*,IntLiteral(67),ArrayCell(Id(t),BinaryOp(%,IntLiteral(56),Id(r))))),ArrayCell(Id(i),IntLiteral(0)))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_neg_and_not_return_func(self):
        
        input = """int a(){
            return ----!!!!fo(a,b,e[3+y])[rewq+67*t[56%r]-i[0]];
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Return(UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,ArrayCell(CallExpr(Id(fo),[Id(a),Id(b),ArrayCell(Id(e),BinaryOp(+,IntLiteral(3),Id(y)))]),BinaryOp(-,BinaryOp(+,Id(rewq),BinaryOp(*,IntLiteral(67),ArrayCell(Id(t),BinaryOp(%,IntLiteral(56),Id(r))))),ArrayCell(Id(i),IntLiteral(0)))))))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_dowhile_for(self):
        input = """int a(){
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
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([VarDecl(Id(b),IntType),VarDecl(Id(s),StringType),BinaryOp(=,Id(s),StringLiteral(Hi)),BinaryOp(=,Id(b),IntLiteral(1)),Dowhile([Block([VarDecl(Id(i),IntType),For(BinaryOp(=,Id(i),IntLiteral(10));BinaryOp(>,Id(i),IntLiteral(0));BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));Block([])),BinaryOp(=,Id(b),BinaryOp(-,Id(b),IntLiteral(1)))])],BinaryOp(>,Id(b),IntLiteral(0))),Return(Id(s))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_else_string(self):
        input = """int a(){
            if(s>6){}
            else{
                "";" ";"astgensuite";//"astgen comment" " comment" @@;
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([If(BinaryOp(>,Id(s),IntLiteral(6)),Block([]),Block([StringLiteral(),StringLiteral( ),StringLiteral(astgensuite)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_dowhile_comment(self):
        input = """int a(){
           do{
               ///" a byte line" do   while;
           }
           while false;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Dowhile([Block([])],BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_for_and_comment(self):
        input = """int a(){
            for("";"";""){
                for("";!a;!!b){
                    for("";--a;11--d){
                        //// day chi la 1 comment "astgen";
                        /// comment1;
                        /// comment2
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([For(StringLiteral();StringLiteral();StringLiteral();Block([For(StringLiteral();UnaryOp(!,Id(a));UnaryOp(!,UnaryOp(!,Id(b)));Block([For(StringLiteral();UnaryOp(-,UnaryOp(-,Id(a)));BinaryOp(-,IntLiteral(11),UnaryOp(-,Id(d)));Block([]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_if_dowhile_for_null_string(self):
        input = """int a(){
            do{
                if(""){}
                else{}
                do{
                    {}{}for("";"";""){}
                }
                while "";
            }
            while "";
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Dowhile([Block([If(StringLiteral(),Block([]),Block([])),Dowhile([Block([Block([]),Block([]),For(StringLiteral();StringLiteral();StringLiteral();Block([]))])],StringLiteral())])],StringLiteral())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_nested_neg_and_not(self):
        input = """int a(){
            return --!!--!!--!!--!!--!!true;
        }"""
        expect = "Program([FuncDecl(Id(a),[],IntType,Block([Return(UnaryOp(-,UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(!,UnaryOp(!,BooleanLiteral(true))))))))))))))))))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,385))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,386))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,387))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,388))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,389))
    # def test_simple_program(self):
    #     input = """int a(){
    #         int a;
    #         a = 1;
    #         /* comment 
    #         //////////*/
    #     }"""
    #     expect = " "
    #     self.assertTrue(TestAST.checkASTGen(input,expect,390))
    
   