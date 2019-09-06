import java.util.Scanner

object BetweenTwoSets {
    def main (args: Array[String]) {
        val sc = new java.util.Scanner(System.in)
        val n = sc.nextInt()
        val m = sc.nextInt()
        val a = (1 to n).map(_ => sc.nextInt).sorted
        val b = (1 to m).map(_ => sc.nextInt).sorted
        
        var result = 0
        for (i <- a.last to b.head){
            if (a.forall(value => i % value == 0) && b.forall(value => value % i == 0)){
                result += 1
            }
        }
        print(result)
    }
}