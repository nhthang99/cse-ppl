import java.io._

class Point(val xc: Int, val yc: Int) {
    var x = xc
    var y = yc

    def move(dx: Int, dy: Int) {
        x += dx
        y += dy
        println("Point x location: " + x)
        println("Point y location: " + y)
    }
}

object Demo {
    def main (args: Array[String]) {
        val pt = new Point(10, 20)
        pt.move(5, 10)
    }
}