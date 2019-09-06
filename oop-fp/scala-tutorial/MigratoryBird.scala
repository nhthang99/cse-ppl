import java.util.Scanner

object MigratoryBird {
    def main(args: Array[String]) {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val birds = (1 to n).map(_ => sc.nextInt()).toArray

        val result:Int = migratoryBird(birds)
        println(result)
    }
    def migratoryBird(birds: Array[Int]): Int = {
        val arr = birds.groupBy(i => i).mapValues(_.size)
        var max_value = arr.values.max
        var arr_result = new Array[Int](0)
        for ((key, value) <- arr){
            if (value == max_value)
                arr_result = arr_result ++ Array(key)
        }
        return arr_result.min
    }
}