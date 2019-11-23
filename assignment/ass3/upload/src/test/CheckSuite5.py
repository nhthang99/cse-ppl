import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_1(self):
        input = """
                int foo(int n,int r) {
                    return 1;
                }

                int main() {
                    int a;
                    a = foo + 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_2(self):
        input = """
                int foo(int n,int r) {
                    return 1;
                }

                int main() {
                    foo = 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_3(self):
        input = """

                int main() {
                    int a[7];
                    a = 10;
                    return 0;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_4(self):
        input = """
                int[] foo(int n,int r) {
                    int a[5];
                    return a;
                }

                int main() {
                    int a;
                    a = foo + 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_5(self):
        """CalPermutation Program """
        input = """
        int foo(){ return 1;}
        int main(){
            int a;
            foo(1,2);
            return 0;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        """CalPermutation Program """
        input = """
        int[] foo(){ 
            int a[4];
            return a;}
        int main(){
            foo()[0] = 1;
            foo() = 1;
            return 0;
        }
                """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        """CalPermutation Program """
        input = """
        int x;
        int main(){
            x();
            return 0;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),[])"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        """CalPermutation Program """
        input = """
        int foo(int a){return 1;}
        int main(){
            foo;
            foo(10);
            return 0;
        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))