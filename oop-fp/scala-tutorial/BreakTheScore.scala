import java.util.Scanner

object BreakTheScore {
    def main(args: Array[String]) {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val scores = (1 to n).map(_ => sc.nextInt()).toArray
        var result = breakingScore(scores, n)
        println(result.mkString(" "))
    }
    def breakingScore(scores: Array[Int], n: Int): Array[Int] = {
        val count_high = 0
        val count_low = 1
        var result:Array[Int] = new Array[Int](2)
        var max, min = scores(0)
        
        for (i <- 1 until n) {
            if (scores(i) > max) {
                max = scores(i)
                result(count_high) += 1
            }
            if (scores(i) < min) {
                min = scores(i)
                result(count_low) += 1
            }
        }
        return result
    }
}