import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
################### test case of teacher ########################
    
    def test_simple_program(self):
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_more_complex_program(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_call_without_parameter(self):
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
########## my simple test #######################
    def test_simple_vardecl1(self):
        input = """int a; """
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_simple_vardecl2(self):
        input = """int a;
        float b[8];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(8,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_simple_vardecl3(self):
        input = """string a,b,c; """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_simple_vardecl4(self):
        input = """boolean a,b,c[6];"""
        expect = str(Program([VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",ArrayType(6,BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_simple_vardecl5(self):
        input = """int a,b,c;
            string d[9],e;"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(9,StringType())),VarDecl("e",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_simple_funcdecl1(self):
        input = """void main(){}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    
    def test_simple_funcdecl2(self):
        input = """boolean exp(int a){ float c[2];}"""
        expect = str(Program([FuncDecl(Id("exp"),[VarDecl("a",IntType())],BoolType(),Block([VarDecl("c",ArrayType(2,FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_simple_funcdecl3(self):
        input = """float foo(int a,int b){
            int a,b[5];
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",IntType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
  
    def test_simple_funcdecl4(self):
        input = """boolean IsHauTall(int a, int b[]){}"""
        expect = str(Program([FuncDecl(Id("IsHauTall"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType()))],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_simple_funcdecl5(self):
        input = """int[] Crazy(){}"""
        expect = str(Program([FuncDecl(Id("Crazy"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
 
    def test_simple_type(self):
        input = """int a;
        float b;
        boolean c;
        string d;
        int e[9];
        void main(){}
        int[] toList(){}"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("e",ArrayType(9,IntType())),FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("toList"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
 
    def test_simple_listeral1(self):
        input = """void LoveU(){
            x = 112;
        }"""
        expect = str(Program([FuncDecl(Id("LoveU"),[],VoidType(),Block([BinaryOp("=",Id("x"),IntLiteral(112))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
 
    def test_simple_listeral2(self):
        input = """void LoveU(){
            x = 1.;
        }"""
        expect = str(Program([FuncDecl(Id("LoveU"),[],VoidType(),Block([BinaryOp("=",Id("x"),FloatLiteral(1.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
  
    def test_simple_listeral3(self):
        input = """void LoveU(){
            x = 1.e8;
            y = .9e-10;
        }"""
        expect = str(Program([FuncDecl(Id("LoveU"),[],VoidType(),Block([BinaryOp("=",Id("x"),FloatLiteral(100000000.0)),BinaryOp("=",Id("y"),FloatLiteral(9e-11))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
  
    def test_simple_listeral4(self):
        input = """void LoveU(){
            meow = "everybody say meow";
        }"""
        expect = str(Program([FuncDecl(Id("LoveU"),[],VoidType(),Block([BinaryOp("=",Id("meow"),StringLiteral("everybody say meow"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
   
    def test_simple_listeral5(self):
        input = """boolean LoveU(){
            if(loveme)
                return true;
            else return false;
        }"""
        expect = str(Program([FuncDecl(Id("LoveU"),[],BoolType(),Block([If(Id("loveme"),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
  
    def test_simple_program1(self):
        input = """void Crazy(){}
        float a;"""
        expect = str(Program([FuncDecl(Id("Crazy"),[],VoidType(),Block([])),VarDecl("a",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
  
    def test_simple_program2(self):
        input = """int Crazy(){}
        string a,b,c;"""
        expect = str(Program([FuncDecl(Id("Crazy"),[],IntType(),Block([])),VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
  
    def test_simple_program3(self):
        input = """boolean a;
        float[] Crazy(){}
        int b[12], c;"""
        expect = str(Program([VarDecl("a",BoolType()),FuncDecl(Id("Crazy"),[],ArrayPointerType(FloatType()),Block([])),VarDecl("b",ArrayType(12,IntType())),VarDecl("c",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
  
    def test_simple_program4(self):
        input = """int Crazy(){
            {}{}
        }"""
        expect = str(Program([FuncDecl(Id("Crazy"),[],IntType(),Block([Block([]),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
 
    def test_simple_program5(self):
        input = """int Crazy(){{}}"""
        expect = str(Program([FuncDecl(Id("Crazy"),[],IntType(),Block([Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
  
    def test_simple_return1(self):
        input = """int Crazy(){
            return 0;
        }"""
        expect = str(Program([FuncDecl(Id("Crazy"),[],IntType(),Block([Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
 
    def test_simple_return2(self):
        input = """void main(int argc[]){
            return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("argc",ArrayPointerType(IntType()))],VoidType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
  
    def test_simple_break1(self):
        input = """void main(){
            break;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
  
    def test_simple_continue(self):
        input = """void main(){
            continue;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
 
    def test_simple_funccall1(self):
        input = """void main(){
            foo(d);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[Id("d")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
  
    def test_simple_funccall2(self):
        input = """void main(){
            Meow(dog,"string");
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("Meow"),[Id("dog"),StringLiteral("string")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
  
    def test_simple_block1(self):
        input = """void main(){
            {return;}{{}}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([Return()]),Block([Block([])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
  
    def test_simple_block2(self):
        input = """void main(){
            {i = 2;}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([BinaryOp("=",Id("i"),IntLiteral(2))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
  
    def test_simple_block3(self):
        input = """void main(){
            {int a,b,c[7];}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(7,IntType()))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
  
    def test_simple_block4(self):
        input = """void main(){
            {return;}{{}}{}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([Return()]),Block([Block([])]),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
  
    def test_simple_if1(self):
        input = """void main(){
            if ( i == 2) return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(2)),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
  
    def test_simple_if2(self):
        input = """void main(){
            if ( i == 2) return; else {continue;}
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(2)),Return(),Block([Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
  
    def test_simple_dowhile1(self):
        input = """void main(){
            do i = 2; while a == b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),IntLiteral(2))],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
 
    def test_simple_dowhile2(self):
        input = """void main(){
            do i = 2; j = 5; while x == y;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("=",Id("j"),IntLiteral(5))],BinaryOp("==",Id("x"),Id("y")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
  
    def test_simple_dowhile3(self):
        input = """void main(){
            do 
                a = 5;
                {b = 2;{}}
                c = a;
            while a > b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(5)),Block([BinaryOp("=",Id("b"),IntLiteral(2)),Block([])]),BinaryOp("=",Id("c"),Id("a"))],BinaryOp(">",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
   
    def test_simple_for1(self):
        input = """void main(){
            for(i = 0; i < 10; i = i + 1) a = a + 1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
  
    def test_simple_for2(self):
        input = """void main(){
            for(i = a[5]; i != 10; i = i * 2) {
                a = a / 2;
                {
                    b = b % 2;
                    c = 5;
                }
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),ArrayCell(Id("a"),IntLiteral(5))),BinaryOp("!=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(2))),Block([BinaryOp("=",Id("a"),BinaryOp("/",Id("a"),IntLiteral(2))),Block([BinaryOp("=",Id("b"),BinaryOp("%",Id("b"),IntLiteral(2))),BinaryOp("=",Id("c"),IntLiteral(5))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
  
    def test_simple_expr_binary1(self):
        input = """void main(){
            a = b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
   
    def test_simple_expr_binary2(self):
        input = """void main(){
            a = b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
 
    def test_simple_expr_binary3(self):
        input = """void main(){
            a == b || a != c;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("a"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
   
    def test_simple_expr_binary4(self):
        input = """void main(){
            if(x >= 2 && y < 4) return;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",BinaryOp(">=",Id("x"),IntLiteral(2)),BinaryOp("<",Id("y"),IntLiteral(4))),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
  
    def test_simple_expr_binary5(self):
        input = """void main(){
            a = (b / 2 + 5) % 4 -1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("%",BinaryOp("+",BinaryOp("/",Id("b"),IntLiteral(2)),IntLiteral(5)),IntLiteral(4)),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
  
    def test_simple_expr_unary(self):
        input = """void main(){
            a = -5;
            c = !(a == 2);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),UnaryOp("-",IntLiteral(5))),BinaryOp("=",Id("c"),UnaryOp("!",BinaryOp("==",Id("a"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
  
    def test_simple_expr_arraycell(self):
        input = """void main(){
            a = b[5];
            c = d[x*x + 2];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),ArrayCell(Id("b"),IntLiteral(5))),BinaryOp("=",Id("c"),ArrayCell(Id("d"),BinaryOp("+",BinaryOp("*",Id("x"),Id("x")),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    

############## more complex test ##############################
    def test_AST49(self):
        input = """int main () {
            boolean a,b,c;
            int k[6];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("k",ArrayType(6,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
  
    def test_AST50(self):
        input = """void foo () {
            int a,b,c,xd;
            int i[4];
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("xd",IntType()),VarDecl("i",ArrayType(4,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
  
    def test_AST51(self):
        input = """int main (){
            int a,b,x;
            if(a != 2)
                x = x + 2;
            else
                a = 2*x;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("x",IntType()),If(BinaryOp("!=",Id("a"),IntLiteral(2)),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(2))),BinaryOp("=",Id("a"),BinaryOp("*",IntLiteral(2),Id("x"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
  
    def test_AST52(self):
        input = """int main() {
            int a,b,c;
            boolean x[50];
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("x",ArrayType(50,BoolType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
  
    def test_AST53(self):
        input = """int main() {
            int a,b;
            if(x!=2){
               a = 100*(2+b);
               return a;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),If(BinaryOp("!=",Id("x"),IntLiteral(2)),Block([BinaryOp("=",Id("a"),BinaryOp("*",IntLiteral(100),BinaryOp("+",IntLiteral(2),Id("b")))),Return(Id("a"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
  
    def test_AST54(self):
        input = """int main() {
            int a,b;
            if(x!=2){
               a = 100*(2+b);
               return a;
            } else {
                b = 68 % a - a;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),If(BinaryOp("!=",Id("x"),IntLiteral(2)),Block([BinaryOp("=",Id("a"),BinaryOp("*",IntLiteral(100),BinaryOp("+",IntLiteral(2),Id("b")))),Return(Id("a"))]),Block([BinaryOp("=",Id("b"),BinaryOp("-",BinaryOp("%",IntLiteral(68),Id("a")),Id("a")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
 
    def test_AST55(self):
        input = """int main() {
            int a,b,c,d;
            if ( a==1) if (b==1) if(c==1) return; else d = a/b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),If(BinaryOp("==",Id("b"),IntLiteral(1)),If(BinaryOp("==",Id("c"),IntLiteral(1)),Return(),BinaryOp("=",Id("d"),BinaryOp("/",Id("a"),Id("b"))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
  
    def test_AST56(self):
        input = """int main() {
            int a,b,c,d;
            if ( a==1)
                a = b;
            else if (b==1){}
            else if(c==1){}
            else
                d = a/b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),Id("b")),If(BinaryOp("==",Id("b"),IntLiteral(1)),Block([]),If(BinaryOp("==",Id("c"),IntLiteral(1)),Block([]),BinaryOp("=",Id("d"),BinaryOp("/",Id("a"),Id("b"))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356)) 
  
    def test_AST57(self):
        input = """int main() {
            float x;
            if (x == 3){
                string s,m,l[6];
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",FloatType()),If(BinaryOp("==",Id("x"),IntLiteral(3)),Block([VarDecl("s",StringType()),VarDecl("m",StringType()),VarDecl("l",ArrayType(6,StringType()))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
  
    def test_AST58(self):
        input = """int main() {}
        float foo(int a,string b[],boolean c){}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(StringType())),VarDecl("c",BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
  
    def test_AST59(self):
        input = """int main() {}
        string a,b,x[2];
        int[] arr(float m, int n){}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("x",ArrayType(2,StringType())),FuncDecl(Id("arr"),[VarDecl("m",FloatType()),VarDecl("n",IntType())],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
  
    def test_AST60(self):
        input = """void main() {}
        boolean exp(){ return;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("exp"),[],BoolType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
  
    def test_AST61(self):
        input = """void main() {
            do{}while 1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
  
    def test_AST62(self):
        input = """void main() {
            do {int a;}{float b;} while x;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType())]),Block([VarDecl("b",FloatType())])],Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
 
    def test_AST63(self):
        input = """void main() {
            int x;
            do {int a;} x = x*x; {float b;} while x;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("x",IntType()),Dowhile([Block([VarDecl("a",IntType())]),BinaryOp("=",Id("x"),BinaryOp("*",Id("x"),Id("x"))),Block([VarDecl("b",FloatType())])],Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
  
    def test_AST64(self):
        input = """void main() {
            do{}while (a + b/2 - 4) || x == 3;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([])],BinaryOp("||",BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("/",Id("b"),IntLiteral(2))),IntLiteral(4)),BinaryOp("==",Id("x"),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
 
    def test_AST65(self):
        input = """int main (){
            int a,b,c;
            do {int d;}
            while b == 1;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([Block([VarDecl("d",IntType())])],BinaryOp("==",Id("b"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
  
    def test_AST66(self):
        input = """int main (){
            int a,b,c;
            do {int d;} x=2;
            while b[6] != (a*b);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([Block([VarDecl("d",IntType())]),BinaryOp("=",Id("x"),IntLiteral(2))],BinaryOp("!=",ArrayCell(Id("b"),IntLiteral(6)),BinaryOp("*",Id("a"),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
  
    def test_AST67(self):
        input = """float[] sqrt(int a[],float b){}
        int main() {
            sqrt(a,b);
        }"""
        expect = str(Program([FuncDecl(Id("sqrt"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType())],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("sqrt"),[Id("a"),Id("b")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
 
    def test_AST68(self):
        input = """int main() { a = a + foo(d);}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("d")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
  
    def test_AST69(self):
        input = """int main() {
        a = 2 + foo(d,x+2,"this is string");}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(2),CallExpr(Id("foo"),[Id("d"),BinaryOp("+",Id("x"),IntLiteral(2)),StringLiteral("this is string")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
   
    def test_AST70(self):
        input = """int main(){
            x = src(foo(a,b),1.e-8,c,"string",1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("x"),CallExpr(Id("src"),[CallExpr(Id("foo"),[Id("a"),Id("b")]),FloatLiteral(1e-08),Id("c"),StringLiteral("string"),IntLiteral(1)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

#Test The For statement
    def test_AST71(self):
        input = """int main (){
            int a,b,c;
            for(foo();x;"string") a + b;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),For(CallExpr(Id("foo"),[]),Id("x"),StringLiteral("string"),BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

#Test break statement
    def test_AST72(self):
        input = """float foo() {
            do{if(i==1) break;} if(i==2) break; while (1);
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[],FloatType(),Block([Dowhile([Block([If(BinaryOp("==",Id("i"),IntLiteral(1)),Break())]),If(BinaryOp("==",Id("i"),IntLiteral(2)),Break())],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

#Test Continue statement
    def test_AST73(self):
        input = """int main() {
            for(i=1;a=1;b=2){
                x = x*x;
                if (y == true) continue;
            }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),Block([BinaryOp("=",Id("x"),BinaryOp("*",Id("x"),Id("x"))),If(BinaryOp("==",Id("y"),BooleanLiteral(True)),Continue())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

#Test return statement
    def test_AST74(self):
        input = """int main() { return 123;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(IntLiteral(123))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    
    def test_AST75(self):
        input = """void main() { return;}"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
  
    def test_AST76(self):
        input = """int main() {return a / foo(a,b,"string");}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("/",Id("a"),CallExpr(Id("foo"),[Id("a"),Id("b"),StringLiteral("string")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

#Test expression and expression statement
    def test_AST77(self):
        input = """int main() { a = a + b - c * d;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
   
    def test_AST78(self):
        input = """int main() {
            boolean a;
            a = (a[d] == 1) && (x !=2 || a >= 3);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",BoolType()),BinaryOp("=",Id("a"),BinaryOp("&&",BinaryOp("==",ArrayCell(Id("a"),Id("d")),IntLiteral(1)),BinaryOp("||",BinaryOp("!=",Id("x"),IntLiteral(2)),BinaryOp(">=",Id("a"),IntLiteral(3)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
 
    def test_AST79(self):
        input = """int main() {159/2*a;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("*",BinaryOp("/",IntLiteral(159),IntLiteral(2)),Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
 
    def test_AST80(self):
        input = """int main() { i = (p =! (x > 2));}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("i"),BinaryOp("=",Id("p"),UnaryOp("!",BinaryOp(">",Id("x"),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
  
    def test_AST81(self):
        input = """int main() {return a+2*b==d%5-1;}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("==",BinaryOp("+",Id("a"),BinaryOp("*",IntLiteral(2),Id("b"))),BinaryOp("-",BinaryOp("%",Id("d"),IntLiteral(5)),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

# Test block statement
    def test_AST82(self):
        input = """int main() {int a,b,c[2];}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(2,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
  
    def test_AST83(self):
        input = """int main() {
            {int a,b,c[6];}
            a = foo("string",b);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(6,IntType()))]),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[StringLiteral("string"),Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
 
    def test_AST84(self):
        input = """int main() {{}}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
 
    def test_AST85(self):
        input = """int main() {{}{}{{}}}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([]),Block([]),Block([Block([])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
 
    def test_AST86(self):
        input = """int main() {{}{}{} float x; {{ if(i==1) return 2;}}}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([]),Block([]),Block([]),VarDecl("x",FloatType()),Block([Block([If(BinaryOp("==",Id("i"),IntLiteral(1)),Return(IntLiteral(2)))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
 
    def test_AST87(self):
        input = """int main() {
            do{{}}return;{}{}while (1);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Block([])]),Return(),Block([]),Block([])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
 
    def test_AST88(self):
        input = """int main() {
            x = "This is block";
            x = true;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("x"),StringLiteral("This is block")),BinaryOp("=",Id("x"),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
  
    def test_AST89(self):
        input = """float a[5];
            int main() {}"""
        expect = str(Program([VarDecl("a",ArrayType(5,FloatType())),FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
  
    def test_AST90(self):
        input = """int get(int a){
            return a[b[2%(main())]];
        }"""
        expect = str(Program([FuncDecl(Id("get"),[VarDecl("a",IntType())],IntType(),Block([Return(ArrayCell(Id("a"),ArrayCell(Id("b"),BinaryOp("%",IntLiteral(2),CallExpr(Id("main"),[])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
 
    def test_AST91(self):
        input = """int main(string args[]){
            int x;
            int y;
            x=1;
            y=2;
            if(x!=y) return 1;
            else return 0;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("args",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),BinaryOp("=",Id("x"),IntLiteral(1)),BinaryOp("=",Id("y"),IntLiteral(2)),If(BinaryOp("!=",Id("x"),Id("y")),Return(IntLiteral(1)),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
  
    def test_AST92(self):
        input = """int main(string args[]){
            int x;
            x=100;
            do --x; y + 2; while x<10;
        }"""
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("args",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(100)),Dowhile([UnaryOp("-",UnaryOp("-",Id("x"))),BinaryOp("+",Id("y"),IntLiteral(2))],BinaryOp("<",Id("x"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
  
    def test_AST93(self):
        input = """int foo() {
            (foo(258,"string")+12.5) == arr[goo(true)];
          }"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("==",BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(258),StringLiteral("string")]),FloatLiteral(12.5)),ArrayCell(Id("arr"),CallExpr(Id("goo"),[BooleanLiteral(True)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
   
    def test_AST94(self):
        input = """int foo() {
            foo(2)[3]=arr[7]=true;
            if(1) arr[7]=true; else arr[7]=false;
            do if(1) arr[7]=true; else arr[7]=false; while arr=6;
            for(i=1;i<9;i=5) do if(1) arr[7]=true; else arr[7]=false; while arr=6;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(3)),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(True))),If(IntLiteral(1),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(True)),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(False))),Dowhile([If(IntLiteral(1),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(True)),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(False)))],BinaryOp("=",Id("arr"),IntLiteral(6))),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(9)),BinaryOp("=",Id("i"),IntLiteral(5)),Dowhile([If(IntLiteral(1),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(True)),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BooleanLiteral(False)))],BinaryOp("=",Id("arr"),IntLiteral(6))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
 
    def test_AST95(self):
        input = """int sub(string x, float y[]){
            for(1;2;3) break;
            break;
            continue;
            return 1;
            return;
        }"""
        expect = str(Program([FuncDecl(Id("sub"),[VarDecl("x",StringType()),VarDecl("y",ArrayPointerType(FloatType()))],IntType(),Block([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Break()),Break(),Continue(),Return(IntLiteral(1)),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_AST96(self):
        input = """
        string b(boolean a[]) {
            if (a == b) {{{{{return;{{{}{{}}}}}}}}}
        }
        string b(boolean a[]) {
            for (a;a;a) {return x;}
        }"""
        expect = str(Program([FuncDecl(Id("b"),[VarDecl("a",ArrayPointerType(BoolType()))],StringType(),Block([If(BinaryOp("==",Id("a"),Id("b")),Block([Block([Block([Block([Block([Return(),Block([Block([Block([]),Block([Block([])])])])])])])])]))])),FuncDecl(Id("b"),[VarDecl("a",ArrayPointerType(BoolType()))],StringType(),Block([For(Id("a"),Id("a"),Id("a"),Block([Return(Id("x"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
  
    def test_AST97(self):
        input = """string b(boolean a[]) {
            for (i;true;i) {{{{{{continue;{{{{{{}{}}}}}}}}}}}}
        }
        string b(boolean a[]) {
            for (i;2;i) {continue;}
        }
        string b(boolean a[]) {
            for (i;2;i) {break;}
        }
        string b(boolean a[]) {
            for (x = 0 ; false ;2) {}
        }"""
        expect = str(Program([FuncDecl(Id("b"),[VarDecl("a",ArrayPointerType(BoolType()))],StringType(),Block([For(Id("i"),BooleanLiteral(True),Id("i"),Block([Block([Block([Block([Block([Block([Continue(),Block([Block([Block([Block([Block([Block([]),Block([])])])])])])])])])])])]))])),FuncDecl(Id("b"),[VarDecl("a",ArrayPointerType(BoolType()))],StringType(),Block([For(Id("i"),IntLiteral(2),Id("i"),Block([Continue()]))])),FuncDecl(Id("b"),[VarDecl("a",ArrayPointerType(BoolType()))],StringType(),Block([For(Id("i"),IntLiteral(2),Id("i"),Block([Break()]))])),FuncDecl(Id("b"),[VarDecl("a",ArrayPointerType(BoolType()))],StringType(),Block([For(BinaryOp("=",Id("x"),IntLiteral(0)),BooleanLiteral(False),IntLiteral(2),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
   
    def test_AST98(self):
        input = """string b(int a) {
            // Hello word
            // I'm the best yasuo
            (foo(3)-go(0))[2];
            a == b < c;
        }
        int main() {
            int a,x,y[5];
        }"""
        expect = str(Program([FuncDecl(Id("b"),[VarDecl("a",IntType())],StringType(),Block([ArrayCell(BinaryOp("-",CallExpr(Id("foo"),[IntLiteral(3)]),CallExpr(Id("go"),[IntLiteral(0)])),IntLiteral(2)),BinaryOp("==",Id("a"),BinaryOp("<",Id("b"),Id("c")))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("x",IntType()),VarDecl("y",ArrayType(5,IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
   
    def test_AST99(self):
        input = """int recursive(int n){
            if (n == 1)
                return 1;
            return n * recursive(n - 1);
            /* Good bye
            see you again */
        }"""
        expect = str(Program([FuncDecl(Id("recursive"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("==",Id("n"),IntLiteral(1)),Return(IntLiteral(1))),Return(BinaryOp("*",Id("n"),CallExpr(Id("recursive"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
   
    def test_AST100(self):
        input = """int main(){
            if (isLove(me) == false) return 0;
            for(i = currentDay;i <= myLife;i = i + 1){
                if (die) return 1; else break;
            }
            do {Love(x);}Love(y);{Love(z[9]);} while (richKid == true);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",CallExpr(Id("isLove"),[Id("me")]),BooleanLiteral(False)),Return(IntLiteral(0))),For(BinaryOp("=",Id("i"),Id("currentDay")),BinaryOp("<=",Id("i"),Id("myLife")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(Id("die"),Return(IntLiteral(1)),Break())])),Dowhile([Block([CallExpr(Id("Love"),[Id("x")])]),CallExpr(Id("Love"),[Id("y")]),Block([CallExpr(Id("Love"),[ArrayCell(Id("z"),IntLiteral(9))])])],BinaryOp("==",Id("richKid"),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    