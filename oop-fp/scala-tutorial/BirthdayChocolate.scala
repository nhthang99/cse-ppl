import java.util.Scanner

object BirthdayChocolate {
    def main(args: Array[String]) {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val squares = (1 to n).map(_ => sc.nextInt()).toArray
        val day = sc.nextInt()
        val month = sc.nextInt()

        val result = birthday(squares, day, month)
        println(result)
    }
    def birthday(squares: Array[Int], birthday: Int, birthmonth: Int): Int = {
        var result = 0
        for (i <- 0 to squares.length - birthmonth) {
            if (squares.slice(i, i + birthmonth).sum == birthday) {
                result += 1
            }
        }
        return result
    }
}