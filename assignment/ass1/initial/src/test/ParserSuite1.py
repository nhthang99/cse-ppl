#Le Cong Linh
#1711948

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

    def test_more_complex_program_33(self):
        """More complex program"""
        input = """
        string c(){
            boolean arr[3];
            crr[3+x-y*342];
            drr(2,4)[3+x-y*342];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))        

    def test_more_complex_program_34(self):
        """More complex program"""
        input = """
        int foo ( int a , float b [] )
        {
            boolean c ;
            int i ;
            i = a + 3 ;
            if( i >0) {
                int d ;
                d = i + 3 ;
                putInt(d ) ;
            }
            return i ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))        

    def test_more_complex_program_35(self):
        """More complex program"""
        input = """
        int main( int argc , float argv[] )
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))                

    def test_more_complex_program_36(self):
        """More complex program"""
        input = """
        int main( int argc , string str )
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_more_complex_program_37(self):
        """More complex program"""
        input = """
        void count(int money[]){
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
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))        

    def test_more_complex_program_38(self):
        """More complex program"""
        input = """void main( ){ if (a) if (b) if (c) for(i=0;i<9;i=i+1) foo(2,4); else a; else for(i=0;i<9;i=i+1) foo(2,4);}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_more_complex_program_39(self):
        """More complex program"""
        input = """void main( ){ if (a) if (b) if (c) a; else a; else a;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_more_complex_program_40(self):
        """More complex program"""
        input = """int main() {
            (a+b)+(c+d)==(a+b)+(c+d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_more_complex_program_41(self):
        """More complex program"""
        input = """int main () {
            putIntLn(2);
            (fun())[4];
            (arr)[5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_more_complex_program_42(self):
        """More complex program"""
        input = """void main( ){ do
        i=0;
        i=count/12;
        goo(3,arr[10]);
        while(x>=9); }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_more_complex_program_43(self):
        """More complex program"""
        input = """void main( ){
        int i,count;
        i=count/12;
        goo(3,arr[10]);
        a=a && 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_more_complex_program_44(self):
        """More complex program"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_more_complex_program_45(self):
        """More complex program"""
        input = """void main( ){ 
            foo(2)[3+x] = a[b[2]] +3;
            goo(2)[x=x||y] = a[b[2+z]] + t;
            100;
            a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_more_complex_program_46(self):
        """More complex program"""
        input = """void main() { if(i>1) {} else {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_more_complex_program_47(self):
        """More complex program"""
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_more_complex_program_48(self):
        """More complex program"""
        input = """string c(){
            s = a +b + c * d;
            d = a && b;
            e = !a;
            return str;
        }
        int main(){
            int a[1];
            if (true) return a;
            else return b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_more_complex_program_49(self):
        """More complex program"""
        input = """int foo(int  c[]){
            if (a==c)
                if (d=f)
                    if(lv=2) c=d;
                    else c = a[cc+9];
                else disc/4;
            else scj=7/3;
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_more_complex_program_50(self):
        """More complex program"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a;  
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_more_complex_program_51(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a
        }"""
        expect = "Error on line 11 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_more_complex_program_52(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else
                else break;
            }
            return a;
        }"""
        expect = "Error on line 8 col 16: else"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_more_complex_program_53(self):
        """More complex program with error"""
        input = """int main() {"""
        expect = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_more_complex_program_54(self):
        """More complex program with error"""
        input = """float number;
                    bool check[5];
        """
        expect = "Error on line 2 col 20: bool"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_more_complex_program_55(self):
        """More complex program with error"""
        input = """float number;
                    boolean check[];
        """
        expect = "Error on line 2 col 34: ]"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_more_complex_program_56(self):
        """More complex program with error"""
        input = """float number;
                    boolean check[x+y+3];
        """
        expect = "Error on line 2 col 34: x"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_more_complex_program_57(self):
        """More complex program with error"""
        input = """float number;
                    boolean check[3];
                    t=5;
        """
        expect = "Error on line 3 col 20: t"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_more_complex_program_58(self):
        """More complex program with error"""
        input = """int main(){
            do{
                a=c;
                d=b;
            }
            {
            }
            while a!=b
        }"""
        expect = "Error on line 9 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_more_complex_program_59(self):
        """More complex program"""
        input = """
        void main() {
            if (a == b)
                if (c == d)
                    foo();
                else
                    foo();
            else
                foo();
            else {
                //comment
            }
        }
        """
        expect = "Error on line 10 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_more_complex_program_60(self):
        """More complex program"""
        input = """int main(){
        int i, num;
        float data;
        printf("Enter total number of elements(1 to 100): ");
        scanf("%d", num);
        // Allocates the memory for 'num' elements.
        if(data == NULL)
        {
        printf("Error!!! memory not allocated.");
        exit(0);
        }
    
        // Stores the number entered by the user.
        for(i = 0; i < num; i = i + 1)
        {
            printf("Enter Number %d: ", i + 1);
            scanf("%f", data + i);
        }
        // Loop to store largest number at address data
        for(i = 1; i < num; i = i + 1)
        {
            // Change < to > if you want to find the smallest number
            if(data < (data + i))
            data = (data + i);
        }
        printf("Largest element = %.2f", data);
        return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_more_complex_program_61(self):
        """More complex program with error"""
        input = """
        int main(string arg[])
        {
            for (i=1;i>1;i+1 {}
        }
        """
        expect = "Error on line 4 col 29: {"
        self.assertTrue(TestParser.checkParser(input,expect,261))        

    def test_more_complex_program_62(self):
        """More complex program with error"""
        input = """int main()
        {
            int i;
            i = 0;
            while(i==1)
            {
            printf("while vs do-while");
            }
            printf("Out of loop");
        }
        """
        expect = "Error on line 5 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_more_complex_program_63(self):
        """More complex program with error"""
        input = """int main() {
            int year;
            printf("Please enter a year to check whether it is a leap year or not");
            scanf("%d", year);
            if ( year%400 == 0)
                printf("%d is a leap year", year);
            if ( year%100 == 0)
                printf("%d is not a leap year", year);
            if ( year%4 == 0 )
                printf("%d is a leap year", year)
            else
                printf("%d is not a leap year", year);  
            return 0;
            }
        """
        expect = "Error on line 11 col 12: else"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_more_complex_program_64(self):
        """More complex program with error"""
        input = """int main(){
            do{
                a=c;
                d=b;
            }
            {
                a=a+4;
                b>4;
            }
            while a!=;
            }
        """
        expect = "Error on line 10 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_more_complex_program_65(self):
        """More complex program with error"""
        input = """void main()
        {
	    clrscr();
	    int no_star, no_row, i, j;
	    for(i=0; i<no_row; i++)
	    {
		    for(j=0; j<p; j++)
		{
			printf("* ");
		}
		printf("");
	    }
	    getch();
        }
        """
        expect = "Error on line 5 col 26: +"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_more_complex_program_66(self):
        """More complex program with error"""
        input = """int x,y;
        int tong, hieu, tich, thuong;
        int main(){
            tong = x + y;
            hieu= x - y;
            int arr[];
            tich = x * y;
            float average;
            average = tong/2;
            return 0;
        }
        """
        expect = "Error on line 6 col 20: ]"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_more_complex_program_67(self):
        """More complex program with error"""
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
        string str(int num);
        int[] compute(int x,int y,int tong[]){
            operator(10);
            return tong;
        }
        """
        expect = "Error on line 11 col 27: ;"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_more_complex_program_68(self):
        """More complex program with error"""
        input = """boolean arr[10];
        void print(boolean arr[){}
        void compute(int x,int y,int tong[]){
            for(i=0;i<100;i=i+1){
                arr[i]=true;
                print(arr);
            }
        }
        """
        expect = "Error on line 2 col 31: )"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_more_complex_program_69(self):
        """More complex program with error"""
        input = """string a;
        int plusFuncInt(int x, int y) {
            int sum;
            sum  x*567 + y/1234;
            return sum-45673;
        }
        float plusFuncDouble(float x, float y) {
            if(x>=y)
                return x;
            else
                return y;
        }       
        """
        expect = "Error on line 4 col 17: x"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_more_complex_program_70(self):
        """More complex program with error"""
        input = """void main( ){ if (a) if (b) if (c) for(i=0;i<9;i=i+1) foo(2,4); else ; else for(i=0;i<9;i=i+1) foo(2,4);}
        """
        expect = "Error on line 1 col 69: ;"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_more_complex_program_71(self):
        """More complex program with error"""
        input = """void main( ){ do
        i=0;
        i=count/12;
        goo(3,arr[10]);
        while(x>=9);
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_more_complex_program_72(self):
        """More complex program with error"""
        input = """{}
        """
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_more_complex_program_73(self):
        """More complex program with error"""
        input = """int a;
        a=2;
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_more_complex_program_74(self):
        """More complex program with error"""
        input = """int int;
        float num;
        void count(int a,int b);
        """
        expect = "Error on line 1 col 4: int"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_more_complex_program_75(self):
        """More complex program with error"""
        input = """
        void main( ){ if (a) if (b) if (c) a; else a; else }
        """
        expect = "Error on line 2 col 59: }"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_more_complex_program_76(self):
        """More complex program with error"""
        input = """
        void main( ){ if if (b) if (c) a; else a; else a;}
        """
        expect = "Error on line 2 col 25: if"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_more_complex_program_77(self):
        """More complex program with error"""
        input = """
        int main() {check = 1 + 2 - 3 * 4  == 5 != 6;}
        """
        expect = "Error on line 2 col 48: !="
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_more_complex_program_78(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i+=y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a;  
        }
        """
        expect = "Error on line 2 col 27: ="
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_more_complex_program_79(self):
        """More complex program with error"""
        input = """int main(){
            a = b() + c() + d();
            print(a);
            a = a / sum(a,b + sub(a,b);
        }
        """
        expect = "Error on line 4 col 38: ;"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_more_complex_program_80(self):
        """More complex program with error"""
        input = """int a;
        int main){}
        float z;
        """
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_more_complex_program_81(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a;  
        }
        """
        expect = "Error on line 6 col 24: else"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_more_complex_program_82(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc++];
                    else disc/4;
                else break;
            }
            return a;  
        }
        """
        expect = "Error on line 6 col 38: +"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_more_complex_program_83(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10 i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a;  
        }
        """
        expect = "Error on line 2 col 21: i"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_more_complex_program_84(self):
        """More complex program with error"""
        input = """int foo(int  c[],int i){
            for(i=10;i<x;i=i+y){
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a;  
        }
        int a;
        a=9;
        """
        expect = "Error on line 13 col 8: a"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_more_complex_program_85(self):
        """More complex program with error"""
        input = """int main(){
        int arr[x+2];
        return 0;
        }
        """
        expect = "Error on line 2 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_more_complex_program_86(self):
        """More complex program with error"""
        input = """void main(int argc, string srrgv[]){
        string boolean;
        }
        """
        expect = "Error on line 2 col 15: boolean"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_more_complex_program_87(self):
        """More complex program with error"""
        input = """string a;
        int plusFuncInt(int x, int y) {
            int sum;
            for(x=1;x<10;x=y+1){
                if(x==5)
                    break;
            }
            returns x;
        }       
        """
        expect = "Error on line 8 col 20: x"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_more_complex_program_88(self):
        """More complex program with error"""
        input = """string a;
        int break(int x, int y) {
            int sum;
            for(x=1;x<10;x=y+1){
                if(x==5)
                    break;
            }
            return x;
        }       
        """
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_more_complex_program_89(self):
        """More complex program with error"""
        input = """int main(string arg[])
        {
            do 
            
            while (a!=b);
        }
        """
        expect = "Error on line 5 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_more_complex_program_90(self):
        """More complex program with error"""
        input = """
        int main(){
            int i;
            i=0;
            for(i=0;i<10;i++)
                printf("hello worlf");
        }
        """
        expect = "Error on line 5 col 27: +"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_more_complex_program_91(self):
        """More complex program with error"""
        input = """int main( int argc , float argv[] )
        {
            boolean c ;
            int i ;
            for(i=0;i<100;i=a+3){
                int d ;
                d = i + 3 ;
                if(d>>5)
                    {putInt(d ) ;}
            }
            print(d);
            return i ;
        }
        """
        expect = "Error on line 8 col 21: >"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_more_complex_program_92(self):
        """More complex program with error"""
        input = """int main( int argc , float argv[] )
        {
            boolean c[2+3+4] ;
            int i ;
            for(i=0;i<100;i=a+3){
                int d ;
                d = i + 3 ;
                putInt(d ) ;
            }
            print(d);
            return i;
        }
        """
        expect = "Error on line 3 col 23: +"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_more_complex_program_93(self):
        """More complex program with error"""
        input = """int main( int argc , float argv[] )
        {
            boolean c ;
            int i ;
            for(i=0;i<100;i=a+3){
                int d=3 ;
                i=d- 3 ;
                putInt(d ) ;
            }
            print(d);
            return i ;
        }
        """
        expect = "Error on line 6 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_more_complex_program_94(self):
        """More complex program with error"""
        input = """int main( int argc , float argv[5] )
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
        }
        """
        expect = "Error on line 1 col 32: 5"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_more_complex_program_95(self):
        """More complex program with error"""
        input = """int main( int argc , float argv[x*3] )
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
        }
        """
        expect = "Error on line 1 col 32: x"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_more_complex_program_96(self):
        """More complex program with error"""
        input = """int main(){
            foo(2,)[3+x] = a[b[2]] + 3;
        }
        """
        expect = "Error on line 2 col 18: )"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_more_complex_program_97(self):
        """More complex program with error"""
        input = """
        int i;
        if(i>=3){
            printf("Hello");
        }
        """
        expect = "Error on line 3 col 8: if"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_more_complex_program_98(self):
        """More complex program with error"""
        input = """int main(string arg[])
        {
            for [i=1;i>1;i+1]{}
        }
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_more_complex_program_99(self):
        """More complex program with error"""
        input = """int main(string arg[])
        {
            for (i=1;i>1;i+1 {}
        }
        """
        expect = "Error on line 3 col 29: {"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_more_complex_program_100(self):
        """More complex program with error"""
        input = """int main(){
            int a+b;
            a = int + 1;
        };
        """
        expect = "Error on line 2 col 17: +"
        self.assertTrue(TestParser.checkParser(input,expect,300))






    
    
    

    

    
    
    

    