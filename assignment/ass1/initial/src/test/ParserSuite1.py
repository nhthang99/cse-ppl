import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_01(self):
        """ Simple program """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_simple_program_02(self):
        """ Simple program """
        input = """int count;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))        

    def test_simple_program_03(self):
        """ Simple program """
        input = """float number;
                    boolean check;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))    

    def test_simple_program_04(self):
        """ Simple program """
        input = """float number;
        int check(int a){}
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_simple_program_05(self):
        """ Simple program """
        input = """float number;
                    boolean check;
                    int arr[4],num,brr[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_simple_program_06(self):
        """ Simple program """
        input = """float number;
                    int year;
                    boolean check_num(int num){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_simple_program_07(self):
        """ Simple program """
        input = """float number;
                    boolean check;
                    float FLOAT_FUNC(int a){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))            

    def test_simple_program_08(self):
        """ Simple program """
        input = """float arr[10],number;
                    boolean list[2],check;
                    float test(int a, boolean list[], float brr[]){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_simple_program_09(self):
        """ Simple program """
        input = """float number;
        int PRINT(int a){
            int a;
            a=10;
            return a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_simple_program_10(self):
        """ Simple program """
        input = """int Date;
        int PRINT(int a){
            Date=9;
            int i;
            for(i=0;i<8;i=i+1)
                Date=Date+1;
            return 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))        

    def test_more_complex_program_11(self):
        """More complex program"""
        input = """int Date;
        int PRINT(int a){
            Date=9;
            int i;
            for(i=0;i<8;i=i+1)
                Date=Date+1;
            return 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))        

    def test_more_complex_program_12(self):
        """More complex program"""
        input = """float Date;
        void PRINT(int a){
            Date=9;
            int i;
            i=10;
            if(i>8)
                Date=Date+3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))  

    def test_more_complex_program_13(self):
        """More complex program"""
        input = """int Date;
        boolean PRINT(int a){
            boolean n;
            n=true;
            return true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_more_complex_program_14(self):
        """More complex program"""
        input = """int Date(){}
        float Month(int date){}
        void PRINT(int date){
            int x;
            x=date;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_more_complex_program_15(self):
        """More complex program"""
        input = """int date[31],month[12];
        int Year(int month[], int date[]){}
        boolean PRINT(int a){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_more_complex_program_16(self):
        """More complex program"""
        input = """int main() {
        printf("Hello World!!!");
        return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_more_complex_program_17(self):
        """More complex program"""
        input = """int main(int argc){ 
     string name[20]; 
     print("Hay nhap ten cua ban:");  
     scanf(name);
     print("Xin chao name");          
     return 0; }  
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_more_complex_program_18(self):
        """More complex program"""
        input = """int operator(int num){   
            int x;
            x = 12;
            int y;
            y = 5;
            int tong, hieu, tich, thuong;
            tong = x + y;
            hieu= x - y;
            tich = x * y;
        }
        int main(){
            operator(10);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))        

    def test_more_complex_program_19(self):
        """More complex program"""
        input = """  
        int x,y;
        int tong, hieu, tich, thuong;
        int main(){
            tong = x + y;
            hieu= x - y;
            tich = x * y;
            float average;
            average = tong/2;
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))        

    def test_more_complex_program_20(self):
        """More complex program"""
        input = """  
        int main(){
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220)) 

    def test_more_complex_program_21(self):
        """More complex program"""
        input = """int operator(int num){   
            int x;
            x = 12;
            int y;
            y = 5;
            int tong, hieu, tich, thuong;
            tong = x + y;
            hieu= x - y;
            tich = x * y;
        }
        int[] compute(int x,int y,int tong[]){
            operator(10);
            return tong;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))        

    def test_more_complex_program_22(self):
        """More complex program"""
        input = """int array(int num){   
            for(i=0;i<100;i=i+1){
                arr[i]=num;
            }
        }
        int[] compute(int x,int y,int tong[]){
            operator(10);
            for(i=0;i<100;i=i+1){
                tong=tong+arr[i];
            }
            return tong;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))        

    def test_more_complex_program_23(self):
        """More complex program"""
        input = """
        boolean arr[10];
        void print(boolean arr[]){}
        void compute(int x,int y,int tong[]){
            for(i=0;i<100;i=i+1){
                arr[i]=true;
                print(arr);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))                

    def test_more_complex_program_24(self):
        """More complex program"""
        input = """
        void print(boolean arr[]){}
        void test_prog(){
            boolean arr[10];
            print(arr);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_more_complex_program_25(self):
        """More complex program"""
        input = """
        string a;
        void printsss(string a){
            print(a);
        }
        void test_program(){
            a = "dfghjkfg";
            printsss(a);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))        

    def test_more_complex_program_26(self):
        """More complex program"""
        input = """
        float a, b, c;
        boolean x, y, z;
        int g, h, y;
        float nty(){}
        int x, y, z;
        string a,w,q; 
        /*
        =======================================
        Comment here
        =======================================
        */
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))        

    def test_more_complex_program_27(self):
        """More complex program"""
        input = """
        string a;
        int plusFuncInt(int x, int y) {
            return x + y;
        }

        float plusFuncDouble(float x, float y) {
            return x + y;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))        

    def test_more_complex_program_28(self):
        """More complex program"""
        input = """
        string a;
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
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))        

    def test_more_complex_program_29(self):
        """More complex program"""
        input = """
        string a;
        int plusFuncInt(int x, int y) {
            int sum;
            for(x=1;x<10;x=y+1){
                if(x==5)
                    break;
            }
            return x;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))                

    def test_more_complex_program_30(self):
        """More complex program"""
        input = """
        string a;
        float plusFuncDouble(float x, float y) {
            for(y=0;y<=x;y=y+1)
            if(y<x)
                continue;
            else
                return y;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))        

    def test_more_complex_program_31(self):
        """More complex program"""
        input = """
        int main(){
            foo(2)[3+x] = a[b[2]] + 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))        

    def test_more_complex_program_32(self):
        """More complex program"""
        input = """
        string c(){
            3[3+x] = true[b[2]] +3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))        






















    def test_more_complex_program_99(self):
        """More complex program"""
        input = """int main () {
            putIntLn(2);
            (fun())[4];
            (arr)[5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test_more_complex_program_100(self):
        """More complex program"""
        input = """void main( ){ if (a) if (b) if (c) a; else a; else a;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    def test_more_complex_program_96(self):
        """More complex program"""
        input = """void main( ){ do
        i=0;
        i=count/12;
        goo(3,arr[10]);
        while(x>=9); }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_more_complex_program_97(self):
        """More complex program"""
        input = """void main( ){ if (a) if (b) if (c) for(i=0;i<9;i=i+1) foo(2,4); else a; else for(i=0;i<9;i=i+1) foo(2,4);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main() {
            (a+b)+(c+d)==(a+b)+(c+d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))