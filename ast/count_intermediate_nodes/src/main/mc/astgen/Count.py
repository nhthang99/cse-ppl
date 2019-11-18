from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return 2 + self.visitVardecls(ctx.vardecls())

    def visitVardecls(self, ctx:MCParser.VardeclsContext):
        return 2 + self.visitVardecl(ctx.vardecl()) + self.visitVardecls(ctx.vardecls()) if ctx.vardecls() else 1 + self.visitVardecl(ctx.vardecl())

    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return 2 + self.visitMctype(ctx.mctype()) + self.visitIds(ctx.ids())

    def visitMctype(self, ctx:MCParser.MctypeContext):
        return 1 + self.visitMctype(ctx.mctype()) if ctx.mctype() else 0

    def visitIds(self, ctx:MCParser.IdsContext):
        return 0
