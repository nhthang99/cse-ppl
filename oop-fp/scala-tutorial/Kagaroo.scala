object Kagaroo {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var x1 = sc.nextInt();
        var v1 = sc.nextInt();
        var x2 = sc.nextInt();
        var v2 = sc.nextInt();
        
        if (x1 == x2) println("YES")
        else if (x1 > x2 && v1 < v2 && ((x1 - x2) % (v2 - v1) == 0)) println("YES")
        else if (x1 < x2 && v1 > v2 && ((x2 - x1) % (v1 - v2) == 0)) println("YES")
        else println("NO")
    }
}