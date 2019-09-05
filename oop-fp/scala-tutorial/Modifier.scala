class Outer {
    class Inner {
        private def f() {
            println("f")
        }
        protected def g(){
            println("g")
        }
        def h(){
            println("h")
        }
        class InnerMost {
            f() // OK
        }
    }

    (new Inner).f() // Fail

    class Inside extends Inner {
        g() // OK
    }

    class Other {
        (new Inner).g() // Fail
    }

    (new Inner).h() // OK because h method is public
}

package society {
    package professional {
       class Executive {
          private[professional] var workDetails = null
          private[society] var friends = null
          private[this] var secrets = null
 
          def help(another : Executive) {
             println(another.workDetails)
             println(another.friends)
             println(another.secrets) //ERROR
          }
       }
    }
}