object Test extends App {

   def time(): Long = {
      println("In time()")
      System.nanoTime
   }
   // `t` is now defined as a by-value parameter (default)
   // A by-value parameter is like receiving a val field; its body is evaluated once, when the parameter is bound to the function.
   // def exec(t: Long): Long = {
   
   // `t` is now defined as a by-name parameter
   // A by-name parameter is like receiving a def method; its body is evaluated whenever it is used inside the function
   def exec(t: => Long) = {
      println("Entered exec, calling t ...")
      println("t = " + t)
      println("Calling t again ...")
      t
   }
 
   println(exec(time()))
 
}