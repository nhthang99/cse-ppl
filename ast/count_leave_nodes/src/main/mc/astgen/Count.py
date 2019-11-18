from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return 1 + self.visitVardecls(ctx.vardecls())

    def visitVardecls(self, ctx:MCParser.VardeclsContext):
        return self.visitVardecl(ctx.vardecl()) + self.visitVardecls(ctx.vardecls()) if ctx.vardecls() else self.visitVardecl(ctx.vardecl())

    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return 1 + self.visitMctype(ctx.mctype()) + self.visitIds(ctx.ids())

    def visitMctype(self, ctx:MCParser.MctypeContext):
        return 5 + self.visitMctype(ctx.mctype()) if ctx.getChildCount() != 1 else 1

    def visitIds(self, ctx:MCParser.IdsContext):
        return len(ctx.ID()) + len(ctx.COMMA())        

