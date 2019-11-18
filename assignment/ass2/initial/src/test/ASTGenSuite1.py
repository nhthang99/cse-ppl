import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program_00(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program_Funcdecl_with_para_01(self):
        """Simple program: int main() {} """
        input = """int main(int i){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(i,IntType)],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_simple_program_funcdecl_with_arraypointer_02(self):
        """Simple program"""
        input = """int main(string i[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(i,ArrayTypePointer(StringType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_simple_program_funcdecl_with_list_para_03(self):
        """Simple program"""
        input = """int main(float a, boolean b,string i[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,FloatType),VarDecl(b,BoolType),VarDecl(i,ArrayTypePointer(StringType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_simple_program_vardecl_04(self):
        """Simple program"""
        input = """
        int a;
            """
        expect = "Program([VarDecl(a,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_simple_program_vardecl_with_array_05(self):
        """Simple program"""
        input = """
        float a[7];
            """
        expect = "Program([VarDecl(a,ArrayType(FloatType,7))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_program_with_mix_vardecl_06(self):
        """Simple program"""
        input = """
        float a, b[7], c;
        int a,b,c;
        string a[2],b[3];
            """
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,ArrayType(FloatType,7)),VarDecl(c,FloatType),VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(a,ArrayType(StringType,2)),VarDecl(b,ArrayType(StringType,3))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_simple_program_fundecl_and_vardecl_07(self):
        """Simple program"""
        input = """
        float a(int i){}
        int a;
            """
        expect = "Program([FuncDecl(Id(a),[VarDecl(i,IntType)],FloatType,Block([])),VarDecl(a,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_simple_program_fundecl_and_vardecl_08(self):
        """Simple program"""
        input = """
        string[] a(int i){}
        int a, b[5];
            """
        expect = "Program([FuncDecl(Id(a),[VarDecl(i,IntType)],ArrayTypePointer(StringType),Block([])),VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_more_complex_program_09(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    
    def test_call_without_parameter_10(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_func_decl_and_operator_11(self):
        """More complex program"""
        input = """int a(int i,int b,string c[]){}
        float b(int c,string d){}
        int[] c(float a, boolean f[]){
            cvb=1;
        }
        """
        expect = "Program([FuncDecl(Id(a),[VarDecl(i,IntType),VarDecl(b,IntType),VarDecl(c,ArrayTypePointer(StringType))],IntType,Block([])),FuncDecl(Id(b),[VarDecl(c,IntType),VarDecl(d,StringType)],FloatType,Block([])),FuncDecl(Id(c),[VarDecl(a,FloatType),VarDecl(f,ArrayTypePointer(BoolType))],ArrayTypePointer(IntType),Block([BinaryOp(=,Id(cvb),IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    
    def test_mix_funcdecl_and_vardecl_12(self):
        """More complex program"""
        input = """int a1,d[10],f[6],e,g,h[2];
        int j;
        int c[3];
        float k[4];
        string l;"""
        expect = "Program([VarDecl(a1,IntType),VarDecl(d,ArrayType(IntType,10)),VarDecl(f,ArrayType(IntType,6)),VarDecl(e,IntType),VarDecl(g,IntType),VarDecl(h,ArrayType(IntType,2)),VarDecl(j,IntType),VarDecl(c,ArrayType(IntType,3)),VarDecl(k,ArrayType(FloatType,4)),VarDecl(l,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_single_array_declaration_float_13(self):
        input = """float a[5];"""
        expect = "Program([VarDecl(a,ArrayType(FloatType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_multi_array_declaration_14(self):
        input = """boolean _1[10],_2[5];"""
        expect = "Program([VarDecl(_1,ArrayType(BoolType,10)),VarDecl(_2,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_program_multi_vardecl_15(self):
        input = """int x; float y; boolean z;"""
        expect = "Program([VarDecl(x,IntType),VarDecl(y,FloatType),VarDecl(z,BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_function_multi_array_16(self):
        input = """void main(boolean a[], float ___[]) {}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(BoolType)),VarDecl(___,ArrayTypePointer(FloatType))],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_program_multi_vardecls_17(self):
        input = """int _,__; float b,z; string a[10], l[6], r; boolean d[5];"""
        expect = "Program([VarDecl(_,IntType),VarDecl(__,IntType),VarDecl(b,FloatType),VarDecl(z,FloatType),VarDecl(a,ArrayType(StringType,10)),VarDecl(l,ArrayType(StringType,6)),VarDecl(r,StringType),VarDecl(d,ArrayType(BoolType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_multi_arraypointertype_func_decl_18(self):
        input = """int[] x(){}
        float[] y(){}
        string[] z(){}
        boolean[] w(int a[],float b[], string c){}"""
        expect = "Program([FuncDecl(Id(x),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(y),[],ArrayTypePointer(FloatType),Block([])),FuncDecl(Id(z),[],ArrayTypePointer(StringType),Block([])),FuncDecl(Id(w),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(c,StringType)],ArrayTypePointer(BoolType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_multi_func_decl_with_block_19(self):
        input = """int[] main() {int a;int b;} boolean[] power() {a=10;}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([VarDecl(a,IntType),VarDecl(b,IntType)])),FuncDecl(Id(power),[],ArrayTypePointer(BoolType),Block([BinaryOp(=,Id(a),IntLiteral(10))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_more_complex_funcdecl_with_assign_20(self):
        input = """int PRINT(int a){
            Date=a;
            b=4567;
            return 1;
        }"""
        expect = "Program([FuncDecl(Id(PRINT),[VarDecl(a,IntType)],IntType,Block([BinaryOp(=,Id(Date),Id(a)),BinaryOp(=,Id(b),IntLiteral(4567)),Return(IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_more_complex_funcdecl_with_return_21(self):
        input = """int PRINTER(int Date){
            Date=1234;
            b=4567;
            return Date;
        }"""
        expect = "Program([FuncDecl(Id(PRINTER),[VarDecl(Date,IntType)],IntType,Block([BinaryOp(=,Id(Date),IntLiteral(1234)),BinaryOp(=,Id(b),IntLiteral(4567)),Return(Id(Date))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_more_complex_funcdecl_with_compare_operator_22(self):
        input = """int PRINTER(int Date){
            Date=1234;
            Date>=1234;
            Date==5;
            return Date;
        }"""
        expect = "Program([FuncDecl(Id(PRINTER),[VarDecl(Date,IntType)],IntType,Block([BinaryOp(=,Id(Date),IntLiteral(1234)),BinaryOp(>=,Id(Date),IntLiteral(1234)),BinaryOp(==,Id(Date),IntLiteral(5)),Return(Id(Date))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_more_funcdecl_with_if_statement_23(self):
        input = """int PRINTER(int Date){
        if(True){
            a;b;c;
        }
        }"""
        expect = "Program([FuncDecl(Id(PRINTER),[VarDecl(Date,IntType)],IntType,Block([If(Id(True),Block([Id(a),Id(b),Id(c)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_more_funcdecl_with_if_else_statement_24(self):
        input = """float IFFER(int Date){
        if(false){
            a;b;c;
        }
        else
            a=567;
        b=567;
        c=4567;
        }"""
        expect = "Program([FuncDecl(Id(IFFER),[VarDecl(Date,IntType)],FloatType,Block([If(BooleanLiteral(false),Block([Id(a),Id(b),Id(c)]),BinaryOp(=,Id(a),IntLiteral(567))),BinaryOp(=,Id(b),IntLiteral(567)),BinaryOp(=,Id(c),IntLiteral(4567))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_more_complex_funcdecl_with_if_else_statement_25(self):
        input = """boolean main() {
            if(a && b || c) 
            printer(hello); 
            else {
                put(5);
                push(ghj);
                int c;
                c=10;}
        }"""
        expect = "Program([FuncDecl(Id(main),[],BoolType,Block([If(BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)),CallExpr(Id(printer),[Id(hello)]),Block([CallExpr(Id(put),[IntLiteral(5)]),CallExpr(Id(push),[Id(ghj)]),VarDecl(c,IntType),BinaryOp(=,Id(c),IntLiteral(10))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_more_complex_funcdecl_with_if_else_statement_and_return_26(self):
        input = """int main(){
            int m,n;
            int i; //counter

            printf("Enter m: ");
            Nhap(m);
            printf("Enter n: ");
            Nhap(n);

            if (n<m){
                printf("Numbers from n to m: ");
                for(i=n;i<=m;i=i+1){
                    printf(i);
                }
            }
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(m,IntType),VarDecl(n,IntType),VarDecl(i,IntType),CallExpr(Id(printf),[StringLiteral(Enter m: )]),CallExpr(Id(Nhap),[Id(m)]),CallExpr(Id(printf),[StringLiteral(Enter n: )]),CallExpr(Id(Nhap),[Id(n)]),If(BinaryOp(<,Id(n),Id(m)),Block([CallExpr(Id(printf),[StringLiteral(Numbers from n to m: )]),For(BinaryOp(=,Id(i),Id(n));BinaryOp(<=,Id(i),Id(m));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(printf),[Id(i)])]))])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_more_complex_funcdecl_if_else_statement_with_callexp_27(self):
        input = """int main( int argc , string str )
        {
            boolean c ;
            int i ;
            i=10;
            if(i>=argc && c==true){
                int d ;
                str = "Hello World";
                putInt(d ) ;
            }
            print(str);
            return i ;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(str,StringType)],IntType,Block([VarDecl(c,BoolType),VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(10)),If(BinaryOp(&&,BinaryOp(>=,Id(i),Id(argc)),BinaryOp(==,Id(c),BooleanLiteral(true))),Block([VarDecl(d,IntType),BinaryOp(=,Id(str),StringLiteral(Hello World)),CallExpr(Id(putInt),[Id(d)])])),CallExpr(Id(print),[Id(str)]),Return(Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_more_complex_funcdecl_if_else_statement_with_callexp_28(self):
        input = """
        boolean check(int a){
            if(true) return true;
            else return false;
        }
        int main( int argc , boolean argv )
        {
            
            if(argc==check(10) && argv!=check(10)){
                int d ;
                putInt(d ) ;
            }
            print(str);
            return i ;
        }"""
        expect = "Program([FuncDecl(Id(check),[VarDecl(a,IntType)],BoolType,Block([If(BooleanLiteral(true),Return(BooleanLiteral(true)),Return(BooleanLiteral(false)))])),FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,BoolType)],IntType,Block([If(BinaryOp(&&,BinaryOp(==,Id(argc),CallExpr(Id(check),[IntLiteral(10)])),BinaryOp(!=,Id(argv),CallExpr(Id(check),[IntLiteral(10)]))),Block([VarDecl(d,IntType),CallExpr(Id(putInt),[Id(d)])])),CallExpr(Id(print),[Id(str)]),Return(Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_more_complex_mix_many_if_else_statement_with_callexp_29(self):
        input = """
        void main( ){ if (a) if (b) if (c) for(i=0;i<9;i=i+1) foo(2,4); else a; else for(i=0;i<9;i=i+1) foo(2,4);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(Id(a),If(Id(b),If(Id(c),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(9));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(foo),[IntLiteral(2),IntLiteral(4)])),Id(a)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(9));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(foo),[IntLiteral(2),IntLiteral(4)]))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_simple_prog_wwith_do_while_30(self):
        input = """void ____1____() {do print(2,4); while(a==1);}"""
        expect = "Program([FuncDecl(Id(____1____),[],VoidType,Block([Dowhile([CallExpr(Id(print),[IntLiteral(2),IntLiteral(4)])],BinaryOp(==,Id(a),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_complex_prog_with_do_while_31(self):
        input = """void main() {
            do {
                if(True(False(Do(1,2,3)))) 
                    printer(a,b,c);
                } 
            while(func(a));
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([If(CallExpr(Id(True),[CallExpr(Id(False),[CallExpr(Id(Do),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]),CallExpr(Id(printer),[Id(a),Id(b),Id(c)]))])],CallExpr(Id(func),[Id(a)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_complex_prog_with_do_while_and_funcall_32(self):
        input = """string count(int money[]){
            int sum,i;
            sum=0;
            i=0;
            do
            sum=sum+money[i+1];
            while(i<=100);
        }
        int main( int argc[] , string str )
        {
            boolean c ;
            count(argc);
            print(str);
            return i ;
        }"""
        expect = "Program([FuncDecl(Id(count),[VarDecl(money,ArrayTypePointer(IntType))],StringType,Block([VarDecl(sum,IntType),VarDecl(i,IntType),BinaryOp(=,Id(sum),IntLiteral(0)),BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(money),BinaryOp(+,Id(i),IntLiteral(1)))))],BinaryOp(<=,Id(i),IntLiteral(100)))])),FuncDecl(Id(main),[VarDecl(argc,ArrayTypePointer(IntType)),VarDecl(str,StringType)],IntType,Block([VarDecl(c,BoolType),CallExpr(Id(count),[Id(argc)]),CallExpr(Id(print),[Id(str)]),Return(Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_more_complex_prog_with_mix_do_while_33(self):
        input = """void main( ){ do
        do 
        i=0;
        do fghj=67/hj;
        while(gh==true);
        while(x<=10);
        i=count/12;
        goo(3,arr[10]);
        while(x>=9); 
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Dowhile([BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([BinaryOp(=,Id(fghj),BinaryOp(/,IntLiteral(67),Id(hj)))],BinaryOp(==,Id(gh),BooleanLiteral(true)))],BinaryOp(<=,Id(x),IntLiteral(10))),BinaryOp(=,Id(i),BinaryOp(/,Id(count),IntLiteral(12))),CallExpr(Id(goo),[IntLiteral(3),ArrayCell(Id(arr),IntLiteral(10))])],BinaryOp(>=,Id(x),IntLiteral(9)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_very_complex_prog_with_many_do_while_34(self):
        input = """void main( ){ 
        do
            do i=0;
                do fghj=34+56-fhg%nbd;
                    do a;
                        do func(12);
                            do printer(a);
                                do say(hello);
                                while(gh==true);
                            while(x<=10);
                        while(x>=9);
                    while(abc==x/456 && gh9);
                while(x && y || z);
            while(x==9);
        while(abc!=88 && e==h);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Dowhile([BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([BinaryOp(=,Id(fghj),BinaryOp(-,BinaryOp(+,IntLiteral(34),IntLiteral(56)),BinaryOp(%,Id(fhg),Id(nbd)))),Dowhile([Id(a),Dowhile([CallExpr(Id(func),[IntLiteral(12)]),Dowhile([CallExpr(Id(printer),[Id(a)]),Dowhile([CallExpr(Id(say),[Id(hello)])],BinaryOp(==,Id(gh),BooleanLiteral(true)))],BinaryOp(<=,Id(x),IntLiteral(10)))],BinaryOp(>=,Id(x),IntLiteral(9)))],BinaryOp(&&,BinaryOp(==,Id(abc),BinaryOp(/,Id(x),IntLiteral(456))),Id(gh9)))],BinaryOp(||,BinaryOp(&&,Id(x),Id(y)),Id(z)))],BinaryOp(==,Id(x),IntLiteral(9)))],BinaryOp(&&,BinaryOp(!=,Id(abc),IntLiteral(88)),BinaryOp(==,Id(e),Id(h))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_simple_prog_with_for_35(self):
        input = """void main() {for(i=0;i<10;i=i+1) printer(1,2,3);}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(printer),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_simple_prog_with_for_36(self):
        input = """int main(int argc, int argv) {for(i=0;i<=567;i=i%1-10) {printer(1,2,3);put(a);push(b);} return 0;}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,IntType)],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(567));BinaryOp(=,Id(i),BinaryOp(-,BinaryOp(%,Id(i),IntLiteral(1)),IntLiteral(10)));Block([CallExpr(Id(printer),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),CallExpr(Id(put),[Id(a)]),CallExpr(Id(push),[Id(b)])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_complex_prog_with_for_37(self):
        input = """boolean test() {
            for(i = 1+a[6];i>=5;i=10/i) 
                {int a;}
            return true;}"""
        expect = "Program([FuncDecl(Id(test),[],BoolType,Block([For(BinaryOp(=,Id(i),BinaryOp(+,IntLiteral(1),ArrayCell(Id(a),IntLiteral(6))));BinaryOp(>=,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(/,IntLiteral(10),Id(i)));Block([VarDecl(a,IntType)])),Return(BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_more_complex_prog_with_for_38(self):
        input = """float main(){
            int i;
            int arr[4];
            i=0;
            for(i=1+2+3-4-6*4;i<=arr[2];i=arr[3]+arr[0]+1+i)
                {
                    printf(hello);
                    put(_);
                    push(___);
                }
            __pull__(____1____);
            return 6.45;
        }"""
        expect = "Program([FuncDecl(Id(main),[],FloatType,Block([VarDecl(i,IntType),VarDecl(arr,ArrayType(IntType,4)),BinaryOp(=,Id(i),IntLiteral(0)),For(BinaryOp(=,Id(i),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp(*,IntLiteral(6),IntLiteral(4))));BinaryOp(<=,Id(i),ArrayCell(Id(arr),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(3)),ArrayCell(Id(arr),IntLiteral(0))),IntLiteral(1)),Id(i)));Block([CallExpr(Id(printf),[Id(hello)]),CallExpr(Id(put),[Id(_)]),CallExpr(Id(push),[Id(___)])])),CallExpr(Id(__pull__),[Id(____1____)]),Return(FloatLiteral(6.45))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_very_complex_prog_with_many_for_39(self):
        input = """float main(){
            int i;
            int arr[4];
            i=0;
            for(i=1+2+3-4-6*4;i<=arr[2];i=arr[3]+arr[0]+1+i)
                for(i=1;i<=cvb;i=arr[3]+arr[0]+1+i)
                {   for(12;23;45)
                    {
                        printf(hello);
                        put(_);
                        push(___);
                        continue;
                    }
                break;
                } 
            __pull__(____1____);
            return 6.45;
        }"""
        expect = "Program([FuncDecl(Id(main),[],FloatType,Block([VarDecl(i,IntType),VarDecl(arr,ArrayType(IntType,4)),BinaryOp(=,Id(i),IntLiteral(0)),For(BinaryOp(=,Id(i),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp(*,IntLiteral(6),IntLiteral(4))));BinaryOp(<=,Id(i),ArrayCell(Id(arr),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(3)),ArrayCell(Id(arr),IntLiteral(0))),IntLiteral(1)),Id(i)));For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(cvb));BinaryOp(=,Id(i),BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(3)),ArrayCell(Id(arr),IntLiteral(0))),IntLiteral(1)),Id(i)));Block([For(IntLiteral(12);IntLiteral(23);IntLiteral(45);Block([CallExpr(Id(printf),[Id(hello)]),CallExpr(Id(put),[Id(_)]),CallExpr(Id(push),[Id(___)]),Continue()])),Break()]))),CallExpr(Id(__pull__),[Id(____1____)]),Return(FloatLiteral(6.45))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_complex_prog_with_continue_40(self):
        input = """float test_continue(){
            int i;
            int arr[4];
            i=0;
            for(i=1+2+3-4-6*4;i<=arr[2];i=arr[3]+arr[0]+1+i)
                {
                    if(true)
                        continue;
                    else
                        continue;
                }
            __pull__(____1____);
            return 345.345;
        }"""
        expect = "Program([FuncDecl(Id(test_continue),[],FloatType,Block([VarDecl(i,IntType),VarDecl(arr,ArrayType(IntType,4)),BinaryOp(=,Id(i),IntLiteral(0)),For(BinaryOp(=,Id(i),BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp(*,IntLiteral(6),IntLiteral(4))));BinaryOp(<=,Id(i),ArrayCell(Id(arr),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(3)),ArrayCell(Id(arr),IntLiteral(0))),IntLiteral(1)),Id(i)));Block([If(BooleanLiteral(true),Continue(),Continue())])),CallExpr(Id(__pull__),[Id(____1____)]),Return(FloatLiteral(345.345))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_complex_prog_with_break_41(self):
        input = """string test_break(){
            int arr[5];
            for(i=0;i<5;i=i+1)
                {
                    if(true)
                        arr[i]=i*i;
                    else
                        break;
                }
            __pull__(____1____);
            return "This is break test";
        }"""
        expect = "Program([FuncDecl(Id(test_break),[],StringType,Block([VarDecl(arr,ArrayType(IntType,5)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BooleanLiteral(true),BinaryOp(=,ArrayCell(Id(arr),Id(i)),BinaryOp(*,Id(i),Id(i))),Break())])),CallExpr(Id(__pull__),[Id(____1____)]),Return(StringLiteral(This is break test))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_mix_prog_with_break_and_continue_42(self):
        input = """string test_break(){
            int arr[5];
            for(i=0;i<5;i=i+1)
                {
                    if(true)
                        {
                            arr[i]=i*i;
                            continue;
                        }
                    else
                    {
                        if(false)
                            break;
                        else
                            return "hello world";
                    }
                        
                }
            __pull__(____1____);
            return "This is test";
        }"""
        expect = "Program([FuncDecl(Id(test_break),[],StringType,Block([VarDecl(arr,ArrayType(IntType,5)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BooleanLiteral(true),Block([BinaryOp(=,ArrayCell(Id(arr),Id(i)),BinaryOp(*,Id(i),Id(i))),Continue()]),Block([If(BooleanLiteral(false),Break(),Return(StringLiteral(hello world)))]))])),CallExpr(Id(__pull__),[Id(____1____)]),Return(StringLiteral(This is test))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_mix_prog_with_dowhile_and_break_43(self):
        input = """boolean test_dowhile_break(){
            int arr[5];
            do
                {
                    if(true)
                        {
                            arr[i]=i*i;
                            continue;
                        }
                    else
                    {
                        if(false)
                            break;
                        else
                            return false;
                    }
                        
                }
            while(__pull__(____1____)!=1);
            return true;
        }"""
        expect = "Program([FuncDecl(Id(test_dowhile_break),[],BoolType,Block([VarDecl(arr,ArrayType(IntType,5)),Dowhile([Block([If(BooleanLiteral(true),Block([BinaryOp(=,ArrayCell(Id(arr),Id(i)),BinaryOp(*,Id(i),Id(i))),Continue()]),Block([If(BooleanLiteral(false),Break(),Return(BooleanLiteral(false)))]))])],BinaryOp(!=,CallExpr(Id(__pull__),[Id(____1____)]),IntLiteral(1))),Return(BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_complex_prog_with_dowhile_continue_and_break_44(self):
        input = """boolean test_dowhile_break_continue(){
            int arr[5];
            do
                {
                    if(true)
                        {
                            do
                                arr[i]=i*i;
                            while(true);
                            continue;
                        }
                    else
                    {
                        if(false)
                            break;
                        else
                            do{
                                print("Hello");
                                if(i==false)
                                {
                                    i=true;
                                    continue;
                                }
                            }
                            while(i==true);
                            break;
                    }
                        
                }
            while(__pull__(____1____)!=1);
            return true;
        }"""
        expect = "Program([FuncDecl(Id(test_dowhile_break_continue),[],BoolType,Block([VarDecl(arr,ArrayType(IntType,5)),Dowhile([Block([If(BooleanLiteral(true),Block([Dowhile([BinaryOp(=,ArrayCell(Id(arr),Id(i)),BinaryOp(*,Id(i),Id(i)))],BooleanLiteral(true)),Continue()]),Block([If(BooleanLiteral(false),Break(),Dowhile([Block([CallExpr(Id(print),[StringLiteral(Hello)]),If(BinaryOp(==,Id(i),BooleanLiteral(false)),Block([BinaryOp(=,Id(i),BooleanLiteral(true)),Continue()]))])],BinaryOp(==,Id(i),BooleanLiteral(true)))),Break()]))])],BinaryOp(!=,CallExpr(Id(__pull__),[Id(____1____)]),IntLiteral(1))),Return(BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_ASSIGN_operator_45(self):
        input = """boolean test_ASSIGN_operator(){
            int arr[3];
            arr[0]=1; arr[1]=2; arr[2]=3;
            print(arr[0], arr[1],arr[2]);
            return true;
        }"""
        expect = "Program([FuncDecl(Id(test_ASSIGN_operator),[],BoolType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(3)),CallExpr(Id(print),[ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(2))]),Return(BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_more_complex_ASSIGN_operator_46(self):
        input = """int num(int a){ return a;}
        int test_ASSIGN_operator(){
            int arr[3];
            arr[0]=num(10); arr[1]=num(11)+num(12); arr[2]=3+num(13);
            print(arr[0]+1, arr[1]+2,arr[2]+3);
            return arr[0]+1+arr[1]+2+arr[2]+3;
        }"""
        expect = "Program([FuncDecl(Id(num),[VarDecl(a,IntType)],IntType,Block([Return(Id(a))])),FuncDecl(Id(test_ASSIGN_operator),[],IntType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),CallExpr(Id(num),[IntLiteral(10)])),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BinaryOp(+,CallExpr(Id(num),[IntLiteral(11)]),CallExpr(Id(num),[IntLiteral(12)]))),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BinaryOp(+,IntLiteral(3),CallExpr(Id(num),[IntLiteral(13)]))),CallExpr(Id(print),[BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(1)),BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(2)),BinaryOp(+,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(3))]),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(1))),IntLiteral(2)),ArrayCell(Id(arr),IntLiteral(2))),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_OR_operator_47(self):
        input = """boolean test_OR_operator(){
            int arr[3];
            arr[0]=1; arr[1]=2; arr[2]=3;
            if(arr[0]+10|| arr[1] || arr[2] || true)
                return true;
            else
                return false;
        }"""
        expect = "Program([FuncDecl(Id(test_OR_operator),[],BoolType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(3)),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(10)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),IntLiteral(2))),BooleanLiteral(true)),Return(BooleanLiteral(true)),Return(BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_more_complex_OR_operator_48(self):
        input = """boolean test_OR_operator(){
            int arr[3];
            arr[0]=1; arr[1]=2; arr[2]=3;
            if(arr[0]+arr[1]|| arr[1]==true || arr[2] || true)
                do{
                    printer("Hello");
                    put(t);
                }
                while(arr[0] || arr[1] || arr[2]);
            else
                return false;
        }"""
        expect = "Program([FuncDecl(Id(test_OR_operator),[],BoolType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(3)),If(BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(==,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true))),ArrayCell(Id(arr),IntLiteral(2))),BooleanLiteral(true)),Dowhile([Block([CallExpr(Id(printer),[StringLiteral(Hello)]),CallExpr(Id(put),[Id(t)])])],BinaryOp(||,BinaryOp(||,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),IntLiteral(2)))),Return(BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_AND_operator_49(self):
        input = """boolean test_AND_operator(){
            float arr[3];
            arr[0]=1.1; arr[1]=2.2; arr[2]=3.3;
            if(arr[0]+10 && arr[1] && arr[2] && true)
                return true;
            else
                return false;
        }"""
        expect = "Program([FuncDecl(Id(test_AND_operator),[],BoolType,Block([VarDecl(arr,ArrayType(FloatType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),FloatLiteral(1.1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),FloatLiteral(2.2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),FloatLiteral(3.3)),If(BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(10)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),IntLiteral(2))),BooleanLiteral(true)),Return(BooleanLiteral(true)),Return(BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_more_complex_AND_operator_50(self):
        input = """float test_AND_operator(){
            float arr[3];
            arr[0]=1.1; arr[1]=2.2; arr[2]=3.3;
            if(arr[0]+10 && arr[1] && arr[2] && true)
                do{
                    printer("Hello");
                    put(t);
                    if(arr[0]==arr[1] && arr[0]==arr[2])
                        return 123.4;
                }
                while(arr[0] || arr[1] || arr[2]);
            else
                return 12.e32;
        }"""
        expect = "Program([FuncDecl(Id(test_AND_operator),[],FloatType,Block([VarDecl(arr,ArrayType(FloatType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),FloatLiteral(1.1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),FloatLiteral(2.2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),FloatLiteral(3.3)),If(BinaryOp(&&,BinaryOp(&&,BinaryOp(&&,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(10)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),IntLiteral(2))),BooleanLiteral(true)),Dowhile([Block([CallExpr(Id(printer),[StringLiteral(Hello)]),CallExpr(Id(put),[Id(t)]),If(BinaryOp(&&,BinaryOp(==,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(==,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(2)))),Return(FloatLiteral(123.4)))])],BinaryOp(||,BinaryOp(||,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),IntLiteral(2)))),Return(FloatLiteral(1.2e+33)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_EQUAL_operator_51(self):
        input = """string test_EQUAL_operator(){
            boolean arr[3];
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(arr[0]==arr[1] && arr[2]== true || arr[1]==false)
                return "True";
            else
                return "False";
        }"""
        expect = "Program([FuncDecl(Id(test_EQUAL_operator),[],StringType,Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(==,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(true))),BinaryOp(==,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(false))),Return(StringLiteral(True)),Return(StringLiteral(False)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_more_complex_EQUAL_operator_52(self):
        input = """string test_complex_EQUAL_operator(){
            int arr[3];
            arr[0]=2; arr[1]=4; arr[2]=5;
            if(arr[0]==arr[1] && arr[2]== 2 || arr[1]==1)
                do{
                    push(True);
                    continue;
                }
                while(i==arr[1]+arr[2]+arr[0]);
            else
                return "False";
        }"""
        expect = "Program([FuncDecl(Id(test_complex_EQUAL_operator),[],StringType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(4)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(5)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(==,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(2))),BinaryOp(==,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(1))),Dowhile([Block([CallExpr(Id(push),[Id(True)]),Continue()])],BinaryOp(==,Id(i),BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(2))),ArrayCell(Id(arr),IntLiteral(0))))),Return(StringLiteral(False)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_NOTEQUAL_operator_53(self):
        input = """string test_NOTEQUAL_operator(){
            boolean arr[3];
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(arr[0]!=arr[1] && arr[2]!= true || arr[1]!=false && true!=false)
                return "True";
            else
                return "False";
        }"""
        expect = "Program([FuncDecl(Id(test_NOTEQUAL_operator),[],StringType,Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(!=,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(!=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(true))),BinaryOp(&&,BinaryOp(!=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(false)),BinaryOp(!=,BooleanLiteral(true),BooleanLiteral(false)))),Return(StringLiteral(True)),Return(StringLiteral(False)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_complex_NOTEQUAL_operator_54(self):
        input = """string test_NOTEQUAL_operator(){
            boolean arr[3];
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(arr[0]!=arr[1] && arr[2]!= true || arr[1]!=false && true!=false)
                do{
                    foo(abc);
                    g00_abc(____a);
                    
                    if(true!=false)
                        break;
                    else
                        continue;
                }
                while(i!=arr[1]+arr[2]+arr[0]);
            else
                return "Test NOTEQUAL";
        }"""
        expect = "Program([FuncDecl(Id(test_NOTEQUAL_operator),[],StringType,Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(!=,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(!=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(true))),BinaryOp(&&,BinaryOp(!=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(false)),BinaryOp(!=,BooleanLiteral(true),BooleanLiteral(false)))),Dowhile([Block([CallExpr(Id(foo),[Id(abc)]),CallExpr(Id(g00_abc),[Id(____a)]),If(BinaryOp(!=,BooleanLiteral(true),BooleanLiteral(false)),Break(),Continue())])],BinaryOp(!=,Id(i),BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(2))),ArrayCell(Id(arr),IntLiteral(0))))),Return(StringLiteral(Test NOTEQUAL)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_LESS_operator_55(self):
        input = """string[] test_LESS_operator(){
            boolean arr[3];
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(arr[0]<arr[1] && arr[2]< true || arr[1]<false && true<false)
                return "True";
            else
                return "False";
        }"""
        expect = "Program([FuncDecl(Id(test_LESS_operator),[],ArrayTypePointer(StringType),Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(<,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(<,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(true))),BinaryOp(&&,BinaryOp(<,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(false)),BinaryOp(<,BooleanLiteral(true),BooleanLiteral(false)))),Return(StringLiteral(True)),Return(StringLiteral(False)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_complex_LESS_operator_56(self):
        input = """string[] test_complex_LESS_operator(){
            boolean arr[3];
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(arr[0]<arr[1] && arr[2]< TTrue || arr[1]<FFalse && ____<_567)
                do{
                    foo(abc);
                    g00_abc(____a);
                    
                    if(True<False)
                        break;
                    else
                        continue;
                }
                while(i<arr[1]+arr[2]+arr[0]);
            else
                return "Test LESS";
        }"""
        expect = "Program([FuncDecl(Id(test_complex_LESS_operator),[],ArrayTypePointer(StringType),Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(<,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(<,ArrayCell(Id(arr),IntLiteral(2)),Id(TTrue))),BinaryOp(&&,BinaryOp(<,ArrayCell(Id(arr),IntLiteral(1)),Id(FFalse)),BinaryOp(<,Id(____),Id(_567)))),Dowhile([Block([CallExpr(Id(foo),[Id(abc)]),CallExpr(Id(g00_abc),[Id(____a)]),If(BinaryOp(<,Id(True),Id(False)),Break(),Continue())])],BinaryOp(<,Id(i),BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(2))),ArrayCell(Id(arr),IntLiteral(0))))),Return(StringLiteral(Test LESS)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_GREATER_operator_57(self):
        input = """int test_GREATER_operator(){
            if(4>6 || 8>3+3)
                return 1;
            else
                return 0;
        }"""
        expect = "Program([FuncDecl(Id(test_GREATER_operator),[],IntType,Block([If(BinaryOp(||,BinaryOp(>,IntLiteral(4),IntLiteral(6)),BinaryOp(>,IntLiteral(8),BinaryOp(+,IntLiteral(3),IntLiteral(3)))),Return(IntLiteral(1)),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_complex_GREATER_operator_58(self):
        input = """float test_complex_GREATER_operator(){
            float arr[3];
            arr[0]=0.1; arr[1]=0.2; arr[2]=0.3;
            if(arr[0]>arr[1] && arr[2]> true || arr[1]>false && true>false)
                return arr[0];
            else
                return arr[1];
        }"""
        expect = "Program([FuncDecl(Id(test_complex_GREATER_operator),[],FloatType,Block([VarDecl(arr,ArrayType(FloatType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),FloatLiteral(0.1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),FloatLiteral(0.2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),FloatLiteral(0.3)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(>,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(>,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(true))),BinaryOp(&&,BinaryOp(>,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(false)),BinaryOp(>,BooleanLiteral(true),BooleanLiteral(false)))),Return(ArrayCell(Id(arr),IntLiteral(0))),Return(ArrayCell(Id(arr),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_LESS_EQUAL_operator_59(self):
        input = """int test_LESS_EQUAL_operator(){
            if(abc<=xyz || 8<=3+3 && asdf<=567.678)
                return 1;
            else
                return 0;
        }"""
        expect = "Program([FuncDecl(Id(test_LESS_EQUAL_operator),[],IntType,Block([If(BinaryOp(||,BinaryOp(<=,Id(abc),Id(xyz)),BinaryOp(&&,BinaryOp(<=,IntLiteral(8),BinaryOp(+,IntLiteral(3),IntLiteral(3))),BinaryOp(<=,Id(asdf),FloatLiteral(567.678)))),Return(IntLiteral(1)),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_complex_LESS_EQUAL_operator_60(self):
        input = """string[] test_complex_LESS_EQUAL_operator(){
            boolean arr[3];
            arr[0]=true; arr[1]=true; arr[2]=false;
            if(arr[0]<=arr[1] && arr[2]<= true || arr[1]<=false && true<=false)
                do{
                    foo(abc);
                    g00_abc(____a);
                    
                    if(True<=False)
                        break;
                    else
                        continue;
                }
                while(i<=arr[1]+arr[2]+arr[0]);
            else
                return "Test LESS EQUAL";
        }"""
        expect = "Program([FuncDecl(Id(test_complex_LESS_EQUAL_operator),[],ArrayTypePointer(StringType),Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(<=,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(<=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(true))),BinaryOp(&&,BinaryOp(<=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(false)),BinaryOp(<=,BooleanLiteral(true),BooleanLiteral(false)))),Dowhile([Block([CallExpr(Id(foo),[Id(abc)]),CallExpr(Id(g00_abc),[Id(____a)]),If(BinaryOp(<=,Id(True),Id(False)),Break(),Continue())])],BinaryOp(<=,Id(i),BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),ArrayCell(Id(arr),IntLiteral(2))),ArrayCell(Id(arr),IntLiteral(0))))),Return(StringLiteral(Test LESS EQUAL)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_GREATER_EQUAL_operator_61(self):
        input = """int test_GREATER_EQUAL_operator(){
            if(zxc>=ctx || 8.665>=3.0+3.1)
                return 1;
            else
                return 0;
        }"""
        expect = "Program([FuncDecl(Id(test_GREATER_EQUAL_operator),[],IntType,Block([If(BinaryOp(||,BinaryOp(>=,Id(zxc),Id(ctx)),BinaryOp(>=,FloatLiteral(8.665),BinaryOp(+,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(IntLiteral(1)),Return(IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_complex_GREATER_EQUAL_operator_62(self):
        input = """float test_complex_GREATER_EQUAL_operator(){
            float arr[3];
            arr[0]=0.1; arr[1]=0.2; arr[2]=0.3;
            if(arr[0]>=arr[1] && arr[2]>= 0.1 || arr[1]>=ZXC_CXZ && __>=__)
                return arr[0];
            else
                return arr[1];
        }"""
        expect = "Program([FuncDecl(Id(test_complex_GREATER_EQUAL_operator),[],FloatType,Block([VarDecl(arr,ArrayType(FloatType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),FloatLiteral(0.1)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),FloatLiteral(0.2)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),FloatLiteral(0.3)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(>=,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(>=,ArrayCell(Id(arr),IntLiteral(2)),FloatLiteral(0.1))),BinaryOp(&&,BinaryOp(>=,ArrayCell(Id(arr),IntLiteral(1)),Id(ZXC_CXZ)),BinaryOp(>=,Id(__),Id(__)))),Return(ArrayCell(Id(arr),IntLiteral(0))),Return(ArrayCell(Id(arr),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_ADD_operator_63(self):
        input = """int test_ADD_operator(){
            if(1+2>2+3 && 8.665>=3.0+3.1)
                return 1+2;
            else
                return 456+cvb;
        }"""
        expect = "Program([FuncDecl(Id(test_ADD_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(>,BinaryOp(+,IntLiteral(1),IntLiteral(2)),BinaryOp(+,IntLiteral(2),IntLiteral(3))),BinaryOp(>=,FloatLiteral(8.665),BinaryOp(+,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(+,IntLiteral(1),IntLiteral(2))),Return(BinaryOp(+,IntLiteral(456),Id(cvb))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_complex_ADD_operator_64(self):
        input = """int test_complex_ADD_operator(){
            if(1+2>2+3+4+4 && 8.665!=3.0+3.1)
                return __(12)+12+vbn+__2__(__2__);
            else
                return 456+cvb+foo(goo(67))+__122__;
        }"""
        expect = "Program([FuncDecl(Id(test_complex_ADD_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(>,BinaryOp(+,IntLiteral(1),IntLiteral(2)),BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(2),IntLiteral(3)),IntLiteral(4)),IntLiteral(4))),BinaryOp(!=,FloatLiteral(8.665),BinaryOp(+,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,CallExpr(Id(__),[IntLiteral(12)]),IntLiteral(12)),Id(vbn)),CallExpr(Id(__2__),[Id(__2__)]))),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(456),Id(cvb)),CallExpr(Id(foo),[CallExpr(Id(goo),[IntLiteral(67)])])),Id(__122__))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_SUB_operator_65(self):
        input = """int test_SUB_operator(){
            if(1-2>2-3 && 8.665>=3.0-3.1)
                return 1-2;
            else
                return 456-cvb;
        }"""
        expect = "Program([FuncDecl(Id(test_SUB_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(>,BinaryOp(-,IntLiteral(1),IntLiteral(2)),BinaryOp(-,IntLiteral(2),IntLiteral(3))),BinaryOp(>=,FloatLiteral(8.665),BinaryOp(-,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(-,IntLiteral(1),IntLiteral(2))),Return(BinaryOp(-,IntLiteral(456),Id(cvb))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_complex_SUB_operator_66(self):
        input = """int test_complex_SUB_operator(){
            if(1-2>2-3-4-46 && 8.665!=3.0-3.1)
                return __(12)-12-vbn-__2__(__2__);
            else
                return 456-cvb-foo(goo(67))-__122__;
        }"""
        expect = "Program([FuncDecl(Id(test_complex_SUB_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(>,BinaryOp(-,IntLiteral(1),IntLiteral(2)),BinaryOp(-,BinaryOp(-,BinaryOp(-,IntLiteral(2),IntLiteral(3)),IntLiteral(4)),IntLiteral(46))),BinaryOp(!=,FloatLiteral(8.665),BinaryOp(-,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(-,BinaryOp(-,BinaryOp(-,CallExpr(Id(__),[IntLiteral(12)]),IntLiteral(12)),Id(vbn)),CallExpr(Id(__2__),[Id(__2__)]))),Return(BinaryOp(-,BinaryOp(-,BinaryOp(-,IntLiteral(456),Id(cvb)),CallExpr(Id(foo),[CallExpr(Id(goo),[IntLiteral(67)])])),Id(__122__))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_DIV_operator_67(self):
        input = """int main( ){ do
        i=0;
        i=count/12;
        goo(3,arr[10]);
        while(x>=9);
        return 345/1;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,Id(i),BinaryOp(/,Id(count),IntLiteral(12))),CallExpr(Id(goo),[IntLiteral(3),ArrayCell(Id(arr),IntLiteral(10))])],BinaryOp(>=,Id(x),IntLiteral(9))),Return(BinaryOp(/,IntLiteral(345),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_complex_DIV_operator_68(self):
        input = """int test_complex_DIV_operator(){
            if((123/123)/123==1 && 8.665/123!=3.0-3.1)
                return (123+foo(12))/13;
            else
                return (123/goo(12))/13/124/21;
        }"""
        expect = "Program([FuncDecl(Id(test_complex_DIV_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(==,BinaryOp(/,BinaryOp(/,IntLiteral(123),IntLiteral(123)),IntLiteral(123)),IntLiteral(1)),BinaryOp(!=,BinaryOp(/,FloatLiteral(8.665),IntLiteral(123)),BinaryOp(-,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(/,BinaryOp(+,IntLiteral(123),CallExpr(Id(foo),[IntLiteral(12)])),IntLiteral(13))),Return(BinaryOp(/,BinaryOp(/,BinaryOp(/,BinaryOp(/,IntLiteral(123),CallExpr(Id(goo),[IntLiteral(12)])),IntLiteral(13)),IntLiteral(124)),IntLiteral(21))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_MOD_operator_69(self):
        input = """int __MODOP( ){ do
        i=0;
        i=count%12;
        goo(3,arr[10]%34);
        while(x>=9);
        return 345%10000;
        }"""
        expect = "Program([FuncDecl(Id(__MODOP),[],IntType,Block([Dowhile([BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,Id(i),BinaryOp(%,Id(count),IntLiteral(12))),CallExpr(Id(goo),[IntLiteral(3),BinaryOp(%,ArrayCell(Id(arr),IntLiteral(10)),IntLiteral(34))])],BinaryOp(>=,Id(x),IntLiteral(9))),Return(BinaryOp(%,IntLiteral(345),IntLiteral(10000)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_complex_MOD_operator_70(self):
        input = """int test_complex_DIV_operator(){
            if((123%123)%123==1 && 8.665%123!=3.0-3.1)
                return (123+foo(12))%13;
            else
                return (123%goo(12))%13%124%21;
        }"""
        expect = "Program([FuncDecl(Id(test_complex_DIV_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(==,BinaryOp(%,BinaryOp(%,IntLiteral(123),IntLiteral(123)),IntLiteral(123)),IntLiteral(1)),BinaryOp(!=,BinaryOp(%,FloatLiteral(8.665),IntLiteral(123)),BinaryOp(-,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(%,BinaryOp(+,IntLiteral(123),CallExpr(Id(foo),[IntLiteral(12)])),IntLiteral(13))),Return(BinaryOp(%,BinaryOp(%,BinaryOp(%,BinaryOp(%,IntLiteral(123),CallExpr(Id(goo),[IntLiteral(12)])),IntLiteral(13)),IntLiteral(124)),IntLiteral(21))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_MUL_operator_71(self):
        input = """int __MULOP( ){ do
        i=0;
        i=count*12;
        goo(3*4,arr[10]*34);
        while(x>=9);
        return 345*10000*__;
        }"""
        expect = "Program([FuncDecl(Id(__MULOP),[],IntType,Block([Dowhile([BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,Id(i),BinaryOp(*,Id(count),IntLiteral(12))),CallExpr(Id(goo),[BinaryOp(*,IntLiteral(3),IntLiteral(4)),BinaryOp(*,ArrayCell(Id(arr),IntLiteral(10)),IntLiteral(34))])],BinaryOp(>=,Id(x),IntLiteral(9))),Return(BinaryOp(*,BinaryOp(*,IntLiteral(345),IntLiteral(10000)),Id(__)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_complex_NUL_operator_72(self):
        input = """int test_complex_MUL_operator(){
            if((123*123)*123==1 && 8.665*123!=3.0*3.1)
                return (123*foo(12))*13;
            else
                return (123*goo(12))*13*124*21;
        }"""
        expect = "Program([FuncDecl(Id(test_complex_MUL_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(==,BinaryOp(*,BinaryOp(*,IntLiteral(123),IntLiteral(123)),IntLiteral(123)),IntLiteral(1)),BinaryOp(!=,BinaryOp(*,FloatLiteral(8.665),IntLiteral(123)),BinaryOp(*,FloatLiteral(3.0),FloatLiteral(3.1)))),Return(BinaryOp(*,BinaryOp(*,IntLiteral(123),CallExpr(Id(foo),[IntLiteral(12)])),IntLiteral(13))),Return(BinaryOp(*,BinaryOp(*,BinaryOp(*,BinaryOp(*,IntLiteral(123),CallExpr(Id(goo),[IntLiteral(12)])),IntLiteral(13)),IntLiteral(124)),IntLiteral(21))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_NOT_operator_73(self):
        input = """int __NOTOP( ){
            if(!false)
                return 2;
            else
                return !true;
        }"""
        expect = "Program([FuncDecl(Id(__NOTOP),[],IntType,Block([If(UnaryOp(!,BooleanLiteral(false)),Return(IntLiteral(2)),Return(UnaryOp(!,BooleanLiteral(true))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_complex_NOT_operator_74(self):
        input = """int test_complex_NOT_operator(){
            if(abc== !(123+134))
                return !(123*foo(12))*13;
            else
                return !4;
        }"""
        expect = "Program([FuncDecl(Id(test_complex_NOT_operator),[],IntType,Block([If(BinaryOp(==,Id(abc),UnaryOp(!,BinaryOp(+,IntLiteral(123),IntLiteral(134)))),Return(BinaryOp(*,UnaryOp(!,BinaryOp(*,IntLiteral(123),CallExpr(Id(foo),[IntLiteral(12)]))),IntLiteral(13))),Return(UnaryOp(!,IntLiteral(4))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_NEGAT_operator_75(self):
        input = """float __NEGA(){
            if(-123)
                return -567.456;
            else
                return -(12+34);
        }"""
        expect = "Program([FuncDecl(Id(__NEGA),[],FloatType,Block([If(UnaryOp(-,IntLiteral(123)),Return(UnaryOp(-,FloatLiteral(567.456))),Return(UnaryOp(-,BinaryOp(+,IntLiteral(12),IntLiteral(34)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_complex_NEGA_operator_76(self):
        input = """int test_complex_NEGA_operator(){
            if(abc!= -(123+134) && abc==12-13-3)
                return -(123*foo(12))*13;
            else
                return -(-(-(-4)));
        }"""
        expect = "Program([FuncDecl(Id(test_complex_NEGA_operator),[],IntType,Block([If(BinaryOp(&&,BinaryOp(!=,Id(abc),UnaryOp(-,BinaryOp(+,IntLiteral(123),IntLiteral(134)))),BinaryOp(==,Id(abc),BinaryOp(-,BinaryOp(-,IntLiteral(12),IntLiteral(13)),IntLiteral(3)))),Return(BinaryOp(*,UnaryOp(-,BinaryOp(*,IntLiteral(123),CallExpr(Id(foo),[IntLiteral(12)]))),IntLiteral(13))),Return(UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLiteral(4)))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_array_index_77(self):
        input = """void main() {a[6];}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),IntLiteral(6))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_many_array_index_78(self):
        input = """void main() {
            boolean arr[3];
            arr[0]=true; 
            arr[1]=true;
            arr[2]=false;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(2)),BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    def test_complex_array_index_79(self):
        input = """void main() {
            boolean arr[3];
            i=0;
            arr[i]=true; 
            arr[i+1]=true;
            arr[i*2]=false;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(arr,ArrayType(BoolType,3)),BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(arr),Id(i)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(+,Id(i),IntLiteral(1))),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(*,Id(i),IntLiteral(2))),BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_more_complex_array_index_80(self):
        input = """int main(int argc, string argv[]) {
            int arr[3];
            i=0;
            arr[i]=1; 
            arr[i+1]=43;
            arr[i*2]=5678;
            return arr[0]+arr[1]-arr[2];
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,ArrayTypePointer(StringType))],IntType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(arr),Id(i)),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(+,Id(i),IntLiteral(1))),IntLiteral(43)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(*,Id(i),IntLiteral(2))),IntLiteral(5678)),Return(BinaryOp(-,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),ArrayCell(Id(arr),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_more_complex_array_index_81(self):
        input = """int main(int argc, string argv[]) {
            int arr[3];
            i=0;
            arr[foo(1)]=1; 
            arr[g00(12)*2-12]=43;
            arr[abc*joo(__)/___]=5678;
            return arr[0]+arr[abc*joo(__)/___]-arr[2];
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,ArrayTypePointer(StringType))],IntType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(arr),CallExpr(Id(foo),[IntLiteral(1)])),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(-,BinaryOp(*,CallExpr(Id(g00),[IntLiteral(12)]),IntLiteral(2)),IntLiteral(12))),IntLiteral(43)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(/,BinaryOp(*,Id(abc),CallExpr(Id(joo),[Id(__)])),Id(___))),IntLiteral(5678)),Return(BinaryOp(-,BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),BinaryOp(/,BinaryOp(*,Id(abc),CallExpr(Id(joo),[Id(__)])),Id(___)))),ArrayCell(Id(arr),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_more_complex_array_index_82(self):
        input = """void main(int argc, string argv[]) {
            int arr[3];
            i=0;
            arr[arr[arr[2]]]=1; 
            arr[g00(12)*arr[4]-12]=43;
            arr[abc*joo(__)/___]=5678;
            return;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,ArrayTypePointer(StringType))],VoidType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(arr),ArrayCell(Id(arr),ArrayCell(Id(arr),IntLiteral(2)))),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(-,BinaryOp(*,CallExpr(Id(g00),[IntLiteral(12)]),ArrayCell(Id(arr),IntLiteral(4))),IntLiteral(12))),IntLiteral(43)),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(/,BinaryOp(*,Id(abc),CallExpr(Id(joo),[Id(__)])),Id(___))),IntLiteral(5678)),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_very_complex_array_index_83(self):
        input = """void main(int argc, string argv[]) {
            int arr[3];
            i=0;
            arr[arr[arr[2]]]= arr[g00(12)*arr[4]-12]-1;
            arr[abc*joo(__)/___]=arr[arr[arr[2]]];
            return;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,ArrayTypePointer(StringType))],VoidType,Block([VarDecl(arr,ArrayType(IntType,3)),BinaryOp(=,Id(i),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(arr),ArrayCell(Id(arr),ArrayCell(Id(arr),IntLiteral(2)))),BinaryOp(-,ArrayCell(Id(arr),BinaryOp(-,BinaryOp(*,CallExpr(Id(g00),[IntLiteral(12)]),ArrayCell(Id(arr),IntLiteral(4))),IntLiteral(12))),IntLiteral(1))),BinaryOp(=,ArrayCell(Id(arr),BinaryOp(/,BinaryOp(*,Id(abc),CallExpr(Id(joo),[Id(__)])),Id(___))),ArrayCell(Id(arr),ArrayCell(Id(arr),ArrayCell(Id(arr),IntLiteral(2))))),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
        

        def test_very_complex_array_index_84(self):
            input = """void main() {
                    if(foo(a[a[2]]))
                        return;  
            }"""
            expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(CallExpr(Id(foo),[ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(2)))]),Return())]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,384))

        def test_call_func_85(self):
            input = """void main() {foo();return;}"""
            expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(foo),[]),Return()]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,385))

        def test_call_func_with_para_86(self):
            input = """boolean main() {foo(123);return true;}"""
            expect = "Program([FuncDecl(Id(main),[],BoolType,Block([CallExpr(Id(foo),[IntLiteral(123)]),Return(BooleanLiteral(true))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,386))

        def test_call_func_with_many_para_87(self):
            input = """float main() {foo(123,abc,xyz,__);return 12.43;}"""
            expect = "Program([FuncDecl(Id(main),[],FloatType,Block([CallExpr(Id(foo),[IntLiteral(123),Id(abc),Id(xyz),Id(__)]),Return(FloatLiteral(12.43))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,387))

        def test_call_func_with_index_para_88(self):
            input = """float main() {foo(__[2],_[_]);return 12.43;}"""
            expect = "Program([FuncDecl(Id(main),[],FloatType,Block([CallExpr(Id(foo),[ArrayCell(Id(__),IntLiteral(2)),ArrayCell(Id(_),Id(_))]),Return(FloatLiteral(12.43))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,388))

        def test_call_func_with_mix_para_89(self):
            input = """float main() {
                x=foo(__[2],12,"true",2.3);
                return 12.e-3;}"""
            expect = "Program([FuncDecl(Id(main),[],FloatType,Block([BinaryOp(=,Id(x),CallExpr(Id(foo),[ArrayCell(Id(__),IntLiteral(2)),IntLiteral(12),StringLiteral(true),FloatLiteral(2.3)])),Return(FloatLiteral(0.012))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,389))
        
        def test_prog_with_multi_stmt_90(self):
            input = """int main(){
                for (a=1;a<10;a=a*2){
                    for(b=2;b==10;b=b*2){
                        int a;
                        string b;
                        b = a + 1;
                    }
                }
                for(d=1;d!=1;d=d+1){
                    int e;
                    e = d;
                }
                for(c=100;c!=0;c=c%2){
                    for(d=1000;d>0;d=d%10){
                        int e;
                        e = d;
                        string d;
                        d = e;
                    }
                }
                return 1;
            }"""
            expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,StringType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))])),For(BinaryOp(=,Id(d),IntLiteral(1));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d))])),For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))])),Return(IntLiteral(1))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,390))

        def test_prog_with_multi_stmt_91(self):
            input = """string a;
            int plusFuncInt(int x, int y) {
                int sum;
                sum = x*567 + y/1234;
                return sum-45673;
            }
            float plusFuncDouble(float x, float y) {
                if(x>=y)
                    return x;
                else
                    return y;
            }"""
            expect = "Program([VarDecl(a,StringType),FuncDecl(Id(plusFuncInt),[VarDecl(x,IntType),VarDecl(y,IntType)],IntType,Block([VarDecl(sum,IntType),BinaryOp(=,Id(sum),BinaryOp(+,BinaryOp(*,Id(x),IntLiteral(567)),BinaryOp(/,Id(y),IntLiteral(1234)))),Return(BinaryOp(-,Id(sum),IntLiteral(45673)))])),FuncDecl(Id(plusFuncDouble),[VarDecl(x,FloatType),VarDecl(y,FloatType)],FloatType,Block([If(BinaryOp(>=,Id(x),Id(y)),Return(Id(x)),Return(Id(y)))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,391))

        def test_prog_with_multi_stmt_92(self):
            input = """int main( int argc , float argv[] )
            {
                boolean c ;
                int i ;
                for(i=0;i<100;i=a+3){
                    int d ;
                    d = i + 3 ;
                    putInt(d ) ;
                }
                print(d);
                return i ;
            }"""
            expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(argv,ArrayTypePointer(FloatType))],IntType,Block([VarDecl(c,BoolType),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(+,Id(a),IntLiteral(3)));Block([VarDecl(d,IntType),BinaryOp(=,Id(d),BinaryOp(+,Id(i),IntLiteral(3))),CallExpr(Id(putInt),[Id(d)])])),CallExpr(Id(print),[Id(d)]),Return(Id(i))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,392))

        def test_full_prog_with_mix_exp_93(self):
            input = """boolean swap(int a, int b){ 
                int tmp;
                tmp = a;
                a = b;
                b = tmp;
                printf(a, b);
                return true;
            }
            int main(){
                int a,b;
                boolean result;
                result = swap(a,b);
                print(result);
            }"""
            expect = "Program([FuncDecl(Id(swap),[VarDecl(a,IntType),VarDecl(b,IntType)],BoolType,Block([VarDecl(tmp,IntType),BinaryOp(=,Id(tmp),Id(a)),BinaryOp(=,Id(a),Id(b)),BinaryOp(=,Id(b),Id(tmp)),CallExpr(Id(printf),[Id(a),Id(b)]),Return(BooleanLiteral(true))])),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(result,BoolType),BinaryOp(=,Id(result),CallExpr(Id(swap),[Id(a),Id(b)])),CallExpr(Id(print),[Id(result)])]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,393))

        def test_full_prog_with_mix_func_decl_94(self):
            input = """int plusFuncInt(int x, int y) {
                int sum;
                sum = x*567 + y/1234;
                return sum-45673;
            }
            float plusFuncDouble(float x, float y) {
                if(x>=y)
                    return x;
                else
                    return y;
            }"""
            expect = "Program([FuncDecl(Id(plusFuncInt),[VarDecl(x,IntType),VarDecl(y,IntType)],IntType,Block([VarDecl(sum,IntType),BinaryOp(=,Id(sum),BinaryOp(+,BinaryOp(*,Id(x),IntLiteral(567)),BinaryOp(/,Id(y),IntLiteral(1234)))),Return(BinaryOp(-,Id(sum),IntLiteral(45673)))])),FuncDecl(Id(plusFuncDouble),[VarDecl(x,FloatType),VarDecl(y,FloatType)],FloatType,Block([If(BinaryOp(>=,Id(x),Id(y)),Return(Id(x)),Return(Id(y)))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,394))

        def test_full_prog_with_mix_if_else_95(self):
            input = """int foo(int  c[],int i){
                for(i=10;i<x;i=i+y){
                    if (a==c)
                        if (d=f)
                            if(lv=2) 
                                continue;
                            else c = a[cc+9];
                        else disc/4;
                    else break;
                }
                return a;
            }"""
            expect = "Program([FuncDecl(Id(foo),[VarDecl(c,ArrayTypePointer(IntType)),VarDecl(i,IntType)],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(10));BinaryOp(<,Id(i),Id(x));BinaryOp(=,Id(i),BinaryOp(+,Id(i),Id(y)));Block([If(BinaryOp(==,Id(a),Id(c)),If(BinaryOp(=,Id(d),Id(f)),If(BinaryOp(=,Id(lv),IntLiteral(2)),Continue(),BinaryOp(=,Id(c),ArrayCell(Id(a),BinaryOp(+,Id(cc),IntLiteral(9))))),BinaryOp(/,Id(disc),IntLiteral(4))),Break())])),Return(Id(a))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,395))

        def test_full_prog_with_mix_index_and_func_96(self):
            input = """int main () {
                putIntLn(2);
                (fun())[4];
                (arr)[5];
            }"""
            expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(2)]),ArrayCell(CallExpr(Id(fun),[]),IntLiteral(4)),ArrayCell(Id(arr),IntLiteral(5))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,396))

        def test_full_prog_with_mix_operator_97(self):
            input = """int main( int argc , string str )
            {
                boolean c ;
                int i ;
                i=10;
                if(i>=argc && c==true){
                    int d ;
                    str = "Hello World";
                    putInt(d ) ;
                }
                print(str);
                return i ;
            }"""
            expect = "Program([FuncDecl(Id(main),[VarDecl(argc,IntType),VarDecl(str,StringType)],IntType,Block([VarDecl(c,BoolType),VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(10)),If(BinaryOp(&&,BinaryOp(>=,Id(i),Id(argc)),BinaryOp(==,Id(c),BooleanLiteral(true))),Block([VarDecl(d,IntType),BinaryOp(=,Id(str),StringLiteral(Hello World)),CallExpr(Id(putInt),[Id(d)])])),CallExpr(Id(print),[Id(str)]),Return(Id(i))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,397))

        def test_prog_with_mix_for_98(self):
            input = """int main(){
                int x, y,arr[10],i;
                x = y =0;
                for(i=0;i<10;i=i+1)
                    arr[i]=i;
                for(i=0;i<10;i=i+1){
                    if(arr[i]%2==0)
                        x = x + arr[i];
                    else
                        return y + arr[i];
                }        
            }"""
            expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(arr,ArrayType(IntType,10)),VarDecl(i,IntType),BinaryOp(=,Id(x),BinaryOp(=,Id(y),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(arr),Id(i)),Id(i))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(arr),Id(i)),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(x),BinaryOp(+,Id(x),ArrayCell(Id(arr),Id(i)))),Return(BinaryOp(+,Id(y),ArrayCell(Id(arr),Id(i)))))]))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,398))

        def test_full_prog_with_mix_stmt_99(self):
            input = """string String(){
                boolean arr[3];
                crr[3+x-y*342];
                drr(2,4)[3+x-y*342];
                return "Hello world";
            }"""
            expect = "Program([FuncDecl(Id(String),[],StringType,Block([VarDecl(arr,ArrayType(BoolType,3)),ArrayCell(Id(crr),BinaryOp(-,BinaryOp(+,IntLiteral(3),Id(x)),BinaryOp(*,Id(y),IntLiteral(342)))),ArrayCell(CallExpr(Id(drr),[IntLiteral(2),IntLiteral(4)]),BinaryOp(-,BinaryOp(+,IntLiteral(3),Id(x)),BinaryOp(*,Id(y),IntLiteral(342)))),Return(StringLiteral(Hello world))]))])"
            self.assertTrue(TestAST.checkASTGen(input,expect,399))
