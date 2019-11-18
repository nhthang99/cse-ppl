import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_300(self):
        input = """int main() 
                   {
                        /*any*/ 
                   }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_301(self):
        input = """int main() 
                    { 
                        printf("Hello!");
                    }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Hello!")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_302(self):
        input = """ int main(){
                        A||B;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("||",Id("A"),Id("B"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_303(self):
        input = """ int main(){
                        int A;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_304(self):
        input = """ int main(){
                        false;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_305(self):
        input = """ int main(){
                        int A;
                        A=B+C+D;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType()),BinaryOp("=",Id("A"),BinaryOp("+",BinaryOp("+",Id("B"),Id("C")),Id("D")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_306(self):
        input =  """ int main(){
                        float A;
                        A=B+C+D*A-B/D;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",FloatType()),BinaryOp("=",Id("A"),BinaryOp("-",BinaryOp("+",BinaryOp("+",Id("B"),Id("C")),BinaryOp("*",Id("D"),Id("A"))),BinaryOp("/",Id("B"),Id("D"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_307(self):
        input =  """ int main(){
                        A||B||C;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("||",BinaryOp("||",Id("A"),Id("B")),Id("C"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_308(self):
        input =  """ int main(){
                        boolean A;
                        A=B&&C&&D;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",BoolType()),BinaryOp("=",Id("A"),BinaryOp("&&",BinaryOp("&&",Id("B"),Id("C")),Id("D")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_309(self):
        input =  """ int main(){
                        string A;
                        A=B=C=D;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",StringType()),BinaryOp("=",Id("A"),BinaryOp("=",Id("B"),BinaryOp("=",Id("C"),Id("D"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_310(self):
        input =  """ int main(){
                        int A;
                        A<=B;
                        C>=D;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType()),BinaryOp("<=",Id("A"),Id("B")),BinaryOp(">=",Id("C"),Id("D"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_311(self):
        input =  """ int main(){
                        int A;
                        float B;
                        string C;
                        boolean D;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType()),VarDecl("B",FloatType()),VarDecl("C",StringType()),VarDecl("D",BoolType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    # def test_311(self):
    #     input =  """ int main(){
    #                     int A;
    #                     float B;
    #                     string C;
    #                     boolean D;
    #                 }
    #                 """
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType()),VarDecl("B",FloatType()),VarDecl("C",StringType()),VarDecl("D",BoolType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_312(self):
        input =  """ int main ()
                    {
                       for( a; a; a)
                       {     
                       }  
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("a"),Id("a"),Id("a"),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_313(self):
        input =  """int main ()
                    {
                       for( A; A; A)
                       { 
                            printf("vong lap mai mai.");    
                       }  
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("A"),Id("A"),Id("A"),Block([CallExpr(Id("printf"),[StringLiteral("vong lap mai mai.")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_314(self):
        input =  """ int main ()
                    {
                       for(111 ; 222; 333)
                       { 
                            printf("vong lap mai mai.");    
                       }  
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(IntLiteral(111),IntLiteral(222),IntLiteral(333),Block([CallExpr(Id("printf"),[StringLiteral("vong lap mai mai.")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_315(self):
        input =  """ int main ()
                    {
                       for(A>B ; A&&B||C; A+B)
                       { 
                            printf("vong lap mai mai.");    
                       }  
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp(">",Id("A"),Id("B")),BinaryOp("||",BinaryOp("&&",Id("A"),Id("B")),Id("C")),BinaryOp("+",Id("A"),Id("B")),Block([CallExpr(Id("printf"),[StringLiteral("vong lap mai mai.")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_316(self):
        input =  """ int main ()
                    {
                       return ;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_317(self):
        input =  """ int main ()
                    {
                       return A*B&&C;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("&&",BinaryOp("*",Id("A"),Id("B")),Id("C")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_318(self):
        input =  """ int main ()
                    {
                       break;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_319(self):
        input =  """ int main ()
                    {
                       continue;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_320(self):
        input =  """ int main ()
                    {
                       return A22+B1223-_C_+1.2+344;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("+",BinaryOp("+",BinaryOp("-",BinaryOp("+",Id("A22"),Id("B1223")),Id("_C_")),FloatLiteral(1.2)),IntLiteral(344)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    
    def test_321(self):
        input =  """ int main ()
                    {
                       if ( 5 < 10 ) {
                            printf( "Five is now less than ten");
                        }if ( true ) {
                            printf( "Do something here");
                        }
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",IntLiteral(5),IntLiteral(10)),Block([CallExpr(Id("printf"),[StringLiteral("Five is now less than ten")])])),If(BooleanLiteral(True),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    
    def test_322(self):
        input =  """ int main ()
                    {
                       if ( true ) {
                            printf( "Do something here");
                        }
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
   
    def test_323(self):
        input =  """ int main ()
                    {
                       if ( A+B+C>C ) {
                            printf( "Do something here");
                        }
                        else
                            printf( "Error!!!!!");
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",BinaryOp("+",BinaryOp("+",Id("A"),Id("B")),Id("C")),Id("C")),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]),CallExpr(Id("printf"),[StringLiteral("Error!!!!!")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_324(self):
        input =  """ int main ()
                    {
                       if ( false ) {
                            printf( "Do something here");
                        }
                        else
                            for(A;B;c){}
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(False),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]),For(Id("A"),Id("B"),Id("c"),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_325(self):
        input =  """ int main ()
                    {
                       if ( AAA234 ) {
                            printf( "Do something here");
                        }
                        else
                            return;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(Id("AAA234"),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_326(self):
        input =  """ int main ()
                    {
                       if ( A>B&&B>C ) {
                            printf( "Do something here");
                        }
                        else
                            break;
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp(">",Id("A"),Id("B")),BinaryOp(">",Id("B"),Id("C"))),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    
    def test_327(self):
        input =  """ int main ()
                    {
                       if ( A>B&&B>C ) {
                            printf( "Do something here");
                        }
                        else
                            if(A>C&&C>B){
                                //Any;;;
                            }
                            else
                                return;   
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp(">",Id("A"),Id("B")),BinaryOp(">",Id("B"),Id("C"))),Block([CallExpr(Id("printf"),[StringLiteral("Do something here")])]),If(BinaryOp("&&",BinaryOp(">",Id("A"),Id("C")),BinaryOp(">",Id("C"),Id("B"))),Block([]),Return()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_328(self):
        input =  """ int main ()
                    {
                       float a[7];
                       
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(7,FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_329(self):
        input =  """ int main ()
                    {
                       float a[20],b[20] ;
                       c[100]=a[b[0]];
                    }
                    """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(20,FloatType())),VarDecl("b",ArrayType(20,FloatType())),BinaryOp("=",ArrayCell(Id("c"),IntLiteral(100)),ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_330(self):
        input =  """int[] foo(int a, float b[])
                    {
                        foo(a-1,b);
                        return c; 
                    }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")]),Return(Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_331(self):
        input =  """ int[] foo(int a, float b[])
                    {
                        int c[3];
                        if (a>0)
                            foo(a-1,b);    
                        return c; 
                    }
                    """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")])),Return(Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_332(self):
        input =  """ int[] foo()
                    {
                        boolean b; 
                        int i; 
                        float f; 
                        boolean ba[5]; 
                        int ia[3]; 
                        float fa[100];
                    }
                    """
        expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([VarDecl("b",BoolType()),VarDecl("i",IntType()),VarDecl("f",FloatType()),VarDecl("ba",ArrayType(5,BoolType())),VarDecl("ia",ArrayType(3,IntType())),VarDecl("fa",ArrayType(100,FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_333(self):
        input =  """int[] foo()
                    {
                        int i;     
                        boolean boo[2];
                        boo[2]=true||false;
                    }
                    """
        expect = str(Program([FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([VarDecl("i",IntType()),VarDecl("boo",ArrayType(2,BoolType())),BinaryOp("=",ArrayCell(Id("boo"),IntLiteral(2)),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_334(self):
        input =  """ int foo ( int a , float b [] )
                    {
                        boolean c ;
                        int i ;
                        i = a + 3 ;
                        if ( i > 0) {
                            int d ;
                            d = i + 3 ;
                            putInt ( d ) ;
                        }
                        return i ;
                    }
                    """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_335(self):
        input =  """ int foo ( int a , float b [] )
                    {
                        foo(2)[3+x] = a[b[2]] +3;
                    }
                    """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_336(self):
        input =  """ 
                    void f(int a[]) {
                     
                    }
                """
        expect = str(Program([FuncDecl(Id("f"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_337(self):
        input =  """ void goo ( float x [] ) {
                        float y [10] ;
                        int z [ 10 ] ;                                      
                        foo ( x ) ; 
                        foo ( y ) ; 
                        foo ( z ) ; 
                    }
                """
        expect = str(Program([FuncDecl(Id("goo"),[VarDecl("x",ArrayPointerType(FloatType()))],VoidType(),Block([VarDecl("y",ArrayType(10,FloatType())),VarDecl("z",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("x")]),CallExpr(Id("foo"),[Id("y")]),CallExpr(Id("foo"),[Id("z")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_338(self):
        input =  """ void foo ( ) {
                        if (A) return; 
                        else return 2 ;
                    }               
                """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(Id("A"),Return(),Return(IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_339(self):
        input =  """ int [] foo ( int b [] ) {
                        i = 1 ;
                        foo (1,2) ;
                        i + 2 ;
                        100;
                    }
                """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([BinaryOp("=",Id("i"),IntLiteral(1)),CallExpr(Id("foo"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("+",Id("i"),IntLiteral(2)),IntLiteral(100)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_340(self):
        input =  """ int [] foo ( int b [] ) {
                        int a , b , c ; 
                        a=b=c =5; 
                        floatf [ 5 ] ; 
                        if ( a==b ) f[0] = 1.0 ; 
                    }
                """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),IntLiteral(5)))),ArrayCell(Id("floatf"),IntLiteral(5)),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",ArrayCell(Id("f"),IntLiteral(0)),FloatLiteral(1.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
   
    def test_341(self):
        input =  """
                     int f ( ) {
                        return 200;
                     }
                     void main ( ) {
                        int main ;
                        main = f ( ) ;
                        putIntLn ( main ) ;
                        {
                             int i ;
                             int main ;
                             int f ;
                             main = f = i = 100;
                             putIntLn ( i ) ;
                             putIntLn ( main ) ;
                             putIntLn ( f ) ;
                        }
                         putIntLn ( main ) ;
                     }
                """
        expect = str(Program([FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("main",IntType()),BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("main")]),Block([VarDecl("i",IntType()),VarDecl("main",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("main")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("main")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_342(self):
        input =  """ int main()
                    {
                        do{ 
                            //Any
                        }while (condition);  
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([])],Id("condition"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_343(self):
        input =  """ int main() {
                        printf("Do-While loop example");
                        fflush (stdout);
                        //int x = 2;
                        do {
                            printf("Value of x = %d", x);
                            x = x + 3;
                            fflush(stdout);
                        } while (x < 10); // Note: ==> Need ';'
                        return 0;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Do-While loop example")]),CallExpr(Id("fflush"),[Id("stdout")]),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Value of x = %d"),Id("x")]),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(3))),CallExpr(Id("fflush"),[Id("stdout")])])],BinaryOp("<",Id("x"),IntLiteral(10))),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_344(self):
        input =  """ int MaxNum(int Num1, int Num2) 
                    {
                       int result;
                     
                       if (Num1 > Num2)
                          result=Num1;
                       else
                          result = Num2;
                     
                       return result; 
                    }
                """
        expect = str(Program([FuncDecl(Id("MaxNum"),[VarDecl("Num1",IntType()),VarDecl("Num2",IntType())],IntType(),Block([VarDecl("result",IntType()),If(BinaryOp(">",Id("Num1"),Id("Num2")),BinaryOp("=",Id("result"),Id("Num1")),BinaryOp("=",Id("result"),Id("Num2"))),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_345(self):
        input =  """ int main ()
                    {
                       int A; 
                       A= 667;
                       int B; 
                       B= 7028;
                       int result;
                       result= MaxNum(A,B);
                     
                       printf( "Max Number is:", result );
                       printf("===========================");
                       return 0;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType()),BinaryOp("=",Id("A"),IntLiteral(667)),VarDecl("B",IntType()),BinaryOp("=",Id("B"),IntLiteral(7028)),VarDecl("result",IntType()),BinaryOp("=",Id("result"),CallExpr(Id("MaxNum"),[Id("A"),Id("B")])),CallExpr(Id("printf"),[StringLiteral("Max Number is:"),Id("result")]),CallExpr(Id("printf"),[StringLiteral("===========================")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_346(self):
        input =  """ int Fun_Sum(int A, int B)
                    {
                        printf ("Value of A: ",A);
                        printf ("Value of B: ",B);            
                        return A + B;
                    }
                """
        expect = str(Program([FuncDecl(Id("Fun_Sum"),[VarDecl("A",IntType()),VarDecl("B",IntType())],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Value of A: "),Id("A")]),CallExpr(Id("printf"),[StringLiteral("Value of B: "),Id("B")]),Return(BinaryOp("+",Id("A"),Id("B")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_347(self):
        input =  """ int main ()
                    {
                        int a; 
                        a= 15;
                        int b; 
                        b= 25;
                        int c;
                        c = Func_Sum (a, b);
                        printf ("Value of C:",  c);
                        return 0;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(15)),VarDecl("b",IntType()),BinaryOp("=",Id("b"),IntLiteral(25)),VarDecl("c",IntType()),BinaryOp("=",Id("c"),CallExpr(Id("Func_Sum"),[Id("a"),Id("b")])),CallExpr(Id("printf"),[StringLiteral("Value of C:"),Id("c")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_348(self):
        input =  """ int main ()
                    {
                        int A;
                        float B;
                        int C;
                        C=A+B+C-A*123/345+(A+B+C)*(123*345+567/(A+B/C*B));
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("A",IntType()),VarDecl("B",FloatType()),VarDecl("C",IntType()),BinaryOp("=",Id("C"),BinaryOp("+",BinaryOp("-",BinaryOp("+",BinaryOp("+",Id("A"),Id("B")),Id("C")),BinaryOp("/",BinaryOp("*",Id("A"),IntLiteral(123)),IntLiteral(345))),BinaryOp("*",BinaryOp("+",BinaryOp("+",Id("A"),Id("B")),Id("C")),BinaryOp("+",BinaryOp("*",IntLiteral(123),IntLiteral(345)),BinaryOp("/",IntLiteral(567),BinaryOp("+",Id("A"),BinaryOp("*",BinaryOp("/",Id("B"),Id("C")),Id("B"))))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_349(self):
        input =  """ int main ()
                    {
                        return;
                        break;
                        continue;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(),Break(),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_350(self):
        input =  """ int main ()
                    {
                        for(e;r;t){
                            do{
                                //Any
                            }
                            while(true);
                        }
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(Id("e"),Id("r"),Id("t"),Block([Dowhile([Block([])],BooleanLiteral(True))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_351(self):
        input =  """ int sum(int n)
                    {
                        int i, S;
                        for (i=0; i<=n; i+a)
                            S = S+i;
                        return S;
                    }
                """
        expect = str(Program([FuncDecl(Id("sum"),[VarDecl("n",IntType())],IntType(),Block([VarDecl("i",IntType()),VarDecl("S",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("n")),BinaryOp("+",Id("i"),Id("a")),BinaryOp("=",Id("S"),BinaryOp("+",Id("S"),Id("i")))),Return(Id("S"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_352(self):
        input =  """ void main()
                    {
                        float ss;
                        int h,m,s;
                        h=ss/3600;
                        m=ss%3600/60;
                        s=ss%60;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("ss",FloatType()),VarDecl("h",IntType()),VarDecl("m",IntType()),VarDecl("s",IntType()),BinaryOp("=",Id("h"),BinaryOp("/",Id("ss"),IntLiteral(3600))),BinaryOp("=",Id("m"),BinaryOp("/",BinaryOp("%",Id("ss"),IntLiteral(3600)),IntLiteral(60))),BinaryOp("=",Id("s"),BinaryOp("%",Id("ss"),IntLiteral(60)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_353(self):
        input =  """ void main()
                    {
                        float ss;
                        ss=12.345-0.02468+1.2345e01-2.468e-02;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("ss",FloatType()),BinaryOp("=",Id("ss"),BinaryOp("-",BinaryOp("+",BinaryOp("-",FloatLiteral(12.345),FloatLiteral(0.02468)),FloatLiteral(12.345)),FloatLiteral(0.02468)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_354(self):
        input =  """ void main()
                    {
                        int a, b;
                        a = b = 6;
                        b = (a= 3)+2;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),IntLiteral(6))),BinaryOp("=",Id("b"),BinaryOp("+",BinaryOp("=",Id("a"),IntLiteral(3)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_355(self):
        input =  """ void main()
                    {
                        float delta,pi;
                        int a,b,c;
                        delta= b*b-4*a*c;
                        pi= 4*atan(1.0);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("delta",FloatType()),VarDecl("pi",FloatType()),VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),BinaryOp("=",Id("delta"),BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c")))),BinaryOp("=",Id("pi"),BinaryOp("*",IntLiteral(4),CallExpr(Id("atan"),[FloatLiteral(1.0)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_356(self):
        input =  """ void main()
                    {
                        if (a>b)
                        {}
                        if (b!=0)
                        {}
                        if (a!=0)
                        {} 
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp(">",Id("a"),Id("b")),Block([])),If(BinaryOp("!=",Id("b"),IntLiteral(0)),Block([])),If(BinaryOp("!=",Id("a"),IntLiteral(0)),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_357(self):
        input =  """ void main()
                    {
                        m = a>b +(a / b);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("m"),BinaryOp(">",Id("a"),BinaryOp("+",Id("b"),BinaryOp("/",Id("a"),Id("b")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_358(self):
        input =  """ void main()
                    {
                        if (n > 0)
                        for (i = 0; i < n; i+a)
                        if (a[i] > 0)
                        {
                            printf("!!!!!");
                            return i;
                        }
                        else
                            printf("!!!!!");
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp(">",Id("n"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),Id("a")),If(BinaryOp(">",ArrayCell(Id("a"),Id("i")),IntLiteral(0)),Block([CallExpr(Id("printf"),[StringLiteral("!!!!!")]),Return(Id("i"))]),CallExpr(Id("printf"),[StringLiteral("!!!!!")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_359(self):
        input =  """ void main()
                    {
                        for (i = 0; i < n; i+a){
                            if ((i-a)==0)
                            {
                                i=i+a;
                            }
                            else
                                break;
                        }
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),Id("a")),Block([If(BinaryOp("==",BinaryOp("-",Id("i"),Id("a")),IntLiteral(0)),Block([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),Id("a")))]),Break())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_360(self):
        input =  """ int fun(int a)
                    {
                        int b; 
                        b=a;
                        if (a<0)
                            b = -a;
                        return b;
                    }
                """
        expect = str(Program([FuncDecl(Id("fun"),[VarDecl("a",IntType())],IntType(),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),Id("a")),If(BinaryOp("<",Id("a"),IntLiteral(0)),BinaryOp("=",Id("b"),UnaryOp("-",Id("a")))),Return(Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_361(self):
        input =  """ int fun(int a)
                    {
                        float a[1000];
                        float b[3000];
                        c[1]=a[1]+a[2]+a[3]*b[3] +a[b[foo(a[1])]]*b[foo(a[b[12]])*foo(b[0])];
                    }
                """
        expect = str(Program([FuncDecl(Id("fun"),[VarDecl("a",IntType())],IntType(),Block([VarDecl("a",ArrayType(1000,FloatType())),VarDecl("b",ArrayType(3000,FloatType())),BinaryOp("=",ArrayCell(Id("c"),IntLiteral(1)),BinaryOp("+",BinaryOp("+",BinaryOp("+",ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("a"),IntLiteral(2))),BinaryOp("*",ArrayCell(Id("a"),IntLiteral(3)),ArrayCell(Id("b"),IntLiteral(3)))),BinaryOp("*",ArrayCell(Id("a"),ArrayCell(Id("b"),CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(1))]))),ArrayCell(Id("b"),BinaryOp("*",CallExpr(Id("foo"),[ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(12)))]),CallExpr(Id("foo"),[ArrayCell(Id("b"),IntLiteral(0))]))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_362(self):
        input =   """ int main(int a[], int N)
                    {
                        for(i=0;i<N-1;i+1)
                            for(j=i+1;j<N;j+1)
                                if(a[i]>a[j])
                                    displayment(a[i],a[j]);                       
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("N",IntType())],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("N"),IntLiteral(1))),BinaryOp("+",Id("i"),IntLiteral(1)),For(BinaryOp("=",Id("j"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("<",Id("j"),Id("N")),BinaryOp("+",Id("j"),IntLiteral(1)),If(BinaryOp(">",ArrayCell(Id("a"),Id("i")),ArrayCell(Id("a"),Id("j"))),CallExpr(Id("displayment"),[ArrayCell(Id("a"),Id("i")),ArrayCell(Id("a"),Id("j"))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_363(self):
        input =  """ int find_Num(int a[], int N, int x)
                    {
                        for(i=0;i<N-1;i+1)
                            if(a[i]==x)
                                return i;
                        return -1;
                    }
                """
        expect = str(Program([FuncDecl(Id("find_Num"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("N",IntType()),VarDecl("x",IntType())],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("N"),IntLiteral(1))),BinaryOp("+",Id("i"),IntLiteral(1)),If(BinaryOp("==",ArrayCell(Id("a"),Id("i")),Id("x")),Return(Id("i")))),Return(UnaryOp("-",IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_364(self):
        input =  """ int main()
                    {
                        int a,b,c,d,r,f;
                        a=foo1();
                        b=foo2();
                        c=foo3();
                        d=foo4();
                        e=foo5();
                        f=foo6();
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("r",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo1"),[])),BinaryOp("=",Id("b"),CallExpr(Id("foo2"),[])),BinaryOp("=",Id("c"),CallExpr(Id("foo3"),[])),BinaryOp("=",Id("d"),CallExpr(Id("foo4"),[])),BinaryOp("=",Id("e"),CallExpr(Id("foo5"),[])),BinaryOp("=",Id("f"),CallExpr(Id("foo6"),[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    
    def test_365(self):
        input =  """int main()
                    {
                        int a,b,c,d,r,f;
                        b=1;c=2;d=3;e=4;f=5;
                        a=foo1(a*foo2(foo3(b+c+d*foo4(foo5(a,b,c,d,e,f,foo6(a+b*c))))));
                        
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("r",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("b"),IntLiteral(1)),BinaryOp("=",Id("c"),IntLiteral(2)),BinaryOp("=",Id("d"),IntLiteral(3)),BinaryOp("=",Id("e"),IntLiteral(4)),BinaryOp("=",Id("f"),IntLiteral(5)),BinaryOp("=",Id("a"),CallExpr(Id("foo1"),[BinaryOp("*",Id("a"),CallExpr(Id("foo2"),[CallExpr(Id("foo3"),[BinaryOp("+",BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",Id("d"),CallExpr(Id("foo4"),[CallExpr(Id("foo5"),[Id("a"),Id("b"),Id("c"),Id("d"),Id("e"),Id("f"),CallExpr(Id("foo6"),[BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c")))])])])))])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_366(self):
        input =  """ int main()
                    {
                        int m,n;
                        do{
                            for(i=0;i<n;i+1)
                                if(i>m)
                                    break;
                            m=m-1;
                        }
                        while(m>0);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("m",IntType()),VarDecl("n",IntType()),Dowhile([Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("+",Id("i"),IntLiteral(1)),If(BinaryOp(">",Id("i"),Id("m")),Break())),BinaryOp("=",Id("m"),BinaryOp("-",Id("m"),IntLiteral(1)))])],BinaryOp(">",Id("m"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_367(self):
        input =  """ int addNumbers(int a, int b)          
                    {
                        int result;
                        result = a+b;
                        return result;                 
                    }
                """
        expect = str(Program([FuncDecl(Id("addNumbers"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([VarDecl("result",IntType()),BinaryOp("=",Id("result"),BinaryOp("+",Id("a"),Id("b"))),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_368(self):
        input =  """ int main()
                    {
                        int n, i, flag ;
                        flag=0;
                        n = getInteger();    
                        for(i=2; i<=n/2; i+1)
                        {
                            if(n%i==0){
                                flag = 1;
                                break;
                            }
                        }
                    } 
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("i",IntType()),VarDecl("flag",IntType()),BinaryOp("=",Id("flag"),IntLiteral(0)),BinaryOp("=",Id("n"),CallExpr(Id("getInteger"),[])),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    
    def test_369(self):
        input =  """ int getInteger()       
                    {
                        int n;
                        printf("Enter a positive integer: ");
                        scanf("%d",n);
                        return n;
                    }
                """
        expect = str(Program([FuncDecl(Id("getInteger"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("printf"),[StringLiteral("Enter a positive integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),Return(Id("n"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_370(self):
        input =  """ int sum(int n) {
                        if (n != 0)
                            return n + sum(n-1); 
                        else
                            return n;
                    }
                """
        expect = str(Program([FuncDecl(Id("sum"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("!=",Id("n"),IntLiteral(0)),Return(BinaryOp("+",Id("n"),CallExpr(Id("sum"),[BinaryOp("-",Id("n"),IntLiteral(1))]))),Return(Id("n")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_371(self):
        input =  """ int hcf(int n1, int n2)
                    {
                        if (n2 != 0)
                           return hcf(n2, n1%n2);
                        else 
                           return n1;
                    }
                """
        expect = str(Program([FuncDecl(Id("hcf"),[VarDecl("n1",IntType()),VarDecl("n2",IntType())],IntType(),Block([If(BinaryOp("!=",Id("n2"),IntLiteral(0)),Return(CallExpr(Id("hcf"),[Id("n2"),BinaryOp("%",Id("n1"),Id("n2"))])),Return(Id("n1")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_372(self):
        input =  """ int multiplyNumbers(int n)
                    {
                        if (n >= 1)
                            return n*multiplyNumbers(n-1);
                        else
                            return 1;
                    }
                """
        expect = str(Program([FuncDecl(Id("multiplyNumbers"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp(">=",Id("n"),IntLiteral(1)),Return(BinaryOp("*",Id("n"),CallExpr(Id("multiplyNumbers"),[BinaryOp("-",Id("n"),IntLiteral(1))]))),Return(IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_373(self):
        input =  """ int main()
                    {
                        int n;
                        int count; 
                        count= 0;
                        printf("Enter an integer: ");
                        scanf("%lld", n);
                        do
                        {
                            n =n/ 10;
                            count=count+1;
                        }while(n != 0);
                        printf("Number of digits: %d", count);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("count",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Enter an integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%lld"),Id("n")]),Dowhile([Block([BinaryOp("=",Id("n"),BinaryOp("/",Id("n"),IntLiteral(10))),BinaryOp("=",Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])],BinaryOp("!=",Id("n"),IntLiteral(0))),CallExpr(Id("printf"),[StringLiteral("Number of digits: %d"),Id("count")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_374(self):
        input =  """ int main()
                    {
                        int number;
                        if(number % 2 == 0)
                            printf("%d is even.", number);
                        else
                            printf("%d is odd.", number);
                        return 0;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("number",IntType()),If(BinaryOp("==",BinaryOp("%",Id("number"),IntLiteral(2)),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is even."),Id("number")]),CallExpr(Id("printf"),[StringLiteral("%d is odd."),Id("number")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    
    def test_375(self):
        input =  """ int a,b,c,d,e,f;
                """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",IntType()),VarDecl("f",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_376(self):
        input =  """ float a,b,c,d,e,f;
                """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("e",FloatType()),VarDecl("f",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_377(self):
        input =  """ string a,b,c,d,e,f;
                """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",StringType()),VarDecl("e",StringType()),VarDecl("f",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_378(self):
        input =  """ boolean a,b,c,d,e,f;
                """
        expect = str(Program([VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),VarDecl("d",BoolType()),VarDecl("e",BoolType()),VarDecl("f",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_379(self):
        input =  """ 
                    int main(){}
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_380(self):
        input =  """ 
                    int main(){}
                    int foo(){}
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_381(self):
        input =  """ 
                int runner()
                {
                    int count; 
                    count= 0;
                    count=count+1;
                    return count;
                }
                
                int main()
                {
                    printf("%d ", runner());
                    printf("%d ", runner());
                    return 0;
                }
                """
        expect = str(Program([FuncDecl(Id("runner"),[],IntType(),Block([VarDecl("count",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),BinaryOp("=",Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))),Return(Id("count"))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("%d " ),CallExpr(Id("runner"),[])]),CallExpr(Id("printf"),[StringLiteral("%d " ),CallExpr(Id("runner"),[])]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_382(self):
        input = """ 
                int a,b,c;
                float d,e,f;
                int main(){
                    return a+b+c+d+e+f;   
                }
                """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("e",FloatType()),VarDecl("f",FloatType()),FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("d")),Id("e")),Id("f")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_383(self):
        input = """ 
                int main() 
                { 
                    boolean ptr; 
                    ptr= "GeeksQuiz"; 
                    int x; 
                    x= 10; 
                    INCREMENT(ptr); 
                    INCREMENT(x); 
                    return 0; 
                } 
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("ptr",BoolType()),BinaryOp("=",Id("ptr"),StringLiteral("GeeksQuiz")),VarDecl("x",IntType()),BinaryOp("=",Id("x"),IntLiteral(10)),CallExpr(Id("INCREMENT"),[Id("ptr")]),CallExpr(Id("INCREMENT"),[Id("x")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_384(self):
        input =  """ 
                int foo1(){
                    int a;
                }
                int foo2(int b){
                    foo1();
                }
                int foo2(){
                    int c;
                    c=foo1()+foo2(c);
                }
                """
        expect = str(Program([FuncDecl(Id("foo1"),[],IntType(),Block([VarDecl("a",IntType())])),FuncDecl(Id("foo2"),[VarDecl("b",IntType())],IntType(),Block([CallExpr(Id("foo1"),[])])),FuncDecl(Id("foo2"),[],IntType(),Block([VarDecl("c",IntType()),BinaryOp("=",Id("c"),BinaryOp("+",CallExpr(Id("foo1"),[]),CallExpr(Id("foo2"),[Id("c")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_385(self):
        input =  """ 
                int a;
                float b;
                boolean c;       
                void main()
                {
                    a=1;b=2;c=true;
                    if(c==true)
                        return a;
                    return b;
                }
                """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),IntLiteral(2)),BinaryOp("=",Id("c"),BooleanLiteral("true")),If(BinaryOp("==",Id("c"),BooleanLiteral("true")),Return(Id("a"))),Return(Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_386(self):
        input =""" 
                 string a;
                 int main(){
                    a="aaaaaaaaa ";
                 }
                """
        expect = str(Program([VarDecl("a",StringType()),FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),StringLiteral("aaaaaaaaa "))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_387(self):
        input =  """ 
                    int main(){
                        float a[5];
                        for(i = 0; i < 3; i+1){
                            if(i==0)
                                a[0]=i;
                            else
                                if(i==1)
                                    a[1]=i;
                                else
                                    if(i==2)
                                        a[2]=i;
                        }    
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(5,FloatType())),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(3)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([If(BinaryOp("==",Id("i"),IntLiteral(0)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),Id("i")),If(BinaryOp("==",Id("i"),IntLiteral(1)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),Id("i")),If(BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(2)),Id("i")))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_388(self):
        input = """ 
                int main(){
                    prev = rank - 1;
                    next = rank + 1;
                    if (rank == 0) prev = num - 1;
                    if (rank == (num - 1)) next = 0;
                }    
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("prev"),BinaryOp("-",Id("rank"),IntLiteral(1))),BinaryOp("=",Id("next"),BinaryOp("+",Id("rank"),IntLiteral(1))),If(BinaryOp("==",Id("rank"),IntLiteral(0)),BinaryOp("=",Id("prev"),BinaryOp("-",Id("num"),IntLiteral(1)))),If(BinaryOp("==",Id("rank"),BinaryOp("-",Id("num"),IntLiteral(1))),BinaryOp("=",Id("next"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_389(self):
        input =  """ 
                    int main(){}
                    int foo(){}
                    float main(){}
                    float foo(){}
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[],IntType(),Block([])),FuncDecl(Id("main"),[],FloatType(),Block([])),FuncDecl(Id("foo"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_390(self):
        input = """ 
                boolean foo1(){}
                int foo2(){}
                string foo3(){}
                float foo4(){}
                """
        expect = str(Program([FuncDecl(Id("foo1"),[],BoolType(),Block([])),FuncDecl(Id("foo2"),[],IntType(),Block([])),FuncDecl(Id("foo3"),[],StringType(),Block([])),FuncDecl(Id("foo4"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_391(self):
        input = """ 
                    int main()
                    {
                        free(a);
                        free(b);
                        free(c);
                        free(d);
                        free(e);
                        free(f);
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("free"),[Id("a")]),CallExpr(Id("free"),[Id("b")]),CallExpr(Id("free"),[Id("c")]),CallExpr(Id("free"),[Id("d")]),CallExpr(Id("free"),[Id("e")]),CallExpr(Id("free"),[Id("f")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_392(self):
        input = """
                    boolean fun()
                    {
                        if(_){}
                        else if(_){}

                    }
                """
        expect = str(Program([FuncDecl(Id("fun"),[],BoolType(),Block([If(Id("_"),Block([]),If(Id("_"),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_393(self):
        input = """
                    boolean fun()
                    {
                        if(c+a>d){}
                        else if(t>f){}

                    }
                """
        expect = str(Program([FuncDecl(Id("fun"),[],BoolType(),Block([If(BinaryOp(">",BinaryOp("+",Id("c"),Id("a")),Id("d")),Block([]),If(BinaryOp(">",Id("t"),Id("f")),Block([])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_394(self):
        input = """
                    int a[11];
                    
                """
        expect = str(Program([VarDecl("a",ArrayType(11,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_395(self):
        input = """ 
                void foo ( int i ) {}
                        int child_of_foo ( float f ) {} 
                        
                    
                """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("i",IntType())],VoidType(),Block([])),FuncDecl(Id("child_of_foo"),[VarDecl("f",FloatType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_396(self):
        input = """ 
                int main()
                    {
                        d = b*b-4*a*c;
                    }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",BinaryOp("*",IntLiteral(4),Id("a")),Id("c"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    
    def test_397(self):
        input = """ 
                int[] foo1(){}
                float[] foo2(){}
                """
        expect = str(Program([FuncDecl(Id("foo1"),[],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("foo2"),[],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_398(self):
        input = """ 
                int[] foo1(int a[], float b){}
                float[] foo2(string c){}
                """
        expect = str(Program([FuncDecl(Id("foo1"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",FloatType())],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("foo2"),[VarDecl("c",StringType())],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_399(self):
        input = """ 
                int end(){
                    return;
                    continue;
                }
                """
        expect = str(Program([FuncDecl(Id("end"),[],IntType(),Block([Return(),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

