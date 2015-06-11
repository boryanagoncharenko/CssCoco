from coco.ast.ast import *
from coco.syntax.cocoListener import cocoListener
from coco.syntax.cocoVisitor import cocoVisitor


class CocoCustomListener(cocoListener):

    def enterStylesheet(self, ctx):

        set = ConventionSet(None)

    def exitStylesheet(self, ctx):
        pass

    def enterContext(self, ctx):
        pass

    def exitContext(self, ctx):
        pass


class CocoCustomVisitor(cocoVisitor):

    def visitStylesheet(self, ctx):
        contexts = []
        for contextCtx in ctx.children:
            contexts.append(self.visitContext(contextCtx))
        return ConventionSet(contexts)

    def visitContext(self, ctx):
        conventions = []
        for conventionCtx in ctx.children:
            conventions.append(self.visitConvention(conventionCtx))
        return Context(conventions, [])

    def visitConvention(self, ctx):
        pass