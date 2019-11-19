from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        declList = []
        for x in ctx.decl():
            decl = self.visitDecl(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)

    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)

    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        primitive_type = self.visitPrimitive_type(ctx.primitive_type())
        IDList = self.visitIdlist(ctx.idlist())
        return [VarDecl(x[1], ArrayType(x[0], primitive_type)) if isinstance(x, tuple) else VarDecl(x, primitive_type) for x in IDList]
    
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.INTTYPE():   return IntType()
        if ctx.FLOATTYPE(): return FloatType()
        if ctx.STRTYPE():   return StringType()
        if ctx.BOOLTYPE():  return BoolType()

    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return [self.visitId_or_arr(x) for x in ctx.id_or_arr()]

    def visitId_or_arr(self, ctx:MCParser.Id_or_arrContext):
        if ctx.INTLIT():
            return (int(ctx.INTLIT().getText()), ctx.ID().getText())
        else:
            return ctx.ID().getText()
            
        
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        func_type = self.visitFunc_type(ctx.func_type())
        paralist = self.visitParalist(ctx.paralist())
        block_stmt = self.visitBlock_stmt(ctx.block_stmt())
        id = Id(ctx.ID().getText())
        return FuncDecl(id, paralist, func_type, block_stmt)

    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        if ctx.VOIDTYPE(): return VoidType()
        elif ctx.getChildCount() == 3: return ArrayPointerType(self.visitPrimitive_type(ctx.primitive_type()))
        else: return self.visitPrimitive_type(ctx.primitive_type())

    def visitParalist(self, ctx:MCParser.ParalistContext):
        return [self.visitPara(x) for x in ctx.para()]

    def visitPara(self, ctx:MCParser.ParaContext):
        if ctx.LSB():
            return VarDecl(ctx.ID().getText(), ArrayPointerType(self.visitPrimitive_type(ctx.primitive_type())))
        else:
            return VarDecl(ctx.ID().getText(), self.visitPrimitive_type(ctx.primitive_type()))

    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        memBlock = []
        for x in ctx.stmt_vardecl():
            stmt_vardecls = self.visitStmt_vardecl(x)
            if isinstance(stmt_vardecls, list):
                memBlock.extend(stmt_vardecls)
            else:
                memBlock.append(stmt_vardecls)
        return Block(memBlock)

    def visitStmt_vardecl(self, ctx:MCParser.Stmt_vardeclContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx:MCParser.StmtContext):
        if ctx.exp():
            return self.visitExp(ctx.exp())
        else:
            return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        if ctx.IF() and ctx.ELSE():
            return If(self.visitExp(ctx.exp()), self.visitStmt(ctx.stmt(0)), self.visitStmt(ctx.stmt(1)))
        else:
            return If(self.visitExp(ctx.exp()), self.visitStmt(ctx.stmt(0)))
    
    def visitDo_while_stmt(self, ctx:MCParser.Do_while_stmtContext):
        exps = self.visitExp(ctx.exp())
        stmts = [self.visitStmt(x) for x in ctx.stmt()]
        return Dowhile(stmts, exps)
    
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        expr = [self.visitExp(x) for x in ctx.exp()]
        loop = self.visitStmt(ctx.stmt())
        return For(expr[0], expr[1], expr[2], loop)

    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return Return(self.visitExp(ctx.exp())) if ctx.exp() else Return() 

    def visitExp(self, ctx:MCParser.ExpContext):
        if ctx.ASSIGN():
            return BinaryOp(ctx.ASSIGN().getText(), self.visitExp1(ctx.exp1()), self.visitExp(ctx.exp()))
        else:
            return self.visitExp1(ctx.exp1())
    
    def visitExp1(self, ctx:MCParser.Exp1Context):
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visitExp1(ctx.exp1()), self.visitExp2(ctx.exp2()))
        else:
            return self.visitExp2(ctx.exp2())

    def visitExp2(self, ctx:MCParser.Exp2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visitExp2(ctx.exp2()), self.visitExp3(ctx.exp3()))
        else:
            return self.visitExp3(ctx.exp3())
    
    def visitExp3(self, ctx:MCParser.Exp3Context):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(), self.visitExp4(ctx.exp4(0)), self.visitExp4(ctx.exp4(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(), self.visitExp4(ctx.exp4(0)), self.visitExp4(ctx.exp4(1)))
        else:
            return self.visitExp4(ctx.exp4(0))

    def visitExp4(self, ctx:MCParser.Exp4Context):
        if ctx.LT():
            return BinaryOp(ctx.LT().getText(), self.visitExp5(ctx.exp5(0)), self.visitExp5(ctx.exp5(1)))
        elif ctx.LE():
            return BinaryOp(ctx.LE().getText(), self.visitExp5(ctx.exp5(0)), self.visitExp5(ctx.exp5(1)))
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(), self.visitExp5(ctx.exp5(0)), self.visitExp5(ctx.exp5(1)))
        elif ctx.GE():
            return BinaryOp(ctx.GE().getText(), self.visitExp5(ctx.exp5(0)), self.visitExp5(ctx.exp5(1)))
        else:
            return self.visitExp5(ctx.exp5(0))

    def visitExp5(self, ctx:MCParser.Exp5Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visitExp5(ctx.exp5()), self.visitExp6(ctx.exp6()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visitExp5(ctx.exp5()), self.visitExp6(ctx.exp6()))
        else:
            return self.visitExp6(ctx.exp6())

    def visitExp6(self, ctx:MCParser.Exp6Context):
        if ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visitExp6(ctx.exp6()), self.visitExp7(ctx.exp7()))
        elif ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visitExp6(ctx.exp6()), self.visitExp7(ctx.exp7()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visitExp6(ctx.exp6()), self.visitExp7(ctx.exp7()))
        else:
            return self.visitExp7(ctx.exp7())

    def visitExp7(self, ctx:MCParser.Exp7Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visitExp7(ctx.exp7()))
        elif ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visitExp7(ctx.exp7()))
        else:
            return self.visitExp8(ctx.exp8())

    def visitExp8(self, ctx:MCParser.Exp8Context):
        if ctx.exp():
            return ArrayCell(self.visitExp9(ctx.exp9()), self.visitExp(ctx.exp()))
        else:
            return self.visitExp9(ctx.exp9())

    def visitExp9(self, ctx:MCParser.Exp9Context):
        if ctx.exp():
            return self.visitExp(ctx.exp())
        else:
            return self.visitOperand(ctx.operand())

    def visitOperand(self, ctx:MCParser.OperandContext):
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRLIT(): return StringLiteral(str(ctx.STRLIT().getText()))
        elif ctx.BOOLLIT(): return BooleanLiteral(True if ctx.BOOLLIT().getText() == 'true' else False)
        elif ctx.ID(): return Id(ctx.ID().getText())
        else: return self.visitCall(ctx.call())

    def visitCall(self, ctx:MCParser.CallContext):
        id = Id(ctx.ID().getText())
        exps = [self.visitExp(x) for x in ctx.exp()]
        return CallExpr(id, exps)

