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
        self._ignores_stack.append(matching.WHITESPACE_PATTERN)

        conventions = []
        for stat in node.statements:
            c = self.visit(stat)
            conventions.append(c)

        self._ignores_stack = self._ignores_stack[:-1]
        return matching.ConventionsMap(conventions)

    @vis.visitor(ast.RequireRule)
    def visit(self, node):
        desc_list = self.visit(node.css_markers)
        pattern = matching.NodePattern(desc_list, self._ignores_stack[-1])
        requirement = self.visit(node.ws_markers)
        return matching.Convention(pattern, requirement)

    @vis.visitor(ast.WhitespaceMarkerSequence)
    def visit(self, node):
        before = self.visit(node.before)
        inner = self.visit(node.inner)
        after = self.visit(node.after)
        return matching.Requirement(before_pattern=before, inner_patterns=inner, after_pattern=after,
                                    ignore_list=[matching.NodeDescriptor(type_='indent')])

    @vis.visitor(ast.MultiMarkers)
    def visit(self, node):
        res = []
        for m in node.markers_list:
            desc_list = self.visit(m)
            res.append(desc_list)
        return res

    @vis.visitor(ast.Markers)
    def visit(self, node):
        res = []
        for m in node.markers:
            desc = self.visit(m)
            res.append(desc)
        return res

    @vis.visitor(ast.RuleMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='ruleset')

    @vis.visitor(ast.SelectorMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='selector') # or simpleselector

    @vis.visitor(ast.DeclarationMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='declaration')

    @vis.visitor(ast.BlockMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='block')

    @vis.visitor(ast.ValueMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='value')

    @vis.visitor(ast.SymbolMarker)
    def visit(self, node):
        return matching.NodeDescriptor(value=node.value)

    @vis.visitor(ast.TabMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='tab', value=node.get_value())

    @vis.visitor(ast.SpaceMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='space', value=node.get_value())

    @vis.visitor(ast.NewlineMarker)
    def visit(self, node):
        return matching.NodeDescriptor(type_='newline', value=node.get_value())
