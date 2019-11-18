# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecls.
    def visitVardecls(self, ctx:MCParser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ids.
    def visitIds(self, ctx:MCParser.IdsContext):
        return self.visitChildren(ctx)



del MCParser