import coco.ast as ast
import coco.visitor_decorator as vis
import src.tree_search as matching


class TypeChecker:
    pass


class Evaluator():

    @staticmethod
    def evaluate(ast):
        e = Evaluator()
        return e.__eval(ast)

    _ignores_stack = []

    def __eval(self, tree):
        return self.visit(tree)

    @vis.visitor(ast.Sheet)
    def visit(self, node):
        return self.visit(node.contexts[0])

    @vis.visitor(ast.WhitespaceContext)
    def visit(self, node):
        self._ignores_stack.append(matching.WHITESPACE_DESC)

        conventions = []
        for stat in node.statements:
            c = self.visit(stat)
            conventions.append(c)

        self._ignores_stack = self._ignores_stack[:-1]
        return matching.ConventionsMap(conventions)

    @vis.visitor(ast.RequireRule)
    def visit(self, node):
        desc_list = self.visit(node.css_markers)
        pattern = matching.NodeSequence(desc_list, self._ignores_stack[-1])
        option_list = self._visit_options(node.ws_options)
        requirement = matching.Requirement(option_list, matching.SimpleDescriptor(type_='indent'))
        return matching.IfThenConvention(pattern, requirement)

    def _visit_options(self, ws_options):
        res = []
        for option in ws_options:
            op = self.visit(option)
            res.append(op)
        return res

    @vis.visitor(ast.MarkerSequenceOption)
    def visit(self, node):
        if not node.marker_sequences:
            return matching.SequenceOption.NONE_OPTION
        res = []
        for sequence in node.marker_sequences:
            s = self.visit(sequence)
            res.append(s)
        return matching.SequenceOption(res, matching.SimpleDescriptor(type_='indent'))

    @vis.visitor(ast.MarkerSequence)
    def visit(self, node):
        res = []
        for m in node.markers:
            desc = self.visit(m)
            res.append(desc)
        return matching.NodeSequence(res, self._ignores_stack[-1])

    @vis.visitor(ast.RuleMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='ruleset')

    @vis.visitor(ast.SelectorMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='selector') # or simpleselector

    @vis.visitor(ast.DeclarationMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='declaration')

    @vis.visitor(ast.BlockMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='block')

    @vis.visitor(ast.ValueMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='value')

    @vis.visitor(ast.EofMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='eof')

    @vis.visitor(ast.CommentMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='comment')

    @vis.visitor(ast.SymbolMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(value=node.value)

    @vis.visitor(ast.TabMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='tab', value=node.get_value())

    @vis.visitor(ast.SpaceMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='space', value=node.get_value())

    @vis.visitor(ast.NewlineMarker)
    def visit(self, node):
        return matching.SimpleDescriptor(type_='newline', value=node.get_value())
