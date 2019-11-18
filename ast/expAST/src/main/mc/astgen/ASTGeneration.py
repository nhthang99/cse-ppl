from MCVisitor import MCVisitor
from MCParser import MCParser
from functools import reduce
from AST import *

class ASTGeneration(MCVisitor):
    def visitExp(self, ctx:MCParser.ExpContext):
        return Binary(ctx.COMPARE().getText(), self.visitTerm(ctx.term(0)), self.visitTerm(ctx.term(1))) if ctx.COMPARE() else self.visitTerm(ctx.term(0))

    def visitTerm(self, ctx:MCParser.TermContext):
        return Binary(ctx.EXPONENT().getText(), self.visitFactor(ctx.factor()), self.visitTerm(ctx.term())) if ctx.EXPONENT() else self.visitFactor(ctx.factor())

    def visitFactor(self, ctx:MCParser.FactorContext):
        df = zip(ctx.ANDOR(), ctx.operand()[1:])
        return reduce(lambda x, y: Binary(y[0].getText(), x, self.visitOperand(y[1])), df, self.visit(ctx.operand(0)))

    def visitOperand(self, ctx:MCParser.OperandContext):
        if ctx.INTLIT(): return IntLit(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT(): return BoolLit(True if ctx.BOOLIT().getText() == "true" else False)
        else: return self.visitExp(ctx.exp())