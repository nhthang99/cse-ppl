import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # base test
    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
            '//Hello\n/*Hi\nYay*///?!@#$%^//',
            '<EOF>',101))
    def test_id(self):
        self.assertTrue(TestLexer.checkLexeme(
            "_ _1 x X aA1_",
            "_,_1,x,X,aA1_,<EOF>",102))
    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme(
            'break continue else for if return do while',
            'break,continue,else,for,if,return,do,while,<EOF>',103))
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme(
            '+ - * / % ! || && != == < > <= >= =',
            '+,-,*,/,%,!,||,&&,!=,==,<,>,<=,>=,=,<EOF>',104))
    def test_bracket(self):
        self.assertTrue(TestLexer.checkLexeme(
            '[ ] { } ( ) ; ,',
            '[,],{,},(,),;,,,<EOF>',105))
    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1 2 3 4 5 6 7 8 9 0 01 10 000',
            '1,2,3,4,5,6,7,8,9,0,01,10,000,<EOF>',106))
    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1. .1 1.e1 1E-2 1.0e1 3.14 ',
            '1.,.1,1.e1,1E-2,1.0e1,3.14,<EOF>',107))
    def test_escape(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "Compiler" "Escape\n" "\f\r\n\t\"\\" ''',
            r'''Compiler,Escape\n,\f\r\n\t\"\\,<EOF>''',108))
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "abc ''',
            r'''Unclosed String: abc ''',109))
    def test_illegal_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "Hi, this is illegall escape \i" ''',
            r'''Illegal Escape In String: Hi, this is illegall escape \i''' ,110))
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1>2?3',
            '1,>,2,Error Token ?',111))

    # normal test
    def test_mul_bracket(self):
        self.assertTrue(TestLexer.checkLexeme(
            '{{{{{{{{{int a= 10;}}}}}}}}}',
            '{,{,{,{,{,{,{,{,{,int,a,=,10,;,},},},},},},},},},<EOF>',112))
    def test_var_dcls(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''int a = (int) 12.6;''',
            'int,a,=,(,int,),12.6,;,<EOF>',113))
    def test_print_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' printf("Hello World"); ''',
            r'''printf,(,Hello World,),;,<EOF>''',114))
    def test_for_loop(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' for(int i = 0; i < n; i = i +1) {printf("");} ''',
            r'''for,(,int,i,=,0,;,i,<,n,;,i,=,i,+,1,),{,printf,(,,),;,},<EOF>''',115))
    def test_while_loop(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' float a; while(a < 10) {a = a - 1;} ''',
            r'''float,a,;,while,(,a,<,10,),{,a,=,a,-,1,;,},<EOF>''',116))
    def test_comment_in_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' /* /*  */ */ ''',
            r'''*,/,<EOF>''',117))
    def test_while_hard_expr(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' while(1<2<3>4>5) {ok();} ''',
            r'''while,(,1,<,2,<,3,>,4,>,5,),{,ok,(,),;,},<EOF>''',118))
    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' if(m % 2 == 0) return true;''',
            r'''if,(,m,%,2,==,0,),return,true,;,<EOF>''',119))
    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "abc\" ''',
            r'''Unclosed String: abc\" ''',120))

    # rare test
    def test_expr(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' ===> ''',
            r'''==,=,>,<EOF>''',121))
    def test_illegal_unclosed_string(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' "abc\mabc ''',
            r'''Illegal Escape In String: abc\m''',122))
    def test_decimal_point(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' . ''',
            r'''Error Token .''',123))
    def test_float_2(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' .e2 ''',
            r'''Error Token .''',124))
    def test_float_3(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' 1.1.1 ''',
            r'''1.1,.1,<EOF>''',125))
    def test_float_4(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' A.1.1 ''',
            r'''A,.1,.1,<EOF>''',126))
    def test_unclosed_string_2(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' "abc              ''',
            r'''Unclosed String: abc              ''',127))
    def test_unclosed_string_3(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' "abc     \\\n\t''',
            r'''Unclosed String: abc     \\\n\t''',128))
    def test_unclosed_string_4(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' "abc     
            ''',
            r'''Unclosed String: abc     ''',129))
    def test_error_char(self):
            self.assertTrue(TestLexer.checkLexeme(
            r''' @members ''',
            r'''Error Token @''',130))

    # long test
    def test_long_1(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''void str_copy(char a, char b,int n, int k)
	{
		for(int i = n; i < k; i++)
		{
			a[i-n] = b[i];
		}
	}''',
            r'''void,str_copy,(,char,a,,,char,b,,,int,n,,,int,k,),{,for,(,int,i,=,n,;,i,<,k,;,i,+,+,),{,a,[,i,-,n,],=,b,[,i,],;,},},<EOF>''',131))
    def test_long_2(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''bool comp_str(string s1, string s2)
	{
		if(s1.length() != s2.length()) return false;
		for (int i = 0; i < s1.length(); ++i)
			if (s1[i] != s2[i]) return false;
		return true;
	}''',
            r'''bool,comp_str,(,string,s1,,,string,s2,),{,if,(,s1,Error Token .''',132))
    def test_long_3(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''heint count(struct student* students)
	{
		for (int i = 0; i < MAX_STUDENT; ++i)
		{
			if(!students[i].ID.length())	return i;
		}
	}llo''',
            r'''heint,count,(,struct,student,*,students,),{,for,(,int,i,=,0,;,i,<,MAX_STUDENT,;,+,+,i,),{,if,(,!,students,[,i,],Error Token .''',133))
    def test_long_4(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''void date()
	{
		for(int i = 0; i < 40; i++) cout << "-";
		cout << __DATE__;
		for(int i = 0; i < 40; i++) cout << "-";
		cout << endl;
	}''',
            r'''void,date,(,),{,for,(,int,i,=,0,;,i,<,40,;,i,+,+,),cout,<,<,-,;,cout,<,<,__DATE__,;,for,(,int,i,=,0,;,i,<,40,;,i,+,+,),cout,<,<,-,;,cout,<,<,endl,;,},<EOF>''',134))
    def test_long_5(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''int char_int(char *);
	float char_float(char *);
	void str_copy(char *,  char *, int, int);
	string str_copy(char *, int , int );''',
            r'''int,char_int,(,char,*,),;,float,char_float,(,char,*,),;,void,str_copy,(,char,*,,,char,*,,,int,,,int,),;,string,str_copy,(,char,*,,,int,,,int,),;,<EOF>''',135))
    def test_long_6(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''int char_int(char *a)
	{
		int temp = 0;
		for(int i = 0; i < strlen(a); i++)
		{
			temp = temp + static_cast<int>(a[i]-48)*pow(10, strlen(a)-i-1); 
		}
		return temp;
	}llo''',
            r'''int,char_int,(,char,*,a,),{,int,temp,=,0,;,for,(,int,i,=,0,;,i,<,strlen,(,a,),;,i,+,+,),{,temp,=,temp,+,static_cast,<,int,>,(,a,[,i,],-,48,),*,pow,(,10,,,strlen,(,a,),-,i,-,1,),;,},return,temp,;,},llo,<EOF>''',136))
    def test_long_7(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''a + b = c
            a * b = c ** 3
            a / = 2 = 5
            a % 2 = 1.e2
            a // 2 = 10
            a && a == 10''',
            r'''a,+,b,=,c,a,*,b,=,c,*,*,3,a,/,=,2,=,5,a,%,2,=,1.e2,a,a,&&,a,==,10,<EOF>''',137))
    def test_long_8(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''int a,b       ,c ,a                   b;
            float a = int (abc) - 12;
            str abc[] = {3,2,1};''',
            r'''int,a,,,b,,,c,,,a,b,;,float,a,=,int,(,abc,),-,12,;,str,abc,[,],=,{,3,,,2,,,1,},;,<EOF>''',138))
    def test_long_9(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''printf("Hello PPL, You are verry hard")''',
            r'''printf,(,Hello PPL, You are verry hard,),<EOF>''',139))
    def test_long_10(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''heint fibonacci (int n)  
{
    if (n==0)
        return 0;
    if (n == 1)   
        return 1;
    else  
        return fibonacci(n-1)+fibonacci(n-2);
} llo''',
            r'''heint,fibonacci,(,int,n,),{,if,(,n,==,0,),return,0,;,if,(,n,==,1,),return,1,;,else,return,fibonacci,(,n,-,1,),+,fibonacci,(,n,-,2,),;,},llo,<EOF>''',140))
    def test_long_11(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''hint gcd(int a, int b) 
{ 
    // Everything divides 0  
    if (a == 0) 
       return b; 
    if (b == 0) 
       return a; 
   
    // base case 
    if (a == b) 
        return a; 
   
    // a is greater 
    if (a > b) 
        return gcd(a-b, b); 
    return gcd(a, b-a); 
}''',
            r'''hint,gcd,(,int,a,,,int,b,),{,if,(,a,==,0,),return,b,;,if,(,b,==,0,),return,a,;,if,(,a,==,b,),return,a,;,if,(,a,>,b,),return,gcd,(,a,-,b,,,b,),;,return,gcd,(,a,,,b,-,a,),;,},<EOF>''',141))
    def test_long_12(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''int main() 
{ 
    int a = 98, b = 56; 
    cout<<"GCD of "<<a<<" and "<<b<<" is "<<gcd(a, b); 
    return 0; 
} ''',
            r'''int,main,(,),{,int,a,=,98,,,b,=,56,;,cout,<,<,GCD of ,<,<,a,<,<, and ,<,<,b,<,<, is ,<,<,gcd,(,a,,,b,),;,return,0,;,},<EOF>''',142))
    def test_long_13(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''heint compare(const void * a, const void * b) 
{ 
    return ( *(int*)a - *(int*)b ); 
}''',
            r'''heint,compare,(,const,void,*,a,,,const,void,*,b,),{,return,(,*,(,int,*,),a,-,*,(,int,*,),b,),;,},<EOF>''',143))
    def test_long_14(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''begin = clock(); 
    qsort(arr, N, sizeof(int), compare); 
    end = clock(); ''',
            r'''begin,=,clock,(,),;,qsort,(,arr,,,N,,,sizeof,(,int,),,,compare,),;,end,=,clock,(,),;,<EOF>''',144))
    def test_long_15(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''time_spent = (double)(end - begin) / CLOCKS_PER_SEC;''',
            r'''time_spent,=,(,double,),(,end,-,begin,),/,CLOCKS_PER_SEC,;,<EOF>''',145))
    def test_long_16(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''int arr[100] = { 0 }; 
    int i, x, pos, n = 10; ''',
            r'''int,arr,[,100,],=,{,0,},;,int,i,,,x,,,pos,,,n,=,10,;,<EOF>''',146))
    def test_long_17(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''void maximum(void* arg) 
{ 
    int i, num = thread_no++; 
    int maxs = 0; 
  
    for (i = num * (max / 4); i < (num + 1) * (max / 4); i++) { 
        if (a[i] > maxs) 
            maxs = a[i]; 
    } 
  
    max_num[num] = maxs; 
} ''',
            r'''void,maximum,(,void,*,arg,),{,int,i,,,num,=,thread_no,+,+,;,int,maxs,=,0,;,for,(,i,=,num,*,(,max,/,4,),;,i,<,(,num,+,1,),*,(,max,/,4,),;,i,+,+,),{,if,(,a,[,i,],>,maxs,),maxs,=,a,[,i,],;,},max_num,[,num,],=,maxs,;,},<EOF>''',147))
    def test_long_18(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''// creating 4 threads 
    for (i = 0; i < Th_max; i++) 
        pthread_create(&threads[i], NULL, 
                       maximum, (void*)NULL); 
  
    // joining 4 threads i.e. waiting for 
    // all 4 threads to complete 
    for (i = 0; i < Th_max; i++) 
        pthread_join(threads[i], NULL); 
  
    // Finding max element in an array 
    // by individual threads 
    for (i = 0; i < Th_max; i++) { 
        if (max_num[i] > maxs) 
            maxs = max_num[i]; 
    } ''',
            r'''for,(,i,=,0,;,i,<,Th_max,;,i,+,+,),pthread_create,(,Error Token &''',148))
    def test_long_19(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''h// Function to print an array 
void printArray() 
{ 
    int i; 
    for (i = 0; i < n; i++) 
        cout << a[i] << " "; 
    cout << endl; 
} ello''',
            r'''h,void,printArray,(,),{,int,i,;,for,(,i,=,0,;,i,<,n,;,i,+,+,),cout,<,<,a,[,i,],<,<, ,;,cout,<,<,endl,;,},ello,<EOF>''',149))
    def test_long_20(self):
            self.assertTrue(TestLexer.checkLexeme(
            r'''void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    { 
        // Same as (l+r)/2, but avoids overflow for 
        // large l and h 
        int m = l+(r-l)/2; 
  
        // Sort first and second halves 
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} ''',
            r'''void,mergeSort,(,int,arr,[,],,,int,l,,,int,r,),{,if,(,l,<,r,),{,int,m,=,l,+,(,r,-,l,),/,2,;,mergeSort,(,arr,,,l,,,m,),;,mergeSort,(,arr,,,m,+,1,,,r,),;,merge,(,arr,,,l,,,m,,,r,),;,},},<EOF>''',150))
    
    # string test
    def test_str_0(self):
        self.assertTrue(TestLexer.checkLexeme(
            """string x;
            x = "hello PPL";
            """,
            """string,x,;,x,=,hello PPL,;,<EOF>""",
            151))
    def test_str_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            "PPL is
            """,
            """Unclosed String: PPL is""",
            152))
    def test_str_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            www = "get a \\n new line" ;
            """,
            """www,=,get a \\n new line,;,<EOF>""",
            153))
    def test_str_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            text = "this "problem 123"
            """,
            """text,=,this ,problem,123,Unclosed String: """,
            154))
    def test_str_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            emptystr = "";
            """,
            """emptystr,=,,;,<EOF>""",
            155))
    def test_str_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            ktx = 'string' ;
            """,
            """ktx,=,Error Token '""",
            156))
    def test_str_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            x = "this string has "another string""
            """,
            """x,=,this string has ,another,string,,<EOF>""",
            157))
    def test_str_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            x = "this string has 'another string'"
            """,
            """x,=,this string has 'another string',<EOF>""",
            158))

    # test comment
    def test_cmt_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """// this is a cute comment 
            abc321 int
            """,
            """abc321,int,<EOF>""",
            159))
    def test_cmt_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            char ppl; // variable a // with integer type
            """,
            """char,ppl,;,<EOF>""",
            160))
    def test_cmt_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            100
            /* hello ppl */
            text
            """,
            """100,text,<EOF>""",
            161))
    def test_cmt_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            void diag () {
            /* first block comment------ /*and another*/ */
            }
            """,
            """void,diag,(,),{,*,/,},<EOF>""",
            162))
    def test_cmt_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            int x; // inline and /* block // and inline /* and block */
            """,
            """int,x,;,<EOF>""",
            163))
    def test_cmt_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            void diag () {
            /* first block co
            
            
            
            
            mment------ /*and another*/ */
            }
            """,
            """void,diag,(,),{,*,/,},<EOF>""",
            164))
    def test_cmt_7(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
            int x; /* block // and 
            // inline and  inline
             /* and block */
            """,
            """int,x,;,<EOF>""",
            165))

    # program test
    def test_program_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''!!!! === !!!!''',
            r'''!,!,!,!,==,=,!,!,!,!,<EOF>''',166))
    def test_program_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''*** <0> ***''',
            r'''*,*,*,<,0,>,*,*,*,<EOF>''',167))
    def test_program_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' }{{}<=== void  ==>{}}''',
            r'''},{,{,},<=,==,void,==,>,{,},},<EOF>''',168))
    def test_program_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''------==-------''',
            r'''-,-,-,-,-,-,==,-,-,-,-,-,-,-,<EOF>''',169))
    def test_program_5(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''""""""""""hello""""""""""''',
        r''',,,,,hello,,,,,,<EOF>''',170))
    def test_program_6(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''{{{{{{{{{{{hello}}}}}}}}}}}''',
        r'''{,{,{,{,{,{,{,{,{,{,{,hello,},},},},},},},},},},},<EOF>''',171))
    def test_program_7(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''"ssh hpcc hcmut edu vn''',
        r'''Unclosed String: ssh hpcc hcmut edu vn''',172))
    def test_program_8(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''curl {"key", "value"} "localhost:8080" ''',
        r'''curl,{,key,,,value,},localhost:8080,<EOF>''',173))
    def test_program_9(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''ls | grep ppl''',
        r'''ls,Error Token |''',174))
    def test_program_10(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''ping google.com''',
        r'''ping,google,Error Token .''',175))
    def test_program_11(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''"hello [] \n \m"''',
        r'''Illegal Escape In String: hello [] \n \m''',176))
    def test_program_12(self):
        self.assertTrue(TestLexer.checkLexeme(
        r''' "?" ''',
        r'''?,<EOF>''',177))
    def test_program_13(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''[][][][][][[][][[[[][][][][][]]]]]]''',
        r'''[,],[,],[,],[,],[,],[,[,],[,],[,[,[,[,],[,],[,],[,],[,],[,],],],],],],<EOF>''',178))
    def test_program_14(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''!@#$%^&*()''',
        r'''!,Error Token @''',179))
    def test_program_15(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''123 098 *&^%''',
        r'''123,098,*,Error Token &''',180))
    def test_program_16(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''def print() : print(hello)''',
        r'''def,print,(,),Error Token :''',181))
    def test_program_17(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''2 + 3 -1 == 2 <= 6 && true''',
        r'''2,+,3,-,1,==,2,<=,6,&&,true,<EOF>''',182))
    def test_program_18(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main(int a) {
do {
    x = x + 1;
}
while true ;
}''',
        r'''void,main,(,int,a,),{,do,{,x,=,x,+,1,;,},while,true,;,},<EOF>''',183))
    def test_program_19(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void foo() {
for ( x = 1 ; x < 3 ; x = x + 1 ) {
    a = a + 2 ;
}
break ;
}''',
        r'''void,foo,(,),{,for,(,x,=,1,;,x,<,3,;,x,=,x,+,1,),{,a,=,a,+,2,;,},break,;,},<EOF>''',184))
    def test_program_20(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void foo() {
for ( x = 1 ; x < 3 ; x = x + 1 ) {
    a = a + 2 ;
}
break ;
}''',
        r'''void,foo,(,),{,for,(,x,=,1,;,x,<,3,;,x,=,x,+,1,),{,a,=,a,+,2,;,},break,;,},<EOF>''',185))
    def test_program_21(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''int[] main() {
int a[2];
return a[];
}''',
        r'''int,[,],main,(,),{,int,a,[,2,],;,return,a,[,],;,},<EOF>''',186))
    def test_program_22(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void f(int a[]) {}''',
        r'''void,f,(,int,a,[,],),{,},<EOF>''',187))
    def test_program_34(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void foo(){
i = 2;
a = "true";
69;
foo(i, a);
}''',
        r'''void,foo,(,),{,i,=,2,;,a,=,true,;,69,;,foo,(,i,,,a,),;,},<EOF>''',188))
    def test_program_23(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void foo(){
i = 2; {
    a = "true"; {
        69;
    }
}
foo(i, a);
}''',
        r'''void,foo,(,),{,i,=,2,;,{,a,=,true,;,{,69,;,},},foo,(,i,,,a,),;,},<EOF>''',189))
    def test_program_24(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main() {
int a;
a = 3.14159;
}''',
        r'''void,main,(,),{,int,a,;,a,=,3.14159,;,},<EOF>''',190))
    def test_program_25(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main() {
putInt(a);
}
int foo(){
    int a;
    a = 1;
}''',
        r'''void,main,(,),{,putInt,(,a,),;,},int,foo,(,),{,int,a,;,a,=,1,;,},<EOF>''',191))
    def test_program_26(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''int a;
void main() {
a = 0;
putInt(a);
}
int foo(){
a = 1;
return a;
}''',
        r'''int,a,;,void,main,(,),{,a,=,0,;,putInt,(,a,),;,},int,foo,(,),{,a,=,1,;,return,a,;,},<EOF>''',192))
    def test_program_27(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main() {
if ( a == 0 ) {
    for ( x = 0 ; x < 3 ; x = x + 1 ) a = a - 1;self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
self.a
}
}''',
        r'''void,main,(,),{,if,(,a,==,0,),{,for,(,x,=,0,;,x,<,3,;,x,=,x,+,1,),a,=,a,-,1,;,self,Error Token .''',193))
    def test_program_28(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main(int x) {
int a;
a = 0;
for ( x = 0 ; a < 3 ; x = x + 1 ) x = x - 1 ;
}''',
        r'''void,main,(,int,x,),{,int,a,;,a,=,0,;,for,(,x,=,0,;,a,<,3,;,x,=,x,+,1,),x,=,x,-,1,;,},<EOF>''',194))
    def test_program_29(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main() {
int a;
a = 2;
return a;
a = a + 1;
}''',
        r'''void,main,(,),{,int,a,;,a,=,2,;,return,a,;,a,=,a,+,1,;,},<EOF>''',195))
    def test_program_30(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main() {
int a;
int b
}''',
        r'''void,main,(,),{,int,a,;,int,b,},<EOF>''',196))
    def test_program_31(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main(){
// first block
{
    // second block
    {
        // third block
        {
            // fourth block
        }
    }
}
}''',
        r'''void,main,(,),{,{,{,{,},},},},<EOF>''',197))
    def test_program_32(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''int f() {
return 69;
}''',
        r'''int,f,(,),{,return,69,;,},<EOF>''',198))
    def test_program_33(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main () { int a, b;}''',
        r'''void,main,(,),{,int,a,,,b,;,},<EOF>''',199))
    def test_program_35(self):
        self.assertTrue(TestLexer.checkLexeme(
        r'''void main () { int a, final;}''',
        r'''void,main,(,),{,int,a,,,final,;,},<EOF>''',200))
