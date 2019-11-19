import java.util.Scanner

object DivisibleSumPair {
    def main(args: Array[String]) {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val k = sc.nextInt()
        val arr = (1 to n).map(_ => sc.nextInt()).toArray

        val result = divisibleSumPair(arr, k)
        println(result)
    }
    def divisibleSumPair(arr: Array[Int], k: Int): Int = {
        var result = 0
        for (i <- 0 until arr.length) {
            for (j <- i + 1 until arr.length) {
                if ((arr(i) + arr(j)) % k == 0)
                    result += 1
            }
        }
        return result
    }
}