from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return Program(self.visitVardecls(ctx.vardecls()))

    def visitVardecls(self, ctx:MCParser.VardeclsContext):
        return [self.visitVardecl(ctx.vardecl())] + self.visitVardecls(ctx.vardecls()) if ctx.vardecls() else [self.visitVardecl(ctx.vardecl())]

    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return VarDecl(self.visitMctype(ctx.mctype()), self.visitIds(ctx.ids()))

    def visitMctype(self, ctx:MCParser.MctypeContext):
        if ctx.INTTYPE(): return IntType()
        if ctx.FLOATTYPE(): return FloatType()

    def visitIds(self, ctx:MCParser.IdsContext):
        return [x.getText() for x in ctx.ID()]