import coco.ast.ast as ast
import coco.analysis.expressions as expr
import coco.visitor_decorator as vis
import coco.analysis.pattern_matcher as p_matcher


class Violations(object):
    def __init__(self):
        self._inner = []

    def add_violation(self, violation):
        self._inner.append(violation)

    def to_string(self):
        vs = []
        for v in self._inner:
            vs.append('\n')
            vs.append(v.to_string())
        return ''.join(vs)


class Violation(object):
    def __init__(self, message, line):
        self._message = message
        self._line = line

    def to_string(self):
        return ''.join(['Violation on line ', str(self._line), ': ', self._message])


class ViolationsFinder(object):

    def __init__(self, tree):
        assert tree
        self._violations = Violations()
        self._tree = tree
        self._context = None

    @staticmethod
    def find(sheet, tree):
        finder = ViolationsFinder(tree)
        finder.visit(sheet)
        print(finder._violations.to_string())

    @vis.visitor(ast.Sheet)
    def visit(self, sheet):
        for c in sheet.contexts:
            # self._set_current_context(c)
            self.visit(c)
            # self._reset_current_context()

    @vis.visitor(ast.SemanticContext)
    def visit(self, context):
        for convention in context.conventions:
            self._set_current_context(context)
            self.visit(convention)
            self._reset_current_context()

    def _set_current_context(self, context):
        self._context = context

    def _reset_current_context(self):
        self._context = None

    def _get_current_context(self):
        return self._context

    @vis.visitor(ast.FindRequireConvention)
    def visit(self, find_require):
        filter_ = p_matcher.Filter(self._get_current_context().get_ignored_and_target_patterns())
        matcher = p_matcher.PatternMatcher(filter_)
        for id_node_table in matcher.find_pattern_in_tree(self._tree, find_require.target_pattern):
            constraint_filter = p_matcher.Filter(self._get_current_context().get_ignored_patterns())
            eval_context = expr.ConstraintContext(p_matcher.PatternMatcher(constraint_filter), id_node_table)
            is_fulfilled = expr.ExprEvaluator.evaluate(find_require.constraint, eval_context)
            if not is_fulfilled.value:
                anchor_desc = find_require.target_pattern.get_anchors()[0]
                anchor_node = id_node_table[anchor_desc]
                self._violations.add_violation(Violation(find_require.message, anchor_node.start_position.line))

    @vis.visitor(ast.ForbidConvention)
    def visit(self, forbid):
        filter_seq = p_matcher.Filter(self._get_current_context().get_ignored_and_target_patterns())
        matcher = p_matcher.PatternMatcher(filter_seq)
        for id_node_table in matcher.find_pattern_in_tree(self._tree, forbid.target_pattern):
            # eval_context = expr.ConstraintContext(matcher, id_node_table)
            # id_node_table = self._context[0]
            anchor_desc = forbid.target_pattern.get_anchors()[0]
            anchor_node = id_node_table[anchor_desc]
            self._violations.add_violation(Violation(forbid.message, anchor_node.start_position.line))

    @vis.visitor(ast.FindForbidConvention)
    def visit(self, find_forbid):
        return expr.ExprEvaluator.evaluate(find_forbid.constraint, self._context[0])
