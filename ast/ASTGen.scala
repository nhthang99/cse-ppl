trait AST
case class Program(sl:Stml) extends AST
trait Stml extends AST
case class Assign(id:String, e:Exp) extends Stml
trait Exp extends AST
case class BinOp(op:String, e1:Stml, e2:Stml) extends Exp
case class Id(id:String) extends Exp
case class Intlit(lit:Int) extends Exp

class ASTGen extends MCBaseVisitor[AST] {
    /* term: ID | INTLIT | LP exp RP */
    override def visitTerm(ctx:TermContext) = {
        if (ctx.getChildCount() == 3) ctx.exp().accept(this)
        else if (ctx.ID != null) Id(ctx.ID.getText)
        else Intlit(ctx.INT.getText.toInt)
    }

    /* exp: exp ADDOP term | term */
    override def visitExp(ctx:ExpContext) = {
        if (ctx.getChildCount() == 1) ctx.term().accept(this)
        else BinOp(ctx.ADDOP.getText,
        ctx.exp().accept(this).asInstanceOf[Exp],
        ctx.term().accept(this).asInstanceOf[Exp]
        )
    }

    /* assign: ID ASSIGN exp SEMI */
    override def visitAssign(ctx:AssignContext) = 
        Assign(ctx.ID.getText, ctx.exp().accept(this).asInstanceOf[Exp])
}